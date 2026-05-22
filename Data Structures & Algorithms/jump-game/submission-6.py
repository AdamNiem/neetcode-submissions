class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        goal_post = len(nums) - 1
        for idx in reversed(range(0, goal_post)):
            if nums[idx] + idx >= goal_post:
                goal_post = idx
        
        return not bool(goal_post)


        #sliding window
        #extend window by r for each jump
        #then want to pick the value in our window
        #that is max for (nums[idx - (len(nums) - idx) ])
        #so basically pick the one that will get you the farthest
        #and keep doing that till you cant expand the window no more