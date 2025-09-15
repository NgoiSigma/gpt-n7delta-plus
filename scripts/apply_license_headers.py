#!/usr/bin/env python3
import pathlib, sys

SPDX = "SPDX-License-Identifier: AGPL-3.0-or-later"

EXTS = {".py", ".js", ".ts", ".sh", ".go", ".rs", ".java", ".c", ".h", ".cpp"}
COMMENT = {
    ".py": "# ", ".sh": "# ",
    ".js": "// ", ".ts": "// ",
    ".go": "// ", ".rs": "// ",
    ".java": "// ", ".c": "/* ", ".h": "/* ", ".cpp": "/* "
}

def needs_header(text): return SPDX not in text.splitlines()[:5]

for p in pathlib.Path(sys.argv[1] if len(sys.argv)>1 else ".").rglob("*"):
    if p.suffix in EXTS and p.is_file():
        t = p.read_text(encoding="utf-8", errors="ignore")
        if needs_header(t):
            if p.suffix in {".c", ".h", ".cpp"}:
                hdr = f"{COMMENT[p.suffix]}{SPDX} */\n"
            else:
                hdr = f"{COMMENT[p.suffix]}{SPDX}\n"
            p.write_text(hdr + t, encoding="utf-8")
            print("Added SPDX:", p)
