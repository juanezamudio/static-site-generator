from textnode import TextType, TextNode
import re
import itertools

import re

def line_type(line):
    l = line.lstrip()
    if l.startswith("```"):
        return "code"
    if re.match(r"^#{1,6} ", l):
        return "heading"
    if l.startswith(">"):
        return "quote"
    if re.match(r"^(\* |- )", l):
        return "ulist"
    if re.match(r"^\d+\.\s", l):
        return "olist"
    if l == "":
        return "blank"
    
    return "paragraph"

def markdown_to_blocks(markdown):
    lines = markdown.splitlines()
    result = []
    current_block = []
    current_type = None
    inside_code = False

    for line in lines:
        lt = line_type(line)

        # -- Handle code block separately --
        if inside_code:
            current_block.append(line)
            if line.lstrip().startswith("```"):
                # Code block ends; finalize and reset
                result.append("\n".join(current_block).strip())
                current_block = []
                inside_code = False
            continue

        # -- Start of code block --
        if lt == "code":
            # If there's an unfinished block, finish it
            if current_block:
                result.append("\n".join(current_block).strip())
                current_block = []
            inside_code = True
            current_block.append(line)
            continue

        # -- New type or blank line --
        if (lt == "blank"):
            if current_block:
                result.append("\n".join(current_block).strip())
                current_block = []
            current_type = None
            continue

        # -- Block types that should be grouped together --
        if current_type in ["ulist", "olist", "quote", "paragraph"] and lt == current_type:
            current_block.append(line)
            continue

        # -- Block type changed --
        if current_block:
            result.append("\n".join(current_block).strip())
            current_block = []

        current_type = lt
        current_block.append(line)

    # Add any last block
    if current_block:
        result.append("\n".join(current_block).strip())

    # Remove empty blocks (just in case)
    return [block for block in result if block]