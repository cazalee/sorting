

# def merge_sort(arr): 
   
#    if len(arr) > 1: 
      
#       left_arr=arr[:len(arr)//2]
#       right_arr=arr[len(arr)//2:]

# # recurssion: using merge_sort
#       merge_sort(left_arr)
#       merge_sort(right_arr)

# #mergestep 
#       i = 0 
#       j = 0 
#       k = 0 
#       while i<len(left_arr) and j<len(right_arr):
          
#          if left_arr[i]<right_arr[j]:
#             arr[k]=left_arr[i]
#             i+=1 
#             k+=1 
         
#          else: 
#             arr[k]=right_arr[j]
#             j+=1 
#             k+=1 

#       while i<len(left_arr): 
#             arr[k] = left_arr[i]
#             i+=1 
#             k+=1 
            
#       while j<len(right_arr): 
#             arr[k] = right_arr[j]
#             j+=1 
#             k+=1 

# arr=[1,5,3,-8,7,0]
# merge_sort(arr)
# print(arr)
        

def merge_sort(arr): 

    if len(arr)>1: 

        left_side=arr[:len(arr)//2]
        right_side=arr[len(arr)//2:]

        i=0 
        j=0 
        k=0
        merge_sort(left_side)
        merge_sort(right_side)

        while i<len(left_side) and j<len(right_side): 
            if left_side[i]<right_side[j]: 
                arr[k]=left_side[i]
                i+=1
                k+=1 
            else: 
                arr[k]=right_side[j]
                j+=1 
                k+=1 

        while i<len(left_side): 
            arr[k]=left_side[i]
            i+=1 
            k+=1

        while j<len(right_side): 
            arr[k]=right_side[j]
            j+=1 
            k+=1

arr=[2,0,-9,44,89,7] 
merge_sort(arr)      
print(arr)    



    