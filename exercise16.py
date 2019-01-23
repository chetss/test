class Date:
    """
        User Defined Date class.

        Attributes
        day - int
        month - int
        year - int
    """   

    def __init__(self,day='',month='',year=''):
        print('init called')
        self.__day = day
        self.__month = month
        self.__year = year

    @property
    def day(self):
        print('day gettter')
        return self.__day
    
    @day.setter    
    def day(self,day):
        print('day setter')
        self.__day = day 

    @property
    def month(self):
        return self.__month
    
    @month.setter
    def month(self,month):
        self.__month = month


    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self,year):
        self.__year = year


    def display(self):
        return f'{self.day}::{self.month}::{self.year}'

# pure function are those function which doesn't modity any of the obejcts passed to it as arguments and 
# it has no effect, like displaying a value of getting user input, other than returning a value.

    # pure function
    def add_day(self,other):
        temp = Date()
        temp.day = self.day+other.day
        temp.month = self.month+other.month 
        temp.year = self.year+other.year

        if temp.day >= 30:
            temp.day -= 30
            temp.month += 1

        if temp.month >= 12:
            temp.month -= 12
            temp.year +=1

        return temp


d1 = Date()
d1.day
