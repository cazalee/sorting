
def pivot_sort(arr,start,end): 

    i=start-1 
    j=start
    pivot=arr[end]

    while j<end: 

        if arr[j]<pivot: 
            i+=1 
            arr[i],arr[j]=arr[j],arr[i]
        j+=1 

    i+=1 
    arr[i],arr[end]=arr[end],arr[i]
    return i 
    
def quick_sort(arr,start,end): 

    if start>end: 
        return 
      
    else: 

        pivot_index=pivot_sort(arr,start,end)
        quick_sort=(arr,start,pivot_index-1)
        quick_sort=(arr,pivot_index+1,end)


x=[9,8,7,1,2,3,4]
quick_sort(x,0,len(x)-1)
print(x)
