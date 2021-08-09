from tamagotchi import Tamagotchi

pets = {}

wasInvalidCommand = False
command = input("Command: ")
while command:
    # Advance time
    if not wasInvalidCommand:
        for key in pets:
            pets[key].increment_time()
    else:
        wasInvalidCommand = False
    
    # Parse the command
    args = command.split(" ")
    
    if args[0] == "create":
        if args[1] in pets:
            if not pets[args[1]].is_dead():
                print("You already have a Tamagotchi called that.")
                wasInvalidCommand = True
                command = input("Command: ")
                continue
            else:
                pets[args[1]] = Tamagotchi(args[1])
        else:
            pets[args[1]] = Tamagotchi(args[1])
    elif args[0] == "feed":
        if not args[1] in pets:
            print("No Tamagotchi with that name.")
            wasInvalidCommand = True
            command = input("Command: ")
            continue
        else:
            pets[args[1]].feed()
    elif args[0] == "play":
        if not args[1] in pets:
            print("No Tamagotchi with that name.")
            wasInvalidCommand = True
            command = input("Command: ")
            continue
        else:
            pets[args[1]].play()
    elif args[0] == "wait":
        # Do nothing
        pass
    else:
        print("Invalid command.")
        wasInvalidCommand = True
        command = input("Command: ")
        continue
    
    # Printing
    petList =[]
    for key in pets:
        petList.append((key, pets[key]))
    petList.sort(key=lambda x:x[0])
    for petTuple in petList:
        print(petTuple[1])
    
    command = input("Command: ")