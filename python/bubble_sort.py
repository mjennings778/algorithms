A = [0, -1, -2, 2, 3, 6, 7, 8, 9, -6, 4, 1]

def bubble_sort(arr):
    n = len(arr)
    flag = True
    while flag:
        flag = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                flag = True
                arr[i-1], arr[i] = arr[i], arr[i-1]
bubble_sort(A)
print(A)
