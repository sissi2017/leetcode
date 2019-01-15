class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        number = 0
        roman_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in range(len(s)-1):
            if roman_dict[s[i]] < roman_dict[s[i+1]]:
                number -= roman_dict[s[i]]
            else:
                number += roman_dict[s[i]]
        number = number+roman_dict[s[-1]]
        return number
        

