#只出现一次的数字
class Solution:
    def singleNumber(self, nums):
        a = sorted(nums)
        for i in range(0, len(nums), 2):
            if i == len(nums)-1 or a[i] != a[i+1]:
                return a[i]
        """
        :type nums: List[int]
        :rtype: int
        """
