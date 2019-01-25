class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1
        if x < 0:
            flag = -1
            x = -x
        R = str(x)[::-1]
        R = int(R)
        if R> 2147483647 or R < -2147483648:
            R = 0
        return R*flag
