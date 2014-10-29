__author__ = 'Konner'
#Konner Sherman
#October 28 2014
#madlib

'''
# At least 2 strings
# At least 2 numbers
# One list/array
# One dictionary
# One conditional statement with at least one logical operator
# One function
# Must return a value
# Must have and use parameters
# One loop
'''
for i in range(0,1):
    print "Hello!"
    print "And Welcome to the Bobby Madlib"
    print "Lets get started"
first_thing = "He was "

age = raw_input("Enter age")

ice_cream = dict()
ice_cream = {"1":'Chocolate','2':'Vanilla'}
number = raw_input("Enter number 1 or 2")


def year_income(hour,year):
    income = hour * year
    return income
hour = int(raw_input("how much does he make an hour"))
year = int(raw_input("How many days in a year?"))
result = year_income(hour,year)

his_friend = raw_input("Enter your best friends Name")
friends = ["Konner","Bobby","Jerry"]
friends.append(his_friend)

weight = int(raw_input("Enter random weight"))
avg_weight = 140
r_number=int(raw_input("Random number"))
thing = True

if r_number >=10:
    thing = True

else:
    thing= False

if avg_weight <= weight or thing:
    print "Bobby was very Fat!"
else:
   print "Bobby is real skinny"

print first_thing + age+ " years old"+ " his favorite ice cream was "+ice_cream[number]+ " he makes " + str(result) +" dollars a year" + " his best friends are"
for f in friends:
    print f




