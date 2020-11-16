car = ""
start = False
while car.lower() != "quit":
    car = input(">")
    if car.lower() == "start":
        if start:
            print("car is already started")
        else:
            start = True
            print("started")
    elif car.lower() == "stop":
        if not start:
            print("car is already stopped")
        else:
            start = False
            print("stopped")
    elif car == "help":
        print('''"start" - Go
"stop" - stops
"quit" - exit''')
    elif car == "quit":
        print("exiting game...")
        break
    else:
        print("i don't understand that")
