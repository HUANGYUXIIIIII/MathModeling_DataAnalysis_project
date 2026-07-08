//Leetcode - 1486-数组异或操作

class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        res = 0
        for i in range(n):
            num = start +2*i
            res =res^num
        return res