A = [0, -1, -2, 2, 3, 6, 7, 8, 9, -6, 4, 1]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

selection_sort(A)
print(A)