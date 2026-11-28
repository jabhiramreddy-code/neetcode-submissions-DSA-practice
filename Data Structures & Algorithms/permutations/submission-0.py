class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        per = [[]]
        for n in nums:
            temp = []
            for p in per:
                for i in range(len(p)+1):
                    p_copy = p.copy()
                    p_copy.insert(i,n)
                    temp.append(p_copy)
            per = temp
        return per
        