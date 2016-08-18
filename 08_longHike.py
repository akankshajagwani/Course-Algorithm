# geedy algo
def maxValueForWeight(w,v,W):
    assert(len(w) == len(v))
    valuePerWeight = {}
    for i in range(0,len(w)):
        key = float(v[i])/w[i]
        # print key
        valuePerWeight[key] = []
        valuePerWeight[key].append([w[i],v[i]])
        
    # print valuePerWeight
    lst_keys = []
    lst_keys = lst_keys + valuePerWeight.keys()
    lst_keys.sort(reverse = True)
    totalWeight = 0
    totalValue = 0
    i_key = 0
    while totalWeight < W:
        n_key = lst_keys[i_key]
        # print n_key
        [[weight,value]] = valuePerWeight.get(n_key)
        
        # print valuePerWeight.get(n_key),weight
        tobeAddedWeight = W - totalWeight
        if weight < tobeAddedWeight:
            totalWeight = totalWeight+ weight
            totalValue = totalValue + value
        else:
            totalWeight = totalWeight+ tobeAddedWeight
            totalValue = totalValue + float(value)*tobeAddedWeight/weight
        i_key = i_key +1    
    return  totalValue   

totValue = maxValueForWeight([20,50,30],[60,100,120],50)
totValue = maxValueForWeight([30],[500],10)
print totValue