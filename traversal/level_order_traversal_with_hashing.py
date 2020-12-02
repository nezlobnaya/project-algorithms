"""
using hashing
traverse the tree in preorder fashion and store every node and its level 
into the multimap using level number as a key.
Finally, we print all nodes corresponding to every level starting from first level.
We can also traverse the tree in oreer or postorder fashion

"""

# Data structure to store a Binary Tree node
class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
 
 
# traverse the tree in pre-order fashion and store nodes into the dictionary
# corresponding to their level
def preorder(root, level, dict):
 
    # base case: empty tree
    if root is None:
        return
 
    # insert current node and its level into the dictionary
    dict.setdefault(level, []).append(root.value)
 
    # recur for left and right subtree by increasing level by 1
    preorder(root.left, level + 1, dict)
    preorder(root.right, level + 1, dict)
    print("Dict :", f"{root.value}: {level}")
    print("Dict whole :", dict)
 
# Recursive function to print level order traversal of given binary tree
def levelOrderTraversal(root):
 
    # create an empty dict to store nodes between given levels
    dict = {}
 
    # traverse the tree and insert its nodes into the dictionary
    # corresponding to the their level
    preorder(root, 1, dict)
 
    # iterate through the dictionary and print all nodes between given levels
    for i in range(1, len(dict) + 1):
        print(f"Level {i}:", dict[i])
 
 
if __name__ == '__main__':
 
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.left = Node(16)
    root.right.right = Node(25)
    root.right.right.right = Node(30)
 
    levelOrderTraversal(root)
 