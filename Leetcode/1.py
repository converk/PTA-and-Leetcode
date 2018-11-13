class Solution:
    def twoSum(self, nums, target):
        for i in nums:
            j = target-i
            if i != j:
                if j in nums:
                    return [nums.index(i), nums.index(j)]
            if i == j:
                nums_1 = nums[::-1]
                a = len(nums)-nums_1.index(j)-1
                b = nums.index(i)
                if a != b:
                    return [b, a]

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
