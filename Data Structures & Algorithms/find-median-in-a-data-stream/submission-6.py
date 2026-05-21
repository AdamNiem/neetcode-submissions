from heapq import (
    heappush_max,
    heappushpop,
    heappush,
    heappushpop_max,
)

class MedianFinder:
    def __init__(self):
        self.upper_min_heap = []
        self.lower_max_heap = []
        self.median = None

    def addNum(self, num: int) -> None:
        if len(self.upper_min_heap) == len(self.lower_max_heap):
            heappush_max(
                self.lower_max_heap, heappushpop( self.upper_min_heap, num )
            )
            self.median = self.lower_max_heap[0]
        else:
            heappush(
                self.upper_min_heap, heappushpop_max( self.lower_max_heap, num )
            )
            self.median = (self.upper_min_heap[0] + self.lower_max_heap[0]) / 2

    def findMedian(self) -> float:
        return self.median
