command = ""
started = False
while True:

    if command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit
        """)
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already Started....")
        else:
             started = True
             print("car is started...")
    elif command == "stop":
        if not started:
            print("car is already stopped...!")
        else:
            print("car is stoped..")
    elif command == "quit":
        break

    else:
        print("we don't understand")





