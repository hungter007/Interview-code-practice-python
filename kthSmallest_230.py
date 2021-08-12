# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = list()
        val_list = self.get_tree_list(root, res)
        return val_list[k-1]

    def get_tree_list(self, root, res):
        if not root:
            return res
        res = self.get_tree_list(root.left, res)
        res.append(root.val)
        res = self.get_tree_list(root.right, res)
        return res
