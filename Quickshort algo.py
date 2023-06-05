sublist_left = []
sublist_right = []
final_list = []

def partitionner(list):
    dernier = len(list)
    pivot = list[dernier -1]
    final_list.append(pivot)
    for i in range(dernier):
        if pivot > list[i]:
            sublist_left.append(list [i])
        elif pivot < list[i]:
            sublist_right.insert(0,list[i])
    if len(sublist_left) > 1:
        partitionner(sublist_left)
    if len(sublist_right) > 1:
         partitionner(sublist_right)
    print(str(sublist_left)+str(final_list)+str(sublist_right))
    return

partitionner ([4, 9, 3, 5, 1, 8, 7, 2, 6])
