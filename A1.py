# def limit (arr , min=None ,max=None) :
#     min_check = lambda val : True if min is None else (val >= min)
#     max_check = lambda val : True if max is None else (val <= max)  
#     return [ val for val in arr if min_check(val) and max_check(val)]
# print(limit([1,47,5,8,74,55,25],max=20))
#############################################################################
def top(arr) :
    values ={}
    result = []
    f_val = 0
    for i in arr :
        if i in values :
            values[i] += 1
        else : 
            values[i] = 1
    print(values)
    f_val = max(values.values())
    for i in values.keys() :
        if values[i] == f_val :
            result.append(i)
        else :
            continue
    return result
print(top([1,2,5,4,5,5,5,3,2,1,5,2,6,9,2,8,2,8]))
###############################################################################