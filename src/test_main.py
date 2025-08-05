import unittest

from main import extract_title

class TestMain(unittest.TestCase):
    def test_extract_title_h1(self):
        markdown = "# This is an h1 header"
        extracted_title = extract_title(markdown)
        self.assertEqual(extracted_title, "This is an h1 header")

    def test_extract_title_h2(self):
        markdown = "## This is an h2 header"
        extracted_title = extract_title(markdown)
        self.assertEqual(extracted_title, "This is an h2 header")

    def test_extract_title_h3(self):
        markdown = "### This is an h3 header"
        extracted_title = extract_title(markdown)
        self.assertEqual(extracted_title, "This is an h3 header")

    def test_extract_title_h4(self):
        markdown = "#### This is an h4 header"
        extracted_title = extract_title(markdown)
        self.assertEqual(extracted_title, "This is an h4 header")

    def test_extract_title_h5(self):
        markdown = "##### This is an h5 header"
        extracted_title = extract_title(markdown)
        self.assertEqual(extracted_title, "This is an h5 header")

    def test_extract_title_h6(self):
        markdown = "###### This is an h6 header"
        extracted_title = extract_title(markdown)
        self.assertEqual(extracted_title, "This is an h6 header")

    def test_extract_title_no_header(self):
        markdown = "This is a text node"
        with self.assertRaises(Exception):
            extract_title(markdown)

    def test_extract_title_empty_string(self):
        markdown = ""
        with self.assertRaises(Exception):
            extract_title(markdown)

    def test_extract_title_double(self):
        actual = extract_title(
            """
# This is a title

# This is a second title that should be ignored
"""
        )
        self.assertEqual(actual, "This is a title")
    
    def test_extract_title_long(self):
        actual = extract_title(
            """
# title

this is a bunch

of text

- and
- a
- list
"""
        )
        self.assertEqual(actual, "title")

    def test_extract_title_none(self):
        try:
            extract_title(
                """
no title
"""
            )
            self.fail("Should have raised an exception")
        except Exception as e:
            pass

if __name__ == "__main__":
    unittest.main()
