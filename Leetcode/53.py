#最大子序和
class Solution:
    def maxSubArray(self, nums):
        this_sum = 0
        max_sum = max(nums)
        for i in range(len(nums)):
            this_sum += nums[i]
            if this_sum >= max_sum:
                max_sum = this_sum
            elif this_sum < 0:
                this_sum = 0
        return max_sum
        """
        :type nums: List[int]
        :rtype: int
        """
