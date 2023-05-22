# Given N numbers: the first number in the input is N, after that N integers are given. Count the number of zeros among the given integers and print it.
# You need to count the number of numbers that are equal to zero, not the number of zero digits.

n = int(input())
count=0

for i in range(1,n+1):
    num = int(input())
    if num==0:
        count+=1
        
print(count)