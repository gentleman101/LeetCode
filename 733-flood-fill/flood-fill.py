class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
            n = len(image)
            m = len(image[0])
            movements = [(1,0),(0,1),(-1,0),(0,-1)]


                        
            def dfs(r,c,og_color):
                image[r][c]=color
                for move in movements:
                    nrow = r + move[0]
                    ncol = c + move[1]
                    if 0<=nrow<n and 0<=ncol<m and image[nrow][ncol]==og_color and image[nrow][ncol]!=color:
                        dfs(nrow,ncol,og_color)
            dfs(sr,sc,image[sr][sc])

            return image
