def postorderTraversal(root):
    # root left right
    if not root:
        return []
    return [root.val] + postorderTraversal(root.left) + postorderTraversal(root.right)
