'''
题目：输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
    	root = ListNode(None)
    	cur = root
    	while pHead1 and pHead2:
    		if pHead1.val >= pHead2.val:
    			new = pHead2
    			pHead2 = pHead2.next
    		else:
    			new = pHead1
    			pHead1 = pHead1.next
    		cur.next = new
    		cur = new
    	cur.next = pHead1 or pHead2
    	return cur.next