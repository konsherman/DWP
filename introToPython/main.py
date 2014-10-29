__author__ = 'Konner'

# print somewhat like console log
'''

this i a multi-lined comment.
or rather...a literal string.

'''
#Konner
#intro to python
#date

# ------------Expressions----
first_name="Konner"
last_name = "Sherman"

# print first_name + " " + last_name

year_born = 1930
current_year = 2014
age = current_year - year_born
age +=1
# print age

# CONDITIONS

budget = 50
shoes = 80
win_lottery = False

if shoes <= budget or win_lottery:
    #if nothing put pass
    print "Yes you can buy the shoes"
    #this is inside the conditional
    #this is after the conditional the indent is what makes it work
else:
    print "No SHOES FOR YOU"

#logical operators = and,or,not (equiv $$,||,!)
grade_per = 90
#what would be the letter grade
'''
if grade_per >= 95:
    print "A+"
elif grade_per >=95 and grade_per > 90:
    print "A"
elif grade_per > 85:
    print "b+"
elif grade_per > 80:
    print "b"
'''
##funciotns------------------
def calc_area(height,width):
    area = height * width
    return area

result = calc_area(200,400)
print str(result) + "sqfeet"

#casting ------ str(var) int(var) float(var) ect

#-------loops
#for NUM in range(start,stop), INC_AMOUNT)

for i in range(5,0,-1):
    print "This is the song that never ends"
    print "Helllllloooo sing song"
    print "Still Singing"
    print i


#-----Arrays $ dictionaries

students = ["Konner","Mike","Bob","Jim","Vic"]
students.append("Paul")
#len() is going to give you the lenght of the array
print students[0]#going to goive you the student with the index number of 0
print len(students)

#dictionaries
football_teams = dict()
football_teams = {'number':32,'total_yards':100,'nfl_prez':'Roger'}

print football_teams['number']



#-----Looping through collections

for s in students:
    print s

#-----User Input

#output - print
#input - raw_input() input()
result = raw_input("Enter Your Name:")
print result +", Hello!"