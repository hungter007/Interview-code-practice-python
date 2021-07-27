"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return root
        self._help(root.left, root.right)

        return root

    def _help(self, left, right):
        """
        :type left: Node
        :type right: Node
        """
        if left is None or right is None:
            return

        left.next = right
        self._help(left.left, left.right)
        self._help(right.left, right.right)
        self._help(left.right, right.left)