import unittest

from htmlnode import HTMLNode

run_node_cases = [
    HTMLNode("a", "This is an anchor", None, {"href": "https://www.google.com"}),
    HTMLNode("h1", "This is a header", None, {"href": "https://www.google.com"}),
    HTMLNode("p", "This is a paragraph", None, {"href": "https://www.google.com"})
]

class TestHTMLNode(unittest.TestCase):
    # Equal Assertions
    
    def test_eq_tag(self):
        node = HTMLNode("p", None, None, None)
        node2 = HTMLNode("p", None, None, None)
        self.assertEqual(node, node2)

    def test_eq_value(self):
        node = HTMLNode(None, "This is a header", None, None)
        node2 = HTMLNode(None, "This is a header", None, None)
        self.assertEqual(node, node2)

    def test_eq_children(self):
        node = HTMLNode(None, None, run_node_cases, None)
        node2 = HTMLNode(None, None, run_node_cases, None)
        self.assertEqual(node, node2)

    def test_eq_props(self):
        node = HTMLNode(None, None, None, {"href": "https://www.boot.dev"})
        node2 = HTMLNode(None, None, None, {"href": "https://www.boot.dev"})
        self.assertEqual(node, node2)

    def test_eq_props_to_html(self):
        node = HTMLNode("p", "This is a paragraph", None, {"href": "https://www.boot.dev", "target": "_blank"}).props_to_html()
        node2 = HTMLNode("p", "This is a paragraph", None, {"href": "https://www.boot.dev", "target": "_blank"}).props_to_html()
        self.assertEqual(node, node2)

    # Not Equal Assertions

    def test_neq_tag(self):
        node = HTMLNode("a", None, None, None)
        node2 = HTMLNode("p", None, None, None)
        self.assertNotEqual(node, node2)

    def test_neq_value(self):
        node = HTMLNode(None, "This is a header", None, None)
        node2 = HTMLNode(None, "This is a paragraph", None, None)
        self.assertNotEqual(node, node2)

    def test_neq_children(self):
        node = HTMLNode(None, None, run_node_cases, None)
        node2 = HTMLNode(None, None, run_node_cases[1:], None)
        self.assertNotEqual(node, node2)

    def test_neq_props(self):
        node = HTMLNode(None, None, None, {"href": "https://www.boot.dev", "target": "_blank"})
        node2 = HTMLNode(None, None, None, {"href": "https://www.boot.dev"})
        self.assertNotEqual(node, node2)

    def test_eq_props_to_html(self):
        node = HTMLNode("p", "This is a paragraph", None, {"href": "https://www.boot.dev", "target": "_blank"}).props_to_html()
        node2 = HTMLNode("p", "This is a paragraph", None, {"href": "https://www.boot.dev"}).props_to_html()
        self.assertNotEqual(node, node2)
    

if __name__ == "__main__":
    unittest.main()
