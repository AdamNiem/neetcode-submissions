class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #start at first positive number
        #sliding window record sum
        #on each window extension see if improves sum
        #if not then store max sum, abandon this window and find next positive number

        i, res, curr_sum = 0, -1001, 0
        max_val_seen = -1001
        l, r = 0, 0
        while l < len(nums) and r < len(nums):
            num = nums[r]
            # if the addition of the next number gives curr_sum worse than global best
            # then 
            # "reset and move the window" and reset curr_sum
            if curr_sum + num <= 0:
                max_val_seen = max(max_val_seen, nums[l])
                l += 1
                res = max(curr_sum, res)
                curr_sum = 0
                r = l
            else:
                curr_sum += num
                res = max(curr_sum, res)
                r += 1  

        if res == 0:
            return max_val_seen  

        return res
            
        
