class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        #sort list by start time
        intervals.sort(key = lambda x : x[0])

        start = intervals[0][0]
        end = intervals[0][1]

        #with this sorted list and starting from lowest to highest at 0
        #theres only 3 possible cases then where we can have merges
        # say A is lowest / initial and B is consequent one in list
        # So the cases are 
        # A starts and B starts after and B ends before A ends
        # B starts after A starts and ends after A ends
        # some equality of those

        i = 1
        while i < len(intervals):
            interval = intervals[i]
            #so if B starts before A ends its an overlap
            if interval[0] <= end:
                end = max(end, interval[1])
                intervals[i - 1][1] = end

                #remove the interval that had merge conflict and adjust index accordingly
                intervals.pop(i)
                i -= 1
            #no overlap
            else:
                end = interval[1]

            i += 1
        
        return intervals