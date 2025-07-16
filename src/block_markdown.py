from textnode import TextType, TextNode
import re
import itertools

def markdown_to_blocks(markdown):
    result = []
    blocks = markdown.split("\n\n")

    for block in blocks:
        if block == "":
            continue

        result.append(block.strip())

    return result