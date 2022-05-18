#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates, target):
        return_list = list()
        if not candidates:
            return return_list

        def helper(temp, count):
            temp.sort()
            if count == target and temp not in return_list:
                return_list.append(temp[:])
                return

            if count > target:
                return

            for i in range(len(candidates)):
                temp.append(candidates[i])
                count += candidates[i]
                helper(temp[:], count)
                count -= candidates[i]
                temp.pop()

        helper([], 0)
        return return_list


# @lc code=end

if __name__ == "__main__":
    so = Solution()
    res = so.combinationSum([2, 3, 5], 8)
    print(res)
