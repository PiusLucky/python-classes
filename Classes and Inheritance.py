# Example of a simple class
class Car:
    tire_numbers = 4
    sterling_color = "Black"
    speed = "100–120 km/h"

# simple class with one method
class Car:
    tire_numbers = 4
    sterling_color = "Black"
    speed = "100–120 km/h"

    def check_speed(self):
        return self.speed

# simple class with two methods
class Car:
    tire_numbers = 4
    sterling_color = "Black"
    speed = "100–120 km/h"
    
    def check_speed(self):
        return self.speed # we access the class attribute with the "self" keyword

    def check_tires_count(self):
        return self.tire_numbers # we access the class attribute with the "self" keyword 


# 'my_car' is an object
my_car = Car() # class instantiation

# We could access Class Car variables like so:
print(my_car.tire_numbers)


# Quick Tip
# To call a function, use the function name followed by parenthesis
# check_speed is a method of the class Car.

print(my_car.check_speed())


# Results from console
# 4
# 100–120 km/h
# [Finished in 0.5s]


# print(dir(Car))

# Results from console
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'check_speed', 'check_tires_count', 'speed', 'sterling_color', 'tire_numbers']
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'check_speed', 'check_tires_count', 'speed', 'sterling_color', 'tire_numbers']


# non-argument class - a class that requires no argument
class Car:
    def __init__(self, tire_numbers=4, sterling_color="Black", speed="100–120 km/h"): # __init__ method
        self.tire_numbers = tire_numbers
        self.sterling_color = sterling_color
        self.speed = speed

    def check_speed(self):
        return self.speed # we access the class attribute with the "self" keyword

    def check_tires_count(self):
        return self.tire_numbers # we access the class attribute with the "self" keyword 


my_car = Car() # class instantiation

print("Car class with", my_car.tire_numbers, "tires") # Car class with 4 tires
print("Car class with", my_car.sterling_color, "sterling") # Car class with Black sterling
print("Car class with", my_car.speed, "of speed") # Car class with 100–120 km/h of speed



# argumennt class - a class that requires arguments
class Car:
    def __init__(self, tire_numbers, sterling_color, speed): # __init__ method with self & 3 parameters
        self.tire_numbers = tire_numbers
        self.sterling_color = sterling_color
        self.speed = speed

    def check_speed(self):
        return self.speed # we access the class attribute with the "self" keyword

    def check_tires_count(self):
        return self.tire_numbers # we access the class attribute with the "self" keyword 


my_car = Car(4, "Black", "100–120 km/h") # class instantiation with arguments

print("Car class with", my_car.tire_numbers, "tires") # Car class with 4 tires
print("Car class with", my_car.sterling_color, "sterling") # Car class with Black sterling
print("Car class with", my_car.speed, "of speed") # Car class with 100–120 km/h of speed



# function
def add_number(first_number, second_number):
    addition = first_number + second_number # addition logic
    print(addition) 
    return addition

add_number(2, 4) # 6


# equivalent class
class AddNumber:
    def __init__(self, first_number, last_number): # __init__ method with self & 2 parameters
        self.first_number = first_number
        self.last_number = last_number
    def add_number(self):
        addition = self.first_number + self.last_number # addition logic
        return addition

# instantiating the AddNumber class
add_number_object = AddNumber(2, 4) # object

# call the add_number method
print(add_number_object.add_number()) # 6



# class inheritance

# BaseClass
class Father:
    def __init__(self, fathers_firstname): # Base __init__ method with self & 1 parameter
        self.fathers_firstname = fathers_firstname

    def get_first_name(self):
        return "Father " + self.fathers_firstname 


# Derived Class
class Child_1(Father):
    # Derived __init__ method with self & 1 base parameter & 1 derived class parameter
    def __init__(self, fathers_firstname, childs_firstname): 
         # Pass in all the attributes of the base class into the super() init function [they are all required]
        super().__init__(fathers_firstname) 
        # You don't need to initialize the base class attributes, just the new attribute needs initializing
        self.childs_firstname = childs_firstname # initializing the new attribute

    # method
    def get_my_first_name(self):
        my_name = self.childs_firstname
        return "Child" + " " + my_name 

    # method
    def get_my_last_name(self): # Equal to get_first_name in BaseClass
        last_name = super(Child_1, self).get_first_name() # Python 2 - super(className,object)
        last_name = super().get_first_name() # Python 3 equivalent
        return last_name

    # method
    def get_my_full_name(self):
        return self.get_my_first_name() + " & " + self.get_my_last_name()

