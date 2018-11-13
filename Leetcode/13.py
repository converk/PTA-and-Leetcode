#罗马数字转整数
class Solution:
    def romanToInt(self, s):
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        a = s[0]
        for i in s[1:]:
            if d[a] < d[i]:
                sum1 = d[i]-2*d[a]
            else:
                sum1 = d[i]
            sum = sum+sum1
            a = i
        return sum+d[s[0]]

        """
        :type s: str
        :rtype: int
        """
