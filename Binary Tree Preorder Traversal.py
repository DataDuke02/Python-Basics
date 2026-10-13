class Solution:
    def preorderTraversal(self, root):
        result = []

        def preorder(node):
            if node is None:
                return

            result.append(node.val)  # Root
            preorder(node.left)      # Left
            preorder(node.right)     # Right

        preorder(root)
        return result
