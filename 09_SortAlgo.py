
# find the minimum, swap it with the first element, and repeat it with the remaining elements
# running time: O(n^2)
def SelectionSort(lst, IorD):
    
    for i in range(0,len(lst)):
        indx = i
        for j in range(i+1,len(lst)):
            if IorD is 'D':
                if lst[j] > lst[indx]:
                    indx = j
            else:
                if lst[j] < lst[indx]:
                    indx = j
            
        temp = lst[i]
        if temp != lst[indx]:
            lst[i]= lst[indx]
            lst[indx]= temp        
    return lst

    
print SelectionSort([8,4,2,5,2],'I')
print SelectionSort([8,4,2,5,2],'D')