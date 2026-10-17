"""Check packaged Skill, relative documentation links, gallery and ZIP integrity."""
from pathlib import Path
import hashlib
import json
import re
import zipfile
import sys
from urllib.parse import unquote

root = Path(__file__).resolve().parents[1]
errors = []
skill = root / 'skills/product-storytelling-studio'
expected = json.loads((root / 'dist/skill-sha256.json').read_text(encoding='utf-8'))
for name,digest in expected.items():
    path = skill / name
    if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest()!=digest:
        errors.append('Skill missing or changed: '+name)
for path in root.rglob('*.md'):
    text = path.read_text(encoding='utf-8-sig')
    for match in re.finditer(r'\]\(([^)]+)\)',text):
        target = match.group(1).strip().strip('<>')
        if re.match(r'^(?:https?://|mailto:|#)',target):
            continue
        target = unquote(target.split('#',1)[0])
        if target and not (path.parent/target).exists():
            errors.append(f'Broken relative link: {path.relative_to(root)} -> {target}')
    if re.search(r'C:[\\/]Users[\\/]USER[\\/]',text):
        errors.append('Personal local path in '+str(path.relative_to(root)))
samples = json.loads((root/'gallery/manifest.json').read_text(encoding='utf-8'))['samples']
if len(samples)!=31 or len({s['key'] for s in samples})!=31:
    errors.append('Gallery should contain 31 unique styles.')
for s in samples:
    if not (root/'gallery'/s['file']).is_file():
        errors.append('Missing gallery image: '+s['file'])
with zipfile.ZipFile(root/'dist/product-storytelling-studio.zip') as z:
    if z.testzip() is not None:
        errors.append('Skill ZIP integrity failure.')
    for name,digest in expected.items():
        data=z.read('product-storytelling-studio/'+name)
        if hashlib.sha256(data).hexdigest()!=digest:
            errors.append('ZIP differs from Skill: '+name)
for p in root.rglob('*'):
    if p.is_file() and '.git' not in p.parts:
        if p.stat().st_size>=100*1024**2:
            errors.append('File exceeds ordinary GitHub size limit: '+str(p.relative_to(root)))
        if p.suffix in ('.md','.json','.txt','.py','.yaml','.html'):
            text=p.read_text(encoding='utf-8-sig')
            if re.search(r'(?:ghp_[A-Za-z0-9]{25,}|github_pat_[A-Za-z0-9_]{35,}|sk-proj-[A-Za-z0-9_-]{25,})',text):
                errors.append('Credential-shaped content: '+str(p.relative_to(root)))
if errors:
    print('\n'.join(errors));sys.exit(1)
print(json.dumps({'skill_files':len(expected),'look_samples':len(samples),'relative_links':'OK','install_zip':'OK'},ensure_ascii=False))
