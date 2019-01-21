# A tuple is a comma-separated list of values
    # t = 1,2,3,4,5

# To create a tuple with a single element, you have to include a final comma
    # t = 1,

# Best way to create dict from two sequences(list,tuples,string....)
# Combining dict with zip yields a concise way to create a dictionary
    # t1 = 1,2,3,4,5
    # t2 = 'a','b','c','d','e'
        # dict(zip(t1,t2))

# Lists are more common than tuples, mostly because they are mutable. 
# But there are a few cases where you might prefer tuples: 
    # 1. In some contexts, like a (return statement), it is syntactically simpler to create a tuple than a list. 
    # 2. If you want to use a (sequence as a dictionary key), you have to use an immutable type like a tuple or string. 
    # 3. If you are passing a (sequence as an argument to a function), 
        # using tuples reduces the potential for unexpected behavior due to aliasing.

def first():
    
    # t = 1,2,3,4,5
    # print(type(t))
    # print(t)
    
    # t = 1,
    # print(type(t))
    # print(t)

    # t = ('A',) + t[1:]
    # print(type(t))
    # print(t)

    # t1 = 'chetan'
    # t2 = 'sharma'
    # print(dict(zip(t1,t2)))


    # list of tuples
    keys = [('sharma','chetan'),('roshan','rakesh'),('harsha','shalendra')]
    values = [9898976789,232323244,4334343443]
    telephone_dict = dict(zip(keys,values))
    print(telephone_dict.get(('sharma','chetan')))

    # keys = [['sharma','chetan'],['roshan','rakesh'],['harsha','shalendra']]
    # values = [9898976789,232323244,4334343443]
    # telephone_dict = dict(zip(keys,values))
    # print(telephone_dict.get(['sharma','chetan']))
    print(hash('sharma'))


def most_frequent(mystring):
    my_dict = dict()
    for x in mystring.split():
        my_dict[x] = my_dict.get(x,0) + 1
    print(my_dict)
    print(sorted(my_dict.items(),key=lambda k: k[1]))

def signature(s):
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t

def all_anagram():
    d = {}
    with open('E:/python_with_virutal_env/my_project/words.txt','r') as file:
        words =  file.read().split()
        for word in words[1:5]:
            t = signature(word)    
            print(t)
            if t not in d:
                d[t] = [word]
            else:
                d[t].append(word)
    print(d)

most_frequent('learn to say no no is great')