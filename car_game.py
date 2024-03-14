started = False
command = ""
while True:
    command = input("> ")
    if command == "start":
        if started:
            print("car has already started")
        else:
            started = True
            print("start car")
    elif command == "stop":
        if not started:
            print("car has already stopped")
        else:
            started = False
        print("stop car")
    elif command == "quit":
        break