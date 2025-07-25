import unittest
from html_node_markdown import markdown_to_html_node
from textnode import TextNode, TextType

class TestHTMLNodeMarkdown(unittest.TestCase):

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )

    def test_heading(self):
        md = """
# Heading 1
## Heading 2
### Heading 3
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3</h3></div>",
        )

    def test_blockquote(self):
        md = "> This is a block quote.\n> It can span multiple lines.\n"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a block quote. It can span multiple lines.</blockquote></div>",
        )

    def test_unordered_list(self):
        md = """
- Item one
- Item two
- Item three
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item one</li><li>Item two</li><li>Item three</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. First item
2. Second item
3. Third item
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First item</li><li>Second item</li><li>Third item</li></ol></div>",
        )

    def test_mixed_blocks(self):
        md = """
# Heading

Paragraph text here.

- List item 1
- List item 2

```
code block
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading</h1><p>Paragraph text here.</p><ul><li>List item 1</li><li>List item 2</li></ul><pre><code>code block\n</code></pre></div>",
        )

    def test_empty_input(self):
        md = """\n\n\n"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div></div>")

    def test_nested_lists_and_blockquotes(self):
        md = """
- Item 1
  - Subitem 1.1
  - Subitem 1.2
- Item 2

> Blockquote line 1
> - List in quote 1
> - List in quote 2
"""
        # Note: This test assumes your parser supports nested lists and lists in blockquotes.
        # If not, adjust the expected output accordingly.
        node = markdown_to_html_node(md)
        html = node.to_html()
        # This is a simplified expected output for flat lists and blockquotes
        self.assertIn("<ul><li>Item 1</li><li>Subitem 1.1</li><li>Subitem 1.2</li><li>Item 2</li></ul>", html)
        self.assertIn("<blockquote>Blockquote line 1 - List in quote 1 - List in quote 2</blockquote>", html)

    def test_multiple_code_blocks_and_inline(self):
        md = """
Here is some code:
```
def foo():
    return 42
```
And some more code: `print('hi')`

```
SELECT * FROM table;
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertIn("<pre><code>def foo():\n    return 42\n</code></pre>", html)
        self.assertIn("<code>print('hi')</code>", html)
        self.assertIn("<pre><code>SELECT * FROM table;\n</code></pre>", html)

    def test_mixed_formatting_in_paragraphs(self):
        md = """
This is a paragraph with **bold**, _italic_, `code`, and a [link](https://example.com).
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertIn("<b>bold</b>", html)
        self.assertIn("<i>italic</i>", html)
        self.assertIn("<code>code</code>", html)
        self.assertIn('<a href="https://example.com">link</a>', html)

    def test_all_blocks_together(self):
        md = """
# Main Heading

Paragraph with _italic_ and **bold**.

> Blockquote here

- Unordered 1
- Unordered 2

1. Ordered 1
2. Ordered 2

```
code block here
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertIn("<h1>Main Heading</h1>", html)
        self.assertIn("<p>Paragraph with <i>italic</i> and <b>bold</b>.</p>", html)
        self.assertIn("<blockquote>Blockquote here</blockquote>", html)
        self.assertIn("<ul><li>Unordered 1</li><li>Unordered 2</li></ul>", html)
        self.assertIn("<ol><li>Ordered 1</li><li>Ordered 2</li></ol>", html)
        self.assertIn("<pre><code>code block here\n</code></pre>", html)

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_code(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
