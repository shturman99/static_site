from textnode import TextNode, TextType 

def split_nodes_delimiter(old_nodes : list[TextNode], delimiter : str, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            
            partition  = node.text.split(delimiter)

            if len(partition) % 2 == 0 :
                raise Exception("unbalances amount of delimters")

            for i in range(len(partition)):
                if i % 2 == 0:
                    if partition[i] != "":
                        new_nodes.append(TextNode(partition[i], TextType.TEXT))
                elif i % 2 == 1:
                    new_nodes.append(TextNode(partition[i], text_type))

    return new_nodes
        
        