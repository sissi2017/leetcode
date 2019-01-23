class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        if n == 2:
            return '11'
        def testcountandsay(self,num,k):
            onenum = num[0]
            leni = 1
            renum = ''
            for i in range(1,len(num),1):
                nextnum = num[i]
                if nextnum == onenum:
                    leni+=1
                else:
                    renum = renum+str(leni)+onenum
                    onenum = nextnum
                    leni = 1
            renum = renum +str(leni)+onenum
            if k==n:
                return renum
            else:
                return testcountandsay(self,renum,k+1)
            
            
        return testcountandsay(self,'11',3)
