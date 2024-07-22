class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set()
        k = []
        for num in nums:
            if num not in s:
                k.append(num)
                s.add(num)
        nums.clear()
        nums.extend(k)
        return len(nums)