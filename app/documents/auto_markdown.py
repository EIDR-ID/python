#!/usr/bin/env python
"""
Generate Markdown documentation from Python source files.

• If called with arguments: behaves like the original script
    python docgen.py <input_path> [output_dir]

• If called with **no** arguments: scans every *.py file one directory up
  (../*) and drops the .md files in the current working directory.
"""
from __future__ import annotations

import ast
import os
import re
import sys
from typing import Iterable, List, Optional
from collections import defaultdict
import ast
from pathlib import Path
from typing import List
# ─────────────────────────────────────────────────────────────────────────────
#  Docstring parsing helpers
# ─────────────────────────────────────────────────────────────────────────────
SECTION_HEADERS = [
    "Args", "Arguments", "Parameters",
    "Returns", "Raises", "Note", "Notes"
]

_param_re = re.compile(r":param\s+(\w+)\s*:\s*(.*)")
_return_re = re.compile(r":return[s]?\s*:\s*(.*)")
_rtype_re = re.compile(r":rtype\s*:\s*(.*)")
_raises_re = re.compile(r":raises\s+([\w\.]+)\s*:\s*(.*)")

INIT_FILE = "__init__.py"
SCHEMA_DIR_PATTERN = re.compile(r"schem[ae]$", re.IGNORECASE)

def is_bullet(line: str) -> bool:
    stripped = line.strip()
    return stripped.startswith(("-", "*"))


def parse_docstring(doc: Optional[str]) -> str:
    """
    Convert a docstring into Markdown with unified section headings.

    Supports both Google/Numpy-style explicit headers **and**
    Sphinx/ReST field‑lists such as ``:param foo:``.
    """
    if not doc:
        return "*No docstring.*"

    lines: List[str] = doc.strip().splitlines()
    output: List[str] = []

    current_section: Optional[str] = None
    sections_found = False
    buffer: List[str] = []

    def flush_description() -> None:
        if buffer:
            output.append("\n**Description:**\n")
            output.append("\n".join(buffer) + "\n")
            buffer.clear()

    for raw in lines:
        line = raw.rstrip()

        # 1 ▸ Explicit section header like "Parameters:"
        header = next(
            (h for h in SECTION_HEADERS
             if line.strip().startswith(h + ":")),
            None
        )
        if header:
            sections_found = True
            flush_description()
            current_section = header
            rest = line[len(header) + 1:].strip()

            output.append(f"\n**{header}:**\n")
            if rest:
                output.append(rest)
            continue

        # 2 ▸ Sphinx/ReST field‑list lines
        stripped = line.lstrip()
        m_param = _param_re.match(stripped)
        m_return = _return_re.match(stripped)
        m_rtype = _rtype_re.match(stripped)
        m_raises = _raises_re.match(stripped)

        if m_param:
            sections_found = True
            flush_description()
            if current_section != "Parameters":
                output.append("\n**Parameters:**\n")
                current_section = "Parameters"
            name, desc = m_param.groups()
            output.append(f"- **{name}**: {desc or ''}")
            continue

        if m_return:
            sections_found = True
            flush_description()
            if current_section != "Returns":
                output.append("\n**Returns:**\n")
                current_section = "Returns"
            output.append(m_return.group(1))
            continue

        if m_rtype:
            if current_section != "Returns":
                output.append("\n**Returns:**\n")
                current_section = "Returns"
            output.append(f"Type: {m_rtype.group(1)}")
            continue

        if m_raises:
            sections_found = True
            flush_description()
            if current_section != "Raises":
                output.append("\n**Raises:**\n")
                current_section = "Raises"
            exc, desc = m_raises.groups()
            output.append(f"- **{exc}**: {desc or ''}")
            continue

        # 3 ▸ Plain text
        if not sections_found:
            buffer.append(line)
        elif current_section:
            if is_bullet(line):
                output.append(line)
            elif re.match(r"\s{2,}[\w\-]+", line):
                output.append(f"- {line.strip()}")
            elif line.strip():
                output.append(line)

    flush_description()
    return "\n".join(output)


