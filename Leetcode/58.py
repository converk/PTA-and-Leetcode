#最后一个单词长度
class Solution:
    def lengthOfLastWord(self, s):
        if s == '':
            return 0
        s = s.strip()
        l = -1
        for i in range(len(s)):
            if s[i] == ' ':
                l = i
        return len(s)-l-1
        """
        :type s: str
        :rtype: int
        """
