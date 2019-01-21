def exercise1(temp_string):
    print(temp_string)

with open('E:/python_with_virutal_env/my_project/words.txt') as file:
    words = file.read()

import string
def clean(word):
    cleansed = ''
    for char in word:
        if (char in string.punctuation) or (char in string.whitespace):
            pass
        else:
            cleansed += char.lower()
    
    return cleansed

def most_common():
    my_dict = {}
    with open('E:/python_with_virutal_env/my_project/my_exercise/emma.txt','r') as file:
        words =  file.read().split()    
        for word in words:
            my_dict[word] = my_dict.get(word,0) + 1
    print(sorted(my_dict.items(),key=lambda key: key[1]))

def database_demo():
    # ! String starting with b'' are byte string
    # ! b'this is byte object not string'
    import dbm
    db = dbm.open('captions','c')
    db['chess.png'] = "{'image of chess': ' test'}"
    print(db['chess.png'])
    print(db['chess.png'].decode('ASCII'))
    db['test'] = 121212
    print(db[1])

database_demo()
# limition of dbm is that it can only work for bytes and string
# and to overcome this pickle is introduced
# values must be bytes or strings

def mypickle():
    import pickle
    l1 = [1,2,3,4,5]
    s = pickle.dumps(l1)
    print(s)
    print(pickle.loads(s))
