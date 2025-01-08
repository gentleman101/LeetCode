class Solution:




    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        # PSE (Previous Smaller Element)
        pse = [-1] * len(heights)
        pse_stack = []
        for i in range(len(heights)):
            while pse_stack and heights[i] <= pse_stack[-1][0]:
                pse_stack.pop()
            pse[i] = pse_stack[-1][1] if pse_stack else -1
            pse_stack.append((heights[i], i))

        # NSE (Next Smaller Element)
        nse = [len(heights)] * len(heights)
        nse_stack = []
        for i in range(len(heights) - 1, -1, -1):
            while nse_stack and heights[i] <= nse_stack[-1][0]:
                nse_stack.pop()
            nse[i] = nse_stack[-1][1] if nse_stack else len(heights)
            nse_stack.append((heights[i], i))

        # Calculate max area
        max_area = 0
        for i in range(len(heights)):
            width = nse[i] - pse[i] - 1
            area = width * heights[i]
            max_area = max(max_area, area)

        return max_area

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        stack = [0] * m
        maxArea = 0
        for row in range(n):
            for col in range(m):
                if int(matrix[row][col])>0:
                    stack[col]+=int(matrix[row][col])
                else:
                    stack[col] = 0
            
            maxArea = max(maxArea,self.largestRectangleArea(stack))


        return maxArea



        