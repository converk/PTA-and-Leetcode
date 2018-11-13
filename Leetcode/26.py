#26. 删除排序数组中的重复项
class Solution:
    def removeDuplicates(self, nums):
        length = len(nums)
        result = 1
        if length == 0:
            return 0
        if length == 1:
            return 1
        for i in range(1, length):
            if nums[i] == nums[i-1]:
                continue
            else:
                nums[result] = nums[i]
                result = result+1
        return result
