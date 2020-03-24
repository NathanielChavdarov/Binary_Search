import datetime
from math import sqrt
import sort as s

l = [1, 4, 7, 2, 5, 3, 9, 8, 6]

def search(l, target):
    """
    This function searches for target inside l.
    """
    a = len(l)
    for i in range(a):
        if target == l[i]:
            print("Found at: ", i)
            return i
    return -1


def binarysearch(l, target):
    low = 0
    s.sort(l)
    high = len(l)-1

    while low <= high:
        mid = int((low + high)/2)
        if target == l[mid]:
            print("Found")
            return True
        elif target < l[mid]:
            high = mid - 1
        else:
            low = mid + 1
    print("Not in list")
    return False

binarysearch(l, 12)
