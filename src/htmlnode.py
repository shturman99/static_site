
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
                out += f" {key}={val} "
        else:
            return ""
        return out

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
        
