class Solution:
    #now we do simple version since only need to store last 2 values each step
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robLinear(arr):
            #first run from (0 to len(nums) - 2)
            rob1 = 0
            rob2 = 0
            for num in arr:
                newRob = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = newRob

            return rob2

        return max(
            robLinear(nums[1:]),
            robLinear(nums[:-1])
        )
