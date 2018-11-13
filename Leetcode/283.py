#移动零
class Solution:
    def moveZeroes(self, nums):
        n = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[n] = nums[i]
                n = n+1
        for i in range(n, len(nums)):
            nums[i] = 0
        return
        """ 
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
