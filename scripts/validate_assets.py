#!/usr/bin/env python3
"""Validate local references, GitHub-compatible markup, and generated motion."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import subprocess
import xml.etree.ElementTree as ET

from PIL import Image, ImageChops, ImageStat

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT/'README.md').read_text()


class Markup(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []

    def handle_starttag(self, tag, attrs):
        assert tag in {'picture','source','img','a','br','sub','strong'}, f'Unsupported HTML: {tag}'
        attrs = dict(attrs)
        assert not any(k in {'style','class'} or k.startswith('on') for k in attrs), attrs
        if tag == 'img':
            assert 'alt' in attrs, 'Every image needs an alt attribute'
            assert attrs.get('width','').isdigit(), 'Images need an explicit width'
        for key in ['src','srcset','href']:
            if key in attrs:
                self.refs.append(attrs[key])


def references(text):
    return re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',text)


def main():
    markup = Markup()
    markup.feed(README)
    refs = markup.refs + references(README)
    local = 0
    headings = set()
    for heading in re.findall(r'^#+\s+(.+)$', README, re.M):
        headings.add(re.sub(r'[^\w\s-]','',heading.lower()).replace(' ','-'))
    for ref in refs:
        parts = urlsplit(ref)
        if ref.startswith('#'):
            assert ref[1:] in headings, f'Missing section: {ref}'
        elif not parts.scheme and parts.path:
            assert (ROOT/unquote(parts.path)).is_file(), f'Missing asset: {ref}'
            local += 1
    print(f'PASS: {local} README image references, section links, alt attributes, and HTML allowlist.')

    # Preserve all existing destinations exactly, including the CV query string.
    original = subprocess.check_output(['git','-C',str(ROOT),'show','HEAD:README.md'],text=True)
    baseline = {u for u in references(original) if urlsplit(u).scheme in {'http','https','mailto'}}
    parser = Markup()
    parser.feed(original)
    baseline.update(u for u in parser.refs if urlsplit(u).scheme in {'http','https','mailto'})
    assert baseline <= set(refs), f'Removed destinations: {baseline-set(refs)}'
    print(f'PASS: all {len(baseline)} original external destinations preserved.')

    svgs = list((ROOT/'assets').rglob('*.svg'))
    for path in svgs:
        svg = ET.parse(path).getroot()
        assert svg.tag == '{http://www.w3.org/2000/svg}svg'
        for element in svg.iter():
            assert element.tag.rsplit('}',1)[-1] not in {'script','foreignObject'}
            for key,value in element.attrib.items():
                assert not key.lower().startswith('on')
                if key.rsplit('}',1)[-1] == 'href':
                    assert value.startswith('#'), f'External SVG resource: {path}'
    print(f'PASS: {len(svgs)} SVGs parse with no scripts or external resources.')

    dimensions = {'hero/hero':(1200,500), 'hero/hero-mobile':(720,760),
                  'motion/data-models-systems':(960,190),
                  'motion/data-models-systems-mobile':(720,390),
                  'projects/edge-slm':(960,250), 'projects/edge-slm-mobile':(720,350)}
    for prefix, size in dimensions.items():
        for theme in ['dark','light']:
            path = ROOT/'assets'/f'{prefix}-{theme}.gif'
            with Image.open(path) as gif:
                assert gif.size == size, path
                assert gif.n_frames == 160, (path,gif.n_frames)
                assert gif.info.get('loop') == 0, f'GIF does not loop forever: {path}'
                palette = gif.copy()
                frames=[]
                duration=0
                for i in range(gif.n_frames):
                    gif.seek(i)
                    gif.load()
                    duration += gif.info['duration']
                    if i in [0,1,80,159]:
                        frames.append(gif.convert('RGB'))
                assert duration == 9600, (path,duration)
                assert ImageChops.difference(frames[0],frames[2]).getbbox(), f'No motion: {path}'
                # The last-to-first transition should be as restrained as a
                # normal frame transition, rather than a cut or full-frame flash.
                seam = sum(ImageStat.Stat(ImageChops.difference(frames[0],frames[3])).mean)
                adjacent = sum(ImageStat.Stat(ImageChops.difference(frames[0],frames[1])).mean)
                assert seam < max(.5,adjacent*3), (path,seam,adjacent)
                if prefix.startswith('hero/'):
                    box = (35,20,590,320) if prefix.endswith('mobile') else (55,20,590,355)
                    assert not ImageChops.difference(frames[0].crop(box),frames[2].crop(box)).getbbox(), 'Hero text moves'
            with Image.open(path.with_name(path.stem+'-static.png')) as still:
                assert still.size == size
                still.load()
                # Compare in the GIF's limited palette: PNG is full color.
                # GIF palette compaction can remap near-identical colors, so
                # allow less than 0.25 RMS on the 0–255 channel scale.
                expected = still.convert('RGB').quantize(palette=palette,dither=Image.Dither.NONE).convert('RGB')
                error = max(ImageStat.Stat(ImageChops.difference(expected,frames[0])).rms)
                assert error < .25, f'PNG and GIF first frame disagree: {path} ({error})'
            assert path.stat().st_size < 3_000_000, f'GIF exceeds size target: {path}'
            print(f'PASS: {path.relative_to(ROOT)} — 160 frames, 9.6 s, seamless boundary, {path.stat().st_size:,} bytes.')


if __name__ == '__main__':
    main()
