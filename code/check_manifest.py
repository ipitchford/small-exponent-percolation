"""Validate the final byte manifest, not mathematical correctness."""
from pathlib import Path, PurePosixPath
import hashlib
import json
import re

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / 'MANIFEST.json').read_text())
entries = manifest.get('files', manifest.get('entries'))
if isinstance(entries, dict):
    entries = [dict(path=k, sha256=v if isinstance(v, str) else v['sha256']) for k,v in entries.items()]
if not isinstance(entries, list) or not entries:
    raise RuntimeError('Manifest must contain a nonempty files or entries collection')
seen = set()
for item in entries:
    name = item.get('path', item.get('file'))
    digest = item.get('sha256')
    if not isinstance(name, str) or not name or '\\' in name:
        raise RuntimeError('Invalid manifest path')
    path = PurePosixPath(name)
    if path.is_absolute() or '..' in path.parts or name in seen or name == 'MANIFEST.json':
        raise RuntimeError('Unsafe, duplicate, or self-referential path: '+name)
    if not isinstance(digest, str) or not re.fullmatch('[0-9a-f]{64}', digest):
        raise RuntimeError('Invalid SHA-256: '+name)
    target = root / name
    if target.is_symlink() or not target.is_file() or not target.resolve().is_relative_to(root):
        raise RuntimeError('Missing or nonregular file: '+name)
    if hashlib.sha256(target.read_bytes()).hexdigest() != digest:
        raise RuntimeError('Hash mismatch: '+name)
    expected_size = item.get('size_bytes')
    if expected_size is not None and target.stat().st_size != expected_size:
        raise RuntimeError('Size mismatch: '+name)
    seen.add(name)
print(json.dumps({'status':'passed', 'checkedFiles':len(seen), 'scope':'byte integrity only'}))
