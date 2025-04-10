
def insertion_sort(list): 
    # use indexing to traverse the len
    indexing_length=range(1,len(list))
    for i in indexing_length: 
        value_to_sort=list[i]

        while list[i-1]>value_to_sort and i>0: 
            list[i],list[i-1]=list[i-1],list[i]
            i-=1
    return list 
print(list)

print(insertion_sort([2,-6,88,40,3,27]))
