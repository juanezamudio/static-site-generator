from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    html_node = HTMLNode("p", "This is a paragraph", None, {"href": "https://www.google.com"})

    print(text_node)
    print(html_node)

main()