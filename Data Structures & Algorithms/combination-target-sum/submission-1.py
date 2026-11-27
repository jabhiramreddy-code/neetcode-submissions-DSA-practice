class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def subCom(temp,i,sans):
            if i >= len(nums):
                return
            if target < sans:
                return;
            elif target == sans:
                # print(sans,ans)
                ans.append(temp.copy())
                return
            # print(sans)
            temp.append(nums[i])
            subCom(temp,i,sans+temp[len(temp)-1])
            x=temp.pop()
            subCom(temp,i+1,sans)
        subCom([],0,0)
        return ans
        