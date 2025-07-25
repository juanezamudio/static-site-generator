from textnode import TextNode, TextType
from htmlnode import HTMLNode
from os import path, listdir, mkdir
from shutil import copy, rmtree

dir_path_static = "./static"
dir_path_public = "./public"

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

def main():
    # text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    # html_node = HTMLNode("p", "This is a paragraph", None, {"href": "https://www.google.com"})

    # print(text_node)
    # print(html_node)

    print("Copying static files to public directory...")
    copy_static(dir_path_static, dir_path_public)

main()