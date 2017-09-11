# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        level1 = [root]
        while level1:
            res.append(level1[-1].val)
            level2 = []
            for node in level1:
                if node.left:
                    level2.append(node.left)
                if node.right:
                    level2.append(node.right)
            level1 = level2
        return res