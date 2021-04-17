from personClasses import *

personlist = ["Ole Martin", "Asshat", "Laughing"]

player = EmoTeen.from_list(personlist)

print(player.dumb_response_converter("Go get a haircut"))
player.teen_responds_to_important_things()

conversation = False