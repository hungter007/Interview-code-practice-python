class Solution:
    def combine(self, n, k):
        # @lc code=end
        return_list = list()

        def helper(start, temp):
            if len(temp) == k:
                return_list.append(temp[:])

            for i in range(start, n + 1):
                temp.append(i)
                helper(i + 1, temp)
                temp.pop()

        helper(1, [])
        return return_list