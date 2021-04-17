from random import randint #Equal dist., don't feed it kwargs directly
from random import choice
import tablesOfStuff as table

class Person:

    evo_stage = 0
    action_count = 0
    evo_construct = []
    evo_stages = {
        0: Person.from_list(evo_construct)
        1: Infant.from_list(evo_construct)
        2: Toddler.from_list(evo_construct)
        3: Kid.from_list(evo_construct)
        4: Tween.from_list(evo_construct)
        5: Youth.from_list(evo_construct)
        6: Adult_Functioning.from_list(evo_construct)
        7: Alcoholic_Functioning.from_list(evo_construct)
        8: Oldster.from_list(evo_construct)
        9: Demented_Old_Bat.from_list(evo_construct)
    }
    
    def __init__(self, name, occupation, hobby):
        self.name = name
        self.occupation = occupation
        self.hobby = [hobby.lower()]
        self.evo_points = 0
        self.evo_check = 50
        cls.evo_construct = [name, occupation, hobby.lower()]

    def __init_subclass__(cls):
        cls.evo_stage += 1
    
    def add_hobby(self, new_hobby):
        if new_hobby.lower() not in self.hobby:
            self.hobby.append(new_hobby.lower())
    
    def remove_hobby(self, old_hobby):
        if old_hobby.lower() in self.hobby:
            self.hobby.remove(old_hobby.lower())

    def incr_evo_points(self, amount):
        self.evo_points += amount
        if self.evo_points >= self.evo_check:
            pass

    def incr_action_count(self, amount):
        self.__class__.action_count += amount
    
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
        self.evo_check += 1 #Ups the limit for evolution
        
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
        if randint(0, self.__class__.evo_points*2) > self.__class__.evo_points:
            self.incr_evo_points(10)
            self.incr_action_count(2)
            print(f"""
            *UWWWAAAHEUPFFFRRRTTTT!*
            How does {self.hobby[0]} all day make {self.name}
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
        self.evo_check = 80

    bribed = 0

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
        if (randint(0, self.__class__.evo_points*2) > self.__class__.evo_points) and self.__class__.bribed < 3:
            self.incr_evo_points(5)
            self.incr_action_count(2)
            print(f"""
            *UWWWAAAHEUPFFFRRRTTTT!*
            How does {self.hobby[0]} all day make {self.name}
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
        self.evo_check = 80

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
        self.evo_check = 80

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
            elif self.__class__.evo_points >= (randint(0, self.__class__.evo_points * 2)):
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
        self.evo_check = 80


class Adult_Functioning(Youth):

    def __init__(self, name, occupation, hobby):
        super().__init__(name, occupation, hobby)
        self.evo_check = 80


class Alcoholic_Functioning(Adult_Functioning):

    def __init__(self, name, occupation, hobby):
        super().__init__(name, occupation, hobby)
        self.evo_check = 80


class Oldster(Alcoholic_Functioning):

    def __init__(self, name, occupation, hobby):
        super().__init__(name, occupation, hobby)
        self.evo_check = 80

    def derp(self):
        self.incr_action_count(1)
        self.incr_evo_points(1)
        print("What? Nothing.")


class Demented_Old_Bat(Oldster):

    def __init__(self, name, occupation, hobby):
        super().__init__(name, occupation, hobby)
        self.evo_check = 80