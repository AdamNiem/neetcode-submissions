"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        starts = sorted([x.start for x in intervals])
        ends = sorted([x.end for x in intervals])

        start, end = 0,0
        rooms = 0
        res = 0

        while start < len(intervals):
            rooms += 1
            while ends[end] <= starts[start]:
                # meeting ended so decrement
                rooms -= 1
                end += 1

            res = max(rooms, res)
            start += 1

        return res
