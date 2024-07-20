from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # p = permutations(nums)
        # return p
        def backtrack(s):
            if s == len(nums):
                p.append(nums[:])
            for i in range(s,len(nums)):
                nums[s],nums[i]=nums[i],nums[s]
                backtrack(s+1)
                nums[s],nums[i] = nums[i],nums[s]
        p = []
        backtrack(0)
        return p
