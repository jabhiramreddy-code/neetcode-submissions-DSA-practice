class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        start = 0
        end = n-1
        # while start + 1 < n and heights[start] < heights[start + 1]:
        #     start += 1
        # while end - 1 > 0 and heights[end] < heights[end - 1]:
        #     end -= 1
        ans = 0
        print(start, end , ans)
        while start < n and end > 0 and start < end:
            ans = max(ans, min(heights[start],heights[end]) * (end - start))
            if heights[end] > heights[start]:
                temp = start
                temp1 = start + 1
                while temp1 < n and heights[temp1] < heights[temp]:
                    temp1 += 1
                start = temp1
            else:
                temp = end
                temp1 = end-1
                while temp1 > 0 and heights[temp1] < heights[temp]:
                    temp1 -= 1
                end = temp1
        return ans;