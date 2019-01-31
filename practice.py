def fib(n):
    A, B = 0, 1
    for i in range(0, n):
        A, B = B, A + B
    return A

#print(fib(10))
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def binary(target, arr):
    mid = arr[len(arr)//2]
    high = arr[-1]
    for x in arr:
        if mid == target:
            return True
        elif mid < target:
            high = mid
            arr = arr[mid:]
            mid = arr[len(arr)//2]
        elif mid > target:
            arr = arr[:mid]
            mid = arr[len(arr)//2]
        else:
            return False

print(binary(7, arr))