Child_1_object = Child_1("Pius", "Lucky") # instantiating the Child_1 class


print(Child_1_object.get_my_full_name()) # Child Lucky & Father Pius



# multiple class inheritance

# BaseClass 1
class Father:
    def __init__(self, fathers_firstname): # Base __init__ method with self & 1 parameter
        self.fathers_firstname = fathers_firstname

    def get_first_name(self):
        return self.fathers_firstname 

# BaseClass 2
class Child_1:
    def __init__(self, child_1_name, hobby): 
        self.child_1_name = child_1_name
        self.hobby = hobby

    def get_child1_name(self):
        return self.child_1_name

    def get_child1_hobby(self):
        return self.hobby

# Derived Class
class Child_2(Father, Child_1):
    """
    Child_2 class takes in two string parameters denoting the Father Class and Child_1 class as Base Class
    Father: str
    Child_1: str
    """
    def __init__(self, fathers_firstname, child_1_name, hobby, childs_2_firstname): 
        # overriding fathers_firstname defined in Child_2 __init__() by the fathers_firstname defined in the Father __init__()
        Father.__init__(self, fathers_firstname) 
        # overriding child_1_name & hobby defined in Child_2 __init__() by the child_1_name & hobby defined in the Child_1 __init__()
        Child_1.__init__(self, child_1_name, hobby)
        self.childs_2_firstname = childs_2_firstname # initializing the new attribute

    # method
    def get_my_first_name(self):
        my_name = self.childs_2_firstname
        return my_name

    # method
    def get_my_last_name(self): # Equal to get_first_name in BaseClass Father
        last_name = super(Child_2, self).get_first_name() # Python 2 - super(className, object)
        last_name = super().get_first_name() # Python 3 equivalent
        return last_name

    # method
    def get_my_full_name(self):
        return "{0} {1}".format(self.get_my_first_name(), self.get_my_last_name())

    # method
    def get_my_sibling_attributes(self):
        sibling_name = super().get_child1_name() # Python 3 equivalent
        sibling_hobby = super().get_child1_hobby() # Python 3 equivalent
        return sibling_name + " & she likes " + sibling_hobby

    # method
    def about_me(self):
        my_full_name = self.get_my_full_name()
        my_sibling_name = self.get_my_sibling_attributes()
        return "My name is {0}, I have a sibling called {1}".format(self.get_my_full_name(), self.get_my_sibling_attributes()) 



Child_2_object = Child_2("Pius", "Happy", "dancing", "Lucky") # instantiating the Child_2 class


print(Child_2_object.about_me()) # My name is Lucky Pius, I have a sibling called Happy & she likes dancing








# BONUS TIPS:

# __doc__


# Use this to get the document string of a particular class
print(Child_2.__doc__)
# Output:
# Child_2 class takes in two string parameters denoting the Father Class and Child_1 class as Base Class
# Father: str
# Child_1: str


# __subclasses__


print(Father.__subclasses__())
# Output:
# [<class '__main__.Child_2'>]

# Implication
# This means that Child_2 Class depends on the Father Class

print(Child_1.__subclasses__())
# Output:
# [<class '__main__.Child_2'>]
# Implication
# This means that Child_2 Class depends on the Father Class


# issubclass

print(issubclass(Child_2, Father)) 
# Output:
# True

# Implication
# This means that Child_2 Class depends on the Father Class


# relationship b/w self and object (or class instance)

class Worker:
    def __init__(self, salary): 
        self.salary = salary 

    # method
    def salary_checker(self):
        my_salary = self.salary # self is the representation of the Worker Object inside the class [self is an instance of the class]
        print(my_salary) # 5000
        return my_salary

worker_object = Worker(5000)      

worker_salary = worker_object.salary_checker() # "worker_salary" is the representation of the Worker object (worker_object) outside of the class [object is an instance of a class]

print(worker_salary) #5000

# NOTE: 

# "worker_salary" is the representation of the object outside of the class 
# "self"  is the representation of the object inside  the class.
# "self" & "object" both return the same result, 5000.