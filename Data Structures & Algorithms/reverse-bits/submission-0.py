class Solution:
    def reverseBits(self, n: int) -> int:
        #just got to shift it 32 times
        #and right before each shift check if leftmost digit is 1
        #if so then we want to preserve it so loop it over afte rthe shift
        #by adding 1 to result
        leftmost_bit = 2**31 #should be in binary 1000000...
        res = 0
        for i in range(32):
            rightmost_bit = ((n >> i) & 1)
            if rightmost_bit > 0: 
                res |= (1 << (31 - i))
                #res += 2**(31 - i)
        return res
