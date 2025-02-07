import os
import shutil
from textnode import TextNode, TextType

def copy_static(src, dst):
    # Remove the destination directory if it exists
    if os.path.exists(dst):
        shutil.rmtree(dst)
    # Create a fresh destination directory
    os.makedirs(dst)
    
    # Recursively copy files and subdirectories from src to dst
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)
        if os.path.isdir(src_path):
            print(f"Copying directory: {src_path}")
            copy_static(src_path, dst_path)
        else:
            print(f"Copying file: {src_path}")
            shutil.copy(src_path, dst_path)

def main():
    # Example use of a TextNode
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)
    # Copy the static directory to public/
    copy_static("static", "public")

if __name__ == "__main__":
    main()
