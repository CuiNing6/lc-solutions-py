




def maxarea(height):
    if len(height) < 2:
        return 0

    res = 0

    i = 0
    j = len(height) - 1

    while i != j:
        h = min(height[i], height[j])

        x = j-i

        if res < h*x:
            res = h*x

        if height[i] < height[j]:
            i+=1
        else:
            j-=1

    return res