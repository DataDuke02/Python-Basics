class Solution:
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False

        if root.left is None and root.right is None:
            return root.val == targetSum

        targetSum -= root.val

        return (
            self.hasPathSum(root.left, targetSum)
            or self.hasPathSum(root.right, targetSum)
        )

  """
        5
       / \
      4   8
     /   / \
    11  13  4

  targetSum = 20

  5 → 4 → 11

  5 + 4 + 11 = 20

  True
  """
