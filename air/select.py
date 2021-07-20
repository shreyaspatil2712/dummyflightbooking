def select(board): # selecting the seat 
    print("select desired column and a seat in that column")
    x = int(input("Enter column number:" ))
    y = int(input("Enter desried seat in the column:" ))
    board[y][x] = "booked"
