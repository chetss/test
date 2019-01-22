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