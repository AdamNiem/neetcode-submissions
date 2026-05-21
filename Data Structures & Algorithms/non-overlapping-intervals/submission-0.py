class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[0])
                
        last_end = intervals[0][1]
        count = 0

        i = 1
        while i < len(intervals):
            interval = intervals[i]
            if interval[0] < last_end:
                #if overlap remove the one which ends later
                if interval[1] > last_end:
                    intervals.pop(i)
                    last_end = last_end
                else:
                    intervals.pop(i - 1)
                    last_end = interval[1]
                i -= 1
                count += 1
            else:
                last_end = interval[1]

            i += 1
           
        return count
