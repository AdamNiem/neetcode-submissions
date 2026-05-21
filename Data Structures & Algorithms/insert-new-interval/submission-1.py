class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []

        for i in range(len(intervals)):
            #case 1: newInterval starts after the current interval's end
            if newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
                
            #case 2: newInterval ends before the current interval's starts
            elif newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            else:
            #case 3: has to be colliding if failed both above
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        
        res.append(newInterval)

        return res
                
