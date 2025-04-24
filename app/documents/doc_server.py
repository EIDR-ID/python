#!/usr/bin/env python3
"""
doc_server.py – browse generated Markdown documentation in a web browser.

Usage
-----
    python doc_server.py [docs_dir] [port]

    docs_dir : directory that holds *.md files (default = current directory)
    port     : port number for the web server (default = 8000)

Features
--------
* Landing page (/) lists every Markdown file, grouped by parent package.
* Each Markdown file is converted to HTML on demand using the `markdown` lib.
* Pure std‑lib server aside from that single dependency.

Install requirement
-------------------
    pip install markdown
"""
from __future__ import annotations

import http.server
import os
import socketserver
import sys
import urllib.parse
from pathlib import Path

import markdown # pip install markdown

# ────────────────────────────────────────────────────────────────────────────
#  Configuration from CLI args
# ────────────────────────────────────────────────────────────────────────────
DOCS_DIR = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 8000

# ────────────────────────────────────────────────────────────────────────────
#  Build an in‑memory index  {module → [Path, …]}
#    The module key is the dotted package path derived from folders.
# ────────────────────────────────────────────────────────────────────────────
def build_index(root: Path) -> dict[str, list[Path]]:
    index: dict[str, list[Path]] = {}
    for md_path in root.rglob("*.md"):
        rel = md_path.relative_to(root)
        package_parts = rel.parts[:-1]  # folders above the md file
        module = ".".join(package_parts) if package_parts else "root"
        index.setdefault(module, []).append(rel)
    return index


MODULE_INDEX = build_index(DOCS_DIR)

# ────────────────────────────────────────────────────────────────────────────
#  Helper to wrap HTML
# ────────────────────────────────────────────────────────────────────────────
def wrap_html(title: str, body: str) -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>
  :root {{
    --bg: #ffffff;
    --fg: #1a1a1a;
    --code-bg: #f4f4f4;
  }}

  /* ↓ automatic dark colours */
  @media (prefers-color-scheme: dark) {{
    :root {{
      --bg: #121212;
      --fg: #e0e0e0;
      --code-bg: #1e1e1e;
    }}
  }}

  body {{ background: var(--bg); color: var(--fg);
         font-family: system-ui, sans-serif;
         max-width: 1000px; margin: 0 auto; padding: 1rem; }}
  pre,code {{ background: var(--code-bg); padding: 2px 4px;
              border-radius: 4px; }}
  nav {{ margin-bottom: 2rem; }}
</style>
</head>
<body>
{body}
</body>
</html>"""



def render_index() -> str:
    """Generate the landing page HTML."""
    parts = ["<h1>Documentation index</h1>"]
    for module in sorted(MODULE_INDEX):
        parts.append(f"<h2>{module}</h2>\n<ul>")
        for rel_path in sorted(MODULE_INDEX[module]):
            url = urllib.parse.quote(str(rel_path).replace(os.sep, "/"))
            parts.append(f'<li><a href="/{url}">{rel_path.stem}</a></li>')
        parts.append("</ul>")
    return wrap_html("Docs index", "\n".join(parts))


def render_markdown_file(md_file: Path) -> str:
    """Read *md_file*, convert to HTML, and wrap in a basic template."""
    html = markdown.markdown(
        md_file.read_text(encoding="utf-8"),
        extensions=["fenced_code", "tables"],
    )
    return wrap_html(md_file.stem, html)


# ────────────────────────────────────────────────────────────────────────────
#  HTTP request handler
# ────────────────────────────────────────────────────────────────────────────
class DocHandler(http.server.SimpleHTTPRequestHandler):
    """Serve the index or individual Markdown pages."""

    def do_GET(self):
        # Strip leading slash, percent‑decode
        req_path = urllib.parse.unquote(self.path.lstrip("/"))

        if req_path == "":
            # ── landing page
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(render_index().encode())
            return

        md_path = (DOCS_DIR / req_path).resolve()

        # Prevent path‑traversal outside DOCS_DIR
        if not str(md_path).startswith(str(DOCS_DIR)):
            self.send_error(404, "Not found")
            return

        if md_path.is_file() and md_path.suffix == ".md":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(render_markdown_file(md_path).encode())
        else:
            self.send_error(404, "Not found")


# ────────────────────────────────────────────────────────────────────────────
#  Run server
# ────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print(f"Serving docs from {DOCS_DIR} on http://localhost:{PORT}")
    with socketserver.TCPServer(("", PORT), DocHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down.")
