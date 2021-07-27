# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root == None:
            return root
        self.flatten(root.left)
        self.flatten(root.right)

        left = root.left
        right = root.right
        root.left = None
        root.right = left

        p = root
        while p.right is not None:
            p = p.right
        p.right = right
        return root
