# For debugging:
# Status-check

print(f"""
{player.__class__.__dict__}
{player.__dict__}
{player.__class__.__name__}

Evo-stage: {player.evo_stage}
Class-token: {player.class_token}
Action-count: {player.action_count}

Name: {player.name}
Occupation: {player.occupation}
Hobby/-ies: {player.hobby}
""")

# Fetches the next class in a linear evolution - One link/stage only
for subclass in player.__class__.__subclasses__():
    print(subclass.__name__)

#Lists all the following subclasses of a given class
def all_subclasses(input_class):
    list_of_classes = [input_class]
    class_count = 0
    while class_count < len(list_of_classes):
        list_of_classes += list_of_classes[class_count].__subclasses__()
        class_count += 1
    return list_of_classes

for a_class in all_subclasses(Person):
    print(a_class.__name__)

print("""
----------------------------------------------------------
""")

#Lists the previous baseclass - One link/stage only
for baseclass in player.__class__.__bases__:
    print(baseclass.__name__)

#Lists all the previous baseclasses of a given class
def all_baseclasses(input_class):
    list_of_classes = [input_class]
    class_count = 0
    while class_count < len(list_of_classes):
        list_of_classes += list_of_classes[class_count].__bases__
        class_count += 1
    list_of_classes.pop() #Last one will always be 'object'
    return list_of_classes

for a_class in all_baseclasses(Demented_Old_Bat):
    print(a_class.__name__)


# Adult: [You know...] I [read]/[made a collage of] [the Wheel of Time] once. It had [horses] in it.
# Adult: *stares emptily* ... What?
# Adult: derps