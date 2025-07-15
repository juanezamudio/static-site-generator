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

def split_nodes_image(old_nodes):
    pass

def split_nodes_link(old_nodes):
    result = []
    
    for node in old_nodes:
        extracted_links = extract_markdown_links(node.text)

        if len(extracted_links) == 0:
            result.append(node)
            return result
        
        text_nodes = []

        for i in range(len(extracted_links)):
            text_split = node.text.split(f"[{extracted_links[i][0]}]({extracted_links[i][1]})", 1)
            text_nodes.append(text_split[0])
            print(text_split[0])
        
        new_nodes = []

        for i in range(len(text_nodes)):
            if text_nodes[i] == "":
                continue

            if i % 2 == 0:
                new_nodes.append(TextNode(text_nodes[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(text_nodes[i], TextType.LINK))
        
        result.extend(new_nodes)

split_nodes_link([TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com)", TextType.TEXT)])