"""Build static HTML: set postponed=false in site-state.json and run this script to restore.
The original landing is kept intact as source; both page and crawler metadata switch together.
"""
from pathlib import Path
import json
import re
ROOT = Path(__file__).resolve().parents[1]
original = (ROOT / 'archive/index-before-postponement-20261008.html.txt').read_text()
state = json.loads((ROOT / 'site-state.json').read_text())
assert isinstance(state['postponed'], bool), 'postponed must be a boolean'
if not state['postponed']:
    result = original
else:
    notice = (ROOT / 'scripts/postponement-page.html').read_text()
    old_body = re.search(r'<body\b[^>]*>(.*?)</body>', original, re.S).group(1)
    # Scripts remain in the preserved DOM but cannot execute/load the old ticket widget.
    def inert_script(match):
        attrs = re.sub(r'\s+type\s*=\s*([\"\']).*?\1', '', match.group(1), flags=re.I)
        return '<script type="text/plain" data-postponement-disabled="true"' + attrs + '>'
    old_body = re.sub(r'<script\b([^>]*)>', inert_script, old_body, flags=re.I)
    preserved = '<div id="preserved-site" hidden inert aria-hidden="true">' + old_body + '</div>'
    notice = notice.replace('<body>', '<body class="postponement-active">' + preserved + '<div id="postponement-overlay" role="dialog" aria-modal="true" aria-labelledby="notice-title" tabindex="-1">')
    notice = notice.replace('</body>', '</div>\n</body>')
    notice = notice.replace('<style>', '''<style>
    html:has(.postponement-active), body.postponement-active {overflow:hidden!important}
    #preserved-site {display:none!important;pointer-events:none!important}
    #postponement-overlay {position:fixed;inset:0;z-index:2147483647;overflow:auto;background:#211d19;overscroll-behavior:contain}
''')
    result = notice
(ROOT / 'index.html').write_text(result)
print('Built', 'postponement overlay' if state['postponed'] else 'original landing')
