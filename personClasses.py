from random import randint #Equal dist., don't feed it kwargs directly
from random import choice
import tablesOfStuff as table

class Person:

    evo_stage = 0
    action_count = 0
    
    def __init__(self, name, occupation, hobby): #For every new instance, this happens
        self.name = name
        self.occupation = occupation
        self.hobby = hobby
        self.evo_points = 0
        self.evo_check = 50

    def __init_subclass__(cls): #For every new subclass(not instance), this happens
        cls.evo_stage += 1

    def incr_evo_points(self, amount):
        self.evo_points += amount
        self.evolve()

    def incr_action_count(self, amount):
        self.__class__.action_count += amount
        self.evolve()

    def evolve(self):
        if self.evo_points >= self.evo_check or self.action_count >= self.evo_stage * 10:
            choice = input(f"Would you like for {self.name} to evolve into a {self.__class__.__subclasses__()[0].__name__}? y/n: ").lower()
            if choice == "y":
                self.__class__ = self.__class__.__subclasses__()[0]
                return self.__class__.__init__(self, self.name, self.occupation, self.hobby)
            else:
                print("Well, whatever you chose - It wasn't 'y'")
        
    def decrease_evo_points(self, amount):
        self.evo_points -= amount

    def decrease_action_count(self, amount):
        self.__class__.action_count -= amount

    #Alternative constructor from array-list
    @classmethod
    def from_list(cls, personlist):
        name, occupation, hobby = personlist
        return cls(name, occupation, hobby)

class Infant(Person):

    def __init__(self, name, occupation, hobby):
        super().__init__(name, occupation, hobby)
        self.evo_check += 10 #Ups the limit for evolution
        
    def cry(self):
        self.incr_evo_points(5)
        self.incr_action_count(1)
        print("""
            Uwwaaaahhhh!
        """)
    
    def wail(self):
        self.incr_evo_points(7)
        self.incr_action_count(1)
        print("""
            UWWAAAAAAAH!
        """)

    def shits_and_giggles(self):
        if randint(0, self.evo_points*2) > self.evo_points:
            self.incr_evo_points(10)
            self.incr_action_count(2)
            print(f"""
            *UWWWAAAHEUPFFFRRRTTTT!*
            How does {self.hobby} all day make {self.name}
            produce shit with this colour?
            """)
        else:
            self.incr_evo_points(10)
            self.incr_action_count(3)
            print(f"""
            UWWWAAAHEURFBLEURFPFFFRRRTTTT!
            It ain't fun 'til it comes out
            ...of both ends.
            {self.name} smells like a tired alcoholic""")  


class Toddler(Infant):
    
    def __init__(self, name, occupation, hobby):
        super().__init__(name, occupation, hobby)
        self.evo_check += 10
        self.bribed = 0
    

    def bribe_with_choc(self):
        self.incr_evo_points(10)
        self.incr_action_count(1)
        self.bribed += 1
        print(f"""
        You give {self.name}
        half a chocolate:
        'Choclet!'
        """)

    def tickles(self):
        self.incr_evo_points(3)
        self.incr_action_count(1)
        print("""
        Teehee
        """)

    #Shits and giggles
    def shits_and_giggles(self):
        if (randint(0, self.evo_points*2) > self.evo_points) and self.bribed < 3:
            self.incr_evo_points(5)
            self.incr_action_count(2)
            print(f"""
            *UWWWAAAHEUPFFFRRRTTTT!*
            How does {self.hobby} all day make {self.name}
            produce shit with this colour?
            """)
        elif self.__class__.bribed >= 2:
            self.incr_evo_points(7)
            self.incr_action_count(3)
            print(f"""
            UWWWAAAHEURFBLEURFPFFFRRRTTTT!
            It ain't fun 'til it comes out
            ...of both ends.
            {self.name} smells like a tired alcoholic""") 
        else:
            print("""
            Shit in, shit out - Give it the Stuff of Sugar!
            """)  


class Kid(Toddler):

    def __init__(self, name, occupation, hobby):
        super().__init__(name, occupation, hobby)
        self.evo_check += 10

    def talk(self):
        self.incr_action_count(5)
        print(f"""
        The {choice(table.animals_table).lower()} in {choice(table.table_of_places)} are {choice(table.adjectives_table)}.
        
        ...
        
        I like {choice(table.animals_table).lower()}!
        """)
    
    def talk_some_more(self):
        self.incr_action_count(5)
        print(f"""
        Give. Me. {choice(table.animals_table).capitalize()}.
        GIVE. ME. {choice(table.animals_table).upper()}!
        """)
    
    def rational_Kid(self):
        self.incr_action_count(5)
        print(f"""
        All the {choice(table.adjectives_table)} {choice(table.animals_table).lower()}
        - in {choice(table.table_of_places)} -
        they're mine now.
        """)


class EmoTeen(Kid):

    def __init__(self, name, occupation, hobby):
        super().__init__(name, occupation, hobby)
        self.evo_check += 10

    def cry(self):
        self.incr_evo_points(5)
        self.incr_action_count(2)
        print(f"""
        *{self.name} starts installing a tripod
         - This fucker is readying a web-cam - *
        No wounds can match the hurt inside!
        Shallow cuts only makes me cry-e-yee
        Cruel, world - Goodbyeeee!
        Uwwaaaahhhh!
         - What a cunt -
        """)

    def dumb_response_converter(self, message):
        output = "No - You "
        for char in message:
            if char == " ":
                output += " "          
            elif self.evo_points >= (randint(0, self.evo_points * 2)):
                output += char.lower()
            else:
                output += char.upper()
        return output

    def teen_responds_to_important_things(self):
        self.incr_evo_points(5)
        self.incr_action_count(2)
        print(f"""
        Who even ARE YOU?!

        Don't you know that {choice(table.animals_table).lower()} in {choice(table.smartass_table)} are {choice(table.adjectives_table2)} due to {choice(table.table_of_bad_things)}?
        """)


class Youth(EmoTeen):
    
    def __init__(self, name, occupation, hobby):
        super().__init__(name, occupation, hobby)
        self.evo_check += 10


class Adult_Functioning(Youth):

    def __init__(self, name, occupation, hobby):
        super().__init__(name, occupation, hobby)
        self.evo_check += 10


class Alcoholic_Functioning(Adult_Functioning):

    def __init__(self, name, occupation, hobby):
        super().__init__(name, occupation, hobby)
        self.evo_check += 10


class Oldster(Alcoholic_Functioning):

    def __init__(self, name, occupation, hobby):
        super().__init__(name, occupation, hobby)
        self.evo_check += 10

    def derp(self):
        self.incr_action_count(1)
        self.incr_evo_points(1)
        print("What? Nothing.")


class Demented_Old_Bat(Oldster):

    def __init__(self, name, occupation, hobby):
        super().__init__(name, occupation, hobby)
        self.evo_check += 10