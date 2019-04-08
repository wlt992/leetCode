def quickSort(a, low, high):
    if low >= high:
        return 
    base = a[low]
    index = low
    i = low
    j = high
    while j != i:
        while j > i and a[j] >= base:
            j = j - 1
        while i < j and a[i] <= base:
            i = i + 1
        a[j], a[i] = a[i], a[j]
    a[index], a[i] = a[i], a[index]
    index = i
    quickSort(a, index+1, high)
    quickSort(a, low, index-1)