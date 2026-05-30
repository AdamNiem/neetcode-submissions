class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #expand window from i until hit 0
        max_product = nums[0]
        def dfs(i):
            nonlocal max_product
            curr = nums[i]
            max_product = max(
                        max_product,
                        curr
            )
            if i + 1 < len(nums):
                for j in range(i+1, len(nums)):
                    if nums[j] == 0:
                        return
                    curr *= nums[j]
                    max_product = max(
                        max_product,
                        curr
                    )

        for i in range(0, len(nums)):
            dfs(i)
    
        return max_product
        