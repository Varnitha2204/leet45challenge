class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        if n&n-1!=0:
            return False
        # Here you need to check the even position '1' is present or not 
        return (n & 0x55555555) != 0
