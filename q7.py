def get_common_elements(list1, list2):
    to_return = []
    for i in list1:
        if i in list2:
            to_return.append(i)
    to_return.sort()
    return to_return