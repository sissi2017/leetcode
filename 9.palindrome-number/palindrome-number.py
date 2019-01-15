class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        xstr = str(x)
        ystr = ''
        for i in range(0,len(xstr)):
            ystr = ystr+xstr[-(i+1)]
        if int(ystr)==x:
            return True
        else:
            return False
        


        
