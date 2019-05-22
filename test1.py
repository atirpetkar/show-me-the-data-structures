input_str = "The bird is the word"

char_freq_tuple_list = list()

char_freq_tuple_list = [('T', 1), ('h', 2), ('e', 2), ('b', 1)]

for char_freq_tuple in char_freq_tuple_list:
    print(char_freq_tuple[0])
    print(char_freq_tuple[1])

print("----------")

char_freq_tuple_list.sort(key=lambda r: r[1])

for char_freq_tuple in char_freq_tuple_list:
    print(char_freq_tuple[0])
    print(char_freq_tuple[1])
