from textnode import TextNode, TextType
from markdown_blocks import markdown_to_html_node
import shutil
import os

def main():
    copy_static_to_public("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")



def copy_static_to_public(src, dst):
    shutil.rmtree(dst, ignore_errors=True)
    os.makedirs(dst, exist_ok=True)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            os.mkdir(d)
            copy_static_to_public(s, d)
        else:
            shutil.copy2(s,d)

def extract_title(markdown: str) -> str:
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("Not a Header.")

def generate_page(from_path, template_path, dest_path):
    print (f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as from_path_read:
        from_data = from_path_read.read()
    with open(template_path) as template_path_read:
        template_data = template_path_read.read()

    mdtohtmlstring = markdown_to_html_node(from_data).to_html()
    title = extract_title(from_data)

    page = template_data.replace("{{ Title }}", title).replace("{{ Content }}", mdtohtmlstring)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(page)


main()
