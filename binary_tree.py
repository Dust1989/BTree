from node import Node


class BinaryTree:
    def __init__(self, head: Node):
        self.head = head

    def add(self, new_node: Node):
        current_node = self.head
        while current_node:
            if new_node.value == current_node.value:
                raise ValueError("A node with that value already exists.")
            elif new_node.value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    break
            elif new_node.value > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    break

    def find(self, value: int):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return current_node
            elif current_node.value > value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        raise LookupError(f"A node with value {value} was not found")

    def inorder(self):
        self._inorder_recursive(self.head)

    def _inorder_recursive(self, current_node):
        if not current_node:
            return
        self._inorder_recursive(current_node.left)
        print(current_node)
        self._inorder_recursive(current_node.right)

    def perorder(self):
        self._perorder_recursive(self.head)

    def _perorder_recursive(self, current_node):
        if not current_node:
            return
        print(current_node)
        self._perorder_recursive(current_node.left)
        self._perorder_recursive(current_node.right)

    def postorder(self):
        self._postorder_recursive(self.head)

    def _postorder_recursive(self, current_node):
        if not current_node:
            return
        self._postorder_recursive(current_node.left)
        self._postorder_recursive(current_node.right)
        print(current_node)

    def find_parent(self, value: int) -> Node:
        # if no parent it will be the head and return the head
        if self.head and self.head.value == value:
            return self.head

        current_node = self.head
        while current_node:
            if (current_node.left and current_node.left.value == value) or (
                    current_node.right and current_node.right.value == value):
                return current_node
            elif current_node.value > value:
                current_node = current_node.left
            else:
                current_node = current_node.right

    def find_rightmost(self, node: Node) -> Node:
        # if no right most it will return itself
        current_node = node
        while current_node.right:
            current_node = current_node.right
        return current_node

    def delete(self, value: int):
        to_delete_parent = self.find_parent(value)
        to_delete = self.find(value)

        if to_delete.left and to_delete.right:
            # has two children node
            rightmost = self.find_rightmost(to_delete.left)
            rightmost_paretn = self.find_parent(rightmost.value)

            if rightmost != to_delete.left:
                rightmost_paretn.right = rightmost.left
                rightmost.left = to_delete.left

            rightmost.right = to_delete.right

            if to_delete == to_delete_parent.left:
                to_delete_parent.left = rightmost
            elif to_delete == to_delete_parent.right:
                to_delete_parent.right = rightmost
            else:
                # to delete node is the head
                self.head = rightmost

        elif to_delete.left or to_delete.right:
            # has one child node
            if to_delete_parent == to_delete:
                self.head = self.head.left or self.head.right
            elif to_delete_parent.left.value == value:
                to_delete_parent.left = to_delete.left or to_delete.right
            else:
                to_delete_parent.right = to_delete.left or to_delete.right
        else:
            # has no child
            if to_delete_parent == self.head:
                self.head = None
            elif to_delete_parent.left.value == value:
                to_delete_parent.left = None
            else:
                to_delete_parent.right = None
