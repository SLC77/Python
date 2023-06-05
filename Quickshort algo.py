sublist_left = []
sublist_right = []
final_list = []

def quicksort(list):
    dernier = len(list)
    pivot = list[dernier -1]
    final_list.append(pivot)
    for i in range(dernier):
        if pivot >= list[i]:z 
            sublist_left.append(list [i])
        else:
            sublist_right.insert(0,list[i])
    if len(sublist_left) < 1:
        quicksort(sublist_left)
    if len(sublist_right) > 1:
         quicksort(sublist_right)
    return quicksort(sublist_left) + [final_list] + quicksort(sublist_right)

print(quicksort([85,42,12,6,3,9,4,7,50]))














# import random

# list = [15,56,2,9,4,23,19]

# def random_pivot(list):
#     index_pivot = random.choice(list)
#     pivot = list(index_pivot)

#     for i in range(len(list)):
#         if i == index_pivot: continue

#     print(pivot)
#     return random_pivot

