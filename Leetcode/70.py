#爬楼梯
#之后再优化
class Solution:
    def climbStairs(self, n):
        if n < 2:
            return 1
        a, b = 1, 1
        while n >= 2:
            c = a+b
            a = b
            b = c
            n = n-1
        return c
        """
        :type n: int
        :rtype: int
        """
