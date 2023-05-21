# def limit (arr , min=None ,max=None) :
#     min_check = lambda val : True if min is None else (val >= min)
#     max_check = lambda val : True if max is None else (val <= max)  
#     return [ val for val in arr if min_check(val) and max_check(val)]
# print(limit([1,47,5,8,74,55,25],max=20))
#############################################################################
# def top(arr) :
#     values ={}
#     result = []
#     f_val = 0
#     for i in arr :
#         if i in values :
#             values[i] += 1
#         else : 
#             values[i] = 1
#     print(values)
#     f_val = max(values.values())
#     for i in values.keys() :
#         if values[i] == f_val :
#             result.append(i)
#         else :
#             continue
#     return result
# print(top([1,2,5,4,5,5,5,3,2,1,5,2,6,9,2,8,2,8]))
###############################################################################
# from string import ascii_letters

# def encrypt(string , key) :
#     alpha = ascii_letters
#     result = ''
#     for ch in string :
#         if ch not in alpha :
#             result += ch
#         else :
#             new_key =  (alpha.index(ch) + key ) % len(alpha)
#             result += alpha[new_key]
#     return result
# def decrypt(string , key) :
#     key *= -1
#     return encrypt(string, key)

# def brute_force(string) :
#     alpha = ascii_letters
#     key = 1
#     resulte =''
#     brute_force_data = {}
#     while key <= len(alpha) :
#         resulte = decrypt(string, key)
#         brute_force_data[key] = resulte
#         resulte = ''
#         key += 1
#     return brute_force_data

# print(brute_force('eqmv'))
###############################################################################
# def search_insert(arr , val) :
#     low = 0
#     high = len(arr)-1
#     mid = high // 2
#     while low <= high :
#         if val > arr[mid] :
#             mid += 1
#             low = mid
#         else :
#             mid -=1
#             high =mid            
#     return mid 
# print(search_insert([2,3,4,5,8,10,11,20], 15)) 
###############################################################################
# def is_isomorphic(s ,t) :
#     if len(s) != len(t) :
#         return False
#     dict={}
#     set_values = set()
#     for i in range(len(s)) :
#         if s[i] not in dict :
#             if t[i] in set_values :
#                 return False
#             dict[s[i]] = t[i]
#             set_values.add(t[i])
#         else :
#             if dict[s[i]] != t[i] :
#                 return False
#     return True
# 
# print(is_isomorphic('hii', 'boo'))
###############################################################################
# def encode (plain) :
#     return [ ord(elm) for elm in plain]
# def decode (encode) :
#     return "".join(chr(elm) for elm in encode)
# print(decode([109, 111, 98, 105, 110]))

# print(encode('mobin'))
###############################################################################
def bead_sort(sequence) :
    if any(not isinstance(x, int) or x < 0 for x in sequence) :
        raise TypeError('ridi')
    for _ in range(len(sequence)):
        for i,(rod_upper , rod_lower) in enumerate(zip(sequence,sequence[1:])) :
            if rod_upper > rod_lower :
                sequence[i] -= rod_upper - rod_lower
                sequence[i+1] += rod_upper - rod_lower
    return sequence       
     
print(bead_sort([1, 5 ,2 ,9 ,3 ,6 ,7,10]))
    