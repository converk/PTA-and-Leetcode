#20. 有效的括号
class Solution:
    def isValid(self, s):
        d1 = ["(", "{", "["]
        d2 = [")", "}", "]"]

        def iskuo(string):
            return string in d1+d2
        a = filter(iskuo, s)
        l = []
        for i in a:
            if i in d1:
                l.append(i)
                #continue
            if i in d2:
                if l == []:
                    return False
                if d1.index(l[-1]) == d2.index(i):
                    del l[-1]
                    continue
                else:
                    return False
        if l == []:
            return True
        else:
            return False

        """
        :type s: str
        :rtype: bool
        """
