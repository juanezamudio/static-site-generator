class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        if not self.tag:
            raise ValueError("HTMLNode must have a tag")
        
        if not self.children:
            return f"<div></div>"
        
        result = ""

        for child in self.children:
            result = f"{result}{child.to_html()}"
            
        
        return (
            f"<{self.tag}{self.props_to_html()}>{result}</{self.tag}>"
        )
    
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
    

