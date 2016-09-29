__author__ = 'student'
A = list(map(int, input().split()))
n=0
s=0
for i in range ( len(A)):
    n=A.count(A[i])
    if n>s:
        s=n
print(A[i])