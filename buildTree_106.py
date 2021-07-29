# coding: utf-8
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        root_value = postorder[-1]
        inorder_root_index = inorder.index(root_value)

        new_left_inorder = inorder[:inorder_root_index]
        new_right_inorder = inorder[inorder_root_index+1:]
        new_left_postorder = postorder[:len(new_left_inorder)]
        new_right_postorder = postorder[len(new_left_inorder): len(new_left_inorder)+len(new_right_inorder)]

        left = self.buildTree(list(new_left_inorder), list(new_left_postorder))
        right = self.buildTree(list(new_right_inorder), list(new_right_postorder))
        root = TreeNode(root_value, left, right)
        return root


if __name__ == '__main__':
    # 中序遍历
    inorder = [9, 3, 15, 20, 7]
    # 后序遍历
    postorder = [9, 15, 7, 20, 3]
    su = Solution()
    tree = su.buildTree(inorder, postorder)
    print tree