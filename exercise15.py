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

    def distance_between_two_point(self,x1=0,y1=0,x2=0,y2=0):
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)

    def __str__(self):
        return f'{self.x},{self.y}'
    
    def display(self):
        print(f'({self.x},{self.y})')

    def __add__(self,other):
        if isinstance(other,point):
            return ((self.x + other.x ), (self.y + other.y))
        else:
            return ((self.x+other[0]),(self.y+other[1]))

    def __radd__(self,other):
        print(self)
        print(other)
        return self.__add__(other)

    def main(self):
        p = point()
        p.x = 1
        p.y = 2
        print(p.distance_between_two_point(2,2,3,3)) #1.4142135623730951
        print(p) #1,2
        p1 = point(1,1)
        p2 = point(2,2)
        print(p1+p2) #(3, 3)
        print(p1+(1,3)) #(2, 4)

        # !BUT Unfortunately, this implementation of addition is not commutative. If the point is not the first operand, you get
        #   print((2,3) + p1) TypeError: can only concatenate tuple (not "point") to tuple


        # TODO solution for this problem: the special method 
        # ?__radd__, which stands for “right-side add”.
        print((1,3)+p1+(10,10))



if __name__ == "__main__":
    p = point()
    p.main()