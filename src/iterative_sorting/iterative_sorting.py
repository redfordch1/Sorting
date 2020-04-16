# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    n = len(arr)
    # loop through all the elements in between 0 and the length of the array minus 1 setting all those elements to i
    for i in range(0, n - 1):
        # setting the current index to i which is all the elements in between 0 and the length of the array minus 1
        cur_index = i
        # looping between the range i plus 1 and the original length of the array n and assigning all those elements to j
        for j in range(i+1, n):
            # if the range between 0 and n minus 1 is greater than the range between i + 1 and n set the current index to j
            if arr[cur_index] > arr[j]:
                # setting the current index to j if  the above statement is true
                cur_index = j
                # swapping the arrays
        arr[i], arr[cur_index] = arr[cur_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # n = the length of the array
    n = len(arr)
    # loop through n assigning each item to i
    for i in range(n):
        # loop through the range between 0 and the length of the n array minus the all the i items minus 1
        for j in range(0, n-i-1):
            # if array index j is greater than array index j plus 1
            if arr[j] > arr[j+1]:
                # swapping the array index j and array index j plus 1 is assigned to array index j plus 1 and array index j
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


# # STRETCH: implement the Count Sort function below
# def count_sort(arr, maximum=-1):

#     return arr
