def solution(board):
    answer = 0
    height = len(board)
    width = len(board[0])
    
    for i in range(1, height):
        for j in range(1, width):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
    
    result = []
    for value in board:
        result.append(max(value))

    return max(result) ** 2