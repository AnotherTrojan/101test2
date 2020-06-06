def process_marks(filename):
    file = open(filename, "r")
    file_str = file.read()
    file_lines = file_str.splitlines()
    file.close()

    scores_dict = {}
    for line in file_lines:
        split_index = line.rfind(",")
        names = line[:split_index]
        scores = line[split_index + 1:]
        names_list = names.split(",")
        scores_list = scores.split(":")

        for name_index in range(len(names_list)):
            if names_list[name_index] in scores_dict:
                scores_dict[names_list[name_index]].append(int(scores_list[name_index]))
            else:
                scores_dict[names_list[name_index]] = [int(scores_list[name_index])]

    to_return = {}
    for i in sorted(scores_dict):
        scores_dict[i].sort()
        to_return[i] = tuple(scores_dict[i])
    return to_return