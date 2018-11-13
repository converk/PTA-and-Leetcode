#加一
class Solution:
    def plusOne(self, digits):
        a = ''
        c = []
        for i in digits:
            a = a+str(i)
        b = int(a)+1
        for i in str(b):
            c.append(int(i))
        return c
        """
        :type digits: List[int]
        :rtype: List[int]
        """
