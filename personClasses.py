from random import randint #Equal dist., don't feed it kwargs directly
from random import choice
import personTables as table

#this is the base/abstract class
class Person:

    #The Person Sim follows a stricthierarchy of class-progression, so I used the opportunity to track certain properties
    # as class-attributes, and others as instance-attributes
    # These keep track of which evolutionary stage in the class-hierarchy the simulation-instance (player) is at
    # and counts how many actions it has taken during the total course of its evolution, across classes
    evo_stage = 0
    action_count = 0
    
    #Constructor
    def __init__(self, name, hobby): #For every new instance, this happens
        self.name = name
        self.hobby = hobby
        self.evo_points = 0
        self.evo_check = 50                                                             #This creates the limit of evo-points/EXP to check for before evolving (see evolve-method, below)
        self.functionlist = [method for method in dir(self.__class__)                   #This constructs the "menu" for choosing actions in the simulator
        if callable(getattr(self.__class__, method)) and method not in dir(Person)]     # but it removes the "abstract"-methods from the Person-class

    def __init_subclass__(cls): #For every new subclass(not instance), the evo_stage-counter is updater with a +1
        cls.evo_stage += 1

    def incr_evo_points(self, amount):
        self.evo_points += amount       #This functions adds evo_points/EXP and
        self.evolve()                   #runs the function to check for whether the instance should evolve to the next class or not

    def incr_action_count(self, amount):
        self.__class__.action_count += amount   # This functions adds action counts, and
        self.evolve()                           # runs the function to check for whether the instance should evolve to the next class or not

    #This is the method that lets the instance evolve, seemingless without creating a new instance (not necessarily true, but it looks seamless)
    def evolve(self):
        if self.evo_points >= self.evo_check or self.action_count >= self.evo_stage * 10:   # Checks if the instance has acquired enough EXP or action counts
            subclass_list = self.__class__.__subclasses__()                                 # Finds the possible subclasses to inherit the current class of the instance - Yet NOT a class-method
            if len(subclass_list) == 1:                                                     # If there's only 1 subclass: Ask if you want to evolve into the next class
                choice = input(f"\n    Would you like for {self.name} to evolve into a {subclass_list[0].__name__}? y/n: ").lower()
                if choice == "y":
                    self.__class__ = subclass_list[0]
                    return self.__class__.__init__(self, self.name, self.hobby)
                else:
                    print("Well, whatever you chose - It wasn't 'y'")
            elif len(subclass_list) == 0:                                                   #If there are no further subclasses - Pass
                pass
            else:                                                                           #If there are several subclass: Ask which one you want to evolve into
                for sub in subclass_list:
                    print(f"{sub.__name__}: {subclass_list.index(sub)}")
                choice = int(input("Choose your next evolutionary step from the numbers given above, or (n)ot to evolve: "))
                if choice in range(len(subclass_list)):
                    self.__class__ = subclass_list[choice]
                    return self.__class__.__init__(self, self.name, self.hobby)
                else:
                    print("Well, whatever you chose - It wasn't one of the numbers listed")

    #For future development: Methods to decrea evo-points and action counts
    #Not used in the current version of Person Sim
    def decrease_evo_points(self, amount):
        self.evo_points -= amount

    def decrease_action_count(self, amount):
        self.__class__.action_count -= amount

    #Class method: Alternative constructor, creating instance from a list-object
    @classmethod
    def from_list(cls, personlist):
        name, hobby = personlist
        return cls(name, hobby)


class Infant(Person):

    def __init__(self, name, hobby):
        super().__init__(name, hobby)   #Gets the common instance-attributes from the super
        self.evo_check += 10            #Ups the limit for evolution by 10 points
        
    def cry(self):
        print("""
    Uwwaaaahhhh!
        """)
        self.incr_action_count(1)       #The acitons count increases are placed before the evo-points as they shouldn't too ofte hit their limit before the evo-points
        self.incr_evo_points(5)         #The evo-points are allways increased last, as they also call on the evolve-method, making sure the action is completed before evolving


    def shits_and_giggles(self):        #Basic function for an infant - Also plays around with the instance-attributes
        if randint(0, self.evo_points*2) > self.evo_points:
            print(f"""
    *UWWWAAAHEUPFFFRRRTTTT!*
    How does {self.hobby.lower()} all day make {self.name}
    produce anything with this colour?
            """)
            self.incr_evo_points(10)
            self.incr_action_count(2)
        else:
            print(f"""
    UWWWAAAHEURFBLEURFPFFFRRRTTTT!
    It ain't fun 'til it comes out
    ...of both ends.
    {self.name} smells like a factory
            """)
            self.incr_evo_points(10)
            self.incr_action_count(3) 


class Toddler(Infant):
    
    def __init__(self, name, hobby):
        super().__init__(name, hobby)
        self.evo_check += 10
        self.bribed = 0                 #Instance-specific attribute new from this subclass of Person
        self.functionlist.remove('cry') #Removes 'cry' from the action-menu


    def bribe_with_choc(self):
        self.bribed += 1
        print(f"""
    You give {self.name} half a chocolate:
    'Choclet!'
        """)
        self.incr_evo_points(10)
        self.incr_action_count(1)


    def shits_and_giggles(self):
        if (randint(0, self.evo_points*2) > self.evo_points) and self.bribed < 3:
            print(f"""
    *UWWWAAAHEUPFFFRRRTTTT!*
    How does {self.hobby.lower()} all day make {self.name}
    produce anything with this colour?
            """)
            self.incr_evo_points(5)
            self.incr_action_count(2)
        elif self.bribed >= 2:
            print(f"""
    UWWWAAAHEURFBLEURFPFFFRRRTTTT!
    It ain't fun 'til it comes out
    ...of both ends.
    {self.name} smells like a tired alcoholic""")
            self.incr_evo_points(7)
            self.incr_action_count(3)
        else:
            print("""
    Shit in, shit out - Give it the Stuff of Sugar!
            """)  


