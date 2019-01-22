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

# limition of dbm is that it can only work for bytes and string
# and to overcome this pickle is introduced
# values must be bytes or strings

def mypickle():
    import pickle
    l1 = [1,2,3,4,5]
    s = pickle.dumps(l1)
    print(s)
    print(pickle.loads(s))


def os_popon():
    import os
    cmd = 'python exercise12.py'
    fs = os.popen(cmd)
    print(fs.read())
    fs.close()

def my_test():
    # ! Reason? Lookup for a function is a costly operation.
    # In the second snippet, I stored the function directly in the scope of the function,
    # so it doesn’t matter how many times I call it, 
    # each time the runtime knows exactly where it has to look for the results.
    import datetime 
    
    alphabets = [str(x)for x in range(10000000)] 
    
    # ?first
    a = datetime.datetime.now() # store initial time 
    for item in alphabets: 
        len(item) 
    b = datetime.datetime.now() # store final time 
    print((b-a).total_seconds()) # results  => 0.5069
    
    # ?second
    a = datetime.datetime.now() 
    fn = len				 # function stored locally 
    for item in alphabets: 
        fn(item) 
    b = datetime.datetime.now() 
    print((b-a).total_seconds()) # resutls => 0.3405


def test():
    my_list = 	['spam','egg','spam','spam','bacon','spam']
    my_dict = {}

    for x in my_list:
        my_dict[x] = my_dict.get(x,0)+1
    print(my_dict)

test()