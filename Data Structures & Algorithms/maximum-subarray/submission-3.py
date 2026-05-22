class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += num
            max_sum = max(max_sum, cur_sum)

        return max_sum