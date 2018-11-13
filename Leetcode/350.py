# 两个数组的交集 II
class Solution:
    def intersect(self, nums1, nums2):
        list1 = []
        if len(nums1) < len(nums2):
            for i in nums1:
                if i in nums2:
                    list1.append(i)
                    del nums2[nums2.index(i)]
        else:
            for i in nums2:
                if i in nums1:
                    list1.append(i)
                    del nums1[nums1.index(i)]
        return list1
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
