#回文数
class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False

        """
        :type x: int
        :rtype: bool
        """
