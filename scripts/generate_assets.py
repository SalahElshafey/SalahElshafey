#!/usr/bin/env python3
"""Original, deterministic portfolio motion. Requires Pillow; no network calls.

Run from any directory: python3 scripts/generate_assets.py
Use --stills for a fast composition review. All animation has a 9.6 second loop.
"""
from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SCALE = 2
FRAMES = 160
DURATION = 60
FONT_DIR = Path('/usr/share/fonts/truetype/dejavu')
THEMES = {
    'dark': dict(bg='#080D19', panel='#0E1728', ink='#F0F5FC', muted='#A0B2CB',
                 line='#26354D', grid='#142037', cyan='#45DBFF', violet='#AD96FF', teal='#49E3C2'),
    'light': dict(bg='#F7FAFF', panel='#EBF1FA', ink='#101E38', muted='#4A607D',
                  line='#CCD8E9', grid='#E4EBF5', cyan='#006B9C', violet='#6941C6', teal='#087D68'),
}


def rgb(value):
    return tuple(bytes.fromhex(value.lstrip('#')))


def mix(a, b, amount):
    return tuple(round(x + (y-x)*amount) for x, y in zip(rgb(a), rgb(b)))


class Canvas:
    def __init__(self, width, height, theme):
        self.w, self.h = width, height
        self.c = THEMES[theme]
        self.image = Image.new('RGB', (width*SCALE, height*SCALE), self.c['bg'])
        self.draw = ImageDraw.Draw(self.image)

    def line(self, points, color, width=1):
        self.draw.line([(round(x*SCALE), round(y*SCALE)) for x,y in points],
                       fill=color, width=max(1,round(width*SCALE)), joint='curve')

    def rect(self, box, fill=None, outline=None, radius=0, width=1):
        self.draw.rounded_rectangle(tuple(round(v*SCALE) for v in box), radius=radius*SCALE,
                                    fill=fill, outline=outline, width=round(width*SCALE))

    def dot(self, x, y, radius, color, outline=None):
        self.draw.ellipse(tuple(round(v*SCALE) for v in (x-radius,y-radius,x+radius,y+radius)),
                          fill=color, outline=outline, width=SCALE)

    def text(self, x, y, content, size=16, color=None, bold=False, mono=False):
        name = 'DejaVuSansMono' if mono else 'DejaVuSans'
        name += '-Bold.ttf' if bold else '.ttf'
        font = ImageFont.truetype(str(FONT_DIR/name), round(size*SCALE))
        self.draw.text((round(x*SCALE),round(y*SCALE)),content,font=font,
                       fill=color or self.c['ink'],stroke_width=0)

    def finish(self):
        return self.image.resize((self.w,self.h), Image.Resampling.LANCZOS)


def curve(start, end, bend=0):
    x1,y1 = start
    x2,y2 = end
    dx = (x2-x1)*.48
    return [((1-t)**3*x1+3*(1-t)**2*t*(x1+dx)+3*(1-t)*t*t*(x2-dx)+t**3*x2,
             (1-t)**3*y1+3*(1-t)**2*t*(y1+bend)+3*(1-t)*t*t*(y2-bend)+t**3*y2)
            for t in (i/80 for i in range(81))]


def model(c, x, y, scale=1):
    p = c.c
    # Three stacked planes: an abstraction of model layers, not a hardware die.
    for index in range(2,-1,-1):
        yy = y + index*22*scale
        points=[(x,yy-40*scale),(x+70*scale,yy),(x,yy+40*scale),(x-70*scale,yy),(x,yy-40*scale)]
        c.draw.polygon([(round(a*SCALE),round(b*SCALE)) for a,b in points],fill=p['panel'])
        c.line(points,p['cyan'] if index==0 else p['line'],1.4)
        for offset in (-.45,0,.45):
            c.line([(x-43*scale,yy+offset*28*scale),(x,yy+25*scale+offset*28*scale),
                    (x+43*scale,yy+offset*28*scale)],p['line'],.7)
    for xx,yy in [(x,y-40*scale),(x+70*scale,y),(x,y+84*scale),(x-70*scale,y)]:
        c.dot(xx,yy,3*scale,p['cyan'])


