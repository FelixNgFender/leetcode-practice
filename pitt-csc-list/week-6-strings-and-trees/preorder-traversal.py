def preorderTraversal(root):
    # left right root
    if not root:
        return []
    return preorderTraversal(root.left) + preorderTraversal(root.right) + [root.val]
