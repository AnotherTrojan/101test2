def get_two_highest_marks(names_marks_list):
    first_mark = 0
    second_mark = 0
    for i in names_marks_list:
        if i[1] > first_mark:
            second_mark = first_mark
            first_mark = i[1]
        elif i[1] > second_mark:
            second_mark = i[1]
    
    to_return = [second_mark, first_mark]
    to_return.sort()
    return to_return