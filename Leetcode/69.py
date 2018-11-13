#x的平方根
class Solution:
    def mySqrt(self, x):
        if x == 1:
            return 1
        lift = 0
        right = x
        a = 0
        while True:
            mid = (lift+right)//2
            if mid*mid > x:
                right = mid
                a = 1
            if mid*mid < x:
                lift = mid
                a = 0
            if mid*mid == x:
                return mid
            if right-lift == 1:
                return mid if a == 0 else mid-1
        """
        :type x: int
        :rtype: int
        """
