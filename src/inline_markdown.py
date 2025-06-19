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

def split_nodes(func, old_nodes, str_format):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text
        matches = func(original_text)

        if len(matches) == 0:
            new_nodes.append(old_node)
            continue
        
        for match in matches:
            regex_test = ""
            if str_format == TextType.IMAGE:
                regex_text = f"![{match[0]}]({match[1]})"
            else:
                regex_text = f"[{match[0]}]({match[1]})"
            sections = original_text.split(regex_text, 1)
            if len(sections) != 2:
                raise ValueError(f"invalid markdown, {str_format} section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(match[0], str_format, match[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def split_nodes_image(old_nodes):
    return split_nodes(extract_markdown_images, old_nodes, TextType.IMAGE)

def split_nodes_link(old_nodes):
    return split_nodes(extract_markdown_links, old_nodes, TextType.LINK)

def text_to_textnodes(text):
    if text == "":
        raise ValueError("invalid text: text empty")





