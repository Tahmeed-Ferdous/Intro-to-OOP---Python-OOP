from class_design_import import Python
# bring items from another py file
from abc import ABC, abstractmethod
# necessary for the the abstract method

class Language:
    class Interpreter: #Nexted Class
        def __init__(self, code):
            self.code=code
        # it has no use, its abstract, disables the function below, these are just samples of functions to copy and write your code inside
        @abstractmethod 
        def uses(self):
            pass
    
    def __init__(self, name):
        self.name=name #attributes
        self.collection=[]
        self.codes=[]
    def lang(self):
        print(f"Code the language")
    def add(self, user, code):
        new_code=self.Interpreter(code) # Nexted class variable
        self.codes.append(new_code)
        self.collection.append(user) # Aggregation, taking ref from child classes to the parent classes by inserting childs objects
    def lst(self):
        return [f"{user.name} and {user.inventor}" for user in self.collection], [f"{user.code} language" for user in self.codes]
    
    @staticmethod
    def validity(code):
            valid='t'
            return code==valid
    # Static Method belongs to a class not object

class Python(Language):#inheritance
    year=2024 #class variable
    number_of_programs=0
    def __init__(self, name, inventor, speciality): #constructor
        super().__init__(name)
        self.inventor=inventor
        self.speciality=speciality
        Python.number_of_programs+=1

    def code(self): #instance methods
        print(f"Code: {self.name}")
    def stop(self):
        print(f"Stop: {self.name}")
    def description(self):
        print(f"It is an easy coding language")

    @classmethod
    def count(cls): # to acceess class variables in methods
        return cls.number_of_programs
    

class Java(Language): 
    year=2024
    number_of_programs=0
    def __init__(self, name, inventor, speciality):
        super().__init__(name)
        self.inventor=inventor
        self.speciality=speciality
        Java.number_of_programs+=1

    def write(self):
        print(f"Code1: {self.name}")
    def delete(self):
        print(f"Stop1: {self.name}")
    def describe(self):
        print(f"It is an easy coding language")
    
    #Overriding
    def __str__(self): #now we can call objects
        return f'{self.name} {self.inventor} {self.speciality}'
    def __eq__(self, other):#check the obj are same or not
        return self.name==other.name
    def __add__(self, other): #add obj
        return f'{self.name+other.name}'
    def __contains__(self, keyword):
        return keyword in self.name or keyword in self.inventor


class Basics(Python):
    def topic1(self):
        topics1=[self.name, 'Boolean', 'loops', 'list', 'dict', 'functions']
        print(topics1)

#double inheritance (Copies functions and attributes)
class OOP(Python, Java):
    def __init__(self, name, inventor, speciality, core):
        # Precaution: You can not use super() (when taking multi classes)
        self.name=Language(name) # composition, one way to bring the attributes of a parent class
        self.__inventor=inventor # cannot access directly
        self.speciality=speciality
        self.core=core

    def topic(self):
        topics=[self.name.name, 'Abstraction', 'Inheritance', 'Polymorphism'] #composition
        print(*topics)
    def setInventor(self, inventor): #Set and Getter method
        self.__inventor=inventor
    def getInventor(self):
        return self.__inventor


#Driver Code (code here to access the class design)
#------------------------------------------------------------------------

d=Language('Programming')
user=Python('Programming1', 'Tahmid', 'Machine Learning')
user0=Java('Programming', 'Sadnan', 'AI')
user1=OOP('OOP', 'Wafiq', 'CSE', 'Core')
user2=Basics('Basics', 'Tasneem', 'EEE')

d.add(user, 't')
d.add(user0, 'd')
print(user.name)
print(user.inventor)
print(Python.number_of_programs)
print(Python.year)
user.code()
user2.stop()
user1.topic()
print(user1.name.name, user1.core)
user.lang()
user1.lang()
user2.code() # it doesnt have any code() function, it takes the function from Parent class = Polymorphism
for i in d.lst():
    print(i[0], i[1])
print(Language.validity('t'))
print(Python.count())
print(user0) # dunder methods __init__ __str__, automatically called by python to change behavior of objects only
print(user0==user0)
print(user0+user0)
print('Tahmeed' in user0)
user1.setInventor('Tasfia')
print(user1.getInventor())

