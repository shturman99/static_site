
class HTMLNode():
    def __init__(self,tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value 
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplemented

    def props_to_html(self):
        out = f""
        if self.props:
            for key,val in self.props:
                out += f' {key}="{val}" '
        else:
            return ""
        return out

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
        
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)
        

    def to_html(self):
        if self.value == None:
            raise ValueError(f"All leaf nodes mush have a value")
        if self.tag == None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=props)
        
        

    def to_html(self):
        if self.children == None:
            raise ValueError(f"All parent nodes must have children")
        elif self.tag == None:
            raise ValueError(f"All parent nodes must have a tag")
        else:
            out = ""
            for child in self.children:
                out  += child.to_html()

            return f"<{self.tag}{self.props_to_html()}>{out}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"