class Solution(object):
    temp_dict = dict()

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.count(1, n + 1)

    def count(self, low, high):
        if low >= high:
            return 1

        temp_key = str(low) + "-" + str(high)
        if temp_key in self.temp_dict:
            return self.temp_dict.get(temp_key)
        res = 0
        for _i in range(low, high):
            left_count = self.count(low, _i)
            right_count = self.count(_i + 1, high)
            count = left_count * right_count
            res += count
        self.temp_dict[temp_key] = res
        return res
