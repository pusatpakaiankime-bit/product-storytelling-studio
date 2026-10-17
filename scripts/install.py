"""Install the packaged Skill locally; no network or additional dependencies."""
from __future__ import annotations
import argparse
import os
from pathlib import Path
import shutil
import zipfile
from datetime import datetime
import uuid

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dest", type=Path, help="Exact destination Skill folder")
    parser.add_argument("--update", action="store_true", help="Back up then update an existing Skill")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    source = root / "skills" / "product-storytelling-studio"
    codex_root = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))).expanduser()
    destination = (args.dest or codex_root / "skills" / source.name).expanduser().resolve()
    if not (source / "SKILL.md").is_file():
        parser.error("The packaged SKILL.md was not found.")
    if destination == source.resolve() or destination == Path.home().resolve() or destination.parent == destination:
        parser.error("Choose a dedicated destination Skill folder.")
    if destination.exists() and not args.update:
        parser.error(f"Destination exists: {destination}\nUse --update after reviewing local edits.")
    if destination.exists():
        if not (destination / "SKILL.md").is_file():
            parser.error("Existing destination is not a Skill folder; refusing to overwrite.")
        backup_root = destination.parent.parent / "skill-backups"
        backup_root.mkdir(parents=True, exist_ok=True)
        tag = datetime.now().strftime("%Y%m%d-%H%M%S") + "-" + uuid.uuid4().hex[:8]
        backup = backup_root / f"product-storytelling-studio-{tag}.zip"
        with zipfile.ZipFile(backup, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for path in sorted(destination.rglob("*")):
                if path.is_file():
                    archive.write(path, str(Path(destination.name) / path.relative_to(destination)))
        print(f"Backup: {backup}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination, dirs_exist_ok=args.update)
    print(f"Installed: {destination}")
    print("The Skill will be available on your next Codex turn.")

if __name__ == "__main__":
    main()

