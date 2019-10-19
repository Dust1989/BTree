from binary_tree import BinaryTree
from node import Node

bt = BinaryTree(Node(14))

# num_list = [5,6,30,99,100,60,10,4]
num_list = [9,13,22,34]

num_str = [str(i) for i in num_list]

for i in num_list:
    bt.add(Node(i))

# bt.inorder()
#
# print(bt.find(99))
#
# bt.delete(99)
#
# bt.inorder()
#
# bt.delete(20)
#
bt.inorder()
bt.perorder()
bt.postorder()

# print("->".join(num_str))