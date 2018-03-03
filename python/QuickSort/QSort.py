def quick_sort(A, p, r):
    if r > p:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


def partition(A, p, r):
    pivot = A[r]
    i = p - 1

    def swap(A, i, j):
        temp = A[i]
        A[i] = A[j]
        A[j] = temp

    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            swap(A, i, j)

    swap(A, i + 1, r)

    return i + 1
