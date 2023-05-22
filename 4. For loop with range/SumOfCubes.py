# For the given integer N calculate the following sum:
#     1^3+2^3+…+N^3

n = int(input())
res=0

for i in range(1,n+1):
    a = i**3
    res=res+a
    
print(res)