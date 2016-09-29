__author__ = 'student'
x=int(input())
A = list(map(int, input().split()))
m=min(A)
k=0
while k<x//2:
    m+=1
    if m in A:
        k+=1
print(m)