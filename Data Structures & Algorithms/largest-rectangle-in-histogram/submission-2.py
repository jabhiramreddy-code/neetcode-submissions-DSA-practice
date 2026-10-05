class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # pair [index, height]
        maxHeight = 0
        for i , h in enumerate(heights):
            start = i
            while stack and stack[-1][1] >= heights[i]:
                index , height = stack.pop()
                maxHeight = max(maxHeight, (height * (i-index)));
                start = index
            stack.append([start,heights[i]])
        while stack:
            index, height = stack.pop()
            maxHeight = max(maxHeight, height * (len(heights)-index))
        return maxHeight
        