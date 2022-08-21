


def qucik(arr):
    left = 0
    right = len(arr) - 1

    mid = right//2

    res = sort(arr, left, right, mid)

    return res

def sort(arr, left, right, mid):
    if left > right:
        return arr

    low = left
    high = right

    key = arr[left]

    while left < right:
        while left < right and arr[right] > key:
            right = right - 1
        arr[left] = arr[right]

        while left < right and arr[left] < key:
            left = left + 1
        arr[right] = arr[left]

    arr[right] = key

    if right >= mid:
        return key

    sort(arr, low, left-1, mid)
    sort(arr, left+1, high, mid)

    return None

arr = [2,2,2,2,1]
res = qucik(arr)
print(res)
