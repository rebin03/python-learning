# Chess queen moves horizontally, vertically or diagonally to any number of cells. Given two different cells of the chessboard, determine whether a queen can go from the first cell to the second in one move.
# The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a queen can go from the first cell to the second in one move, or NO otherwise.

c1 = int(input())
r1 = int(input())

c2 = int(input())
r2 = int(input())

if c1 == c2 or r1 == r2 or abs(c1 - c2) == abs(r1 - r2):
    print("YES")
else:
    print("NO")