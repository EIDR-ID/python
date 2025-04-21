import ast
import sys
import re
import os

SECTION_HEADERS = ["Args", "Arguments", "Parameters", "Returns", "Raises", "Note", "Notes"]


def is_bullet(line):
    stripped = line.strip()
    return stripped.startswith(("-", "*"))


def parse_docstring(doc):
    if not doc:
        return "*No docstring.*"

    lines = doc.strip().splitlines()
    output = []
    current_section = None
    buffer = []
    sections_found = False

    def flush_description():
        if buffer:
            output.append("\n**Description:**\n")
            output.append("\n".join(buffer) + "\n")
            buffer.clear()

    for line in lines:
        line = line.rstrip()

        # Detect section header line (with or without inline content)
        section_match = next((sh for sh in SECTION_HEADERS if line.strip().startswith(sh + ":")), None)

        if section_match:
            sections_found = True
            flush_description()
            current_section = section_match
            rest = line[len(section_match) + 1:].strip()

            output.append(f"\n**{current_section}:**\n")
            if rest:
                output.append(rest)
            continue

        if not sections_found:
            buffer.append(line)
        elif current_section:
            if is_bullet(line.strip()):
                output.append(line)
            elif re.match(r"\s{2,}[\w\-]+", line):
                output.append(f"- {line.strip()}")
            elif line.strip():
                output.append(line)
        else:
            output.append(line)

    flush_description()
    return "\n".join(output)


def extract_to_markdown(path):
    with open(path) as f:
        node = ast.parse(f.read(), filename=path)
        md_lines = []

        md_lines.append(f"# Documentation for `{path}`\n")

        mod_doc = ast.get_docstring(node)
        if mod_doc:
            md_lines.append(f"## Module Docstring\n\n{parse_docstring(mod_doc)}\n")

        for n in node.body:
            if isinstance(n, ast.FunctionDef):
                doc = parse_docstring(ast.get_docstring(n))
                md_lines.append(f"### Function: `{n.name}`\n\n{doc}\n")

            elif isinstance(n, ast.ClassDef):
                cls_doc = parse_docstring(ast.get_docstring(n))
                md_lines.append(f"## Class: `{n.name}`\n\n{cls_doc}\n")

                for item in n.body:
                    if isinstance(item, ast.FunctionDef):
                        method_doc = parse_docstring(ast.get_docstring(item))
                        md_lines.append(f"### Method: `{item.name}`\n\n{method_doc}\n")

        return '\n'.join(md_lines)


if __name__ == "__main__":
    input_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else os.getcwd()

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    def write_markdown_file(source_path):
        markdown = extract_to_markdown(source_path)
        filename = os.path.splitext(os.path.basename(source_path))[0] + ".md"
        out_path = os.path.join(output_dir, filename)

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(markdown)

        print(f"✅ Markdown written to {out_path}")

    if os.path.isdir(input_path):
        for root, _, files in os.walk(input_path):
            for file in files:
                if file.endswith(".py"):
                    full_path = os.path.join(root, file)
                    write_markdown_file(full_path)
    else:
        write_markdown_file(input_path)
