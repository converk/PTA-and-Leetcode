#二进制求和
class Solution:
    def addBinary(self, a, b):
        index1, index2 = len(a) - 1, len(b) - 1
        result = ""
        # 进位的值，0表示不进位（进位0），1表示进位1
        add1 = 0
        while index1 >= 0 or index2 >= 0:
            t1 = int(a[index1]) if index1 >= 0 else 0
            t2 = int(b[index2]) if index2 >= 0 else 0
            temp = t1 + t2 + add1
            result = str(temp % 2) + result
            add1 = temp // 2
            index1 -= 1
            index2 -= 1
        if add1 == 1:
            result = "1" + result
        return result
        """
        :type a: str
        :type b: str
        :rtype: str
        """
