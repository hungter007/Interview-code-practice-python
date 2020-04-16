'''
题目：输入一个链表，反转链表后，输出链表的所有元素。
'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
    	if not pHead and not pHead.next:
    		return pHead
    	pre = None
    	while pHead:
    		next = pHead.next
    		pHead.next = pre
    		pre = pHead
    		pHead = next
    	return pre
