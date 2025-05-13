from textnode import TextType, TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue


        text_node = node.text.split(delimiter)
        new_nodes = []

        match len(text_node) % 2:
            case 0:
                raise ValueError(f"invalid markdown syntax: missing closing delimiter - '{delimiter}'")
            case _:
                for i in range(len(text_node)):
                    if text_node[i] == "":
                        continue
                    
                    if i % 2 == 0:
                        new_nodes.append(TextNode(text_node[i], TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(text_node[i], text_type))
        
                result.extend(new_nodes)

    return result

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)