if __name__ == "__main__":
    board = [["_"] * 3 for i in range(3)]
    print(board)

    board[1][2] = "X"
    print(board)

    # Wrong version
    weired_board = [["_"] * 3] * 3
    weired_board[1][2] = "O"
    print(weired_board)
