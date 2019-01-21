import math
class point:
    def __init__(self,x=0,y=0):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self,x):
        self.__x = x

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self,y):
        self.__y = y

    def display(self):
        print(f'({self.x},{self.y})')

    def distance_between_two_point(self,x1=0,y1=0,x2=0,y2=0):
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)

p = point()
p.x = 1
p.y = 2


print(p.distance_between_two_point(2,2,3,3))