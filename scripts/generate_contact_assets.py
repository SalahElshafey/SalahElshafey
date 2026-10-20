#!/usr/bin/env python3
"""Generate original SVG contact, navigation, and repository actions."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets' / 'contact'
ACTION_OUT = ROOT / 'assets' / 'actions'
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
    'x': '<path d="m21 22 18 20M39 22 21 42"/>',
    'facebook': '<path d="M34 21h-4c-4 0-5 3-5 7v15m-6-13h15"/>',
}
LABELS = {'website':'Website', 'email':'Email me', 'linkedin':'LinkedIn', 'resume':'Resume', 'github':'GitHub',
          'x':'X / Twitter', 'facebook':'Facebook'}
CONTACT_LINKS = {
    'website':'https://salah-elshafey.netlify.app/',
    'email':'mailto:Salaheldinelshafie@gmail.com',
    'linkedin':'https://www.linkedin.com/in/salah-elshafey/',
    'resume':'https://drive.google.com/file/d/1Vv9GS6_QjldfRYYANVyX-hqmCcank_7z/view?usp=sharing',
    'github':'https://github.com/SalahElshafey',
    'x':'https://twitter.com/salah_elshafie',
    'facebook':'https://fb.com/salah.cx',
}
# Labels, destinations, and artwork identity live together for maintenance and
# destination validation. README anchors still work without a runtime script.
ACTIONS = {
    'nav-approach':dict(kind='navigation',label='Approach',detail='',href='#data-models-systems'),
    'nav-work':dict(kind='navigation',label='Selected work',detail='',href='#selected-engineering-work'),
    'nav-toolbox':dict(kind='navigation',label='Toolbox',detail='',href='#technical-toolbox'),
    'nav-connect':dict(kind='navigation',label='Connect',detail='',href='#lets-build-something-meaningful'),
    'repo-edge':dict(kind='repository',label='Explore repository',detail='Edge SLM',href='https://github.com/SalahElshafey/Edge-SLM-Offline-Domain-Specific-Small-Language-Model-Pipeline'),
    'repo-hpc':dict(kind='repository',label='Explore repository',detail='Distributed LLM fine-tuning',href='https://github.com/SalahElshafey/VT-Cluster--Parallel-and-Distributed-Programming-of-Machine-Learning-Models'),
    'repo-gpt':dict(kind='repository',label='Explore repository',detail='GPT Visualization',href='https://github.com/SalahElshafey/GPT-Visualization'),
    'repo-aria':dict(kind='repository',label='Explore repository',detail='Aria object recognition',href='https://github.com/SalahElshafey/RGU-Aria-Meta-Glasses-Object-Recognition-in-Daily-Life'),
    'repo-vr':dict(kind='repository',label='Explore repository',detail='Virtual Reality Fitness Trainer',href='https://github.com/SalahElshafey/Virtual-Reality-Fitness-Trainer'),
    'repo-home':dict(kind='repository',label='Explore repository',detail='Home Security App',href='https://github.com/SalahElshafey/HomeSecurityApp'),
    'extra-opencv':dict(kind='exploration',label='Image processing',detail='OpenCV experiments',href='https://github.com/SalahElshafey/Image-Processing'),
    'extra-desktop':dict(kind='exploration',label='Desktop software',detail='C# application',href='https://github.com/SalahElshafey/Computer-System-Company'),
    'extra-air-hockey':dict(kind='exploration',label='Air hockey',detail='OpenGL',href='https://github.com/SalahElshafey/Air-Hockey_OpenGL'),
    'extra-url-saver':dict(kind='exploration',label='URL Saver',detail='JavaScript browser extension',href='https://github.com/SalahElshafey/URL-Saver-Extension'),
    'activity-repos':dict(kind='activity',label='Repositories',detail='Browse my public work',href='https://github.com/SalahElshafey?tab=repositories'),
    'activity-contributions':dict(kind='activity',label='Contributions',detail='View GitHub activity',href='https://github.com/SalahElshafey?tab=overview'),
}


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


def action(name, theme, mobile=False):
    p = THEMES[theme]
    item = ACTIONS[name]
    navigation = item['kind'] == 'navigation'
    repository = item['kind'] == 'repository'
    width, height = (176, 48) if navigation else ((640, 96) if repository and not mobile else (400, 96))
    title = item['label']
    if navigation:
        return svg(width, height, title, f'Jump to {title.lower()}.', f'''
  <rect x="1" y="1" width="174" height="46" rx="23" fill="{p['bg']}" stroke="{p['border']}"/>
  <text x="79" y="30" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif" font-size="18" font-weight="500" fill="{p['ink']}">{escape(title)}</text>
  <path d="m145 22 4 4-4 4" stroke="{p['accent']}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
''')
    accent = p['accent']
    if name in {'repo-hpc','repo-vr','extra-desktop','activity-contributions'}:
        accent = '#AD96FF' if theme == 'dark' else '#6941C6'
    elif name in {'repo-home','extra-air-hockey'}:
        accent = '#49E3C2' if theme == 'dark' else '#087D68'
    tx = 80 if width == 640 else 67
    size = 24 if width == 640 else 21
    ax = width-46
    return svg(width, height, f'{title}: {item["detail"]}', f'{title}. {item["detail"]}.', f'''
  <defs>
    <linearGradient id="surface" x1="0" y1="0" x2="{width}" y2="96" gradientUnits="userSpaceOnUse"><stop stop-color="{p['surface']}"/><stop offset="1" stop-color="{p['bg']}"/></linearGradient>
    <linearGradient id="edge"><stop stop-color="{accent}" stop-opacity=".8"/><stop offset=".65" stop-color="{p['border']}"/></linearGradient>
  </defs>
  <rect x="1" y="1" width="{width-2}" height="94" rx="14" fill="url(#surface)" stroke="url(#edge)"/>
  <path d="M22 2h92" stroke="{accent}" stroke-opacity=".3" stroke-linecap="round"/>
  <rect x="17" y="27" width="36" height="41" rx="9" fill="{p['bg']}" stroke="{p['border']}"/>
  <g fill="{p['bg']}" stroke="{accent}" stroke-width="1.5" stroke-linecap="round">
    <path d="M29 38v20m0-11h5c7 0 8-3 8-8"/>
    <circle cx="29" cy="36" r="3"/><circle cx="29" cy="60" r="3"/><circle cx="42" cy="36" r="3"/>
  </g>
  <text x="{tx}" y="40" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif" font-size="{size}" font-weight="600" fill="{p['ink']}">{escape(title)}</text>
  <text x="{tx}" y="68" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif" font-size="{'18' if width==640 else '16'}" fill="{p['muted']}">{escape(item['detail'])}</text>
  <rect x="{ax-5}" y="32" width="32" height="32" rx="9" fill="{p['bg']}" stroke="{p['border']}"/>
  <path d="M{ax+4} 53l12-12m-11 0h11v11" stroke="{accent}" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>
''')


def main():
    OUT.mkdir(exist_ok=True)
    ACTION_OUT.mkdir(exist_ok=True)
    for theme in THEMES:
        for name in LABELS:
            (OUT/f'{name}-{theme}.svg').write_text(button(name, theme))
        for mobile in [False, True]:
            suffix = '-mobile' if mobile else ''
            (OUT/f'website-card{suffix}-{theme}.svg').write_text(website_card(theme, mobile))
        for name, item in ACTIONS.items():
            (ACTION_OUT/f'{name}-{theme}.svg').write_text(action(name, theme))
            if item['kind'] == 'repository':
                (ACTION_OUT/f'{name}-mobile-{theme}.svg').write_text(action(name, theme, True))
    print('Generated 14 contact buttons, 4 website cards, and 44 portfolio action variants.')


if __name__ == '__main__':
    main()
