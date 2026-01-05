
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
                out += f' {key}={val} '
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
