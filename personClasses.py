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

    def incr_class_token(self, amount):
        self.__class__.class_token += amount

    def incr_action_count(self, amount):
        self.__class__.action_count += amount
    
    def decrease_class_token(self, amount):
        self.__class__.class_token -= amount

    def decrease_action_count(self, amount):
        self.__class__.action_count -= amount
    
    #Alternative constructor from array-list
    @classmethod
    def from_list(cls, personlist):
        name, occupation, hobby = personlist
        return cls(name, occupation, hobby)


class Infant(Person):
    
    def cry(self):
        self.__class__.incr_class_token(self, 5)
        self.__class__.incr_action_count(self, 1)
        print("""
            Uwwaaaahhhh!
        """)
    
    def wail(self):
        self.__class__.incr_class_token(self, 7)
        self.__class__.incr_action_count(self, 1)
        print("""
            UWWAAAAAAAH!
        """)

    def shits_and_giggles(self):
        if randint(0, self.__class__.class_token*2) > self.__class__.class_token:
            self.__class__.incr_class_token(10)
            self.__class__.incr_action_count(2)
            print(f"""
            *UWWWAAAHEUPFFFRRRTTTT!*
            How does {self.hobby[0]} all day make {self.name}
            produce shit with this colour?
            """)
        else:
            self.__class__.incr_class_token(10)
            self.__class__.incr_action_count(3)
            print(f"""
            UWWWAAAHEURFBLEURFPFFFRRRTTTT!
            It ain't fun 'til it comes out
            ...of both ends.
            {self.name} smells like a tired alcoholic""")  


class Toddler(Infant):
    
    bribed = 0

    def bribe_with_choc(self):
        self.__class__.incr_class_token(10)
        self.__class__.incr_action_count(1)
        self.bribed += 1
        print(f"""
        You give {self.name}
        half a chocolate:
        'Choclet!'
        """)

    def tickles(self):
        self.__class__.incr_class_token(3)
        self.__class__.incr_action_count(1)
        print("""
        Teehee""")

    #Shits and giggles
    def shits_and_giggles(self):
        if (randint(0, self.__class__.class_token*2) > self.__class__.class_token) and self.__class__.bribed < 3:
            self.__class__.incr_class_token(5)
            self.__class__.incr_action_count(2)
            print(f"""
            *UWWWAAAHEUPFFFRRRTTTT!*
            How does {self.hobby[0]} all day make {self.name}
            produce shit with this colour?
            """)
        elif self.__class__.bribed >= 2:
            self.__class__.incr_class_token(7)
            self.__class__.incr_action_count(3)
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

    def talk(self):
        self.__class__.incr_action_count(5)
        print(f"""
        The {choice(table.animals_table).lower()} in {choice(table.table_of_places)} are {choice(table.adjectives_table)}.
        
        ...
        
        I like {choice(table.animals_table).lower()}!
        """)
    
    def talk_some_more(self):
        self.__class__.incr_action_count(5)
        print(f"""
        Give. Me. {choice(table.animals_table).capitalize()}.
        GIVE. ME. {choice(table.animals_table).upper()}!
        """)
    
    def rational_Kid(self):
        self.__class__.incr_action_count(5)
        print(f"""
        All the {choice(table.adjectives_table)} {choice(table.animals_table).lower()}
        - in {choice(table.table_of_places)} -
        they're mine now.
        """)


class EmoTeen(Kid):
   
    def cry(self):
        self.__class__.incr_class_token(self, 5)
        self.__class__.incr_action_count(self, 2)
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
            elif self.__class__.class_token >= (randint(0, self.__class__.class_token * 2)):
                output += char.lower()
            else:
                output += char.upper()
        return output

    def teen_responds_to_important_things(self):
        self.__class__.incr_class_token(5)
        self.__class__.incr_action_count(2)
        print(f"""
        Who even ARE YOU?!

        Don't you know that {choice(table.animals_table).lower()} in {choice(table.smartass_table)} are {choice(table.adjectives_table2)} due to {choice(table.table_of_bad_things)}?
        """)


class Youth(EmoTeen):
    
    def __init__(self, name, occupation, hobby, cigarettes):
        super().__init__(name, occupation, hobby)
        self.cigarettes = int(cigarettes)


class Adult_Functioning(Youth):
    pass


class Alcoholic_Functioning(Adult_Functioning):
    pass


class Oldster(Alcoholic_Functioning):
    
    def derp(self):
        self.__class__.action_count += 1
        self.__class__.class_token += 1
        print("What? Nothing.")


class Demented_Old_Bat(Oldster):
    pass