from htmlnode import HTMLNode

class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value")
        
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:  # Only raise error if value is None, empty string is allowed
            raise ValueError("all leaf nodes must have a value")
        
        if self.tag is None:
            return self.value
        
        return (
            f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        )
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
