#!/usr/bin/env python3
"""Copy built add-on zips into addons/ so the Kodi repository publishes them.

For add-ons developed in their own repositories that ship release zips (not git subtrees): the LG webOS TV
add-on (dangerouslaser/kodi-webos-control, `python3 scripts/build_zip.py`) and the Estuary LG skin
(dangerouslaser/skin.estuary.lg, same). Each zip's top folder is the add-on id; addons/<id>/ is replaced with the
zip's contents, so only runtime files are bundled. Run it with the new zips, then bump and tag a release.

  python3 tools/sync_bundled_addons.py ../kodi-webos-control/dist/service.webostv-0.5.1.zip \
      ../skin.estuary.lg/dist/skin.estuary.lg-4.1.0+lg.3.zip
"""

from __future__ import annotations

import shutil
import sys
import zipfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = {"service.webostv", "skin.estuary.lg"}


def sync(zip_path: Path) -> str:
    with zipfile.ZipFile(zip_path) as archive:
        names = [n for n in archive.namelist() if not n.endswith("/")]
        tops = {PurePosixPath(n).parts[0] for n in names}
        if len(tops) != 1 or not tops <= ALLOWED:
            raise SystemExit(f"{zip_path}: expected one top folder in {sorted(ALLOWED)}, got {sorted(tops)}")
        addon_id = tops.pop()
        for name in names:
            parts = PurePosixPath(name).parts
            if ".." in parts or PurePosixPath(name).is_absolute():
                raise SystemExit(f"{zip_path}: unsafe path {name}")
        target = ROOT / "addons" / addon_id
        if target.exists():
            shutil.rmtree(target)
        for name in names:
            destination = ROOT / "addons" / name
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(archive.read(name))
    return addon_id


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    for arg in sys.argv[1:]:
        print(f"{sync(Path(arg))}: synced from {arg}")


if __name__ == "__main__":
    main()
