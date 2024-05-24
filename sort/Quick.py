import sys

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def Quick(self , list):
        # write code here
        left = 0
        right = len(list)-1
        res = self.sort(list, left, right)

        return res

    def sort(self, list, left, right):
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
        self.sort(list,low,left-1)
        self.sort(list,left+1, high)

        return list


    def partition(self, list, low, high):
        i = low - 1
        flag = list[high]

        for j in range(low, high):
            if list[j] < flag:
                i += 1
                list[i], list[j] = list[j], list[i]

        list[i+1], list[high] = list[high], list[i+1]

        return i+1

    def QuickSort(self, list, low, high):
        if low < high:
            flag = self.partition(list, low, high)

            self.QuickSort(list, low, flag-1)
            self.QuickSort(list, flag+1, high)


#list_int = [9,6,8,5,7,4,2,0,1,3]
list_int = [8,5,7,4,2,0,1,3]
# list = sys.argv[1]
#list_int = [int(i) for i in list.split(",")]
#r = Solution().Quick(list_int)
#r = Solution().QuickSort(list_int, 0, len(list_int)-1)
#print (list_int)



def partition(list, low, high):
    i = low - 1
    flag = list[high]

    for j in range(low, high):
        if list[j] < flag:
            i += 1
            list[i], list[j] = list[j], list[i]

    list[i+1],list[high] = list[high],list[i+1]

    return i+1

def QuickSort(list,low,high):
    if low < high:
        flag = partition(list, low, high)

        QuickSort(list, low, flag-1)
        QuickSort(list, flag+1, high)



# list = [8,5,7,4,2,0,1,3]
#
# QuickSort(list,0,len(list)-1)
# print(list)


def linked_quick_sort(start, end):
    if start.next != end:
        pre, last = linked_partition(start, end)

        linked_quick_sort(start, pre)
        linked_quick_sort(last, end)


def linked_partition(start, end):
    node = start.next.next
    pre = start.next
    pre.next = end
    last = pre

    while node != end:
        temp = node.next
        if node.val > pre.val:
            node.next = last.next
            last.next = node
        elif node.val < pre.val:
            node.next = start.next
            start.next = node
        else:
            node.next = last.next
            last.next = node
            last = last.next

        node = temp

    return [pre, last]

# l1 = ListNode(1)
# l1.next = ListNode(3)
# l1.next.next = ListNode(2)
#
# newHead = ListNode(0)
# newHead.next = l1
# linked_quick_sort(newHead, None)
#
# print (newHead.next.val, newHead.next.next.val, newHead.next.next.next.val)





def a(list, low, high):
    if low < high:
        flag = p(list, low, high)

        a(list, low, flag-1)
        a(list, flag+1, high)

def p(list, low, high):
    if low > high:
        return list

    i = low - 1
    flag = list[high]

    for j in range(low, high):
        if list[j] < flag:
            i += 1
            list[i], list[j] = list[j], list[i]

    list[high], list[i+1] = list[i+1], list[high]

    return i+1

# list = [8,5,7,4,2,0,1,3]
#
# a(list,0,len(list)-1)
# print(list)


def topk(arr, low, high, k):
    if (k > 0 and k <= high - low + 1):
        i = partition_k(arr, low, high)

        if i-low+1 == k:
            return
        elif i-low+1 > k:
            topk(arr, low, i - 1, k)
        else:
            topk(arr, i + 1, high, k-1-i+low)

def partition_k(arr, low, high):
    i = low - 1
    flag = arr[high]

    for j in range(low, high):
        if arr[j] >= flag:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i+1

arr = [2,3,5,7,8,9,10,11,12]
k = 5
topk(arr, 0, len(arr)-1, k)
print(arr)
print(arr[k-1])





def partition_a(arr, low, high):
    i = low - 1
    flag = arr[high]

    for j in range(low, high):
        if arr[j] >= flag:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[high], arr[i+1] = arr[i+1], arr[high]

    return i+1

def top_k(arr, low, high, k):
    if k > 0 and k <= high - low + 1:
        i = partition_a(arr, low, high)

        if i-low+1 == k:
            return
        elif i-low+1 > k:
            top_k(arr, low, i-1, k)
        else:
            top_k(arr, i+1, high, k-i-1+low)

# arr = [2,3,5,7,8,9,10,11,12]
# k = 7
# top_k(arr, 0, len(arr)-1, k)
# print(arr)
# print(arr[k-1])






def top_k_again(arr,low,high,k):
    if k > 0 and k <= high - low + 1:
        i = top_k_partition(arr, low, high)

        if i-low+1 == k:
            return
        elif i-low+1 > k:
            top_k_again(arr,low,i-1,k)
        else:
            top_k_again(arr,i+1,high,k-i-1+low)

