
import unittest

from code1 import *


class TestCode(unittest.TestCase):
    def test_split(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        ans = [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ]
        self.assertEqual(ans, new_nodes)
    
    def test_split1(self):
        node = TextNode("This is text with a `code` block word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        ans = [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ]
        self.assertNotEqual(ans, new_nodes)

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

    def test_extract_markdown_imagies_from_text(self):
        text = "Here is an image ![alt text](http://example.com/image.png) in markdown."
        images = extract_markdown_imagies_from_text(text)
        expected = [{'alt_text': 'alt text', 'url': 'http://example.com/image.png'}]
        self.assertEqual(images, expected)

    def test_split_nodes_image(self):
        node = TextNode("this is an image in markdown ![alt text](http://example.com/image.png) end of text", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("this is an image in markdown ", TextType.TEXT),
            TextNode("![alt text](http://example.com/image.png)", TextType.IMAGE),
            TextNode(" end of text", TextType.TEXT),
        ]
        self.assertEqual(expected, new_nodes)

    def test_split_nodes_link(self):
        node = TextNode("this is a [link text](http://example.com) end of text", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("this is a ", TextType.TEXT),
            TextNode("[link text](http://example.com)", TextType.LINK),
            TextNode(" end of text", TextType.TEXT),
        ]
        self.assertEqual(expected, new_nodes)

if __name__ == "__main__":
    unittest.main()