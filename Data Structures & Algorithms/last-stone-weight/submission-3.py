class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        if n == 1:
            return stones[0]
        stones.sort()
        ans = stones[-1]
        while len(stones) > 1:
            temp = stones.pop()
            stones[-1] = abs(temp - stones[-1])
            stones.sort()
            # print(stones)
        return stones[-1]
        