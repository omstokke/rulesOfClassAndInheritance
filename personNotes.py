
# This is not a functions script, just a set of notes to be kept as I tried to track to down
# how to write the code for the Person Sim, as well as someplace to keep code I didn't use
# but found useful.

# Handy for debugging/status-check
# player is name I gave the active instance of a given class

print(f"""
{player.__class__.__dict__}
{player.__dict__}
{player.__class__.__name__}

Evo-stage: {player.evo_stage}
Evo-points: {player.evo_points}
Action-count: {player.action_count}

Name: {player.name}
Hobby: {player.hobby}
""")

#Get all functions and properties (also inherited)
print(dir(player.__class__))

#Get all callable methods for the class w/o those inherited from Person (the abstract class)
function_list = []
for method in dir(player.__class__):
    if callable(getattr(player.__class__, method)) and method not in dir(Person):
        function_list.append(method)

#Same as above
function_list = [method for method in dir(player.__class__)
    if callable(getattr(player.__class__, method)) and method not in dir(Person)]

# Fetches the next class in a linear evolution - One link/stage only
for subclass in player.__class__.__subclasses__():
    print(subclass.__name__)

#Lists all the following subclasses of a given class for the Person Sim class hierarchy
def all_subclasses(input_class):
    list_of_classes = [input_class]
    class_count = 0
    while class_count < len(list_of_classes):
        list_of_classes += list_of_classes[class_count].__subclasses__()
        class_count += 1
    return list_of_classes

for a_class in all_subclasses(Person):
    print(a_class.__name__)

#Lists the previous baseclass - One link/stage only
for baseclass in player.__class__.__bases__:
    print(baseclass.__name__)

#Lists all the previous baseclasses of a given class for the Person Sim class hierarchy
def all_baseclasses(input_class):
    list_of_classes = [input_class]
    class_count = 0
    while class_count < len(list_of_classes):
        list_of_classes += list_of_classes[class_count].__bases__
        class_count += 1
    list_of_classes.pop() #Last one will always be 'object'
    return list_of_classes

#example of listing all baseclasses using the final class in the evolution of a Person,
# in the Person Sim (Oldster)
for a_class in all_baseclasses(Oldster):
    print(a_class.__name__)