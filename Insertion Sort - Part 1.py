def insertionSort1(n, arr):
    # Write your code here
    c = arr[-1]
    j = 0
    for i in range(n - 2, -1, -1):
        if arr[i] > c:
            arr[i + 1] = arr[i]
            j += 1
        else:
            arr[i + 1] = c
            break
        print(*arr)
    if j == n - 1:
            arr[0] = c
    print(*arr)
