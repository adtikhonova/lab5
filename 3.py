__author__ = 'student'
A = list(map(int, input().split()))
i=0
for i in range(len(A) // 2):
    print(A[i],A[-i-1], end=' ')


if len(A) // 2 !=0:
    print(A[len(A) // 2])