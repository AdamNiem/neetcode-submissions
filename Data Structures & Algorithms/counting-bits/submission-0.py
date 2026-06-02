class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            #assuming its 64 bit integer
            res.append(0)
            t = 1
            for _ in range(64):
                #have t = 0000...001 initially
                #so we do a & (and bitwise) for the first bit of i
                #if true then increment counter and bitshift t to left regardless
                if t & i > 0:
                    res[i] += 1
                t <<= 1 #bitshift the 1 aka 't' to the left
        return res