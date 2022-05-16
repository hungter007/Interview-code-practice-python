from copy import deepcopy


class Solution:

    def subsets(self, nums):
        self.return_list = list()
        temp_list = list()
        self.traceback(nums, temp_list, 0)
        return self.return_list

    def traceback(self, nums, temp_list, start):
        self.return_list.append(temp_list)

        for i in range(start, len(nums)):
            temp_list.append(nums[i])
            next_temp = deepcopy(temp_list)
            self.traceback(nums, next_temp, i + 1)
            temp_list.remove(nums[i])