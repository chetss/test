def exercise1():
    """Search the word in the word dict"""
    with open('E:/python_with_virutal_env/my_project/words.txt') as file:
        my_word_dict = {x: 1 for x in file.read().split()}
        print(my_word_dict.get('zymase'))
