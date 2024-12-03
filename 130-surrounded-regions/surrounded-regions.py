from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        q = deque()
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        # First row and last row
        for col in range(0,len(board[0])):
            if board[0][col]=='O':
                visited[0][col]=True
                q.append((0,col))
            if board[len(board)-1][col]=='O':
                visited[len(board)-1][col]=True
                q.append((len(board)-1,col))
        # First col and last col
        for row in range(0,len(board)):
            if board[row][0]=='O':
                visited[row][0]=True
                q.append((row,0))

            if board[row][len(board[0])-1]=='O':
                visited[row][len(board[0])-1]=True
                q.append((row,len(board[0])-1))
        movements = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while q:
            row,col = q.popleft()

            for move in movements:
                nrow = row + move[0]
                ncol = col + move[1]
                if (0<=nrow<len(board)) and (0<=ncol<len(board[0])) and (board[nrow][ncol]=='O') and (not visited[nrow][ncol]):
                    q.append((nrow,ncol))
                    visited[nrow][ncol]=True

        for row in range(0,len(board)):
            for col in range(0,len(board[0])):
                if (board[row][col]=='O') and (not visited[row][col]):
                    board[row][col]='X'




