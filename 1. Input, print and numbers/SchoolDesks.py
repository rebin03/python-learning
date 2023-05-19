# A school decided to replace the desks in three classrooms. Each desk sits two students. Given the number of students in each class, print the smallest possible number of desks that can be purchased.
# The program should read three integers: the number of students in each of the three classes, a, b and c respectively.

# In the first test there are three groups. The first group has 20 students and thus needs 10 desks. The second group has 21 students, so they can get by with no fewer than 11 desks. 11 desks is also enough for the third group of 22 students. So we need 32 desks in total.

 a = int(input())
 b = int(input())
 c = int(input())
 
 j=a//2
 k=b//2
 l=c//2
 
 p=a%2
 q=b%2
 r=c%2
 
 total = j+k+l+p+q+r
 
 print(total)
 