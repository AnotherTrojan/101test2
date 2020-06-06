def remove_all_repeats(numbers_list):
    numbers_list.sort()
    has_num = []
    to_remove_indexes = []
    for i in range(len(numbers_list)):
        if numbers_list[i] not in has_num:
            has_num.append(numbers_list[i])
        else:
            to_remove_indexes.append(i)
    
    to_remove_indexes.reverse()
    for i in to_remove_indexes:
        numbers_list.pop(i)