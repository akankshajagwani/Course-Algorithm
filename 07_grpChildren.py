# greedy algo
def GroupChildrn(x,n):
    # x- age list of children, n-number of children
    #NoGroups -minimum no. of groups
    assert(len(x) == n)
    NoGroups = len(x)
    x.sort()
    grp = {}
    i = 0
    k=0
    while i < len(x):
        key = i
        grp[key] = []
        grp[key].append(x[i])
        k = k+1
        print i,grp[key] 
        lowerBar = min(grp[key])
        print "lowerBar: ",lowerBar
        while i+1 < len(x) and x[i+1] - lowerBar <= 1:
            print "i+1",grp[key]
            grp[key].append(x[i+1])
            print "updated",grp[key]
            i = i+1
            k = k+1
        i = i+1
    print grp
    print k
    NoGroups = len(grp.keys())  
    return NoGroups   
    
NoGroups = GroupChildrn([3.167, 3.67, 5, 4.5, 4.0, 5.2, 4.8, 7.2, 15.4, 45, 12, 6.3, 4.5, 4.7, 9.8, 1.2, 5.2, 2.0, 4.5,4.8], 20)
print NoGroups