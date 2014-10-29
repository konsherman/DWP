__author__ = 'Konner'
#Konner Sherman
#October 28 2014
#madlib

'''
# At least 2 strings
# At least 2 numbers
One list/array
# One dictionary
One conditional statement with at least one logical operator
# One function
# Must return a value
# Must have and use parameters
# One loop
'''
for i in range(0,3):
    print "Loading.."
first_thing = "Bobby was "
# print first_thing
age = raw_input("Enter age")
# print first_thing+age+" Years old"
ice_cream = dict()
ice_cream = {"1":'Chocolate','2':'Vanilla'}
number = raw_input("Enter number 1 or 2")
# print "his favorite ice cream was " +  ice_cream[number]

def year_income(hour,year):
    income = hour * year
    return income
hour = int(raw_input("how much does he make an hour"))
year = int(raw_input("How many days in a year?"))
result = year_income(hour,year)
print first_thing + age+ "years old"+ "his favorite ice cream was "+ice_cream[number]+ "he makes " + str(result) +" a year"




