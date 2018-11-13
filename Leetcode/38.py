#报数
class Solution:
    def countAndSay(self, n):
        if n == 1:
            a = '1'
            return a
        if n == 2:
            a = '11'
            return a
        if n == 3:
            a = '21'
            return a
        s = self.countAndSay(n-1)
        s0 = s[0]
        count = 0
        l = ''
        b, c = 0, ''
        for i in s:
            if i == s0:
                count = count+1
                b = count
               # c=s0
            else:
                l = l+str(count)
                l = l+str(s0)
                s0 = i
                count = 0
                count = count+1
                b = count
                c = s0
        l = l+str(b)
        l = l+c
        return l

        """
        :type n: int
        :rtype: str
        """