class Kid(Toddler): #For the most part, this class is used to play around with functions and lists in print-statements

    def __init__(self, name, hobby):
        super().__init__(name, hobby)
        self.evo_check += 10
        self.functionlist.remove('bribe_with_choc')
        self.functionlist.remove('shits_and_giggles')


    def talk(self):
        print(f"""
    The {choice(table.animals_table).lower()} in {choice(table.table_of_places)} are {choice(table.adjectives_table)}.
        
    ...
        
    I like {choice(table.animals_table).lower()}!
        """)
        self.incr_action_count(1)
    
    def talk_some_more(self):
        print(f"""
    Give. Me. {choice(table.animals_table).capitalize()}.
    GIVE. ME. {choice(table.animals_table).upper()}!
        """)
        self.incr_action_count(1)
    
    def rational_Kid(self):
        print(f"""
    All the {choice(table.adjectives_table)} {choice(table.animals_table).lower()}
    - in {choice(table.table_of_places)} -
    they're mine now.
        """)
        self.incr_action_count(1)


class EmoTeen(Kid):

    def __init__(self, name, hobby):        #Redefines the menu alot, also sorts it
        super().__init__(name, hobby)
        self.evo_check += 10
        self.functionlist.remove('talk')
        self.functionlist.remove('talk_some_more')
        self.functionlist.remove('rational_Kid')
        self.functionlist.append('cry')
        self.functionlist.sort()
        

    def cry(self):
        print(f"""
    *{self.name} starts installing a tripod
     - Your subject is readying a web-cam - *
    No wounds can match the hurt inside!
    Shallow cuts only makes me cry-e-yee
    Cruel, world - Goodbyeeee!
    Uwwaaaahhhh!
     - What a talented young thing -
        """)
        self.incr_evo_points(5)
        self.incr_action_count(2)

    def dumb_response(self):
        message = input(f"""
    Command {self.name} what to do: """)
        output = "No - You "
        for char in message:
            if char == " ":
                output += " "          
            elif self.evo_points >= (randint(0, self.evo_points * 2)):
                output += char.lower()
            else:
                output += char.upper()
        print(f"""
    {output}!
        """)
        self.incr_evo_points(5)
        self.incr_action_count(1)

    def important_things(self):
        print(f"""
    Who even ARE YOU?! 
    Don't you know that {choice(table.animals_table).lower()} in {choice(table.smartass_table)} are {choice(table.adjectives_table2)} due to {choice(table.table_of_bad_things)}?
        """)
        self.incr_evo_points(5)
        self.incr_action_count(2)


class Youth(EmoTeen):
    
    def __init__(self, name, hobby):
        super().__init__(name, hobby)
        self.evo_check += 10
        self.derp_count = 0
        self.functionlist.remove('cry')
        self.functionlist.remove('dumb_response')


    def important_things(self):
        print(f"""
    Did you know that {choice(table.animals_table).lower()} in {choice(table.smartass_table)} are {choice(table.adjectives_table2)} due to {choice(table.table_of_bad_things)}?
        """)
        self.incr_evo_points(5)
        self.incr_action_count(1)

    def derp(self):
        self.derp_count += 1
        derp_hit = randint(0, self.derp_count)
        if derp_hit == self.derp_count:
            print(f"""
    {choice(table.small_table)}
        """)
        else:
            print("""
    What? Nothing.
        """)
        self.incr_evo_points(10)
        self.incr_action_count(1)
        

class Adult(Youth):

    def __init__(self, name, hobby):
        super().__init__(name, hobby)
        self.evo_check += 10
        self.derp_count = 0
        

    def derp(self):
        self.derp_count += 1
        derp_hit = randint(0, self.derp_count)
        if derp_hit == self.derp_count:
            print(f"""
    {choice(table.small_table)}
        """)
        else:
            print(f"""
    *{self.name} stares off into the distance*
        ....
            ....
                ....
                    
                    What?            
            """)
        self.incr_evo_points(10)
        self.incr_action_count(1)


class Oldster(Adult): #The last stage

    def __init__(self, name, hobby):
        super().__init__(name, hobby)
        self.evo_check += 10
        self.functionlist.remove('important_things')

    def derp(self):
        print(f"""
        {choice(table.animals_table)} are {choice(table.adjectives_table)}!
        {choice(table.adjectives_table).capitalize()} and {choice(table.adjectives_table)} and {choice(table.adjectives_table)}!
        But some {choice(table.animals_table).lower()} are {choice(table.adjectives_table)}.
        Also - In {choice(table.smartass_table)}...
        {choice(table.small_table)}
        {choice(table.animals_table).upper()}!!!
        """)
        self.incr_evo_points(10)
        self.incr_action_count(1)