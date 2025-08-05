from textnode import TextNode, TextType
from htmlnode import HTMLNode
from os import path, listdir, mkdir, makedirs
from shutil import copy, rmtree
import re
import sys
from html_node_markdown import markdown_to_html_node

dir_path_static = "static"
dir_path_docs = "docs"
dir_path_content = "content"
dir_path_template = "template.html"

def copy_static(src, dst):
    if path.exists(dst):
        rmtree(dst)

    mkdir(dst)

    files = listdir(src)

    for file in files:
        src_path = path.join(src, file)
        dst_path = path.join(dst, file)
        print(f" * {src_path} -> {dst_path}")

        if path.isfile(src_path):
            copy(src_path, dst_path)
        else:
            copy_static(src_path, dst_path)

def extract_title(markdown):
    # Split the markdown into lines
    lines = markdown.split('\n')
    
    # Look for the first line that starts with #
    for line in lines:
        match = re.match(r"#+\s+(.*)", line.strip())
        if match:
            return match.group(1).strip()
    
    # If no header is found, raise an exception
    raise Exception("There is no header in the markdown")

def generate_page(from_path, template_path, dest_path, base_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path} with base path {base_path}")

    with open(from_path, "r") as markdown_file:
        markdown = markdown_file.read()

    with open(template_path, "r") as template_file:
        template = template_file.read()

    html_string = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_string)
    template = template.replace('href="/', f'href="{base_path}')
    template = template.replace('src="/', f'src="{base_path}')
    template = template.replace('url(/', f"url('{base_path}")
    template = template.replace("url(/", f'url("{base_path}')


    if path.dirname(dest_path):
        makedirs(path.dirname(dest_path), exist_ok=True)
    
    with open(dest_path, "w") as dest_file:
        dest_file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dir_path_docs, base_path):
    files = listdir(dir_path_content)

    for file in files:
        src_path = path.join(dir_path_content, file)
        dest_path = path.join(dir_path_docs, file)

        if path.isfile(src_path):
            if file.endswith(".md"):
                html_file = file[:-3] + ".html"
                dest_path = path.join(dir_path_docs, html_file)
            generate_page(src_path, template_path, dest_path, base_path)
        else:
            generate_pages_recursive(src_path, template_path, dest_path, base_path)

def main():
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    else:
        base_path = "/"
    
    # Make sure base_path ends with a slash
    if not base_path.endswith("/"):
        base_path += "/"
    
    print(f"Using base path: '{base_path}'")  # Debug print
    
    print("Deleting docs directory...")
    if path.exists(dir_path_docs):
        rmtree(dir_path_docs)

    print("Copying static files to docs directory...")
    copy_static(dir_path_static, dir_path_docs)

    print("Generating pages...")
    generate_pages_recursive(
        dir_path_content,
        dir_path_template,
        dir_path_docs,
        base_path  # Make sure this is passed through
    )

main()