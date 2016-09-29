__author__ = 'student'
A = list(map(int, input().split()))
for i in range ( len(A)):
    if A.count(A[i])==1:
        print(A[i])


for x in A:
    if A.count(x)==1:
        print(x)