# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        max_num = max(nums)
        max_index = nums.index(max_num)
        cur_node = TreeNode(max_num)
        cur_node.left = self.constructMaximumBinaryTree(nums[:max_index]) if nums[:max_index] else None
        cur_node.right = self.constructMaximumBinaryTree(nums[max_index+1:]) if nums[max_index+1:] else None
        return cur_node
