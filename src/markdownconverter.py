from textnode import TextType, TextNode
import re
import itertools

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
    result = []
    
    for node in old_nodes:
        extracted_links = extract_markdown_images(node.text)

        if node.text_type != TextType.TEXT:
            result.append(node)
            continue

        if len(extracted_links) == 0:
            result.append(node)
            continue
        
        text_nodes = []
        node_text = node.text

        for i in range(len(extracted_links)):
            text_split = node_text.split(f"![{extracted_links[i][0]}]({extracted_links[i][1]})", 1)
            text_nodes.append(text_split[0])
            node_text = text_split[1]

        if node_text != "":
            text_nodes.append(node_text)
        
        zipped_list = [item for pair in itertools.zip_longest(text_nodes, extracted_links) for item in pair if item is not None]

        new_nodes = []

        for i in range(len(zipped_list)):
            
            if zipped_list[i] == "":
                continue

            if i % 2 == 0:
                new_nodes.append(TextNode(zipped_list[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(zipped_list[i][0], TextType.IMAGE, zipped_list[i][1]))

        result.extend(new_nodes)

    return result

def split_nodes_link(old_nodes):
    result = []
    
    for node in old_nodes:
        extracted_links = extract_markdown_links(node.text)

        if node.text_type != TextType.TEXT:
            result.append(node)
            continue

        if len(extracted_links) == 0:
            result.append(node)
            continue
        
        text_nodes = []
        node_text = node.text

        for i in range(len(extracted_links)):
            text_split = node_text.split(f"[{extracted_links[i][0]}]({extracted_links[i][1]})", 1)
            text_nodes.append(text_split[0])
            node_text = text_split[1]

        if node_text != "":
            text_nodes.append(node_text)
        
        zipped_list = [item for pair in itertools.zip_longest(text_nodes, extracted_links) for item in pair if item is not None]

        new_nodes = []

        for i in range(len(zipped_list)):
            
            if zipped_list[i] == "":
                continue

            if i % 2 == 0:
                new_nodes.append(TextNode(zipped_list[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(zipped_list[i][0], TextType.LINK, zipped_list[i][1]))

        result.extend(new_nodes)
        
    return result