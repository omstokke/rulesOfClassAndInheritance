from random import choice

#this module is a collection of lists used in instance-methods of personClasses
#the purpose of which is to demonstrate how the random.choice()-function works
# in print-statements using f-strings

#Also because I had some fun with the statements - Helps learning things quicker

animals_table = [
        "Elephants",
        "Dogs",
        "Mermaids",
        "Penguins",
        "Capybara",
        "Dolphins",
        "KITTENS!",
        "Daddies",
        "Mommies",
        "Humans",
        "Stupids"
        ]

adjectives_table = [
        "brown",
        "red",
        "small",
        "funny",
        "tasty",
        "savage",
        "salty",
        "sweet",
        "strange",
        "important",
        "weak",
        "good"
        ]

#Think smart-ass emo kid, circa 16 and an active Reddit-feed
adjectives_table2 = [
        "thirsty",
        "dying",
        "decaying",
        "sinking",
        "vanishing",
        "withering",
        "moribund",
        "fated to a life of flaws",
        "fading into abyss-like states of blind disobedience",
        "doomed",
        "hungry",
        "not smiling",
        "getting crazy-eyed",
        "being turned into glue"
        ]

table_of_places = [
        "my house",
        "Daddys garden",
        "Mommys garden",
        "your house",
        "IKEA",
        "McDonalds",
        "Oslo",
        "Stockholm",
        "Chicago",
        "under the stairs",
        "rice fields",
        "the cave where they found me"
        ]

#Ref. Reddit-feed mentioned above
smartass_table = [
        "Batu",
        "the fjords of Austria",
        "southern caves of Deng'Hoi",
        "rice fields",
        "swamplands outside of Mexico",
        "the Gulf",
        "Swaziland",
        "Area 43, which is the actual 51,",
        "Gulskogen",
        "Mjosa, by Sweden"
        ]

table_of_bad_things = [
        "Covid-19",
        "plastic",
        "calamari drought",
        "lack of avocados in native Papa New-Guinea",
        "lizard people buying all the Pepsi from 3rd world countries",
        "Nazis losing their dinosaurs",
        "magical stories no longer being available to the dying minds of youth",
        "low internet access and loss of crypto-currency value",
        "poor media coverage of the real problems in our world",
        "misplaced AirPods, leading to feelings of loss and acute suicidal tendencies",
        "bad haircuts in Ukraine diminishing their returns on their annual people/vegetable-ratio"
        ]

#Wanted to see if it made any sense referencing a list inside a list using an f-string.
#It did.
small_table = [
        "...You got any money?",
        "I need some food I could trade for beers",
        "I need some beers I could trade for cigarettes",
        f"I need some... {choice(adjectives_table).lower()} {choice(animals_table).lower()}",
        "I prefer boxes over chairs",
        "My body cleans itself, thank you"
        ]