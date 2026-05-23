class Solution:
    def hammingWeight(self, n: int) -> int:
        #1 + 2 + 4 + 16 = 23
        # 23 - 1 = 22
        # 22 - 16 - 4 - 2 - 1
        # so 23 mod 2 = 1
        # 22 = 11

        res = 0
        for i in range(0, 32):
            if n & (1 << i) > 0:
                res += 1
        
        return res

