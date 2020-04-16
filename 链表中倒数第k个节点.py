'''
题目：输入一个链表，输出该链表中倒数第k个结点。
'''
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        res = []
        cur = head
        while cur:
        	res.append(head.val)
        	cur = cur.next

		if k > len(res) or k < 1:
            return None

        return res[-k]