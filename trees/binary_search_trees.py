class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        new_node = Node(new_val)
        self.insert_internal(self.root, new_node)

    def insert_internal(self, obj, new_node):

        if new_node.value < obj.value:
            if obj.left:
                self.insert_internal(obj.left, new_node)
            else:
                obj.left = new_node

        elif new_node.value > obj.value:
            if new_node.value < obj.value:
                if obj.right:
                    self.insert_internal(obj.right, new_node)
                else:
                    obj.right = new_node

    def search(self, find_val):
        return self.search_internal(self.root, find_val)

    def search_internal(self, obj, find_val):
        if obj:

            if obj.value == find_val:
                return True
            elif obj.value < find_val:
                self.search_internal(obj.left, find_val)
            else:
                self.search_internal(obj.right, find_val)

        return False


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))
