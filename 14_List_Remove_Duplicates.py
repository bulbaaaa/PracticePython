a = [1, 1, 3, 4, 5, 5, 67, 67, 100, 120, 131, 131, 900]

def remove_duplicates_set(a):
    return list(set(a))



def remove_duplicates_func(a):
    new_list = []
    for i in a:
        if i not in new_list:
            new_list.append(i)

    return new_list

print(remove_duplicates_func(a))
