# Given an integer n,
# print the sum 1!+2!+3!+...+n!
# 
# This problem has a solution with only one loop, so try to discover it. And don't use the math library :)

n = int(input())
num=1
res=0

for i in range(1,n+1):
    num*=i
    res+=num
    
print(res)