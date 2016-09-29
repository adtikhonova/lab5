__author__ = 'student'
A = list(map(int, input().split()))
B = A.insert(0,A.pop())
print(' '.join(map(str, A)))