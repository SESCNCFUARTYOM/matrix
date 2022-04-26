# !/usr/bin/env python3
# /-*- coding: UTF-8 -*-

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    A = []
    for i in range(a):
        c = list(map(int, input().split()))
        assert len(c) == b
        A.append(c)

    A.sort(key = lambda row: c(j for j in row if (j > 0 and j % 2 == 0)))
    print(A)