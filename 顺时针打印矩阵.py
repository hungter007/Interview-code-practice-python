'''
题目：输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，
如果输入如下矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''

'''
思路超神：
可以模拟魔方逆时针旋转的方法，一直做取出第一行的操作
例如
1 2 3
4 5 6
7 8 9
输出并删除第一行后，再进行一次逆时针旋转，就变成：
6 9
5 8
4 7
继续重复上述操作即可
'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return matrix
        res = []
        while matrix:
            res += matrix.pop(0)
            if not matrix:
                break
            matrix = self.turn(matrix)
        return res
    
    def turn(self, matrix: List[List[int]]) -> List[List[int]]:
        cow = len(matrix)
        col = len(matrix[0])
        out_matrix = []
        for i in range(col):
            new_cow = []
            for j in range(cow):
                new_cow.append(matrix[j][i])
            out_matrix.append(new_cow)
        out_matrix.reverse()
        return out_matrix