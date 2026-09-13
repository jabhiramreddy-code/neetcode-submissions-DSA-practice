class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for i in nums:
            dic[i] +=1
        heap = []
        for i in dic.keys():
            heapq.heappush(heap, (dic[i], i))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        print(heap)
        for i in range(k):
            res.append(heap[i][1])
        return res