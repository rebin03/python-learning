# Chess king moves horizontally, vertically or diagonally to any adjacent cell. Given two different cells of the chessboard, determine whether a king can go from the first cell to the second in one move.
# The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a king can go from the first cell to the second in one move, or NO otherwise.

c1 = int(input())
r1 = int(input())

c2 = int(input())
r2 = int(input())

if (c2==c1 or c2==c1+1 or c2==c1-1) and (r2 ==r1 or r2==r1+1 or r2==r1-1):
    print("YES")
else:
    print('NO')