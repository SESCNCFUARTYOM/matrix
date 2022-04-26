# !/usr/bin/env python3
# /-*- coding: UTF-8 -*-

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    A = []
    for _ in range(a):
        c = list(map(int, input().split()))
        assert len(c) == b
        A.append(c)

    for i in range(a - 1):
        for j in range(b - 1):
            countrow = len([A[i][j] for A[i][j] in i if A[i][j] == 0])
            if countrow == a:
                del A[i]
    for j in range(b - 1):
        for j in range(a - 1):
            countrow = len([A[i][j] for A[i][j] in j if A[i][j] == 0])
            if countrow == a:
                del A[j]
    print(A)