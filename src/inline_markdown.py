import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        split_text = node.text.split(delimiter)
        
        if len(split_text) % 2 == 0:
            raise ValueError("invalid markdown: missing closing delimiter")

        for i in range(len(split_text)):
            if split_text[i] == "":
                continue
            if i % 2 != 0:
                new_nodes.append(TextNode(split_text[i], text_type))
            else:
                new_nodes.append(TextNode(split_text[i], TextType.TEXT))

    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_images(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        matches = extract_markdown_images(old_node.text)

        if len(matches) == 0:
            return old_nodes

        original_text = old_node.text
        for match in matches:
            sections = original_text.split(f"![{match[0]}]({match[1]})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(match[0], TextType.LINK, match[1]))
            if sections[1] != "":
                original_text = sections[1]
        if len(original_text) > 0:
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        matches = extract_markdown_links(old_node.text)
        
        if len(matches) == 0:
            return old_nodes

        original_text = old_node.text
        for match in matches:
            sections = original_text.split(f"[{match[0]}]({match[1]})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(match[0], TextType.LINK, match[1]))
            if sections[1] != "":
                original_text = sections[1] 
        if len(original_text) > 0:
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes



node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) yo dawg", TextType.TEXT,)
new_nodes = split_nodes_link([node])
print(new_nodes)
