class Solution:
    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        # res_perm = [[]]
        # for num in nums:
        #     temp = []
        #     for perm in res_perm:
        #         for i in range(len(perm)+1):
        #             temp.append(perm[:i]+[num]+perm[i:])
        #     res_perm = temp
        # return res_perm
        res = []
        self.dfs(nums, [], res)
        return res
        
    def dfs(self ,nums ,path, res):
        if len(nums)==0:
            print(path)
            res.append(path)
        for i in range(len(nums)):
            print(i)
            self.dfs(nums[:i]+nums[i+1:], path + [nums[i]], res)
