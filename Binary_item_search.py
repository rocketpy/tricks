from random import randint
 

# create a new list and sort them
new_list = []

for i in range(10):
    new_list.append(randint(1, 20))
new_list.sort()
# print(a)
 
# digit for search
value = int(input())

high = len(new_list) - 1
mid = len(new_list) // 2
low = 0
 
while new_list[mid] != value and low <= high:
    if value > new_list[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2
 
if low > high:
    print("No value found")
else:
    print("ID = ", mid)
 

