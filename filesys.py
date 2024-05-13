import re
import json
import os

from treenode import Node

class FileSystem:
    def __init__(self):
        self.root = Node('/', True)
        self.current = self.root
    
    def get_current_path(self):
        path = []
        node = self.current
        while node is not None:
            path.append(node.name)
            node = node.parent
        return '/'.join(reversed(path)) or '/'

    def mkdir(self, path):
        paths = path.split('/')
        current = self.current
        for name in paths:
            if name in current.children:
                return f"{name} already exists"
            else:
                new_dir = Node(name, True, current)
                current.children[name] = new_dir
                current = new_dir
        return path + " created"

    def cd(self, path):
        if path == '/':
            self.current = self.root
        elif path == '..':
            if self.current.parent is not None:
                self.current = self.current.parent
        elif path.startswith('../'):
            if self.current.parent is not None:
                paths = path.split('/')
                for p in paths[1:]:
                    # if p == '..':
                    #     if self.current.parent is not None:
                    #         self.current = self.current.parent
                    if p in self.current.children and self.current.children[p].is_directory:
                        self.current = self.current.children[p]
                    else:
                        return "Invalid path"
        elif path.startswith('/'):
            self.current = self.root
            paths = path.split('/')[1:]
            for p in paths:
                if p in self.current.children and self.current.children[p].is_directory:
                    self.current = self.current.children[p]
                else:
                    return "Invalid path"
        else:
            paths = path.split('/')
            for p in paths:
                if p in self.current.children and self.current.children[p].is_directory:
                    self.current = self.current.children[p]
                else:
                    return "Invalid path"

    def ls(self, path=None):
        if path:
            dir = self.current.children[path]
        else:
            dir = self.current
        keys = list(dir.children.keys())
        # return keys ......
        return keys if keys else "Empty"

    def grep(self, pattern, file):
        if file in self.current.children and not self.current.children[file].is_directory:
            words = self.current.children[file].content.split()
            matches = [word for word in words if re.search(pattern, word, re.IGNORECASE)]
            return matches
        return "File not found"

    def cat(self, file):
        if file in self.current.children and not self.current.children[file].is_directory:
            return self.current.children[file].content
        return "File not found"

    def touch(self, name):
        if name in self.current.children:
            return "File already exists"
        self.current.children[name] = Node(name, False, "")


    def echo(self, text, file):
        if file in self.current.children and not self.current.children[file].is_directory:
            if self.current.children[file].content is None:
                self.current.children[file].content = text
            else:
                self.current.children[file].content += text
        else:
            return "File not found"

    def mv(self, src, dest):
        src_paths = src.split('/')
        dest_paths = dest.split('/')
        src_name = src_paths[-1]
        # Find the source node
        src_node = self.root if src.startswith('/') else self.current
        for p in src_paths[1:-1]:
            if p in src_node.children:
                src_node = src_node.children[p]
            else:
                return "Source not found"
        
        # Find the destination node
        dest_node = self.root if dest.startswith('/') else self.current
        for p in dest_paths[1:]:
            if p in dest_node.children:
                dest_node = dest_node.children[p]
            else:
                return "Destination not found"
        
        if src_name in src_node.children:
            src_node.children[src_name].parent = dest_node
            dest_node.children[src_name] = src_node.children[src_name]
            del src_node.children[src_name]
        else:
            return "Source not found"

    def cp(self, src, dest):
        if src == dest:
            src_paths = src.split('/')
            src_name = src_paths[-1]
            src_node = self.root if src.startswith('/') else self.current
            for p in src_paths[1:-1]:
                if p in src_node.children:
                    src_node = src_node.children[p]
                else:
                    return "Source not found"
            if src_name in src_node.children:
                # Create a new file with a name based on the original file's name
                new_name = src_name + "_copy"
                new_file = Node(new_name, False)
                new_file.content = src_node.children[src_name].content
                new_file.parent = src_node
                src_node.children[new_name] = new_file
            else:
                return "Source not found"
        else:
            src_paths = src.split('/')
            dest_paths = dest.split('/')
            src_name = src_paths[-1]
            # Find the source node
            src_node = self.root if src.startswith('/') else self.current
            for p in src_paths[1:-1]:
                if p in src_node.children:
                    src_node = src_node.children[p]
                else:
                    return "Source not found"
            
            # Find the destination node
            dest_node = self.root if dest.startswith('/') else self.current
            for p in dest_paths[1:]:
                if p in dest_node.children:
                    dest_node = dest_node.children[p]
                else:
                    return "Destination not found"
            
            if src_name in src_node.children:
                src_node.children[src_name].parent = dest_node
                dest_node.children[src_name] = src_node.children[src_name]
            else:
                return "Source not found"

    def rm(self, name):
        if name in self.current.children:
            del self.current.children[name]
        else:
            return "File or directory not found"
    
    def save_state(self, path):
        with open(path, 'w') as f:
            json.dump(self.root.to_dict(), f)

    def load_state(self, path):
        if os.path.exists(path) and os.path.getsize(path) > 0:
            with open(path, 'r') as f:
                data = json.load(f)
                self.root = self.dict_to_node(data)
                self.current = self.root
        else:
            self.root = Node('/', True)

    def dict_to_node(self, data):
        node = Node(data['name'], data['is_directory'], None, data['content'])
        node.children = {name: self.dict_to_node(child_data) for name, child_data in data['children'].items()}
        for child in node.children.values():
            child.parent = node
        return node
    