'''
题目：输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
'''

'''
分析，两个序列才能确定一个一棵树，所以先用先序遍历，再用字符串进行匹配是不对的，因为的树的结构你确定不了。
这一题，首先判断根节点是不是相同，不相同是一个递归，把pRoot1的左右子树一次和PRoot2进行判断
如果根节点相同，那么进入下一个函数，接着判断，左边节点的下一级和左边子树下一级是不是相同，又是一个递归。
两个递归操作
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        result = False
        if A != None and B != None:
            if A.val == B.val:
                result = self.same(A, B)
            if not result:
                result = self.isSubStructure(A.left, B)
            if not result:
                result = self.isSubStructure(A.right, B)
        return result

    def same(self, A: TreeNode, B: TreeNode) -> bool:
        if B == None:
            return True
        if A == None:
            return False
        if A.val != B.val:
            return False
        return self.same(A.left, B.left) and self.same(A.right, B.right)