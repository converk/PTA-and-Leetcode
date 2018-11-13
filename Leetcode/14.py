#最长公共前缀
class Solution:
    def longestCommonPrefix(self, strs):
        if strs == []:
            a = ""
            return a
        a = strs[0]
        for i in strs:
            if i.startswith(a):
                continue
            else:
                b = a if len(a) <= len(i) else i
                s = 0
                for j in range(len(b)):
                    if a[j] == i[j]:
                        s = j+1
                        continue
                    else:
                        s = j
                        break
                a = b[:s]
        return a
        """
        :type strs: List[str]
        :rtype: str
        """
