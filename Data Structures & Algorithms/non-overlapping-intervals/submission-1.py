class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = 0

        prev_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prev_end:
                #no overlap case
                prev_end = end
            else:
                #overlap case, greedy so pick soonest ending interval
                prev_end = min(prev_end, end)
                res += 1

        return res