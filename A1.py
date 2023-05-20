def limit (arr , min=None ,max=None) :
    min_check = lambda val : True if min is None else (val >= min)
    max_check = lambda val : True if max is None else (val <= max)
    
    return [ val for val in arr if min_check(val) and max_check(val)]
print(limit([1,47,5,8,74,55,25],max=20))