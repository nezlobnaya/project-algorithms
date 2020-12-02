"""
We make use of queues to do the level order traversal. 
What we did is we visit a node and put its left and right child in the queue
and delete the current node. 
In this way we visit the tree in level order.
"""

class Node:

        def __init__(self,data):

                self.left = None

                self.right = None

                self.data = data

def level_order(queue):

        if len(queue) == 0:

                return

        node = queue[0]

        queue.pop(0)

        if node.left:

                queue.append(node.left)

        if node.right:

                queue.append(node.right)

        print(node.data)

        level_order(queue)

queue = list()

root = Node(1)

queue.append(root)

root.left = Node(2)

root.right = Node(3)

root.left.left = Node(4)

root.left.right = Node(5)

level_order(queue)

# 1 2 3 4 5 