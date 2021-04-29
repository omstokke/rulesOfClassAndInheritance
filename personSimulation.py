from personFunctions import *

personlist = []
simulation = True

onboarding(personlist)

player = Infant.from_list(personlist)

onboarding_2(player)

while simulation == True:
    action_limit = 70
    
    end_loop(player, action_limit)

    simulation_menu(player)
    
    perform_action(player)

    print("_" * 65 + "\n" * 2 + "   ")