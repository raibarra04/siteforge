from textnode import TextNode, TextType

def main():
    test_node = TextNode("This is a test", TextType.LINK, "https://ww.me.com")
    print(test_node)

main()
