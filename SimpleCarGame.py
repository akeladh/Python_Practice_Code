#The following is a program that is simulating a simple car game
#User can have the option to write the commands to start to stop the car
#User can exit out of game at any moment when quit command is typed
#User can have menu pop up of command options when help commands is typed
#Any other command will not be accepted
command = ''
#while command.lower() != 'quit': -- you can write this but it's repeating step 20
while True: #while this block of code is True
    command = input("> ")
    if command == 'help':
        print('''
        start - to start the car 
        stop - to stop the car 
        quit - to exit
        ''')
    elif command == 'start':
        print('Car started...Ready to go!')
    elif command == 'stop':
        print('Car stopped!')
    elif command == 'quit':
        print('You have exited the game')
        break
    else:
        print("I don't understand")
