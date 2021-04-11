#To build and expand upon the tutorials given by Mike and Mosh, Corey Schafer explains in more detail
#Addendum: Trust in Corey - He explains the stuff good-like, and with a nice drawl

#The following sort of deviates from the rule of trying not to copy too much, but the explainations from Corey are too good to be simplified and messed around with.
#The other programs in this repository will be more in the geist of the rules.

#Data and functions associated with a specific class are called "attributes" and "methods"

class Employee:
    
    raise_amount = 1.04 #Class variable: Variables shared between all instances of a class
    num_of_emps = 0

    def __init__(self, first_name, last_name, pay): #the "self" is replaced by the instance /object-name
        self.first_name = first_name #attributes of the class, defining the instance variables only pertaining to the instance
        self.last_name = last_name
        self.pay = pay
        self.email = first_name.replace(" ", ".").lower() + "." + last_name.replace(" ", ".").lower() + "@company.com" #creates company email, along with some formatting

        Employee.num_of_emps += 1 #This will make sure that the counting token for the total number of employees are updated across all the instances of Employee
    
    def full_name(self): #having the method associated with an instance guarantees that the object-name is always passed as an argument, hence the need to "self"
        return f'{self.first_name} {self.last_name}'
    
    def apply_raise (self):
        self.pay = int(self.pay * self.raise_amount) #calling the class variable through the instance(self.raise_amount), and not the class in general(Employee.raise_amount)
        # This will allow the instance to choose between instance-specific variable of the class variable, or the class variable set across all instances of Employee
        # See more on this below (Keep an eye out for .raise_amount)

    #Introducing "class methods":    
    @classmethod #"Decorator" - A function that adds to a function - Read this: https://www.programiz.com/python-programming/decorator
    def set_raise_amount(cls, amount): #cls == class, and is a higher-level parameter than self (class>instance) - cannot use "class" as it already is a keyword
        cls.raise_amount = amount
    
    @classmethod #Creating an alternative constructor where we can enter a string to define an instance
    def from_string_construct_instance(cls, emp_str):
        first_name, last_name, pay = emp_str.split(",") # Parses the string and creates the constructing arguments (from a .csv in this case)
        return cls(first_name, last_name, pay) #initializes the constructor using the arguments from the string
    
    #Introducing "static methods": The do not take any class-related arguments, but are in some way logically connected to the class
    @staticmethod
    def is_workday(day):
        if day.weekday() in [5, 6]: # the .weekday-method sets Monday == 0 and Sunday == 6
            return False
        return True
    #Doesn't contain any cls. or self. ! Hence: "Static"

#Class vs. instance variable: The call will always check for the variable in 
#(1) the instance, 
#(2) the class of the instance and
#(3) any class that the class of the instance inherits from
#which means that the class variable can be called as an instance variable (self.variable) or class variable (class.variable)

print(f"num_of_emps before creating any instances: {Employee.num_of_emps}")

emp_1 = Employee("Ole Martin", "Bøe Stokke", 40) #instance 1 of the Employee class
emp_2 = Employee("Stomp", "Stomperud", 50) #instance 2 of the Employee class

# print(emp_1.full_name()) #Calling the full_name method of the Employee class using the instance variables of emp_1
# print(Employee.full_name(emp_1)) #This is what actually happens (remember that emp_1 = lots of stuff and read out the whole line)
# Pay attention to the fact that any call relying on an instance variable HAS to contain a reference to the specific instance (class alone is not enough)

print(emp_1.__dict__) #prints the dictionary of the instance emp_1
print(Employee.__dict__) #prints the dictionary of the class Employee

emp_1.raise_amount = 1.06 #sets a new instance of the class variable, making it an instance-specific variable
# to see the effects:

print(Employee.raise_amount,"|", emp_1.raise_amount, "|", emp_2.raise_amount)
# if the class method apply_raise called the raise_amount as Employee.raise_amount - It would still be using 1.04 instad of 1.06 for emp_1!
# This will also allow any sub-class to override the class variable, should we want it to

Employee.set_raise_amount(1.05) #Calling the class-method

print(Employee.raise_amount,"|", emp_1.raise_amount, "|", emp_2.raise_amount)
# emp_1.raise_amount still set to its instance-specific amount
# setting instance-specific amounts thus has it's ups and downs with regards to keeping class variables "open"
# could in this case be solved with an if-statement checking self. with cls.

#testing the alternative constructor
string_of_information = "Snurre,Sprett,45"

emp_3 =  Employee.from_string_construct_instance(string_of_information)
print(emp_3.__dict__)
print(f"num_of_emps after creating instances: {Employee.num_of_emps}")

#Checking the static method
import datetime
print(Employee.is_workday(datetime.date.today()))