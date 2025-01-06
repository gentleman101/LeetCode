class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
            
        for row_num in range(numRows):
            row = [1]  # Start the row with a 1
            
            if row_num > 1:
                for i in range(1, row_num):  # Add intermediate numbers
                    row.append(triangle[row_num - 1][i - 1] + triangle[row_num - 1][i])
            
            if row_num > 0:
                row.append(1)  # End the row with a 1
            
            triangle.append(row)
        
        return triangle

