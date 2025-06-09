from textnode import TextNode, TextType
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)

        split_text = node.text.split(delimiter)
        
        if len(split_text) % 2 == 0:
            raise Exception("invalid markdown: missing closing delimiter")

        for i in range(len(split_text)):
            if len(split_text[i]) == 0:
                continue
            if i % 2 != 0:
                new_nodes.append(TextNode(split_text[i], text_type))
            else:
                new_nodes.append(TextNode(split_text[i], TextType.TEXT))
    print(new_nodes)

    return new_nodes
                

node = TextNode("This is text with a `code block``` word", TextType.TEXT)
new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
