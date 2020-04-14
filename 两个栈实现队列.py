'''
题目：用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''

class Solution:
    def __init__(self):
        self.stackA = []
        self.stackB = []


    def push(self, value):
    	self.stackA.append(value)

    def pop(self):
    	if self.stackB:
    		return self.stackB.pop()
    	else:
    		if not self.stackA:
    			return None
    		else:
    			while self.stackA:
    				self.stackB.append(self.stackA.pop())
    			return self.stackB.pop()