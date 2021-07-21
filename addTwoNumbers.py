# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def add_two_numbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pre = ListNode()
        cur = pre
        temp = 0
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            sum = l1_val + l2_val + temp
            if sum >= 10 :
                sum = sum % 10
                temp = 1
            else:
                temp = 0
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur.val = sum
            if l1 or l2:
                cur.next = ListNode()
            else:
                if temp:
                    cur.next = ListNode(temp)
                else:
                    cur.next = None
            cur = cur.next

        return pre


if __name__ == '__main__':
    su = Solution()
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    res = su.add_two_numbers(l1, l2)
    print res
