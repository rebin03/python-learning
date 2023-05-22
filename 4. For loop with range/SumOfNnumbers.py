# N numbers are given in the input. Read them and print their sum.
# The first line of input contains the integer N, which is the number of integers to follow. Each of the next N lines contains one integer. Print the sum of these N integers.

n = int(input())
res=0

for i in range(1,n+1):
    num=int(input())
    res=res+num
    
print(res)