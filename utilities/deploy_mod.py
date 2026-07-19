#!/usr/bin/env python3
"""Deploy the local Toranaga mod folder into a Starsector mods directory."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path


DEFAULT_MOD_NAME = "Toranaga"
DEFAULT_DEST_ROOT = Path(
    r"C:\Program Files (x86)\Fractal Softworks\Starsector\mods"
)


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy the Toranaga mod directory into Starsector's mods folder."
    )
    parser.add_argument(
        "--mod-dir",
        type=Path,
        default=repo_root() / DEFAULT_MOD_NAME,
        help="Path to the deployable mod directory. Defaults to ../Toranaga.",
    )
    parser.add_argument(
        "--dest-root",
        type=Path,
        default=DEFAULT_DEST_ROOT,
        help=f"Starsector mods folder. Defaults to {DEFAULT_DEST_ROOT}.",
    )
    parser.add_argument(
        "--no-clean",
        action="store_true",
        help="Overlay files onto an existing deployed mod instead of replacing it.",
    )
    return parser.parse_args()


def validate_mod_dir(mod_dir: Path) -> None:
    if not mod_dir.is_dir():
        raise FileNotFoundError(f"Mod directory not found: {mod_dir}")

    mod_info = mod_dir / "mod_info.json"
    if not mod_info.is_file():
        raise FileNotFoundError(f"Expected mod_info.json in mod directory: {mod_info}")


def read_mod_version(mod_dir: Path) -> str:
    mod_info = mod_dir / "mod_info.json"
    with mod_info.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    version = data.get("version")
    if not version:
        raise ValueError(f"Expected version in {mod_info}")

    return str(version)


def deploy(mod_dir: Path, dest_root: Path, clean: bool) -> Path:
    mod_dir = mod_dir.resolve()
    dest_root = dest_root.resolve()
    dest_dir = dest_root / mod_dir.name

    validate_mod_dir(mod_dir)

    if not dest_root.exists():
        raise FileNotFoundError(
            f"Destination mods folder does not exist: {dest_root}\n"
            "Check your Starsector install path or pass --dest-root."
        )

    if clean and dest_dir.exists():
        shutil.rmtree(dest_dir)

    shutil.copytree(mod_dir, dest_dir, dirs_exist_ok=True)
    return dest_dir


def main() -> int:
    args = parse_args()

    try:
        deployed_to = deploy(args.mod_dir, args.dest_root, clean=not args.no_clean)
    except PermissionError as exc:
        print(
            "Permission denied while deploying the mod. Run this script from an "
            "Administrator terminal, or deploy to a writable --dest-root.",
            file=sys.stderr,
        )
        print(f"Details: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"Deploy failed: {exc}", file=sys.stderr)
        return 1

    version = read_mod_version(deployed_to)
    print(f"Deployed {args.mod_dir.resolve()} to {deployed_to}")
    print(f"Version deployed: {version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
