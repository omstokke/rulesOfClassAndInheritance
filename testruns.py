from personClasses import *

personstring = "Ole Martin,Asshat,Laughing" 
player = Person.from_string(personstring)

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

player = Infant.from_string(personstring)

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

personlist = ["Ole Martin", "Asshat", "Laughing"]

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

player.talk(player)
player.cry()
player.wail()
player.shits_and_giggles(player)
player.talk_some_more(player)
player.rational_Kid(player)
