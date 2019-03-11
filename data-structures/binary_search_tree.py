class MyTreeNode(object):
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left_child = None
        self.right_child = None

    def get_generator(self):
        if self.left_child:
            for elem in self.left_child.get_generator():
                yield elem
        yield self.data
        if self.right_child:
            for elem in self.right_child.get_generator():
                yield elem

    def __str__(self):
        left_data = self.left_child.data if self.left_child is not None else self.left_child
        right_data = self.right_child.data if self.right_child is not None else self.right_child
        return f'{left_data} <--( {self.data} )--> {right_data}'


class MyBinarySearchTree:
    def __init__(self, root_value=None):
        self.root = MyTreeNode(root_value)

    def insert(self, value):
        current_node = self.root
        left_child, right_child, parent = None, None, None
        while current_node is not None and current_node.data is not None:
            parent = current_node
            if value >= current_node.data:
                current_node = current_node.right_child
                if not current_node:
                    right_child = True
            else:
                current_node = current_node.left_child
                if not current_node:
                    left_child = True
        if left_child:
            parent.left_child = MyTreeNode(value, parent)
        elif right_child:
            parent.right_child = MyTreeNode(value, parent)
        else:
            self.root = MyTreeNode(value)

    def remove(self, value):
        node_to_remove = self._get_node(value)
        node_to_replace = self._get_node_to_replace(node_to_remove)

        if node_to_replace is not None:

            # set connection with the parent
            node_to_replace.parent = node_to_remove.parent
            if node_to_replace.parent is not None:
                node_to_replace.parent.right_child = node_to_replace
            else:
                self.root = None

            # set connection with the right child
            if not node_to_remove.right_child == node_to_replace:
                node_to_replace.right_child = node_to_remove.right_child
                if node_to_replace.right_child:
                    node_to_replace.right_child.parent = node_to_replace

            # set connection with the left child
            if not node_to_remove.left_child == node_to_replace:
                node_to_replace.left_child = node_to_remove.left_child
                if node_to_replace.left_child:
                    node_to_replace.left_child.parent = node_to_replace

        elif node_to_remove.parent is not None:
            node_to_remove.parent.right_child = None
        else:
            self.root = None

    def min_value(self, subtree_root=None):
        return self.min_node(subtree_root).data

    def max_value(self, subtree_root=None):
        return self.max_node(subtree_root).data

    def minmax_value(self, subtree_root=None):
        return self.min_value(subtree_root), self.max_value(subtree_root)

    def min_node(self, subtree_root=None):
        current_node = self.root if subtree_root is None else subtree_root
        while current_node.left_child is not None:
            current_node = current_node.left_child
        return current_node

    def max_node(self, subtree_root=None):
        current_node = self.root if subtree_root is None else subtree_root
        while current_node.right_child is not None:
            current_node = current_node.right_child
        return current_node

    def _get_node(self, value):
        current_node = self.root
        while current_node is not None:
            if value > current_node.data:
                current_node = current_node.right_child
            elif value < current_node.data:
                current_node = current_node.left_child
            else:
                return current_node
        print("Value is not in the tree")

    def _get_node_to_replace(self, node_to_remove):
        if node_to_remove.left_child is not None:
            return self.max_node(node_to_remove.left_child)
        elif node_to_remove.right_child is not None:
            return node_to_remove.right_child
        return

    def get_generator(self):
        return self.root.get_generator()

    def _get_list_of_values(self, root):
        if root is None:
            return ''
        if root.left_child == root.right_child:
            return [root.data]
        else:
            return [self._get_list_of_values(root.left_child),
                    root.data,
                    self._get_list_of_values(root.right_child)]

    def __str__(self):
        return str(self._get_list_of_values(self.root))


if __name__ == '__main__':
    my_tree = MyBinarySearchTree(6)
    my_tree.insert(2)
    my_tree.insert(1)
    my_tree.insert(4)
    my_tree.insert(3)
    my_tree.insert(5)
    my_tree.insert(7)
    my_tree.insert(8)
    my_tree.insert(9)
    print(my_tree)
    my_tree.remove(7)
    print(my_tree)
    my_tree.insert(7)
    print(my_tree)
    for x in my_tree.get_generator():
        print(x, end=' ')

# [[[1], 2, [[3], 4, [5]]], 6, ['', 7, ['', 8, [9]]]]
# [[[1], 2, [[3], 4, [5]]], 6, ['', 8, [9]]]
# [[[1], 2, [[3], 4, [5]]], 6, [[7], 8, [9]]]
# 1 2 3 4 5 6 7 8 9
