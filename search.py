import datetime

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def binarysearch(l, target):
    low = 0
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
    return False

binarysearch(l, 9)
