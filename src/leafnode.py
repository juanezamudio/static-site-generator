from htmlnode import HTMLNode

class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value")
        
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.tag is None:
            if self.value is None:
                raise ValueError("all leaf nodes must have a value")
            return self.value

        if self.tag == "img":
            return f"<img{self.props_to_html()}>"

        if not self.value:
            raise ValueError("all leaf nodes must have a value")

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

