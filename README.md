# Python Static Site Generator (Node-Based HTML Builder)

A robust, extensible Python static site generator that converts Markdown into HTML using a custom node-based parsing system. This project is designed for clarity, testability, and easy extension, making it ideal for learning, hacking, or as a foundation for your own static site generator.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Markdown Support](#markdown-support)
- [API Reference](#api-reference)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Roadmap & Limitations](#roadmap--limitations)

---

## Overview
This project parses Markdown files and converts them into HTML using a tree of custom node classes. It supports a wide range of Markdown features, both block-level (headings, lists, blockquotes, code blocks, paragraphs) and inline (bold, italic, code, links, etc.), and is fully covered by a comprehensive test suite.

---

## Features
- **Block-level Markdown support:**
  - Headings (`#`, `##`, ...)
  - Paragraphs
  - Blockquotes (`>`)
  - Unordered lists (`-`, `*`)
  - Ordered lists (`1.`, `2.`, ...)
  - Code blocks (fenced with triple backticks)
- **Inline Markdown support:**
  - Bold (`**bold**`)
  - Italic (`_italic_`)
  - Inline code (`` `code` ``)
  - Links (`[text](url)`)
- **Node-based HTML generation:**
  - Each block or inline element is represented as a node (e.g., `HTMLNode`, `TextNode`)
  - Easy to extend for new HTML/Markdown features
- **Comprehensive unit tests:**
  - All block types, inline features, and edge cases are tested
  - Complex/nested markdown scenarios covered
- **Extensible and maintainable:**
  - Modular codebase with clear separation of concerns
  - Easy to add new block or inline types

---

## Project Structure
```
static-site-generator/
├── main.sh                  # Demo script
├── test.sh                  # Test runner
├── README.md                # This file
├── LICENSE                  # License
├── public/                  # (Optional) Output/static files
└── src/
    ├── main.py              # Example/demo usage
    ├── htmlnode.py          # HTML node base class
    ├── leafnode.py          # Leaf node (text, images, etc.)
    ├── parentnode.py        # Parent node (with children)
    ├── textnode.py          # Text node and inline parsing
    ├── block.py             # Block type definitions
    ├── block_markdown.py    # Block-level markdown parsing
    ├── inline_markdown.py   # Inline markdown parsing
    ├── html_node_markdown.py# Markdown-to-HTML node conversion logic
    ├── test_htmlnode.py     # Unit tests for HTMLNode
    ├── test_leafnode.py     # Unit tests for LeafNode
    ├── test_parentnode.py   # Unit tests for ParentNode
    ├── test_textnode.py     # Unit tests for TextNode
    ├── test_block_markdown.py # Unit tests for block parsing
    ├── test_inline_markdown.py # Unit tests for inline parsing
    └── test_html_node_markdown.py # Unit tests for markdown-to-HTML conversion
```

---

## Installation & Setup
1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd static-site-generator
   ```
2. **(Optional) Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   - No external dependencies are required for core functionality. If you add features, update this section accordingly.

---

## Usage

### Basic Example
Convert Markdown to HTML using the main API:
```python
from html_node_markdown import markdown_to_html_node

markdown = """
# Welcome

This is a **bold** paragraph with _italic_ and `code`.

- List item 1
- List item 2

> Blockquote here

```
Code block
```
"""

html_node = markdown_to_html_node(markdown)
html = html_node.to_html()
print(html)
```
**Expected Output:**
```html
<div><h1>Welcome</h1><p>This is a <b>bold</b> paragraph with <i>italic</i> and <code>code</code>.</p><ul><li>List item 1</li><li>List item 2</li></ul><blockquote>Blockquote here</blockquote><pre><code>Code block
</code></pre></div>
```

---

## Markdown Support
### Block Elements
- **Headings:** `#`, `##`, ..., up to 6 levels
- **Paragraphs:** Separated by blank lines
- **Blockquotes:** Lines starting with `>`
- **Unordered Lists:** Lines starting with `-` or `*`
- **Ordered Lists:** Lines starting with `1.`, `2.`, etc.
- **Code Blocks:** Fenced with triple backticks (```)

### Inline Elements
- **Bold:** `**text**`
- **Italic:** `_text_`
- **Inline Code:** `` `code` ``
- **Links:** `[text](url)`

---

## API Reference
- **`markdown_to_html_node(markdown: str) -> HTMLNode`**
  - Main entry point. Converts a markdown string to an HTML node tree.
- **Block conversion functions:**
  - `header_block_to_html_node(block)`
  - `paragraph_block_to_html_node(block)`
  - `quote_block_to_html_node(block)`
  - `unordered_list_block_to_html_node(block)`
  - `ordered_list_block_to_html_node(block)`
  - `code_block_to_html_node(block)`
- **`text_to_children(text)`**
  - Converts inline markdown in a string to a list of HTML nodes.

---

## Testing

### Running the Tests
- All tests are located in `src/test_html_node_markdown.py` and other `test_*.py` files.
- To run all tests:
  ```bash
  python3 -m unittest discover -s src
  ```
  Or, to run just the main suite:
  ```bash
  python3 -m unittest src/test_html_node_markdown.py
  ```
  Or, using the provided script:
  ```bash
  ./test.sh
  ```

### Test Coverage
- All block types (headings, paragraphs, blockquotes, lists, code blocks)
- Inline formatting (bold, italic, code, links)
- Complex/nested markdown
- Edge cases (empty input, multiple code blocks, etc.)

### Adding New Tests
- Add new test methods to the appropriate `test_*.py` file in `src/`.
- Use the `unittest` framework for consistency.

---

## Contributing
- Follow PEP8 and standard Python best practices.
- Add tests for any new features or bug fixes.
- Document new functions and update the README as needed.
- Open a pull request with a clear description of your changes.

---

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Roadmap & Limitations
- **Known limitations:**
  - Nested lists and blockquotes are only partially supported (flat structure by default)
  - Images are not yet supported
  - Some advanced Markdown features (tables, footnotes, etc.) are not implemented
- **Planned improvements:**
  - Add support for images and more inline elements
  - Improve nested list and blockquote handling
  - Add CLI for batch conversion of Markdown files
  - Performance optimizations for large documents

---

## Credits
Built with ❤️ by Juan Zamudio.