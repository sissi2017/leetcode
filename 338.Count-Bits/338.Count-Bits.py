class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        
        """
        a = [0]
        for n in range(1,num+1):
            one_num = bin(n)[2:].count('1')
            a.append(one_num)
        return a
