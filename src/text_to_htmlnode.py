from htmlnode import *
from textnode import *
def normalize_internal_href(href: str) -> str:
    if not href.startswith("/"):
        return href

    if href.endswith("/"):
        return href

    last = href.rsplit("/", 1)[-1]
    if "." in last:
        return href

    return href + "/"

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        href = normalize_internal_href(text_node.url)
        return LeafNode("a", text_node.text, props=[("href", href)])  
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", props=[("src", text_node.url), ("alt", text_node.text)])  
    else:
        return LeafNode(None, text_node.text)  