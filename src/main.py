from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    test_node = TextNode("This is a test", TextType.LINK, "https://ww.me.com")
    print(test_node)
    
    test_html_node = HTMLNode("p", "This is the value", None,{"name": "hello", "class": "heading"})
    print(test_html_node)


main()
