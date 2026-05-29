class Solution:
    def countSubstrings(self, s: str) -> int:
        #two options, dp but it will be n^2 memory and runtime
        # can do iterative solution with window
        #visit each letter and expand as much as can, add to set and return length of set

        palindromes = []

        def get_max_palindromes(l: int, r: int) -> None:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palindromes.append(s[l:r+1])
                l -= 1
                r += 1
        
        for i in range(len(s)):
            get_max_palindromes(i, i)
            if i + 1 < len(s):
                get_max_palindromes(i, i+1)

        return len(palindromes)