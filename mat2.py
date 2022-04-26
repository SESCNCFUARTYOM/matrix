# !/usr/bin/env python3
# /-*- coding: UTF-8 -*-

if __name__ == "__main__":
    a = 3
    b = 3
    A = []
    count = 0
    for _ in range(n):
        c = list(map(int, input().split()))
        assert len(c) == b
        A.append(c)
    B = []
    for _ in range(b):
        B.append([0] * a)
    for i in range(a):
        for j in range(b):
            B[j][i] = A[i][j]
    C = []
    for _ in range(a - 1):
        for c in A:
            for c in B:
                for x in c:
                    for y in c:
                        if c[x] == c[y]:
                            print([x for x in c])
