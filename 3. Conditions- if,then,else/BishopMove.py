# In chess, the bishop moves diagonally, any number of squares. Given two different squares of the chessboard, determine whether a bishop can go from the first to the second in one move.
# The program receives as input four numbers from 1 to 8, specifying the column and row numbers of the starting square and the column and row numbers of the ending square. The program should output YES if a Bishop can go from the first square to the second in one move, or NO otherwise.

c1 = int(input())
r1 = int(input())

c2 = int(input())
r2 = int(input())

if abs(c1 - c2) == abs(r1 - r2):
    print("YES")
else:
    print("NO")