import unittest
from markdown_blocks import (

    markdwon_to_blocks,
)

from textnode import TextNode, TextType


class TestMarkdownBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        text = """this is plain text without any md.

this is **bold** text. and second block.

this is third blockk                     





"""
        blocks = markdwon_to_blocks(text)
        self.assertListEqual(
            [
                "this is plain text without any md.",
                "this is **bold** text. and second block.",
                "this is third blockk",   
            ], blocks )


if __name__ == "__main__":
    unittest.main()
