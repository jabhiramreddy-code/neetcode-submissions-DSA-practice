class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []
        for i in points:
            x = math.dist([0,0],i);
            heapq.heappush(q,(x,i))
        result = []
        for i in range(k):
            x,y = heapq.heappop(q)
            result.append(y)
        return result

        