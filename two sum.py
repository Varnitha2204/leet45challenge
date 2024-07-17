class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for i,num in enumerate(nums):
            c = target-num
            if c in index:
                return [index[c],i]
            index[num]=i
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        #             break
                
