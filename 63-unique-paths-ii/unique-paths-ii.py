class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        columns = len(obstacleGrid[0])
        
        # Initialize the previous row
        prev = [0] * columns
        
        for i in range(rows):
            # Temporary array for the current row
            temp = [0] * columns
            for j in range(columns):
                # If there's an obstacle, no paths are possible
                if obstacleGrid[i][j] == 1:
                    temp[j] = 0
                    continue
                
                # Base case: Starting cell
                if i == 0 and j == 0:
                    temp[j] = 1
                    continue
                
                # Check the top and left cells
                top = prev[j] if i > 0 else 0
                left = temp[j - 1] if j > 0 else 0
                
                # Number of ways to reach the current cell
                temp[j] = top + left
            
            # Update the previous row to the current row
            prev = temp
        
        # Return the result at the bottom-right corner
        return prev[columns - 1]
