import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_children_none(self):
        node = HTMLNode("p", "This is the value", None,{"name": "hello", "class": "heading"})
        self.assertIsNone(node.children)

    def test_not_eq(self):
        node = HTMLNode("p", "Hello Everyone!", [],{"name": "hello", "class": "welcome"})
        node2 = HTMLNode("p", "Bye Everyone", [],{"name": "goodbye", "class": "welcome"})
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = HTMLNode("p", "This is the value", None,{'name': 'hello', 'class': 'heading'})
        self.assertEqual(
                repr(node),
                "HTMLNode(p, This is the value, children: None, {'name': 'hello', 'class': 'heading'})")


if __name__ == "__main__":
    unittest.main()
