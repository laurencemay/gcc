__author__ = 'laurence'

location = "myroom"
ready_for_school = False

print("Welcome to GCC Big Little Text Adventure")
print()
print("You find yourself in a room desperately trying to get out of house")
print("and catch bus to school. But things are not that well...")
print()
print("You can use commands like 'go', 'pick', 'put on' and 'use' followed by location or object")

while location != "exit":
    if location == "myroom":
        print("You are in your room. You look around and see window, door, desk,")
        print("wardrobe and bed.")

        command = raw_input("What do you want to do? ")

        if command == "go door":
            print("You got out to the hall")
        elif command == "go wardrobe":
            location = "wardrobe"
            print("You are in your wardrobe now")
        else:
            print("Command '" + command + "' not recognised.")
    elif location == "wardrobe":
        print("you are desperately battling with evil jumpers to get out")
        print("Do you put on a coat, t-shirt or tie on?")
        print("or do you want to go out")
        command = raw_input("What do you want to do? ")
        if command == "go out":
            location = "myroom"
        elif command == "put on tie":
            print("you are ready for school!!")
            ready_for_school = True
        elif command == "put on t-shirt":
            print("It's not the weekend! Stop slacking off and put some uniform on!")
            location = "wardrobe"
        elif command == "put on coat":
            print("you will get warm but your teachers will still give you a 'not good enough'")
        else:
            print("Command '" + command + "' not recognised.")
    elif location == "hall":
        print("Do you want to go to the bathroom or go outside")
        command = raw_input("What do you want to do? ")

    else:
        print("PROGRAMMER'S ERROR: location '" + location + "' is not known!")
        location = "exit"

print("Well done! You did it!")