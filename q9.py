def get_average_number_of_vowels(words_list):
    if len(words_list) == 0:
        return 0
    vowel_list = "AEIOUaeiou"
    vowel_count = 0
    word_count = 0
    for word in words_list:
        word_count += 1
        for letter in word:
            if letter in vowel_list:
                vowel_count += 1
    
    return round(vowel_count / word_count, 1)