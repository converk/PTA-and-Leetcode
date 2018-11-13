#旋转图像
class Solution:
    def rotate(self, matrix):
        lens = len(matrix)
        n = int(lens/2)
        for m in range(n):
            for p in range(m, lens-m-1):
                matrix[lens-p-1][m], matrix[m][p] = matrix[m][p], matrix[lens-p-1][m]
                matrix[lens-p-1][m], matrix[lens-m-1][lens-p -
                                                      1] = matrix[lens-m-1][lens-p-1], matrix[lens-p-1][m]
                matrix[lens-m-1][lens-p-1], matrix[p][lens-m -
                                                      1] = matrix[p][lens-m-1], matrix[lens-m-1][lens-p-1]
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