def endpoint(c,x,y,kind,color):
    p=c.c
    c.rect((x-24,y-24,x+24,y+24),p['panel'],p['line'],10)
    if kind=='app':
        c.rect((x-10,y-14,x+10,y+14),outline=color,radius=3)
        c.line([(x-5,y+9),(x+5,y+9)],color,1)
    elif kind=='vision':
        c.line([(x-14,y),(x-6,y-8),(x+6,y-8),(x+14,y),(x+6,y+8),(x-6,y+8),(x-14,y)],color,1.2)
        c.dot(x,y,4,color)
    else:
        c.rect((x-10,y-10,x+10,y+10),outline=color,radius=2)
        for offset in (-5,5):
            for sign in (-1,1):
                c.line([(x+sign*10,y+offset),(x+sign*15,y+offset)],color)
                c.line([(x+offset,y+sign*10),(x+offset,y+sign*15)],color)


def hero(theme,mobile=False):
    w,h=(720,760) if mobile else (1200,500)
    c=Canvas(w,h,theme)
    p=c.c
    # Fine construction grid on the visual half; text stays quiet.
    for x in range(32,w,28):
        for y in range(32,h-55,28):
            if mobile and y<330 or not mobile and x<640:
                continue
            c.dot(x,y,.65,p['grid'])
    c.rect((1,1,w-2,h-2),outline=p['line'],radius=20)
    margin=40 if mobile else 60
    c.line([(margin,42),(margin+30,42)],p['cyan'],3)
    c.text(margin+43,29,'SALAH ELSHAFEY',21,p['ink'],mono=True)
    if mobile:
        c.text(margin,94,'Engineering',57,bold=True)
        c.text(margin,163,'intelligence.',57,p['cyan'],bold=True)
        c.text(margin,248,'From data and models',24,p['muted'])
        c.text(margin,281,'to real-world systems.',24,p['muted'])
        cx,cy=355,464
        inputs=[(100,407),(90,496),(140,585)]
        outputs=[(610,412),(620,503),(570,592)]
    else:
        c.text(margin,101,'Engineering',61,bold=True)
        c.text(margin,175,'intelligence.',61,p['cyan'],bold=True)
        c.text(margin,278,'From data and models',23,p['muted'])
        c.text(margin,311,'to real-world systems.',23,p['muted'])
        c.text(797,34,'INTELLIGENCE IN MOTION',11,p['muted'],mono=True)
        cx,cy=885,219
        inputs=[(655,157),(645,245),(680,334)]
        outputs=[(1110,160),(1120,250),(1085,339)]
    # Orbital construction lines frame the layers without distracting glow.
    for r in [108,136]:
        c.draw.ellipse(tuple(round(v*SCALE) for v in (cx-r,cy+22-r,cx+r,cy+22+r)),outline=p['grid'],width=SCALE)
    paths=[]
    for i,(x,y) in enumerate(inputs):
        color=[p['cyan'],p['violet'],p['teal']][i]
        pts=curve((x,y),(cx-70,cy+22))
        c.line(pts,p['line'],1.2)
        paths.append((pts,color,i*.11))
        c.dot(x,y,6,p['bg'],color)
        c.dot(x,y,2,color)
        c.line([(x-20,y-15),(x-12,y-15)],p['line'])
        c.line([(x-20,y+15),(x-12,y+15)],p['line'])
    for i,(x,y) in enumerate(outputs):
        color=[p['violet'],p['cyan'],p['teal']][i]
        pts=curve((cx+70,cy+22),(x-24,y))
        c.line(pts,p['line'],1.2)
        paths.append((pts,color,.48+i*.10))
        endpoint(c,x,y,['app','vision','hardware'][i],color)
    model(c,cx,cy)
    c.text(cx-44,cy+112,'MODEL',12,p['muted'],mono=True)
    c.text(inputs[0][0]-25,inputs[0][1]-44,'DATA',11,p['muted'],mono=True)
    c.text(outputs[0][0]-47,outputs[0][1]-47,'SYSTEMS',11,p['muted'],mono=True)
    footer=h-66
    c.line([(margin,footer),(w-margin,footer)],p['line'])
    c.text(margin,footer+22,'DATA  →  MODELS  →  SYSTEMS',14 if mobile else 15,p['muted'],mono=True)
    if not mobile:
        c.text(815,footer+23,'COMPUTER SYSTEMS / AI + ML',12,p['muted'],mono=True)
    return c,paths,(cx,cy)


