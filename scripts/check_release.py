"""Check release syntax, metadata and example graph integrity without models."""
import ast
import json
import re
import tomllib
from pathlib import Path

root = Path(__file__).resolve().parents[1]
metadata = tomllib.loads((root / "pyproject.toml").read_text(encoding="utf-8"))
assert re.fullmatch(r"[A-Za-z][A-Za-z0-9._-]*", metadata["project"]["name"])
assert re.fullmatch(r"[0-9]+[.][0-9]+[.][0-9]+", metadata["project"]["version"])
assert metadata["project"]["urls"]["Repository"].startswith("https://github.com/mariobilly/")
assert (root / metadata["project"]["license"]["file"]).is_file()
for path in root.rglob("*.py"):
    if any(part.startswith(".") or part == "__pycache__" for part in path.relative_to(root).parts):
        continue
    ast.parse(path.read_text(encoding="utf-8-sig"), filename=str(path))
for path in root.rglob("*.json"):
    if any(part.startswith(".") for part in path.relative_to(root).parts):
        continue
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict) or not isinstance(data.get("nodes"), list):
        continue
    nodes = {n["id"]: n for n in data["nodes"]}
    assert len(nodes) == len(data["nodes"]), f"Duplicate node IDs: {path}"
    for link in data.get("links", []):
        if not isinstance(link, list):
            continue  # Newer frontend graph formats can use object links.
        number, source, source_slot, target, target_slot, kind = link
        assert source in nodes and target in nodes, f"Dangling link: {path}"
        assert 0 <= source_slot < len(nodes[source].get("outputs", [])), f"Invalid source slot: {path}"
        assert 0 <= target_slot < len(nodes[target].get("inputs", [])), f"Invalid target slot: {path}"
        assert nodes[target]["inputs"][target_slot].get("link") == number, f"Mismatched link: {path}"
print("Release syntax, metadata and example graph checks passed")
