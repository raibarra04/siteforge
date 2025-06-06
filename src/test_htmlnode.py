import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parent_no_children(self):
        parent_node = ParentNode("div", [])
        self.assertRaises(ValueError, parent_node.to_html)

    def test_child_no_value(self):
        child_node = LeafNode("span", None)
        parent_node = ParentNode("div", [child_node])
        self.assertRaises(ValueError, parent_node.to_html)


if __name__ == "__main__":
    unittest.main()
