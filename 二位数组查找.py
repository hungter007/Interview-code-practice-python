'''
题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if not array:
            return
        row = len(array)
        col = len(array[0])

        for i in range(row):
            for j in range(col):
                if target == array[i][j]:
                    return True

        return False