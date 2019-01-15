class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        minlen = min([len(x) for x in strs])
        end = 0
        while end< minlen:
            for i in range(1,len(strs)):
                if strs[i][end]!=strs[i-1][end]:
                    return strs[0][:end]
            end = end +1
        return strs[0][:end]


