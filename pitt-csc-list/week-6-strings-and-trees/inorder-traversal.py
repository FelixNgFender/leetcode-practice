def inorderTraversal(root):
    # left root right
    if not root:
        return []
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)

def inorderTraversalIterative(root):
    