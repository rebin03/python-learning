# 10 numbers are given in the input. Read them and print their sum. Use as few variables as you can.

result=0

for i in range(1,11):
    a = int(input())
    result = result+a
    
print(result)