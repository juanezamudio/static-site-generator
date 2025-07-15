# Python Static Site Generator (Node-Based HTML Builder)

A Python library and demonstration project for converting Markdown-like text into HTML using a custom node-based system. This project is a foundation for building a static site generator, with a focus on parsing text and generating HTML elements programmatically.

## Features

- **Node-Based HTML Generation**: Compose HTML using `HTMLNode`, `LeafNode`, and `ParentNode` classes.
- **Markdown-Like Parsing**: Convert text with bold (`**bold**`), italic (`_italic_`), code (`` `code` ``), links (`[text](url)`), and images (`![alt](url)`) into HTML nodes.
- **Extensive Unit Tests**: Comprehensive test suite for all node types and Markdown parsing logic.

## Project Structure

```
static-site-generator/
├── main.sh                # Run the demo script
├── test.sh                # Run all unit tests
├── src/
│   ├── main.py            # Demo: creates and prints example nodes
│   ├── htmlnode.py        # Base HTML node class
│   ├── leafnode.py        # Leaf node (text, images, etc.)
│   ├── parentnode.py      # Parent node (with children)
│   ├── textnode.py        # Text node and Markdown parsing
│   ├── markdownconverter.py # Markdown parsing utilities
│   └── test_*.py          # Unit tests
└── README.md
```

## Getting Started

### Prerequisites
- Python 3.7+

### Run the Demo
To see a demonstration of node creation and HTML output:

```bash
./main.sh
```

This will run `src/main.py`, which prints example `TextNode` and `HTMLNode` objects.

### Run the Tests
To run all unit tests:

```bash
./test.sh
```

Or directly with Python:

```bash
python3 -m unittest discover -s src
```

## Usage Example

You can use the provided classes to build HTML programmatically:

```python
from textnode import TextNode, TextType, text_node_to_html_node
from leafnode import LeafNode
from parentnode import ParentNode

# Create a bold text node and convert to HTML
node = TextNode("Bold text", TextType.BOLD)
html_node = text_node_to_html_node(node)
print(html_node.to_html())  # <b>Bold text</b>

# Compose parent and leaf nodes
child1 = LeafNode("span", "child1")
child2 = LeafNode("b", "child2")
parent = ParentNode("div", [child1, child2])
print(parent.to_html())  # <div><span>child1</span><b>child2</b></div>
```

## Markdown Parsing Features
- **Bold**: `**bold**` → `<b>bold</b>`
- **Italic**: `_italic_` → `<i>italic</i>`
- **Code**: `` `code` `` → `<code>code</code>`
- **Links**: `[text](url)` → `<a href="url">text</a>`
- **Images**: `![alt](url)` → `<img src="url" alt="alt">`

## Contributing

Contributions are welcome! Please open issues or pull requests for improvements or bug fixes.

## License

MIT License. See [LICENSE](LICENSE) for details.

---

Built with ❤️ by Juan Zamudio