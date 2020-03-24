def binarysearch(l, target):
    low = 0
    high = len(l)-1
    while low <= high:
        mid = int((low + high)/2)
        if target == l[mid]:
            return 1
        elif target < l[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1
