class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        start = 0
        end = n-1
        while start + 1 < n and height[start] < height[start + 1]:
            start += 1
        while end - 1 > 0 and height[end] < height[end - 1]:
            end -= 1
        ans = 0
        diff = 0
        first = True
        preMin = 0
        while start < n and end > 0 and start < end:
            # print(start, end, ans, "in" , diff)
            cal = min(height[start],height[end])
            i = start;
            for i in range(start+1, end):
                if height[i] < cal and not first:
                    if preMin < height[i]:
                        ans += cal - height[i];
                    else:
                        ans += diff
                    # print(ans , "diff")
                elif height[i] < cal:
                    ans += cal - height[i];
                    # print(ans, "not diff")
            if height[start] < height[end]:
                temp = start
                while start < end and height[temp] >= height[start]:
                    start += 1
            else:
                temp = end
                while start < end and height[temp] >= height[end]:
                    end -= 1;
            diff = min(height[start],height[end]) - cal
            # print(start, end, ans, "out", diff)
            preMin = cal
            first = False
        return ans

        