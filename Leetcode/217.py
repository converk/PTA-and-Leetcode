#存在重复元素
class Solution:
    def containsDuplicate(self, nums):
        b = list(set(nums))
        if len(b) < len(nums):
            return True
        return False
        """
        :type nums: List[int]
        :rtype: bool
        """
