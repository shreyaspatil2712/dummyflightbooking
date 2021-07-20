def showstatus(board):
    #
    # the function accepts one parameter containing the board's current status
    # and prints it out to the console
    #
    print(
        f"""
+_column0_+_column1_+_column2_+
|         |         |         |
|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
|         |         |         |
+_________+_________+_________+
|         |         |         |
|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
|         |         |         |
+_________+_________+_________+
|         |         |         |
|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
|         |         |         |
+_________+_________+_________+
|         |         |         |
|   {board[3][0]}   |   {board[3][1]}   |   {board[3][2]}   |
|         |         |         |
+_________+_________+_________+
        """)

        
