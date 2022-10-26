# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.


class Solution:
    def reverse(self, x: int) -> int:
        retval = int(str(abs(x))[::-1])
        
        if(retval.bit_length()>31):
            return 0
    
        if x<0:
            return -1*retval
        else:
            return retval
