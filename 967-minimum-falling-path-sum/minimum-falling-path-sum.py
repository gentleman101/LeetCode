class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # Initialize `prev` with the first row of the matrix
        prev = matrix[0]
        
        # Iterate over rows starting from the second row
        for i in range(1, len(matrix)):
            temp = [0] * len(matrix[0])
            for j in range(len(matrix[0])):
                # Calculate the minimum path to the current cell
                up = matrix[i][j] + prev[j]
                
                diagonal_LeftUp = matrix[i][j]
                if j - 1 >= 0:
                    diagonal_LeftUp += prev[j - 1]
                else:
                    diagonal_LeftUp = float('inf')
                
                diagonal_RightUp = matrix[i][j]
                if j + 1 < len(matrix[0]):
                    diagonal_RightUp += prev[j + 1]
                else:
                    diagonal_RightUp = float('inf')
                
                # Store the minimum path sum for the current cell
                temp[j] = min(up, diagonal_LeftUp, diagonal_RightUp)
            
            # Update `prev` after processing the entire row
            prev = temp
        
        # The minimum value in `prev` contains the answer
        return min(prev)
