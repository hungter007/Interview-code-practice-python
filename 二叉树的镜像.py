'''
题目：操作给定的二叉树，将其变换为源二叉树的镜像。
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = root.right, root.left
            self.mirrorTree(root.right)
            self.mirrorTree(root.left)
        return root