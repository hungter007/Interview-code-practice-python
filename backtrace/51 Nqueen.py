class Solution:

    def solveNQueens(self, n):
        self.return_res = list()
        res_list = [["." for i in range(n)] for j in range(n)]
        self.back_track(res_list, n, 0)
        return self.return_res

    def is_valid(self, res_list, row, col, n):
        for i in range(row - 1, -1, -1):
            if res_list[i][col] == "Q":
                return False
        off = 1
        while row - off >= 0:
            if col - off >= 0:
                if res_list[row - off][col - off] == "Q":
                    return False
            if col + off <= n - 1:
                if res_list[row - off][col + off] == "Q":
                    return False
            off += 1
        return True

    def back_track(self, res_list, n, row):
        if len(res_list) == row:
            self.return_res.append(["".join(item) for item in res_list])
            return

        for col in range(n):
            if self.is_valid(res_list, row, col, n):
                res_list[row][col] = "Q"
                self.back_track(res_list, n, row + 1)
                res_list[row][col] = "."