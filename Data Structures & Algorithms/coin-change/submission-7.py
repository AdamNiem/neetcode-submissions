from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        queue = deque([0])
        seen = set()
        level = 0
        while queue:
            print(queue)
            l = len(queue)
            level += 1
            for i in range(l):
                curr = queue.popleft()
                for coin in coins:
                    if curr + coin < amount and curr + coin not in seen:
                        queue.append(curr + coin)
                        seen.add(curr + coin)
                    if curr + coin == amount:
                        return level
            
        return -1