# Given two cells of a chessboard. If they are painted in one color, print the word YES, and if in a different color - NO.
# The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell.

c1 = int(input())
r1 = int(input())

c2 = int(input())
r2 = int(input())

n1 = (c1+r1)%2
n2 = (c2+r2)%2

if n1 == n2:
    print('YES')
else:
    print('NO')