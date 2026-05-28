class Solution:
    def longestPalindrome(self, s: str) -> str:            
        def get_max_palindrome(l: int, r: int) -> str:
            #l, r represent index of center(s)
            #print(l, r)
            while l >= 0 and r < len(s) and s[l] == s[r]:
                #print(s[l:r+1])
                l -= 1
                r += 1
            l += 1
            r -= 1
            #print(s[l:r+1])
            return s[l:r+1]

        res = ""
        for i in range(len(s)):
            output = get_max_palindrome(i, i)
            
            if len(output) > len(res):
                res = output
            
            if i + 1 < len(s) and s[i] == s[i + 1]:
                output = get_max_palindrome(i, i + 1)
                if len(output) > len(res):
                    res = output

        return res