def top_k_partition(arr, low, high):
    i = low-1
    flag = arr[high]

    for j in range(low,high):
        if arr[j] >= flag:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]

    arr[high],arr[i+1] = arr[i+1],arr[high]

    return i+1

# arr = [2,3,5,7,8,9,10,11,12]
# k = 6
# top_k_again(arr, 0, len(arr)-1, k)
# print(arr)
# print(arr[k-1])








def top_k_sort(arr,low,high,k):
    if k > 0 and k <= high - low + 1:
        i = top_k_partition_again(arr, low, high)

        if i-low+1==k:
            return
        elif i-low+1>k:
            top_k_sort(arr,low,i-1,k)
        else:
            top_k_sort(arr,i+1,high,k-i-1+low)

def top_k_partition_again(arr, low, high):
    i = low-1
    flag = arr[high]

    for j in range(low,high):
        if arr[j] >= flag:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]

    arr[high],arr[i+1]=arr[i+1],arr[high]

    return i+1

# arr = [2,3,5,7,8,9,10,11,12]
# k = 6
# top_k_sort(arr, 0, len(arr)-1, k)
# print(arr)
# print(arr[k-1])






def more_than_half_num(arr):
    if not arr:
        return None

    dict = {}

    for i,  num in enumerate(arr):
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1

    return max(dict,key=lambda x:dict[x])


# arr=[3,3,3,3,2,2,2]
# res = more_than_half_num(arr)
# print(res)



class Solution_v1:
    def findKth(self , a , n , K ):
        # write code here
        if not a:
            return 0

        def sort(a, low, high, K):
            if K>0 and K<=high-low+1:
                i = partition_n(a, low, high)

                if i-low+1==K:
                    return
                elif i-low+1>K:
                    sort(a,low,i-1,K)
                else:
                    sort(a,i+1,high,K-i-1+low)

        def partition_n(a,low,high):
            i = low - 1
            flag = a[high]

            for j in range(low,high):
                if a[j] >= flag:
                    i+=1
                    a[i],a[j] = a[j],a[i]

            a[high],a[i+1] = a[i+1],a[high]

            return i+1

        sort(a,0,n,K)
        print(a)

        return a[K-1]


# arr = [1,3,5,2,2]
# n = 5
# K = 2
# r = Solution_v1()
# res = r.findKth(arr,n-1,K)
# print(res)



# arr = [[1,2],[1,4],[2,3]]
# # arr = [1,0,2]
# print(sorted(arr, key=lambda x : x[-1]))


def quick(arr, low, high):
    if not arr:
        return

    if low < high:
        i = partition_again(arr, low, high)

        quick(arr, low, i-1)
        quick(arr, i+1, high)

def partition_again(arr, low, high):
    if low > high:
        return arr

    i = low-1
    flag = arr[high]

    for j in range(low, high):
        if arr[j] < flag:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[high], arr[i+1] = arr[i+1], arr[high]

    return i+1


#
# list = [8,5,7,4,2,0,1,3]
#
# quick(list,0,len(list)-1)
# print(list)



def top_k_c(arr,low,high,k):
    if k>0 and high-low>=k-1:
        i = top_k_c_partition(arr, low, high)

        if i-low+1==k:
            return arr
        elif i-low+1>k:
            top_k_c(arr, low, i-1, k)
        elif i-low+1<k:
            top_k_c(arr, i+1, high, k-i+low-1)

def top_k_c_partition(arr, low, high):
    if low > high:
        return arr

    i = low-1
    flag = arr[high]

    for j in range(low, high):
        if arr[j] > flag:
            i += 1
            arr[j],arr[i]=arr[i],arr[j]

    arr[high],arr[i+1]=arr[i+1],arr[high]

    return i+1


# arr = [2,3,5,7,8,9,10,11,12]
# k = 3
# top_k_c(arr, 0, len(arr)-1, k)
# print(arr)
# print(arr[k-1])




def coin(amount,coins):
    res = []
    track = []

    def dfs(amount,coins,track):
        if sum(track) == amount:
            if track not in res:
                res.append(track[:])
            return

        if sum(track) > amount:
            return

        for i in range(len(coins)):
            track.append(coins[i])
            dfs(amount,coins,track)
            track.pop()

    dfs(amount,coins,track)

    res_f = []
    for j in res:
        j.sort()
        if j not in res_f:
         res_f.append(j)

    return len(res_f)

# amount = 3
# coins = [2]
#
# print(coin(amount,coins))
