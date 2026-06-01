from collections import Counter

from heapq import (
    heappush,
    heappop,
)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        counts = Counter(nums)
        heap = []

        #populate heap
        for num in nums:
            if len(heap) < k:
                heappush(heap, num)
            else:
                heappush(heap, num)
                heappop(heap)

        #now we have heap of size k for largest items in the list
        #get k elements from heap so get last element in the heap
        return heap[0]
