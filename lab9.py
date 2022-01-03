# -*- coding: utf-8 -*-
"""lab9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hZP5rcFEC78CkYUU07U9XJrZI5OcioHa

1. Write a program that defines a shape class with a 
constructor that gives value to width and height. The 
define two sub-classes triangle and rectangle, that 
calculate the area of the shape area (). In the main, 
define two variables a triangle and a rectangle and then 
call the area() function in this two variables.
"""

class shape():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
class rectangle(shape):
        def area(self):
           return self.breadth*self.length
class triangle(shape):
        def area(self):
           return .5*self.breadth*self.length 
a=int(input("Enter length of rectangle: "))
b=int(input("Enter breadth of rectangle: "))
obj=rectangle(a,b)
print("Area of rectangle:",obj.area())    
obj2=triangle(a,b)
print("Area of triangle:",obj2.area())

"""2. Write a program with a mother class and an inherited 
daughter class. Both of them should have a method void 
display () that prints a message (different for mother and 
daughter).In the main define a daughter and call the 
display () method on it.
"""

class mother:
  def pr1(self):
    print("Function of mother class.")

class daughter(mother):
  def pr2(self):
    print("Function of daughter class.")

object1 =daughter()
object1.pr1()
object1.pr2()

"""3. Write a program with a mother class animal. Inside it 
define a name and an age variables, and set_value() 
function. Then create two sub class Zebra and Dolphin 
which write a message telling the age, the name
"""

class Animal:

      def set_data (self,a,b):
        self.age=a
        self.name=b

class Zebra(Animal):
   def set_data (self,a,b):
        self.age=a
        self.name=b

   def message_zebra(self):
        print("The zebra named ",self.name ," is",self.age)
    
class Dolphin(Animal):
    def set_data (self,a,b):
        self.age=a
        self.name=b

    def message_dolphin(self):
      print( "The dolphin named ",self.name , " is ",self.age )

ob1= Zebra()
ob1.set_data(44,"ccc")
ob1.message_zebra()
ob2=Dolphin()
ob2.set_data(77,"hh")
ob2.message_dolphin()

"""4. Create a child class Bus that will inherit all of the 
variables and methods of the Vehicle class
"""

class Vehicle:

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
       

class Bus(Vehicle):
    pass

b_bus = Bus("coco", 6)
print("Vehicle Name:",b_bus.name, "Speed:",b_bus.speed)

"""5. Define property that should have the same value for 
every class instance
"""



"""6. Create a class called Employee whose objects are 
records for an employee. This class will be a derived 
class of the class person which you will have to copy into 
a file of your own and compile. An employee record has 
an employee's name (inherited from the class Person), an 
annual salary represented as a single value of 

"""

class  person:
  def __init__ (self,name):
    self.name=name
class employee( person):
  def __init__ (self,annual_salary,name):
       Super.__init__(name)
       self.annual_salary=annual_salary

  def info():    
      print("employee name is",self.name,"annual salary is",self.annual_salary)
  
    
ob1= employee(22,"yy")
ob1.info()

