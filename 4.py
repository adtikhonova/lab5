__author__ = 'student'
A = list(map(int, input().split()))
x=int(input())
for i in range(x):
    A.insert(-1-A[-1],A.pop())
print(' '.join(map(str, A[::1])))
