# Given two integers A and B. Print all numbers from A to B inclusively, in ascending order, if A < B, or in descending order, if A ≥ B.

x = int(input())
y = int(input())

if x<y:
    for i in range(x,y+1):
        print(i)
else:
    for i in range(x,y-1,-1):
        print(i)