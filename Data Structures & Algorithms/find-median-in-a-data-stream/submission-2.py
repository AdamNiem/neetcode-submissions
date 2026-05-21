from heapq import (
    heappush,
    heappop,
)

class MedianFinder:

    def __init__(self):
        #low is the lower half of sorted nums which is a max heap
        #high is the upper half of sorted nums which is a min heap
        self.low, self.high = [], []

    def addNum(self, num: int) -> None:
        #default case just add to low heap, heappush will heapify automatically too
        heappush(self.low, -1 * num) #-1 to make min-heap act as max-heap since heappush is for min-heap

        #case: low heap cannot be longer than high heap by more than 1
        if len(self.low) - len(self.high) > 1:
            #move max of low heap to high heap
            val = heappop(self.low)
            heappush(self.high, val * -1)

        #case: same but for high heap not sure if this will ever get triggered
        elif len(self.high) - len(self.low) > 1:
            #move min of high heap to low heap
            val = heappop(self.high)
            heappush(self.low, val * -1)
            
        #case: if max of lower half is greater than min of upper half then swap them
        if self.low and self.high and (self.low[0] * -1) > self.high[0]:
            val_low = heappop(self.low)
            val_high = heappop(self.high)
            heappush(self.high, val_low * -1)
            heappush(self.low, val_high * -1)

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return (self.low[0] * -1)
        elif len(self.high) > len(self.low):
            return self.high[0]
        else:
            return ((self.low[0] * -1) + self.high[0]) / 2
        