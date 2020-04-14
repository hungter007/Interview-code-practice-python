'''
题目：
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
n<=39
'''

class Solution:
    def Fibonacci(self, n):
        # write code here
        if not n:
        	return 0
        if n < 3:
        	return 1
        else:
        	return self.Fibonacci(n-1) + self.Fibonacci(n-2)