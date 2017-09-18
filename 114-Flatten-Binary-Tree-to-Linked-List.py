# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        def flat(root):
            if not root:
                return
            left = root.left
            right = root.right
            if left:
                while left.right:
                    left = left.right
                root.right, root.left, left.right = root.left, None, right
            flat(root.right)
        flat(root)
                
