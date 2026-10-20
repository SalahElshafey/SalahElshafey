#!/usr/bin/env python3
"""Generate original theme-aware SVG contact links. Standard library only."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets' / 'contact'
THEMES = {
    'dark': dict(bg='#0B1424', surface='#13243B', border='#334A65', ink='#F0F5FC',
                 muted='#A0B2CB', accent='#45DBFF', primary='#163F5B', primary_end='#102B43'),
    'light': dict(bg='#FFFFFF', surface='#EDF3FB', border='#C2D0E3', ink='#101E38',
                  muted='#4A607D', accent='#006B9C', primary='#086F9E', primary_end='#164777'),
}
ICONS = {
    'website': '<circle cx="30" cy="32" r="10"/><ellipse cx="30" cy="32" rx="4" ry="10"/><path d="M20 32h20"/>',
    'email': '<rect x="19" y="24" width="22" height="16" rx="3"/><path d="m20 25 10 8 10-8"/>',
    'linkedin': '<path d="M22 28v12m7 0V28m0 5c0-7 10-7 10 0v7"/><circle cx="22" cy="23" r="1"/>',
    'resume': '<path d="M22 21h12l6 6v16H22zM34 21v7h6M27 33h8m-8 5h6"/>',
    'github': '<path d="m26 25-7 7 7 7m10-14 7 7-7 7m-3-16-6 18"/>',
}
LABELS = {'website':'Website', 'email':'Email me', 'linkedin':'LinkedIn', 'resume':'Resume', 'github':'GitHub'}


def svg(width, height, title, description, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" role="img" aria-labelledby="title desc">
  <title id="title">{escape(title)}</title>
  <desc id="desc">{escape(description)}</desc>
{body}
</svg>
'''


def button(name, theme):
    p = THEMES[theme]
    primary = name == 'website'
    bg, end = (p['primary'], p['primary_end']) if primary else (p['surface'], p['bg'])
    ink, accent = ('#FFFFFF', '#FFFFFF') if primary else (p['ink'], p['accent'])
    return svg(192, 64, LABELS[name], f'{LABELS[name]} contact link.', f'''
  <defs>
    <linearGradient id="surface" x1="0" y1="0" x2="192" y2="64" gradientUnits="userSpaceOnUse"><stop stop-color="{bg}"/><stop offset="1" stop-color="{end}"/></linearGradient>
    <linearGradient id="edge"><stop stop-color="{p['accent']}" stop-opacity=".8"/><stop offset="1" stop-color="{p['border']}"/></linearGradient>
  </defs>
  <rect x="1" y="1" width="190" height="62" rx="14" fill="url(#surface)" stroke="{'url(#edge)' if primary else p['border']}"/>
  <path d="M21 2h74" stroke="{accent}" stroke-opacity=".3" stroke-linecap="round"/>
  <g stroke="{accent}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</g>
  <text x="53" y="39" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif" font-size="20" font-weight="600" fill="{ink}">{LABELS[name]}</text>
  <path d="M163 37l9-9m-8 0h8v8" stroke="{ink}" stroke-opacity=".75" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
''')


def website_card(theme, mobile=False):
    p = THEMES[theme]
    width, height = (640, 320) if mobile else (960, 224)
    x, y = (528, 241) if mobile else (809, 92)
    radius = 49 if mobile else 53
    body = f'''
  <defs><linearGradient id="panel" x1="0" y1="0" x2="{width}" y2="{height}" gradientUnits="userSpaceOnUse"><stop stop-color="{p['bg']}"/><stop offset="1" stop-color="{p['surface']}"/></linearGradient></defs>
  <rect x="1" y="1" width="{width-2}" height="{height-2}" rx="18" fill="url(#panel)" stroke="{p['border']}"/>
  <path d="M32 31h24" stroke="{p['accent']}" stroke-width="3" stroke-linecap="round"/>
  <text x="68" y="36" font-family="monospace" font-size="13" letter-spacing="1.3" fill="{p['accent']}">EXPLORE / PERSONAL WEBSITE</text>
  <text x="32" y="{'99' if mobile else '96'}" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif" font-size="{'38' if mobile else '42'}" font-weight="650" letter-spacing="-1" fill="{p['ink']}">Beyond the README.</text>
  <text x="32" y="{'143' if mobile else '135'}" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif" font-size="22" fill="{p['muted']}">Visit my personal website.</text>
  <text x="32" y="184" font-family="monospace" font-size="{'21' if mobile else '17'}" fill="{p['accent']}">salah-elshafey.netlify.app</text>
  <g stroke="{p['border']}" stroke-width="1.2">
    <circle cx="{x}" cy="{y}" r="{radius+16}" stroke-dasharray="2 8"/>
    <circle cx="{x}" cy="{y}" r="{radius}"/>
    <ellipse cx="{x}" cy="{y}" rx="{radius*.42}" ry="{radius}"/>
    <path d="M{x-radius} {y}h{radius*2}M{x-radius*.85} {y-24}h{radius*1.7}M{x-radius*.85} {y+24}h{radius*1.7}"/>
  </g>
  <circle cx="{x+radius}" cy="{y}" r="4" fill="{p['accent']}"/>
'''
    bx, by = (32, 225) if mobile else (720, 162)
    body += f'''
  <rect x="{bx}" y="{by}" width="180" height="48" rx="10" fill="{p['primary']}"/>
  <text x="{bx+19}" y="{by+31}" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif" font-size="19" font-weight="600" fill="#FFFFFF">Visit website</text>
  <path d="M{bx+149} {by+29}l10-10m-9 0h9v9" stroke="#FFFFFF" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
'''
    return svg(width, height, 'Beyond the README.', 'Visit Salah Elshafey’s personal website at salah-elshafey.netlify.app.', body)


def main():
    OUT.mkdir(exist_ok=True)
    for theme in THEMES:
        for name in LABELS:
            (OUT/f'{name}-{theme}.svg').write_text(button(name, theme))
        for mobile in [False, True]:
            suffix = '-mobile' if mobile else ''
            (OUT/f'website-card{suffix}-{theme}.svg').write_text(website_card(theme, mobile))
    print('Generated 10 contact buttons and 4 responsive website cards.')


if __name__ == '__main__':
    main()
