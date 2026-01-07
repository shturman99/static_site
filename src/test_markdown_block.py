import unittest
from markdown_blocks import (

    markdwon_to_blocks,
    block_to_block_type,
    BlockType
    
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

    def test_block_to_block_type_header(self):
        text1 = "# this is header"
        text2 = "## this is also a header"
        text3 = "###### this is also a header"

        block1 = block_to_block_type(text1)
        block2 = block_to_block_type(text2)
        block3 = block_to_block_type(text3)

        self.assertEqual(block1, BlockType.HEADING)
        self.assertEqual(block2, BlockType.HEADING)
        self.assertEqual(block3, BlockType.HEADING)

    def test_block_to_block_type_code(self):
        text =  "```\n " \
        "this is code " \
        " ```"
        block = block_to_block_type(text)
        self.assertEqual(block, BlockType.CODE)

    def test_block_to_block_type_quote(self):
        text = "> this is quote"
        block = block_to_block_type(text)
        self.assertEqual(block, BlockType.QUOTE)

    def test_block_to_block_type_unordered_list(self):
        text = "- item 1\n- item 2\n- item 3"
        block = block_to_block_type(text)
        self.assertEqual(block, BlockType.UNORDERED_LIST)

    def test_block_to_block_type_ordered_list(self):
        text1 = "1. item 1\n2. item 2\n3. item 3"
        text2 = "1. item 1\n item 2\n3. item 3"
        block1 = block_to_block_type(text1)
        block2 = block_to_block_type(text2)
        self.assertEqual(block2, BlockType.PARAGRAPH)
        self.assertEqual(block1, BlockType.ORDERED_LIST)

if __name__ == "__main__":
    unittest.main()
