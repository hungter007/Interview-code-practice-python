'''
题目：
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个非递减排序的数组的一个旋转，输出旋转数组的
最小元素。例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。NOTE：给出的所有元素都大于0，若数组大小为0，
请返回0。
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return 0
        first = 0
        last = len(nums)-1
        if len(nums) == 1:
            return nums[0]

        if nums[last] > nums[0]:
            return nums[0]

        while first <= last:
            mid = first + (last - first) // 2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            
            if nums[first] > nums[mid]:
                last -= 1
            else:
                first += 1