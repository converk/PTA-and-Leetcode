#旋转数组
class Solution:
    def rotate(self, nums, k):
        j = len(nums)
        if k > len(nums):
            k = k % len(nums)
        for i in range(j-k):
            nums.append(nums[0])
            del nums[0]
        return
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
