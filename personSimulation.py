from personClasses import *

def onboarding(list):
    print("""
        Welcome!

        What follows is a short simulation,
        enabling you to catch up on the current status of humanity.""")

    list.append(input("""
        What is the name of our subject today? """))

    list.append(input("""
        What is the subjects favorite past-time activity? """))


def onboarding_2(player):
    print(f"""
        Okidoki then - Meet {player.name} - for now, this little human
        classifies as '{player.__class__.__name__}' on the evolutionary
        ladder of two-legged hairless mammals.

        It seems to enjoy {player.hobby.lower()}, which should prove
        to be an important observation during the course of our
        small study of it, and its kind. 
    """)


def simulation_menu(player):
    print(f"Your current stage is: {player.__class__.__name__}\n    ")
    
    flist = player.functionlist

    for method in flist:
        indeks = str(flist.index(method))
        print("    " + indeks + " " + method)


def perform_action(player):
    flist = player.functionlist
    try:
        a = int(input(f"\n    Choose an action for {player.name}, using its index: "))
        getattr(player, flist[a])()

    except ValueError:
        perform_action(player)
    
    except IndexError:
        perform_action(player)
      

personlist = []
onboarding(personlist)

player = Infant.from_list(personlist)

onboarding_2(player)

while True:
    action_limit = 70
    
    if player.action_count > action_limit and player.evo_stage == 7:
        decision = input("Would you like to end this simulation? y/n: ")
        if decision.lower() == "y":
            print(f"""
    You had a final score of {player.action_count} actions done!
                """)
            break
        else:
            print("""
    Okidoki - Let's see you get some poetry done!
                """)

    simulation_menu(player)
    
    perform_action(player)

    print("_" * 65 + "\n" * 2 + "   ")