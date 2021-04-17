
person1 = Person(input("What is my name?: "))
userName = Person(input("What is YOUR name?: "))

while True:
    command = input(f"Hello, {userName.name} - Would you like me to speak (y/n)? ").lower() #conversion to lower case is added removing need for input validation
    if command == "y":
        person1.talk()  #object-oriented method
        if person1.speakingToken < 10: #object-oriented attribute specifically called for person1 (and not self.)
            print(f"I have now spoken {person1.speakingToken} times")
        elif person1.speakingToken >= 10 and person1.speakingToken < 15:
            print(f"You seem to be enjoying this, {userName.name} - I have now spoken {person1.speakingToken} times")
        else:
            print(f"I am getting tired, as I have spoken {person1.speakingToken} times - Please end this!")
    elif command == "n":
        if person1.speakingToken <15:
            print(f"Thanks for letting me speak to you, {userName.name} - Bye!")
            break
        else:
            print("Ah, sweet release, I welcome thee!!!")
            break
    else:
        person1.speakingToken += 1
        print(f"{userName.name}, you should really input a 'y' for 'Yes' or an 'n' for 'No', or I will simply have to speak just to give you this message!")
        print(f"I have now spoken {person1.speakingToken} times.")