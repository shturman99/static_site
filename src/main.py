from textnode import *
from static_to_public  import generate_pages_resurcivly,  markdown_to_html_node, static_to_public, generate_page
import os

public_dir="./public"
static_dir="./static"
content_dir="./content"
template_path="./template.html"


def main():

    static_to_public(static_dir, public_dir)
    generate_pages_resurcivly(static_dir, template_path, public_dir)
    generate_pages_resurcivly(content_dir, template_path,public_dir)
    

    

if __name__=="__main__":
    main()
