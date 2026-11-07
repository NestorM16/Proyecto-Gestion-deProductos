# ordenamiento.py

def insertion_sort(arr, key=lambda x: x, reverse=False):
    a = arr.copy()
    for i in range(1, len(a)):
        key_item = a[i]
        j = i - 1
        while j >= 0 and ((key(a[j]) > key(key_item)) if not reverse else (key(a[j]) < key(key_item))):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key_item
    return a

def merge_sort(arr, key=lambda x: x, reverse=False):
    if len(arr) <= 1:
        return arr.copy()
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key, reverse)
    right = merge_sort(arr[mid:], key, reverse)
    
    return merge(left, right, key, reverse)

def merge(left, right, key, reverse):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        cond = (key(left[i]) <= key(right[j])) if not reverse else (key(left[i]) >= key(right[j]))
        if cond:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr, key=lambda x: x, reverse=False):
    if len(arr) <= 1:
        return arr.copy()
    
    pivot = arr[len(arr) // 2]
    pivot_val = key(pivot)
    
    left = [x for x in arr if ((key(x) < pivot_val) if not reverse else (key(x) > pivot_val))]
    middle = [x for x in arr if key(x) == pivot_val]
    right = [x for x in arr if ((key(x) > pivot_val) if not reverse else (key(x) < pivot_val))]
    
    return quick_sort(left, key, reverse) + middle + quick_sort(right, key, reverse)