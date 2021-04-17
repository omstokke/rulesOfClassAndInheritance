from personClasses import *

personlist = ["Ole Martin", "Asshat", "Laughing"]
player = Person.from_list(personlist)

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

player = Infant.from_list(personlist)

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

player = Toddler.from_list(personlist)

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

player = Kid.from_list(personlist)

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

player = EmoTeen.from_list(personlist)

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

player.cry()
print(player.dumb_response_converter("Go get a haircut"))
player.teen_responds_to_important_things()