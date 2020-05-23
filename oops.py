'''class Dog:
    def __init__(self,first,second):  #paramt. constructor
        self.first = first
        self.second = second


    def fun(self):
        print('this is ',self.first)
        print('this is ',self.second)

obj = Dog('labrador','husky')
obj.fun()
'''
'''
class Addition:

    def __init__(self,f,s):
        self.first = f
        self.second = s

    def calculation(self):
        print(self.first + self.second)

obj = Addition(10,20)
obj.calculation()
'''

#destructor
'''
class Employee:
    def __init__(self):
        print("employee constructor created!!")

    def __del__(self):
        print("destructor!!!")

obj = Employee()

del obj

'''

# simple inheritance example:


'''
class Person(object):
    def __init__(self,name):
        self.name = name #self is holding yhe obj; 'name' is parameter

    def isEmployee(self):
        return False

    def getName(self):
        return self.name


class Employee(Person):

    def isEmployee(self):
        return True

emp = Person("jack")
print(emp.getName(),emp.isEmployee())

emp = Employee("Kim")
print(emp.getName(),emp.isEmployee())

'''
# python supports multiple and multilevel only
#   Multiple Inheritance
'''''
class Person1:
    def __init__(self):
        self.name1 = "Kim"
        print("in person")

class Person2:
    def __init__(self):
        self.name2 = "tae"
        print("in person 2")

class Derived(Person1,Person2):
    def __init__(self):
        Person2.__init__(self) # calling super class constructor
        Person1.__init__(self)
        print("in derived class")
    def fun(self):
        print(self.name1,self.name2)

obj = Derived()
obj.fun()
'''

##### access parent class member   #######

# 1. using  "super().__init__(name)"
'''''
class Base(object):
    def __init__(self,x):
        self.x = x

class Child(Base):
    def __init__(self,x,y):
        super( Child, self ).__init__(x)
        self.y = y

    def show(self):
        print(self.x, self.y)

obj = Child(10,20)
obj.show()

'''
#  2.using parent class name
'''
class Base(object):

    def __init__(self,x):
        self.x = x

class Child(Base):

    def __init__(self,xi,y):
        Base.x = xi
        self.y = y

    def show(self):
        print( Base.x, self.y )

obj = Child(10,20)

obj.show()
'''

######### multilevel inheritance ########

## PENDING ----DO IT



### ENCAPSULATION ###

'''Protected members (in C++ and JAVA) are those members of the class which cannot be accessed outside the class
    but can be accessed from within the class and it’s subclasses. To accomplish this in Python, 
     just follow the convention by prefixing the name of the member by a single underscore “_”.
       
         ### PRIVATE MEMBER ###
     Private members are similar to protected members, the difference is that 
     the class members declared private should neither be accessed outside the class nor by any base class. 
    
     In Python, there is no existence of Private instance variables that cannot be accessed except inside a class.
      However, to define a private member prefix the member name with double underscore “__”.
     
     '''
'''''
class Base:

    def __init__(self):
        self.a = 'bts'
        self.__c = 'singers'

class Derived(Base):

    def __init__(self):

        Base.__init__(self)# calling parent class constructor
        print("calling private member of parent class:")
        print(self.__a)


obj1 = Base()
print(obj1.a)

'''
## protected data members ##
'''''
class Base:

    def __init__(self):

        self._a = 2

class Derived(Base):

    def __init__(self):

        Base.__init__(self)  # calling base class constructor

        print("calling protected member of base class:")
        print(self._a)

obj1 = Derived()
obj2 = Base()

print(obj2.a)  ## calling protected member outside the class ,so its error
'''''

### private member ### "__" double underscore is used to define private member
'''example:1
class Base:

    def __init__(self):

        self.a = "geeks are best"
        self.c = "geeksforgeeks"


class Derived(Base):

    def __init__(self):

        # calling base class constructor

        Base.__init__(self)
        print("calling private member of base class")
        print(self.__c)   # private data members cant be accessed using object

obj = Derived()
print(obj.c)
'''

# example 2
'''''
class Base:
    def __init__(self):
        self.a = "geeks" # not private
        self.__c = "best"  # private

class Derived(Base):

    def __init__(self):

        Base.__init__(self)

        print("calling private data members")
        print(self.__a) # now private member of DErived class

obj = Base()
print(obj.a)
print(obj.c) # private member of Base class
# obj1 = Derived()
#print(obj1.a) -->  error cause private member of Derived class

'''''

## polymorphism
## method overloading is not possible in python (methods with same name but differnt paramt)

# method overriding

''''
 feature tht allows child class to provide specific
 implementation of a method i.e. already provided in parent class.'''''
'''''
class Base:

    def show(self):

        print("inside base class")

class Derived(Base):

    def show(self):

        print("inside child class")


obj = Base()
obj2 = Derived()

obj.show()
obj2.show()

'''''

## polymorphism in class methods
'''''

class Cat:

    def __init__(self,name,age):

        self.name = name
        self.age = age

    def info(self):

        print(f"I'm a cat my name is {self.name}. and I'm {self.age} years old")

    def sound(self):

        print("meow")

class Dog:

    def __init__(self,name,age):

        self.name = name
        self.age = age

    def info(self):

        print (f"I am dog my name is {self.name}. and age is {self.age} ")

    def sound(self):

        print("bark")



cat1 = Cat('kitty',2)
dog1 = Dog('rehu',9)

for animal in (cat1, dog1):
    animal.info()
    animal.sound()

'''''

#polymorphism and inheritance
'''''
from math import pi

class Shape:

    def __init__(self,name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "two dimensional shape"

    def __str__(self):
        return self.name

class Square(Shape):

    def __init__(self,length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Square):

    def __init__(self,radius):
        super().__init__("circle cls")
        self.radius = radius

    def area(self):
        return pi*self.radius**2

a = Square(3)
b = Circle(2)

print(b)
print(b.fact())
print(a)
print(a.fact())
print(b.area())

'''''
### exception handling ###
















































