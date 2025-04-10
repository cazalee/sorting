

def bubble_sort(arr_1): 
    n=len(arr_1)
    for i in range(n): 
        swapped=False
        for j in range(0,n-i-1): 
            if arr_1[j]>arr_1[j+1]: 
                arr_1[j],arr_1[j+1]=arr_1[j+1],arr_1[j]
                swapped=True 

        if not swapped: 
            break 
arr_1=[10,2,303,40]
bubble_sort(arr_1)
print(arr_1)

