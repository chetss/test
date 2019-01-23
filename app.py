my_dict = {('a', 'b'): ['word']}
prefix = ('a','b')

try:
    my_dict[prefix].append('chetan')
except KeyError:
    my_dict[prefix] = 'word'

print(my_dict)