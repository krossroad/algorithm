import sys


def merge_sort(A, p, r):
    if r > p:
        q = int((p + r) / 2)
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)


def merge(A, p, q, r):
    L = A[p: q + 1]
    R = A[q + 1: r + 1]
    L.append(sys.maxint)
    R.append(sys.maxint)

    j = k = 0

    for i in range(p, r + 1):
        if L[j] <= R[k]:
            A[i] = L[j]
            j += 1

        else:
            A[i] = R[k]
            k += 1
