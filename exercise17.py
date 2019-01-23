class kangaroo:
    # def __init__(self,pouch_contents=[]):
    #     self.__pouch_contents = pouch_contents

        # The problem with the above method is the default value for pouch_contents .
        # Default values get evaluated ONCE, when the function
        # is defined; they don't get evaluated again when the
        # function is called.

        # In this case that means that when __init__ is defined,
        # [] gets evaluated and contents gets a reference to
        # an empty list.

        # After that, every Kangaroo that gets the default
        # value gets a reference to THE SAME list.  If any
        # Kangaroo modifies this shared list, they all see
        # the change.

    def __init__(self,pouch_contents=None):
        if pouch_contents == None:
            pouch_contents = []
        self.__pouch_contents = pouch_contents
    

    def put_in_pouch(self,any_type_object):
        self.__pouch_contents.append(any_type_object)

    def __str__(self):
        return f'{self.__pouch_contents}'
    


kanga = kangaroo()
roo = kangaroo()
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)
print(kanga)
print(roo)