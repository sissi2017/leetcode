class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = {')':'(', ']':'[', '}':'{'}
        l = [None]
        for i in s:
            if i in a and a[i] == l[-1]:
                l.pop()
            else:
                l.append(i)
        return len(l)==1
