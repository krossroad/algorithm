class Heap(object):
    def __init__(self, heap_size):
        self.heap_size = heap_size
        self.heap = [0] * heap_size

    def max_heapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2

        largest = left if left < self.heap_size and self.heap[left] > self.heap[i] else i
        largest = right if right < self.heap_size and self.heap[right] > self.heap[largest] else largest

        if i != largest:
            temp = self.heap[i]
            self.heap[i] = self.heap[largest]
            self.heap[largest] = temp

            self.max_heapify(largest)

    def build_heap(self, A):
        self.heap = A
        to = int(len(A) / 2)
        for i in range(to, -1, -1):
            self.max_heapify(i)

    def __str__(self):
        return self.heap.__str__()


def heap_sort(A):
    size = len(A)
    hp = Heap(size)
    hp.build_heap(A)

    for i in range(size - 1, 0, -1):
        temp = hp.heap[0]
        hp.heap[0] = hp.heap[i]
        hp.heap[i] = temp

        hp.heap_size -= 1
        hp.max_heapify(0)

    print hp
