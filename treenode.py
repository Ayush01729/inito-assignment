
class Node:
    def __init__(self, name, is_directory, parent=None, content=None):
        self.name = name
        self.is_directory = is_directory
        self.parent = parent
        self.content = content
        self.children = {}
    
    def to_dict(self):
        return {
            'name': self.name,
            'is_directory': self.is_directory,
            'parent': self.parent.name if self.parent else None,
            'content': self.content,
            'children': {name: child.to_dict() for name, child in self.children.items()}
        }