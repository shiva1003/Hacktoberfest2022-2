def selec_sort(arr):
    for i in range(0, len(arr)-1):
        cur_min_idx=i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[cur_min_idx]:
                cur_min_idx=j
        arr[i],arr[cur_min_idx]=arr[cur_min_idx],arr[i]
arr=[5,4,8,9,7,3]
selec_sort(arr)
print(arr)
        
