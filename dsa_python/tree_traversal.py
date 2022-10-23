from dataclasses import dataclass
from turtle import left


class Node:
    def __init__(self,data,left = None, right = None) -> None:
        self.data = data
        self.left = left
        self.right = right


def pre_order_traversal(node,path = ""):
    if node:
        path += str(node.data) + "-"
        path = pre_order_traversal(node.left,path)
        path = pre_order_traversal(node.right,path)
    return path


def post_order_traversal(node,path = ""):
    if node:
        path = post_order_traversal(node.left,path)
        path = post_order_traversal(node.right,path)
        path += str(node.data) + "-"
    return path

def in_order_traversal(node,path = ""):
    if node:
        path = in_order_traversal(node.left,path)
        path += str(node.data) + "-"
        path = in_order_traversal(node.right,path)
    return path

root = Node(15)
root.left = Node(10)
root.left.left = Node(5)
root.left.right = Node(12)

root.right = Node(18)
root.right.left = Node(16)
root.right.right = Node(19)


print("--------------Pre-order Traversal--------------")
print(pre_order_traversal(root))

print("--------------Post order Traversal--------------")
print(post_order_traversal(root))

print("--------------Inorder Traversal--------------")
print(in_order_traversal(root))