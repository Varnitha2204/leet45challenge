class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # if n <= 0:
        #     return False
        # while n % 3 == 0:
        #     n //= 3
        # return n == 1
        if n<=0:
            return False
        else:
            # As 3^20 will be greater than range of 32 bit signed integer
            x = 3**19
            return x%n==0
        
