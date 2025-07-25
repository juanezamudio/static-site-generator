from textnode import TextType, TextNode, text_node_to_html_node
from block import BlockType
from htmlnode import HTMLNode
from block_markdown import markdown_to_blocks
from block import block_to_block_type
from inline_markdown import text_to_textnodes
import re
import itertools

def markdown_to_html_node(markdown):
    return convert_to_blocks(markdown)

def header_block_to_html_node(block):
    counter = 0

    for char in block:
        match char:
            case '#': 
                counter += 1
            case _: break
    
    stripped_block = block[counter:].lstrip()
    header = ""

    match counter:
        case 1: header = "h1"
        case 2: header =  "h2"
        case 3: header = "h3"
        case 4: header = "h4"
        case 5: header = "h5"
        case 6: header = "h6"
        case _: raise ValueError("Not a valid header")

    return header, stripped_block

def paragraph_block_to_html_node(block):
    return " ".join(block.splitlines())

def quote_block_to_html_node(block):
    result = []

    text = block.splitlines()
    
    for line in text:
        stripped_block = line.lstrip()

        if stripped_block.startswith(">"):
            stripped_block = stripped_block[1:].lstrip()
            result.append(stripped_block)
    
    return " ".join(result)

def unordered_list_block_to_html_node(block):
    children = []

    text = block.splitlines()

    for line in text:
        stripped_block = line.lstrip()

        if stripped_block.startswith("- ") or stripped_block.startswith("* "):
            stripped_block = stripped_block[2:].lstrip()
            text_child = text_to_children(stripped_block)

            html_node = HTMLNode("li", None, text_child)
            children.append(html_node)

    return children

def ordered_list_block_to_html_node(block):
    children = []
    counter = 1

    text = block.splitlines()

    for line in text:
        stripped_block = line.lstrip()

        if stripped_block.startswith(f"{counter}. "):
            stripped_block = stripped_block[3:].lstrip()
            text_child = text_to_children(stripped_block)
            
            html_node = HTMLNode("li", None, text_child)
            children.append(html_node)
            counter += 1

    return children

def code_block_to_html_node(block):

    if block.startswith("```") and block.endswith("```"):
        stripped_block = block[3:-3].strip("\n")
    else:
        stripped_block = block

    children = text_node_to_html_node(TextNode(stripped_block, TextType.CODE))
    
    return HTMLNode("pre", None, [children])

def text_to_children(text):
    result = []
    
    text_nodes = text_to_textnodes(text)

    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        result.append(html_node)

    return result

def convert_to_blocks(markdown):
    blocks = markdown_to_blocks(markdown)

    children = []

    
    for block in blocks:
        type = block_to_block_type(block)

        match type:
            case BlockType.HEADING:
                heading, text = header_block_to_html_node(block)
                text_children = text_to_children(text)

                html_node = HTMLNode(heading, None, text_children)
                children.append(html_node)

            case BlockType.PARAGRAPH:
                text = paragraph_block_to_html_node(block)
                text_children = text_to_children(text)

                html_node = HTMLNode("p", None, text_children)
                children.append(html_node)

            case BlockType.QUOTE:
                text = quote_block_to_html_node(block)
                text_children = text_to_children(text)

                html_node = HTMLNode("blockquote", None, text_children)
                children.append(html_node)

            case BlockType.UNORDERED_LIST:
                text_children = unordered_list_block_to_html_node(block)

                html_node = HTMLNode("ul", None, text_children)
                children.append(html_node)

            case BlockType.ORDERED_LIST:
                text_children = ordered_list_block_to_html_node(block)

                html_node = HTMLNode("ol", None, text_children)
                children.append(html_node)

            case BlockType.CODE:
                html_node = code_block_to_html_node(block)
                children.append(html_node)
            case _:
                raise ValueError("Block type is not defined")

    return HTMLNode("div", None, children, None)


convert_to_blocks("""
This is **bolded** paragraph
text in a p
tag here
""")