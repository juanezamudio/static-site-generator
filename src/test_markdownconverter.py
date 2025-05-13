import unittest
from textnode import TextNode, TextType
from markdownconverter import split_nodes_delimiter, extract_markdown_images, extract_markdown_links

class TestMarkdownConverter(unittest.TestCase):

    def test_code_block(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            new_nodes, 
            [TextNode("This is text with a ", TextType.TEXT, None), 
              TextNode("code block", TextType.CODE, None), 
              TextNode(" word", TextType.TEXT, None)
            ]
        )

    def test_bold_block(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            new_nodes, 
            [TextNode("This is text with a ", TextType.TEXT, None), 
              TextNode("bold", TextType.BOLD, None), 
              TextNode(" word", TextType.TEXT, None)
            ]
        )

    def test_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_italic_block(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            new_nodes, 
            [TextNode("This is text with an ", TextType.TEXT, None), 
              TextNode("italic", TextType.ITALIC, None), 
              TextNode(" word", TextType.TEXT, None)
            ]
        )
    
    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_no_text_block(self):
        node = TextNode("This is text with an _italic_ word", TextType.ITALIC)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            new_nodes, 
            [node]
        )

    def test_invalid_markdown(self):
        try:
            node = TextNode("This is text with an _italic word", TextType.TEXT)
            new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        except ValueError as e:
            self.assertEqual(str(e), "invalid markdown syntax: missing closing delimiter - '_'")

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )

        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_no_images(self):
        matches = extract_markdown_images(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) but no images"
        )

        self.assertListEqual([], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link in the [message](https://i.imgur.com/zjjcJKZ.png)"
        )
        
        self.assertListEqual([("message", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown__no_links(self):
        matches = extract_markdown_links(
            "This is text with no links in the message and an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        
        self.assertListEqual([], matches)