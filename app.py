<<<<<<< HEAD
class shape:
    
    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self,length):
        self.__length = length

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self,width):
        self.__width = width

    def display(self):
        print(f'{self.length} {self.width}')

a = shape()
a.length = 10       
a.width = 20
a.display()
=======
class Kangaroo:
    """A Kangaroo is a marsupial."""
    
    def __init__(self, name, contents=None):
        """Initialize the pouch contents.

        name: string
        contents: initial pouch contents.
        """
        self.name = name
        if contents == None:
            contents = []
        self.pouch_contents = contents

    def __str__(self):
        """Return a string representaion of this Kangaroo.
        """
        t = [ self.name + ' has pouch contents:' ]
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """Adds a new item to the pouch contents.

        item: object to be added
        """
        self.pouch_contents.append(item)


kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)

print(kanga)
print(roo)
>>>>>>> b920a3c3bdef387baa2d42771d9c1dddb69a43f2
