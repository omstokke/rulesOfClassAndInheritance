from random import randint #Equal dist., don't feed it kwargs directly
from random import choice
import tablesOfStuff as table

class Person:

    evo_stage = 0
    class_token = 0
    action_count = 0
    
    def __init__(self, name, occupation, hobby):
        self.name = name
        self.occupation = occupation
        self.hobby = [hobby.lower()]

    def __init_subclass__(cls):
        cls.evo_stage += 1
        cls.class_token = 0
    
    def add_hobby(self, new_hobby):
        if new_hobby.lower() not in self.hobby:
            self.hobby.append(new_hobby.lower())
    
    def remove_hobby(self, old_hobby):
        if old_hobby.lower() in self.hobby:
            self.hobby.remove(old_hobby.lower())

    @classmethod
    def incr_class_token(cls, amount):
        cls.class_token += amount

    @classmethod
    def incr_action_count(cls, amount):
        cls.action_count += amount
    
    @classmethod
    def decrease_class_token(cls, amount):
        cls.class_token -= amount

    @classmethod
    def decrease_action_count(cls, amount):
        cls.action_count -= amount
    
    # Alternative constructor with string/.csv
    @classmethod
    def from_string(cls, stringperson):
        name, occupation, hobby = stringperson.split(",")
        return cls(name, occupation, hobby)
    
    #Alternative constructor from array-list
    @classmethod
    def from_list(cls, personlist):
        name, occupation, hobby = personlist
        return cls(name, occupation, hobby)


class Infant(Person):
    
    def cry(cls):
        cls.incr_class_token(5)
        cls.incr_action_count(1)
        print("""
            Uwwaaaahhhh!
        """)
    
    def wail(cls):
        cls.incr_class_token(7)
        cls.incr_action_count(1)
        print("""
            UWWAAAAAAAH!
        """)

    def shits_and_giggles(cls, self):
        if randint(0, cls.class_token*2) > cls.class_token:
            cls.incr_class_token(10)
            cls.incr_action_count(2)
            print(f"""
            *UWWWAAAHEUPFFFRRRTTTT!*
            How does {self.hobby[0]} all day make {self.name}
            produce shit with this colour?
            """)
        else:
            cls.incr_class_token(10)
            cls.incr_action_count(3)
            print(f"""
            UWWWAAAHEURFBLEURFPFFFRRRTTTT!
            It ain't fun 'til it comes out
            ...of both ends.
            {self.name} smells like a tired alcoholic""")  


class Toddler(Infant):
    
    bribed = 0

    def bribe_with_choc(cls, self):
        cls.incr_class_token(10)
        cls.incr_action_count(1)
        self.bribed += 1
        print(f"""
        You give {self.name}
        half a chocolate:
        'Choclet!'
        """)

    def tickles(cls):
        cls.incr_class_token(3)
        cls.incr_action_count(1)
        print("""
        Teehee""")

    #Shits and giggles
    def shits_and_giggles(cls, self):
        if (randint(0, cls.class_token*2) > cls.class_token) and cls.bribed < 3:
            cls.incr_class_token(5)
            cls.incr_action_count(2)
            print(f"""
            *UWWWAAAHEUPFFFRRRTTTT!*
            How does {self.hobby[0]} all day make {self.name}
            produce shit with this colour?
            """)
        elif cls.bribed >= 2:
            cls.incr_class_token(7)
            cls.incr_action_count(3)
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

    def talk(cls, self):
        cls.incr_action_count(5)
        print(f"""
        The {choice(table.animals_table).lower()} in {choice(table.table_of_places)} are {choice(table.adjectives_table)}.
        
        ...
        
        I like {choice(table.animals_table).lower()}!
        """)
    
    def talk_some_more(cls, self):
        cls.incr_action_count(5)
        print(f"""
        Give. Me. {choice(table.animals_table).capitalize()}.
        GIVE. ME. {choice(table.animals_table).upper()}!
        """)
    
    def rational_Kid(cls, self):
        cls.incr_action_count(5)
        print(f"""
        All the {choice(table.adjectives_table)} {choice(table.animals_table).lower()}
        - in {choice(table.table_of_places)} -
        they're mine now.
        """)



class EmoTeen(Kid):
   
    def cry(cls, self):
        cls.incr_class_token(5)
        cls.incr_action_count(2)
        print(f"""
        *{self.name} starts installing a tripod
         - This fucker is readying a web-cam - *
        No wounds can match the hurt inside!
        Shallow cuts only makes me cry-e-yee
        Cruel, world - Goodbyeeee!
        Uwwaaaahhhh!
         - What a cunt -
        """)

    def dumb_response_converter(cls, message):
        output = "No - You "
        for char in message:
            if char == " ":
                output += " "          
            elif cls.class_token >= (randint(0, cls.class_token * 2)):
                output += char.lower()
            else:
                output += char.upper()
        return output

    def teen_responds_to_important_things():
        pass


class Youth(EmoTeen):
    pass


class Adult_Functioning(Youth):
    pass


class Alcoholic_Functioning(Adult_Functioning):
    pass


class Oldster(Alcoholic_Functioning):
    
    def derp(self):
        self.action_count += 1
        self.class_token += 1
        print("What? Nothing.")


class Demented_Old_Bat(Oldster):
    pass