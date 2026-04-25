from textnode import TextType, TextNode

def main():
    unittest = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(unittest)

main()
