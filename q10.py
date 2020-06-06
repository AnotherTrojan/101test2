def has_exactly_2_of_each(a_list):
    int_dict = {}
    for i in a_list:
        if i in int_dict:
            int_dict[i] += 1
        else:
            int_dict[i] = 1
    
    for i in int_dict.values():
        if i != 2:
            return False
    
    return True