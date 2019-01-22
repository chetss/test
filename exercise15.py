import math
class Point:
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

    def distance_between_two_point(self,x1=0,y1=0,x2=0,y2=0):
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)

    def __str__(self):
        return f'{self.__x},{self.__y}'
    
    def display(self):
        print(f'({self.__x},{self.__y})')

    def __add__(self,other):
        print('here')
        print(type(self))
        print(other)
        if isinstance(other,Point):
            return ((self.__x + other.__x ), (self.__y + other.__y))
        else:
            # ! BELOW 2 LINES are written so that sum can work properly
            # ! by default sum() pass other = 0 for the first time 
            if other == 0:
                return ((self.__x + 0),(self.__y+0))
            
            return ((self.__x+other[0]),(self.__y+other[1]))

    def __radd__(self,other):
        return self.__add__(other)

    def main(self):
        # p = Point()
        # p.x = 1
        # p.y = 2
        # print(p.distance_between_two_point(2,2,3,3)) #1.4142135623730951
        # print(p) #1,2
        p1 = Point(1,1)
        p2 = Point(2,2)
        p3 = Point(2,2)
        # print(p1+p2) #(3, 3)
        # print(p1+(1,3)) #(2, 4)

        # !BUT Unfortunately, this implementation of addition is not commutative. If the Point is not the first operand, you get
        #   print((2,3) + p1) TypeError: can only concatenate tuple (not "Point") to tuple


        # TODO solution for this problem: the special method 
        # ?__radd__, which stands for “right-side add”.
        # after defining __radd__()
        # print((1,3)+p1) #(2, 4)
        print('last')

        print(sum([p1,p2,p3]))



if __name__ == "__main__":
    p = Point()
    p.main()