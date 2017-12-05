from random import shuffle

from QuickSort.QSort import quick_sort

A = range(21, 10, -1)
print len(A)
# shuffle(A)
print "Before sorting !!"
print A
quick_sort(A, 0, 10)
print "After sorting !!"
print A

