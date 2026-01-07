from static_to_public  import generate_pages_recursively,  markdown_to_html_node, static_to_public, generate_page
import sys


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    public_dir = "docs"
    static_dir = "static"
    content_dir = "content"
    template_path = "template.html"
    static_to_public(static_dir, public_dir)
    generate_pages_recursively(content_dir, template_path, public_dir, basepath)


    

if __name__=="__main__":
    main()
