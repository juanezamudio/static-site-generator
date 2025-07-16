from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

class Block:

    # def __init__(self, text, text_type, url=None):
    #     self.text = text
    #     self.text_type = text_type
    #     self.url = url

    # def __eq__(self, other_node):
    #     return (
    #         self.text == other_node.text
    #         and self.text_type == other_node.text_type 
    #         and self.url == other_node.url
    #     )
    
    # def __repr__(self):
    #     return (
    #         f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    #     )

    pass
    
def block_to_block_type(markdown_block):
    
    split_lines = markdown_block.splitlines()
    
    if (len(split_lines) > 1 and split_lines[0].startswith("```") and split_lines[-1].endswith("```")):
        return BlockType.CODE
    
    if (split_lines[0].startswith("#", 0, 5)):
            return BlockType.HEADING

    all_quoted = True
    all_unordered = True
    all_ordered = True

    counter = 1

    for line in split_lines:
        prefix = f"{counter}. "
        
        if (not line.startswith(">")):
            all_quoted = False

        if (not line.startswith("- ")):
            all_unordered = False

        if (not line.startswith(prefix)):
            all_ordered = False
        
        counter += 1
        
    if all_quoted:
        return BlockType.QUOTE
    elif all_unordered:
        return BlockType.UNORDERED_LIST
    elif all_ordered:
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
                