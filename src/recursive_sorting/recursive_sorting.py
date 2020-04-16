# TO-DO: complete the help function below to merge 2 sorted arrays
def merge(arrA, arrB, merged):
    arrA_cursor, arrB_cursor = 0, 0
    while arrA_cursor < len(arrA) and arrB_cursor < len(arrB):
        if arrA[arrA_cursor] <= arrB[arrB_cursor]:
            merged[arrA_cursor + arrB_cursor] = arrA[arrA_cursor]
            arrA_cursor += 1
        else:
            merged[arrA_cursor + arrB_cursor] = arrB[arrB_cursor]
            arrB_cursor += 1
    for arrA_cursor in range(arrA_cursor, len(arrA)):
        merged[arrA_cursor + arrB_cursor] = arrA[arrA_cursor]
    for arrB_cursor in range(arrB_cursor, len(arrB)):
        merged[arrA_cursor + arrB_cursor] = arrB[arrB_cursor]

    return merged


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    arrA, arrB = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    return merge(arrA, arrB, arr.copy())


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
