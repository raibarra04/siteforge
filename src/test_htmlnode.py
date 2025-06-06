import unittest

from htmlnode import HTMLNode, LeafNode


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

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_w_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")
        
    def test_leaf_no_value(self):
        node = LeafNode("h1", None)
        self.assertRaises(ValueError, node.to_html)

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


if __name__ == "__main__":
    unittest.main()
