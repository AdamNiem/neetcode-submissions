class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        #base case: newInterval inserted and no overlap, good!
        #lets add newInterval and then sort by first element first

        intervals.append(newInterval)

        #sort by first element of each interval
        intervals.sort(key=lambda x: x[0])

        end = intervals[0][1]

        i = 1
        while i < len(intervals):
            interval = intervals[i]
            if interval[0] <= end:
                #overlap detected so will merge them
                #update former interval and remove current and increment index
                end = max(end, interval[1])
                intervals[i - 1][1] = end
                intervals.pop(i)
                i -= 1
            else:
                #no overlap so update start and end
                start = interval[0]
                end = interval[1]
            
            i += 1
        
        return intervals
                
