import os
import shutil
from markdown_blocks import extract_titile
from markdown_to_html import markdown_to_html_node

def static_to_public(static_dir='static', public_dir='docs'):
    if not os.path.exists(public_dir):
        os.makedirs(public_dir, exist_ok=True)
    else:
        shutil.rmtree(public_dir)
        print(f"Removed existing directory {public_dir}")
        os.makedirs(public_dir, exist_ok=True)

    recursive_copy(static_dir, public_dir)

def recursive_copy(static_dir, public_dir):    
    if os.path.exists(static_dir):
        for item in os.listdir(static_dir):
            s = os.path.join(static_dir, item)
            p = os.path.join(public_dir, item)

            if os.path.isdir(s):
                os.makedirs(p, exist_ok=True)
                print(f"Copied dir {s} to {p}")
                recursive_copy(s, p)
            else:
                shutil.copy2(s, p)
                print(f"Copied {s} to {p}")


def generate_page(from_path, template_path, to_path, basepath):
    print(f"Generating page from {from_path} using template {template_path} to {to_path}")

    with open(template_path, 'r', encoding='utf-8') as template_file:
        template_content = template_file.read()
    
    with open(from_path, 'r') as from_file:
        content = from_file.read()

    # Extract title from markdown
    title = extract_titile(content)
    print(f"Extracted title: {title}")

    # Convert markdown to HTML
    content = markdown_to_html_node(content).to_html()
    print(f"Converted markdown to HTML content.")


    # Replace placeholders in template
    final_content = template_content.replace("{{ Title }}", title)
    final_content = final_content.replace("{{ Content }}", content)
    final_content = final_content.replace(f'href="/', f'href="{basepath}')
    final_content = final_content.replace(f'src="/', f'src="{basepath}')
    final_content = final_content.replace(f'src=/', f'src={basepath}')

    with open(to_path, 'w') as to_file:
        to_file.write(final_content)

    print(f"Wrote generated page to {to_path}")

def generate_pages_recursively(from_path, template_path, to_path, basepath):

    print(f"Generating page from {from_path} using template {template_path} to {to_path}")

    if not os.path.exists(to_path):
        os.makedirs(to_path, exist_ok=True)
    for item in os.listdir(from_path):
        s = os.path.join(from_path, item)
        p = os.path.join(to_path, item)
        print(f"Processing {s} to {p}")
        if os.path.isdir(s):
            os.makedirs(p, exist_ok=True)
            print(f"Created directory {p}")
            generate_pages_recursively(s, template_path, p, basepath)
        else:
            if item.endswith('.md'):
                to_file_path = os.path.join(to_path, item[:-3] + '.html')
                print(f"Generating HTML page {to_file_path} from markdown {s}")
                generate_page(s, template_path, to_file_path, basepath)
            else:
                shutil.copy2(s, p)
                print(f"Copied {s} to {p}")

   