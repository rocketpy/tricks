not_sorted = [3, 5, 1, 7, 2, 4, 6]

def bubble_sort(ls):
    n = len(ls)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if ls[j] > ls[j + 1] :
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
    return print(not_sorted)
  
bubble_sort(not_sorted)
# print(not_sorted)

"""
ls = [3, 5, 1, 7, 2, 4, 6, 8]

def bubble_sort(ls):
    length = len(ls)
    for i in range(length):
        for j in range(length - i):
            a = ls[j]
            if a != ls[-1]:
                b = ls[j + 1]
                if a > b:
                    ls[j] = b
                    ls[j + 1] = a
    return print(ls) 
    
bubble_sort(ls)
"""
