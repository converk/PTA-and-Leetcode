#27. 移除元素
class Solution:
    def removeElement(self, nums, val):
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count = count+1
        return count
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
