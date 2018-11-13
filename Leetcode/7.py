#反转整数
class Solution:
    def reverse(self, x):
        a = str(x)
        m = 2**31-1
        n = -2**31
        if a[0] == '-':
            b = '-'+a[::-1]
            b = b[:-1]
            c = int(b)
        else:
            c = int(a[::-1])
        if c < m and c > n:
            return c
        return 0
        """
        :type x: int
        :rtype: int
        """
