def print_inverted_mirrored_right_angle_triangle(symbols, index, number_of_rows):
    spacer = ""
    if len(symbols) - 1 < index:
        start_value = index
        while number_of_rows > 0:
            to_print = spacer
            for i in range(start_value, start_value + number_of_rows):
                to_print += str(i)
            print (to_print)
            spacer += " "
            number_of_rows -= 1

    else:
        while number_of_rows > 0:
            print (spacer + number_of_rows * symbols[index])
            spacer += " "
            number_of_rows -= 1

print_inverted_mirrored_right_angle_triangle(['%', '$', '#', '@', '&', '*'], 2, 4)
print ()
print_inverted_mirrored_right_angle_triangle(['%', '$', '#'], 3, 5)