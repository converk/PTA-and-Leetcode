#有效的字母异位词
class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        dict1 = {}
        dict2 = {}
        for i in t:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
        for i in s:
            if i not in dict2:
                dict2[i] = 1
            else:
                dict2[i] += 1
        if dict1 == dict2:
            return True
        return False

        """
        :type s: str
        :type t: str
        :rtype: bool
        """
