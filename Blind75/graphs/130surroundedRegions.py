class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return 
        
        xMax, yMax = len(board), len(board[0])          
                
        def dfs(x, y, board, check, change):
            if  0 <= x < xMax and 0 <= y < yMax and board[x][y] == check:
                board[x][y] = change
                dfs(x + 1, y, board, check, change)
                dfs(x - 1, y, board, check, change)                
                dfs(x, y + 1, board, check, change)                
                dfs(x, y - 1, board, check, change)      
                
        for x in range(xMax):
            dfs(x, 0, board, "O", "#")
            dfs(x, yMax - 1, board, "O", "#")
            
        for y in range(yMax):
            dfs(0, y, board, "O", "#")
            dfs(xMax - 1, y, board, "O", "#")
        
        for x in range(xMax):
            for y in range(yMax):
                if board[x][y] == "#":
                    board[x][y] = "O"
                else:
                    board[x][y] = "X"
                    