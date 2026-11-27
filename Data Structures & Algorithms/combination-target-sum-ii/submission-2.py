class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def sumCom(temp,i,scom):
            if scom == target:
                ans.append(temp.copy())
                return
            if i >= len(candidates) or target < scom:
                return
            temp.append(candidates[i])
            sumCom(temp,i+1,scom+candidates[i]);
            while len(candidates)>i+1 and candidates[i]==candidates[i+1]:
                i+=1
            temp.pop()
            sumCom(temp,i+1,scom)
        sumCom([],0,0)
        return ans
        