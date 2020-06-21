#-------------C A R  G A M E---------------#

print("Let's play car game.")
command = ""
started = False
while True:
    command = input("start or stop : ").lower()
    if command == "start":
        if started:
            print("Car is already started !")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped !")
        else:
            started = False
            print("Car stopped.")
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand everything.")

#   This game is very important for python developers    #
