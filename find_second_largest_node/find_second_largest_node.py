def find_largest(root_node):
    current = root_node
    while current:
        if not current.right:
            return current.value
        current = current.right


def find_second_largest(root_node):
    if (root_node is None or
            (root_node.left is None and root_node.right is None)):
        raise ValueError('Tree must have at least 2 nodes')

    current = root_node
    while current:
        # Case: current is largest and has a left subtree
        # 2nd largest is the largest in that subtree
        if current.left and not current.right:
            return find_largest(current.left)

        # Case: current is parent of largest, and largest has no children,
        # so current is 2nd largest
        if (current.right and
                not current.right.left and
                not current.right.right):
            return current.value

        current = current.right

'''
Complexity
We're doing one walk down our BST, which means O(h)time, 
where h is the height of the tree 
(again, that's O(lg⁡n) if the tree is balanced, O(n) otherwise). 
O(1) space.

'''
def second_largest(root):
    def reverse_inorder(root, traversal):
        if root is None or len(traversal) == 2:
            return
        reverse_inorder(root.right, traversal)
        traversal.append(root.val)
        reverse_inorder(root.left, traversal)
        return
    
    traversal = []
    
    reverse_inorder(root, traversal)
    
    return traversal[1]