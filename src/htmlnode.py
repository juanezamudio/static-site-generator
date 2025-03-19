class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        string = ""

        if self.props:
            for key, value in self.props.items():
                string = string + f' {key}="{value}"'

        return string
    
    def __eq__(self, other_node):
        return (
            self.tag == other_node.tag
            and self.value == other_node.value
            and self.children == other_node.children
            and self.props == other_node.props
        )
    
    def __repr__(self):
        return (
            f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
        )
    

