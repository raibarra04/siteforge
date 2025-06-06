import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_url_none(self):
        node = TextNode("This is a text node with url as none", TextType.TEXT)
        self.assertIsNone(node.url)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.IMAGE, "we@notequal.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
