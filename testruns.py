from personClasses import *

personlist = ["Ole Martin", "Asshat", "Laughing"]
personlist2 = ["Snurre Sprett", "Wonkyballs", "Derping"]
personlist3 = ["Mogens", "Wonkyballs", "Derping"]

player = Infant.from_list(personlist)

print(f"""
{player.__class__.__dict__}
{player.__dict__}
{player.__class__.__name__}
""")

player.incr_evo_points(60)

print(f"""
{player.__class__.__dict__}
{player.__dict__}
{player.__class__.__name__}
""")