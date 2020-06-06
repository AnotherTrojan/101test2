def get_list_of_countries(filename):
    file = open(filename, "r")
    file_str = file.read()
    file_list = file_str.split()
    return file_list

def create_country_code_dictionary(lines_list):
    to_return = {}
    for i in lines_list:
        colon_index = i.find(":")
        to_return[i[:colon_index]] = i[colon_index + 1:]
    
    return to_return