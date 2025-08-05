# Static Site Generator

A powerful Python-based static site generator that converts Markdown files into a fully functional website. This project features a custom Markdown parser, template system, and supports GitHub Pages deployment out of the box.

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

- **Markdown to HTML Conversion**
  - Full support for CommonMark syntax
  - Nested lists and complex document structures
  - Code blocks with syntax highlighting
  - Inline formatting (bold, italic, code, links)

- **Template System**
  - Custom HTML templates with placeholders
  - Automatic title extraction from Markdown
  - Support for custom base paths

- **Build System**
  - Recursive directory processing
  - Automatic static file copying
  - Clean build directory handling

- **Deployment Ready**
  - GitHub Pages compatible
  - Configurable base paths for different environments
  - Optimized for production use

---

## Project Structure
```
static-site-generator/
├── content/           # Your markdown content
│   ├── blog/          # Blog posts
│   └── contact/       # Contact page
├── static/            # Static assets (CSS, images)
│   └── images/        # Image assets
├── docs/              # Generated HTML output (for GitHub Pages)
├── src/               # Source code
│   ├── main.py        # Main script
│   ├── htmlnode.py    # HTML node classes
│   ├── leafnode.py    # Leaf node implementation
│   └── ...            # Other source files
├── template.html      # HTML template
├── build.sh           # Build script
└── main.sh            # Development server script
```

---

## Getting Started

### Prerequisites
- Python 3.8+
- Git (for deployment)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/juanezamudio/static-site-generator.git
   cd static-site-generator
   ```

2. Set up a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

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

The project includes a comprehensive test suite. To run all tests:

```bash
python -m unittest discover -s src -p "test_*.py"
```

Or run individual test files:

```bash
python -m unittest src/test_main.py
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