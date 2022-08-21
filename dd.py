
def topK(list, K):
    if list is None or len(list) < K:
        return None

    left = 0
    right = len(list) - 1

    res = sort(list,left, right, K)

    return res


def sort(list, left, right, K):
    if left > right:
        return list

    low = left
    high = right

    key = list[left]

    while left < right:
        while left < right and list[right] > key:
            right = right - 1
        list[left] = list[right]

        while left < right and list[left] < key:
            left = left + 1
        list[right] = list[left]

        list[right] = key

        if right == K:
            return list[right]
        elif right > K:
            sort(list,low, left-1)
        else:
            sort(list, left+1, high)

    return list[right]






