# program to print even length words in a string

def return_even_len_words(str1):
    words_list = []
    for words in str1.split():
        if len(words) % 2 == 0:
            words_list.append(words)
    return words_list


input_str = input('Enter a string to find even length words from it: ')

print('list of even words from give string --> ', return_even_len_words(input_str))