def pipeline(theme,mobile=False):
    c=Canvas(720,390,theme) if mobile else Canvas(960,190,theme)
    p=c.c
    c.rect((1,1,c.w-2,c.h-2),outline=p['line'],radius=14)
    paths=[]
    if mobile:
        for i,(title,subtitle) in enumerate([('01 / DATA','Acquire · normalize · trace'),
                                            ('02 / MODELS','Understand · adapt · evaluate'),
                                            ('03 / SYSTEMS','Connect · integrate · observe')]):
            y=31+i*119
            color=[p['cyan'],p['violet'],p['teal']][i]
            c.dot(42,y+22,5,color)
            c.text(70,y,title,24,color,bold=True,mono=True)
            c.text(70,y+41,subtitle,22,p['muted'])
            if i<2:
                pts=[(42,y+35+j) for j in range(75)]
                c.line(pts,p['line'],1.5)
                paths.append((pts,color,i*.4))
        return c,paths,None
    for i,(x,title,subtitle) in enumerate([(36,'01 / DATA','Acquire · normalize · trace'),
                                         (353,'02 / MODELS','Understand · adapt · evaluate'),
                                         (682,'03 / SYSTEMS','Connect · integrate · observe')]):
        color=[p['cyan'],p['violet'],p['teal']][i]
        c.text(x,33,title,18,color,bold=True,mono=True)
        c.text(x,119,subtitle,15,p['muted'])
        for j in range(6):
            c.rect((x+j*27,78,x+12+j*27,89),p['panel'],p['line'],3)
        if i<2:
            end=353 if i==0 else 682
            pts=curve((x+168,84),(end-18,84))
            c.line(pts,p['line'],1.5)
            paths.append((pts,color,i*.4))
    return c,paths,None


def edge(theme,mobile=False):
    c=Canvas(720,350,theme) if mobile else Canvas(960,250,theme)
    p=c.c
    c.rect((1,1,c.w-2,c.h-2),outline=p['line'],radius=14)
    if mobile:
        c.text(32,23,'01 / EDGE SLM',17,p['cyan'],mono=True)
        c.text(32,63,'Keep the source in the story.',31,bold=True)
        c.text(32,111,'Documents → chunks → training tasks',21,p['muted'])
        paths=[]
        for i,y in enumerate([190,232,274]):
            c.rect((52,y-13,80,y+13),p['panel'],p['muted'],3)
            c.line([(59,y-4),(74,y-4)],p['muted'])
            pts=curve((80,y),(326,232))
            c.line(pts,p['line'])
            paths.append((pts,p['cyan'],i*.12))
        c.rect((326,205,389,259),p['panel'],p['cyan'],9)
        c.text(337,214,'{ }',24,p['cyan'],mono=True)
        for i,y in enumerate([201,263]):
            pts=curve((389,232),(546,y))
            c.line(pts,p['line'])
            paths.append((pts,p['teal'],.5+i*.13))
            c.rect((546,y-20,676,y+20),p['panel'],p['teal'],7)
            c.text(565,y-13,'JSONL',19,p['teal'],mono=True)
        c.text(218,309,'PROVENANCE RETAINED',15,p['muted'],mono=True)
        return c,paths,None
    c.text(32,22,'01 / EDGE SLM',13,p['cyan'],mono=True)
    c.text(32,54,'Keep the source',27,bold=True)
    c.text(32,87,'in the story.',27,bold=True)
    c.text(32,139,'One data contract.',16,p['muted'])
    c.text(32,165,'Traceable training tasks.',16,p['muted'])
    paths=[]
    for i,y in enumerate([75,125,175]):
        c.rect((403,y-14,430,y+14),p['panel'],p['muted'],4)
        c.line([(409,y-5),(424,y-5)],p['muted'])
        c.line([(409,y+2),(421,y+2)],p['muted'])
        pts=curve((430,y),(588,125))
        c.line(pts,p['line'],1.3)
        paths.append((pts,p['cyan'],i*.12))
    c.rect((588,98,650,152),p['panel'],p['cyan'],10)
    c.text(600,108,'{ }',23,p['cyan'],mono=True)
    for i,y in enumerate([88,162]):
        pts=curve((650,125),(792,y))
        c.line(pts,p['line'],1.3)
        paths.append((pts,p['teal'],.5+i*.13))
        c.rect((792,y-19,907,y+19),p['panel'],p['teal'],7)
        c.text(807,y-10,'JSONL',15,p['teal'],mono=True)
    c.line([(411,206),(885,206)],p['line'])
    c.text(488,216,'PROVENANCE RETAINED',11,p['muted'],mono=True)
    return c,paths,None


