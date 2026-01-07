import re
import enum
def markdwon_to_blocks(text):

    blocks = list(map(lambda x: x.strip(), text.split("\n\n")))
    out = []    
    for block in blocks:
        if block == "":
            continue
        else:
            out.append(block)
    return out


class BlockType(enum.Enum):
    PARAGRAPH = 1
    HEADING = 2
    CODE = 3
    QUOTE = 4
    UNORDERED_LIST = 5
    ORDERED_LIST = 6



def block_to_block_type(block: str) -> BlockType:
    lines = block.split("\n")
    first_line = lines[0]

    # Heading: 1–6 '#' followed by space
    if re.match(r"^#{1,6} ", first_line):
        return BlockType.HEADING

    # Code block
    if block.startswith("```") and block.rstrip().endswith("```"):
        return BlockType.CODE

    # Quote
    if all(line.startswith("> ") for line in lines):
        return BlockType.QUOTE

    # Unordered list
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    # Ordered list
    if all(re.match(rf"{i+1}\. ", line) for i, line in enumerate(lines)):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH