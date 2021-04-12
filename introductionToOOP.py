#To build and expand upon the tutorials given by Mike and Mosh, Corey Schafer explains in more detail
#Addendum: Trust in Corey - He explains the stuff good-like, and with a nice drawl

#The following sort of deviates from the rule of trying not to copy too much, but the explanations from Corey are too good to be simplified and messed around with.
#The other programs in this repository will be more in the geist of the rules.
#That being said - The following have been expanded upon a bit, where I felt comfortable with it.
#I also need these notes for some more original stuff later on.

#Data and functions associated with a specific class are called "attributes" and "methods"

class Employee:
    
    raise_amount = 1.04 #Class variable: Variables shared between all instances of a class
    num_of_emps = 0

    def __init__(self, first_name, last_name, pay): #the "self" is replaced by the instance /object-name
        self.first_name = first_name #attributes of the class, defining the instance variables only pertaining to the instance
        self.last_name = last_name
        self.pay = pay
        Employee.num_of_emps += 1 #This will make sure that the counting token for the total number of employees are updated across all the instances of Employee


    @property #the property decorator lets us define a method and call it as an attribute (self.email and not self.email())
    def email(self):
        if self.first_name is None or self.last_name is None: #Seeing as I added a deleter which might trigger a None-value, below
            return None
        else:
            return f'{self.first_name.replace(" ", ".").lower()}.{self.last_name.replace(" ", ".").lower()}@company.com' #creates company email, along with some formatting


    @property #the property decorator lets us define a method and call it as an attribute (self.full_name and not self.full_name())
    def full_name(self): #having the method associated with an instance guarantees that the object-name is always passed as an argument, hence the need to "self"
        if self.first_name is None or self.last_name is None:
            return None
        else:
            return f'{self.first_name} {self.last_name}'

    
    @full_name.setter #This is a setter - It let's you define the previous method-cum-attribute backwards, and updates its components too (full_name = first_name + last_name)
    def full_name(self, new_name): #Should be able to handle names longer than len=2, which means a default is set as last_name=the last name, and everything else as first_name
        new_name = new_name.split(" ")
        self.last_name = new_name[-1]
        new_first_name = ""
        for i in range(len(new_name)-1):
            new_first_name += f"{new_name[i]} " #Adds every name but the last to new_first_name with a space following
        self.first_name = new_first_name.rstrip() #Set the new first_name, stripping the ending whitespace


    @full_name.deleter #This is a deleter - It let's you delete a set attribute/property-method, and updates its components too (full_name = first_name + last_name)
    def full_name(self):
        print(f"You are deleting the names of {self.full_name}")
        self.last_name = None
        self.first_name = None


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

# print(emp_1.full_name) #Calling the full_name method of the Employee class using the instance variables of emp_1
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

#Testing the static method
import datetime
print(Employee.is_workday(datetime.date.today()))

class Developer(Employee): #Defines a class of a class - A sub-class - which inherits all the methods and attributes of the parent class
    raise_amount = 1.10  # Re-defines the class variable to a new value specific for this sub-class - Does not affect the parent class (Employee)

    def __init__(self, first_name, last_name, pay, programming_language): # a new constructor in order to fix Programming Language as an attribute to our Devs
        super().__init__(first_name, last_name, pay) #fetches the common factor attributes from Employee, letting the parent class handle those arguments for the Dev-instances
        # Employee.__init__(self, first, last, pay) can also be done, but this only works with single step inheritance, and is not maintanable for multiple inheritance (subs of subs)
        self.programming_language = programming_language

class Manager (Employee):
    
    raise_amount = 1.11

    def __init__(self, first_name, last_name, pay, employees=None): #Never pass mutable data types as a default argument - Hence the following if-statement
        super().__init__(first_name, last_name, pay)
        if employees is None:
            self.employees =  [] # sets the mutable argument we normally would use in an independant variable
        else:
            self.employees = employees
    
    def add_employee_to_manager_list(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee_from_manager_list(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_list_of_employees(self):
        for emp in self.employees:
            print(f"{self.employees.index(emp) + 1} --- {emp.full_name}")

dev_1 = Developer("Ole Martin", "Bøe Stokke", 40, "Python")
dev_2 = Developer("Tor", "Haakonsen", 110, "Java Script")
emp_1 = Employee("Borri Bork", "Boerresen", 45)
mgr_1 = Manager("Snurre", "Sprett", 60)

# print(help(Developer)) #the help-function visualizes - amongst other things - the method resolution order of the sub-class "Developer"

#Testing the Manager methods, and inheritance from Employee
print(mgr_1.email)
mgr_1.add_employee_to_manager_list(dev_1)
mgr_1.print_list_of_employees()
mgr_1.add_employee_to_manager_list(emp_1)
mgr_1.remove_employee_from_manager_list(dev_1)
mgr_1.add_employee_to_manager_list(dev_1)
mgr_1.add_employee_to_manager_list(dev_2)
mgr_1.print_list_of_employees()

print(isinstance(mgr_1, Manager)) #Checks if the value is an instance of a given class - mgr_1 will return True on Manager and Employee, but not Developer
print(issubclass(Developer, Employee)) #Check if a given class is a sub-class of another

#Some notes on special methods
# Double-underscored ("dunder")
# Read this: https://docs.python.org/3/reference/datamodel.html#basic-customization
#Some common ones are: 
class Teacher(Employee):

    def __init_subclass__(self): #New dunder - https://docs.python.org/3/reference/datamodel.html#customizing-class-creation
        pass

    def __repr__(self): #Used for debugging and logging and whatever - Simple representation of the object seen by other developers
        return f"Teacher('{self.first_name}', '{self.last_name}', {self.pay})"

    def __str__(self): #Readable representation of the object, used as a display to the end-user
        return f"{self.full_name} - {self.email}"
    
    def __add__(self, other): #Let's you define how the class adds self and other by calling self, for example adding and returning two employees
        return self.pay + other.pay

tch_1 = Teacher("Sue", "Stolit", 55)
print(repr(tch_1))
print(str(tch_1))

# str will be prio over repr, so if they are both defined, str will be resolved first. A print-statement of the instance will show str > repr > strange memory object thing
# that is : print(tch_1)

#Testing the __add__ of our Teacher - Remember that emp_1 doesn't have this dunder, so only work when Teacher is the self
print(tch_1 + emp_1)
print(tch_1.__add__(emp_1))

#Testing the deleter of Employee.full_name
del tch_1.full_name
print(tch_1.first_name)
print(tch_1.email)
print(tch_1.full_name)

#Poor Susan gets her name back; Testing the setter of Employee.full_name - From Susan Stolit to Susan Sto Helit
tch_1.full_name = "Susan Sto Helit"
print(tch_1.first_name)
print(tch_1.email)
print(tch_1.full_name)
