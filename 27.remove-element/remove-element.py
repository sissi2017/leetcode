class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index= 0
        for i in range(0,len(nums)):
            if nums[i]!= val:
                nums[index]=nums[i]
                index=index+1
        return index
        
