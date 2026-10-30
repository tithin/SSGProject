from textnode import TextNode, TextType
import shutil
import os

def main():
    copy_static_to_public("static", "public")


def copy_static_to_public(src, dst):
    shutil.rmtree(dst, ignore_errors=True)
    os.makedirs(dst, exist_ok=True)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            os.mkdir(d)
            copy_static_to_public(s, d)
        else:
            shutil.copy2(s,d)

main()
