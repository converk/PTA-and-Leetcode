#验证回文串
class Solution:
    def isPalindrome(self, s):
        a = ''
        s = s.lower()
        for i in s:
            if (i >= '0' and i <= '9') or (i >= 'a' and i <= 'z'):
                a += i
        return a == a[::-1]
        if not s.strip():
            return True
        """
        :type s: str
        :rtype: bool
        """
