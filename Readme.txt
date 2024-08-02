INTRO TO OPP

Four Pillars of Object Oriented Programming:

Encapsulation:
It describes the idea of wrapping data (properties) and the methods (function calls) that work on data within one unit (class).
---Reduce Complexities and increases reusability

Abstraction:
Allows us to simplify complex concepts and focus on the essential details
---Reduces complexity and isolate impact of changes

Inheritance:
One class inherits the attributes and methods of another class.
---Eliminate redundant code

Polymorphism: (Many Form)
the same function name is being used for different (class)
---Refactor ugly switch/case statements



Basic naming and functions:

Object= A bundle of related attributes(variables) and methods(function)

Class = blueprint used to design and structure and layout of an object

Class Variable = Shared among all instances of a class, Defined outside the container, Share data among all objects created from the class

super() = Function used in a child to call methods from a parent class (super class)

ducktyping = Set a class variable if the attribute is not present in the exiting class, to take that attributes place.

Nested Class = private within once class and keeps the namespace clean

Methods: 
insance method: the methods we use to have functionality
Get/Set method: enables protection and cannot be access directly
@staticmethod: belongs to a class not object, call by class
@abstractmethod: these are samples of functions to copy and write 
@classmthod: (cls) call class variables in a method
Method Overiding: dunder methods __init__ __str__, automatically called by python to change behavior of objects only

composition: one way to bring the attributes of a parent class
Aggregation, taking ref from child classes to the parent classes by inserting childs object