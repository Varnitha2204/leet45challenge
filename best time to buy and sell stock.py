class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = float('inf') 
        m1 = 0
        for i in prices:
            if i<m:
                m = i
            p = i - m
            if p>m1:
                m1 = p
        return m1
            
