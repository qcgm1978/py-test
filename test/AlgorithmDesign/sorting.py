def bubblesort(list):
# Swap the elements to arrange in order
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp
def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
# Find the middle point and devide it
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return merge(left_list, right_list)
# Merge the sorted halves
def merge(left_half,right_half):
    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res
def insertion_sort(InputList):
    ret=InputList.copy()
    for i in range(1, len(ret)):
        j = i-1
        nxt_element = ret[i]
# Compare the current element with next one
        while (ret[j] > nxt_element) and (j >= 0):
            ret[j+1] = ret[j]
            j=j-1
        ret[j + 1] = nxt_element
    return ret
def shellSort(input_list):
    ret=input_list.copy()
    gap = len(ret) // 2
    while gap > 0:
        for i in range(gap, len(ret)):
            temp = ret[i]
            j = i
# Sort the sub list for this gap
            while j >= gap and ret[j - gap] > temp:
                ret[j] = ret[j - gap]
                j = j-gap
            ret[j] = temp
# Reduce the gap for the next element
        gap = gap // 2
    return ret
def selection_sort(input_list):
    ret=input_list.copy()
    for idx in range(len(ret)):
        min_idx = idx
        for j in range( idx +1, len(ret)):
            if ret[min_idx] > ret[j]:
                min_idx = j
# Swap the minimum value with the compared value
        ret[idx], ret[min_idx] = ret[min_idx], ret[idx]
    return ret