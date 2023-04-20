#Create a weight converter in which when the user inputs a weight
#ask if it's lbs or kgs --> should not be case sensitive
#should print out --> you are ___ pounds/kilograms

#Input
user_weight = input("Hello there what is your weight?: ")
measurement = input("(L)bs or (K)g: ")

#Convert the weight to an int
user_weight = int(user_weight)

#check to see if upper/lower case L or K
unit = ""
if measurement == 'l' or measurement == 'L':
    user_weight *= 0.45
    unit = "Kgs"
elif measurement == 'k' or measurement == 'K':
    user_weight *= 2.20
    unit = "Pounds"
else:
    print("Invalid value")
print(f'You are {user_weight} {unit}')