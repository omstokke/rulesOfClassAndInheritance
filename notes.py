# For debugging:
# Status-check

print(f"""
{player.__dict__}
{player.__class__}

Evo-stage: {player.evo_stage}
Class-token: {player.class_token}
Action-count: {player.action_count}

Name: {player.name}
Occupation: {player.occupation}
Hobby/-ies: {player.hobby}
""")

# as Person:

player.add_hobby("Hackysack")
player.incr_action_count(5)
player.incr_class_token(5)

player.remove_hobby("Hackysack")
player.decrease_class_token(2)
player.decrease_action_count(3)


    #Can I create a class method for evolving
    # to the next subclass, given a dict o.s.
    # with key-value evo_stage: Subclass?

    @classmethod
    def evolve(self):
        0: Person
        1: Infant
        2: Toddler
        3: Kid
        4: Tween
        5: Youth
        6: Adult_Functioning
        7: Alcoholic_Functioning
        8: Oldster
        9: Demented_Old_Bat
        #finds the current stage and sets an instance of the next stage
        pass

#Function for converting age into stupid ways of saying numbers

# Kid : Talking function with tables
# Teens: Tables - "Who even are you?" and "Don't you know what [horses] in [Batu] are [thirsty] due to [covid-19]?"
# Adult: [You know...] I [read]/[made a collage of] [the Wheel of Time] once. It had [horses] in it.
# Adult: *stares emptily* ... What?
# Adult: derps