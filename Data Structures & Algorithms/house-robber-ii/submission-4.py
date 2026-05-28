class Solution:
    #now we do a bottom up dp solution by creating a copy of nums called dp
    #and storing current max in every other item in dp somehow
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 0:
            return 0

        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [0 for _ in range(len(nums) - 1)]
        #first run from (0 to len(nums) - 2)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums) - 1):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        res = dp[-1]

        #second run from (1 to len(nums) - 1)
        dp = [0 for _ in range(0, len(nums))]
        dp[1] = nums[1]
        dp[2] = max(nums[1], nums[2])
        for i in range(2+1, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        '''
        [0, 0, 0, 0, 0]
        [0, 9, 8, 0, 0]
        [0, 9, 8,12, 0]
        [0, 9, 8,12, ]
        '''

        print("yes")
        print(dp)
       
        return max(res, dp[-1])
