from MergeSort.MSort import merge_sort
from random import shuffle

unsorted = range(20, 40)
shuffle(unsorted)

print "Before sorting!!"
print unsorted

sorted = merge_sort(unsorted, 0, len(unsorted) - 1)

print "After sorting!!"

print unsorted
