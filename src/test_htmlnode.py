import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode(tag="div", value="Hello", children=[], props=[("class", "container")])
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, [("class", "container")])

    def test_props_to_html_with_props(self):
        node = HTMLNode(props=[("class", "container"), ("id", "main")])
        props_html = node.props_to_html()
        self.assertIn('class=container', props_html)
        self.assertIn('id=main', props_html)

    def test_props_to_html_without_props(self):
        node = HTMLNode()
        props_html = node.props_to_html()
        self.assertEqual(props_html, "")

    def test_repr(self):
        node = HTMLNode(tag="p", value="Paragraph", children=[], props=[])
        expected_repr = "HTMLNode(p, Paragraph, [], [])"
        self.assertEqual(repr(node), expected_repr)

if __name__ == "__main__":
    unittest.main()