class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        reversed_str = str(abs(x))[::-1]
        result = sign * int(reversed_str)
        
        return result if -2**31 <= result <= 2**31 - 1 else 0