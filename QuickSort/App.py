from random import shuffle

from QuickSort.QSort import quick_sort

A = range(10, 21)
print len(A)
# shuffle(A)
print "Before sorting !!"
print A
quick_sort(A, 0, 10)
print "After sorting !!"
print A