# ─────────────────────────────────────────────────────────────────────────────
#  Source‑to‑Markdown converter
# ─────────────────────────────────────────────────────────────────────────────



def extract_to_markdown(path: str | Path) -> str:
    """
    Parse *path* and return a Markdown string with module, class, and
    callable docstrings.  Items lacking a docstring are skipped and recorded
    in a “Missing docstrings” appendix at the end of the document.
    """
    path = Path(path)
    node = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))

    md_lines: List[str] = [f"# Documentation for `{path.name}`\n"]
    missing: defaultdict[str, List[str]] = defaultdict(list)  # type ➟ [names]

    # ── module docstring ────────────────────────────────────────────────────
    mod_doc = ast.get_docstring(node)
    if mod_doc:
        md_lines.append("## Module Docstring\n\n" + parse_docstring(mod_doc) + "\n")
    else:
        ...
        #missing["Module"].append(path.stem)

    # ── top‑level definitions ───────────────────────────────────────────────
    for top in node.body:
        if isinstance(top, ast.FunctionDef):
            doc = ast.get_docstring(top)
            if doc:
                md_lines.append(
                    f"### Function: `{top.name}`\n\n{parse_docstring(doc)}\n"
                )
            else:
                missing["Function"].append(top.name)

        elif isinstance(top, ast.ClassDef):
            cls_name = top.name
            cls_doc = ast.get_docstring(top)
            if cls_doc:
                md_lines.append(
                    f"## Class: `{cls_name}`\n\n{parse_docstring(cls_doc)}\n"
                )
            else:
                missing["Class"].append(cls_name)

            # methods
            for item in top.body:
                if isinstance(item, ast.FunctionDef):
                    m_doc = ast.get_docstring(item)
                    meth_sig = f"{cls_name}.{item.name}"
                    if m_doc:
                        md_lines.append(
                            f"### Method: `{item.name}`\n\n{parse_docstring(m_doc)}\n"
                        )
                    else:
                        missing["Method"].append(meth_sig)

    # ── add appendix if anything is missing ────────────────────────────────
    if missing:
        md_lines.append("\n## Missing docstrings\n")
        for kind, names in missing.items():
            for name in names:
                md_lines.append(f"- **{kind}** `{name}`")

    return "\n".join(md_lines)


# ─────────────────────────────────────────────────────────────────────────────
#  Main program
# ─────────────────────────────────────────────────────────────────────────────
def write_markdown_file(source_path: str | Path, output_dir: Path) -> None:
    markdown = extract_to_markdown(source_path)
    filename = Path(source_path).stem + ".md"
    out_path = output_dir / filename
    out_path.write_text(markdown, encoding="utf-8")
    print(f"✅ Markdown written to {out_path}")


def iter_py_files(root: Path) -> Iterable[Path]:
    """
    Yield every *.py file under *root* **except**

    • any file named ``__init__.py``
    • anything that lives inside a directory whose name ends with
      “schema” or “scheme” (case‑insensitive).
    """
    for dirpath, dirnames, files in os.walk(root):
        # ── remove schema/scheme‑style dirs from traversal ───────────────────
        dirnames[:] = [
            d for d in dirnames if not SCHEMA_DIR_PATTERN.match(d)
        ]

        for filename in files:
            if (
                filename.endswith(".py")
                and filename != INIT_FILE
            ):
                yield Path(dirpath) / filename


if __name__ == "__main__":
    # 1 ▸ Resolve input/output paths
    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1]).resolve()
        output_dir = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else Path.cwd()
    else:
        input_path = Path.cwd().parent.resolve()   # ../
        output_dir = Path.cwd()
        print(f"[info] No arguments given → scanning {input_path} …")

    output_dir.mkdir(parents=True, exist_ok=True)

    if input_path.is_dir():
        for py_file in iter_py_files(input_path):
            write_markdown_file(py_file, output_dir)
    else:
        # Single‑file mode: still honour the skip rules
        if (
                input_path.name != INIT_FILE
                and not any(
            SCHEMA_DIR_PATTERN.match(p.name) for p in input_path.parents
        )
        ):
            write_markdown_file(input_path, output_dir)