def animate(base, paths, center, t):
    c=Canvas(base.w,base.h,'dark')
    c.image=base.image.copy()
    c.draw=ImageDraw.Draw(c.image)
    for pts,color,offset in paths:
        # Signals fade at both ends; all trajectories and intensities are periodic.
        phase=(t-offset)%1
        position=phase*1.25
        if position>1:
            continue
        fade=min(1,position*9,(1-position)*9)
        for trail in range(10,-1,-1):
            j=round((position-trail*.006)*(len(pts)-1))
            if j<0: continue
            x,y=pts[min(j,len(pts)-1)]
            intensity=fade*(1-trail/12)
            c.dot(x,y,1.4 if trail else 2.8,mix(base.c['bg'],color,intensity))
    if center:
        x,y=center
        # Small layer activation marks. No full-field flashes or text animation.
        for i in range(3):
            amount=.35+.35*(1+math.sin(2*math.pi*(t-.33-i*.08)))/2
            color=mix(base.c['panel'],base.c['cyan'],amount)
            c.line([(x-17,y+i*22),(x,y+10+i*22),(x+17,y+i*22)],color,2)
    return c.finish()


def write_asset(relative, factory, theme, stills):
    canvas,paths,center=factory(theme)
    dest=ROOT/'assets'/relative
    dest.parent.mkdir(parents=True,exist_ok=True)
    first=animate(canvas,paths,center,0)
    still=dest.with_name(dest.name+'-static').with_suffix('.png')
    still_temp=still.with_name('.'+still.stem+'.tmp.png')
    first.save(still_temp,optimize=True)
    still_temp.replace(still)
    if stills:
        print('Still:',dest,flush=True)
        return
    # One palette per asset prevents frame-to-frame color shimmer. Include the
    # whole scene plus dynamic accents before choosing 128 colors.
    reference=first.copy()
    d=ImageDraw.Draw(reference)
    for row,key in enumerate(['cyan','violet','teal']):
        for col in range(64):
            d.rectangle((col*2,row*4,col*2+1,row*4+3),fill=mix(canvas.c['bg'],canvas.c[key],col/63))
    palette=reference.quantize(colors=128,method=Image.Quantize.MEDIANCUT)
    frames=[animate(canvas,paths,center,i/FRAMES).quantize(palette=palette,dither=Image.Dither.NONE)
            for i in range(FRAMES)]
    path=dest.with_suffix('.gif')
    temporary=path.with_name('.'+path.stem+'.tmp.gif')
    frames[0].save(temporary,save_all=True,append_images=frames[1:],duration=DURATION,
                   loop=0,optimize=True,disposal=1)
    temporary.replace(path)
    print(f'{path.relative_to(ROOT)}: {path.stat().st_size/1024:.0f} KiB',flush=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--stills',action='store_true',help='only generate static PNGs')
    parser.add_argument('--only',choices=['all','hero','pipeline','edge'],default='all',
                        help='regenerate just one family of artwork')
    args=parser.parse_args()
    if not (FONT_DIR/'DejaVuSans.ttf').exists():
        parser.error('Install DejaVu Sans fonts (fonts-dejavu-core on Debian/Ubuntu).')
    for theme in THEMES:
        if args.only in ['all','hero']:
            write_asset(f'hero/hero-{theme}',hero,theme,args.stills)
            write_asset(f'hero/hero-mobile-{theme}',lambda t:hero(t,True),theme,args.stills)
        if args.only in ['all','pipeline']:
            write_asset(f'motion/data-models-systems-{theme}',pipeline,theme,args.stills)
            write_asset(f'motion/data-models-systems-mobile-{theme}',lambda t:pipeline(t,True),theme,args.stills)
        if args.only in ['all','edge']:
            write_asset(f'projects/edge-slm-{theme}',edge,theme,args.stills)
            write_asset(f'projects/edge-slm-mobile-{theme}',lambda t:edge(t,True),theme,args.stills)


if __name__=='__main__':
    main()
