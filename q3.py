def get_unique_3_letter_words(text):
    text_list = text.split()
    to_return = []
    for i in text_list:
        if len(i) == 3 and i.lower() not in to_return:
            to_return.append(i.lower())

    to_return.sort()
    return to_return