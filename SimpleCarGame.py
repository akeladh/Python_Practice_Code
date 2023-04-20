#The following is a program that is simulating a simple car game
#User can have the option to write the commands to start to stop the car
#User can exit out of game at any moment when quit command is typed
#User can have menu pop up of command options when help commands is typed
#Any other command will not be accepted
command = input(">")
while command != 'quit':
    if command == 'help':
        print('''
        start - to start the car 
        stop - to stop the car 
        quit - to exit
        ''')
    if command == 'start':
        print('Car started...Ready to go!')
    elif command == 'stop':
        print('Car stopped!')
    elif command == 'quit':
        break
    else:
        print("I don't understand")
