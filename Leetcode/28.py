#实现strStr()
class Solution:
    def strStr(self, haystack, needle):
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1

        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
