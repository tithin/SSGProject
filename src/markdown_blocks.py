from enum import Enum
from htmlnode import ParentNode, HTMLNode, LeafNode
from inlinemarkdown import text_to_textnodes
from textnode import text_node_to_html_node


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    OLIST = "ordered_list"
    ULIST = "unordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    return BlockType.PARAGRAPH

def text_to_children(text: str) -> list[HTMLNode]:
    return [text_node_to_html_node(node) for node in text_to_textnodes(text)]

def markdown_to_html_node(markdown):
    htmlblocks = markdown_to_blocks(markdown)
    collatedblocklist = []
    for block in htmlblocks:
        classification = block_to_block_type(block)

        if classification == BlockType.PARAGRAPH:
            text = " ".join(block.splitlines())
            children = text_to_children(text)
            collatedblocklist.append(ParentNode("p", children))

        elif classification == BlockType.HEADING:
            level = len(block) - len(block.lstrip("#"))
            text = block[level:].strip()
            children = text_to_children(text)
            collatedblocklist.append(ParentNode(f"h{level}", children))

        elif classification == BlockType.CODE:
            lines = block.splitlines()
            content = "\n".join(lines[1:-1]) + "\n"
            leaf = LeafNode("code", content)
            collatedblocklist.append(ParentNode("pre", [leaf]))


        elif classification == BlockType.QUOTE:
            text = " ".join(line.lstrip(">").lstrip() for line in block.splitlines())
            children = text_to_children(text)
            collatedblocklist.append(ParentNode("blockquote", children))

        elif classification == BlockType.OLIST:
            lis = []
            for line in block.splitlines():
                text = line.split(". ", 1)[1].lstrip()
                lis.append(ParentNode("li", text_to_children(text)))
            collatedblocklist.append(ParentNode("ol", lis))


        elif classification == BlockType.ULIST:
            lis = []
            for line in block.splitlines():
                text = line.split("- ", 1)[1].lstrip()
                lis.append(ParentNode("li", text_to_children(text)))
            collatedblocklist.append(ParentNode("ul", lis))


    return ParentNode("div", collatedblocklist)