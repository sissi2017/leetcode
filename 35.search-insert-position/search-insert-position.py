class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = int((right-left)/2)+left
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                right = mid-1
            else:
                left = mid+1
        return left
