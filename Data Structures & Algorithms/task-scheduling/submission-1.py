class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        l= dict(Counter(tasks))
        q=[]

        for key,value in l.items():
            heapq.heappush(q,(-value,key))
        ans = 0
        while len(q) > 0 :
            temp = []
            nTrack = 0    
            while nTrack <= n:
                if len(q) == 0:
                    break;
                key,val = heapq.heappop(q)
                key += 1
                if key < 0:
                    temp.append((key,val))
                ans += 1
                nTrack += 1
            if nTrack <= n and (temp or q):
                ans += n - nTrack +1
            for i in temp:
                heapq.heappush(q,(i[0],i[1]))
            
        return ans
        