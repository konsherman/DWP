class Student(object):
    def __init__(self):
        #----Public----

        self.hair = ""
        self.gender = ""

        #^^^^public^^^^
        #-------------
        #---PROTECTED----

        self._age = 0

        #^^^PROTECTED^^
        #--------------
        #----PRIVATE----

        self.__height = 0

    def full_student(self):
        #gets the student and adds it into one big student
        all = self.hair + self.gender + str(self._age) + str(self.__height)
        return all

    def math(self):
        return self._age + int(self.__height)  #adding the self and the age and reutnring it

    def print_out(self):
        print "Hello world" #printing out hellow world



class Custodian(object):
    def __init__(self):
        self.position = ''
        self.hair_color = ''
        self._hours = 0
        self.__name = ''

    def pay_check(self, hours, pay_rate):
        #this method calulates how much money the person is going to make
        money = hours * pay_rate
        return money

    def run_it(self):
        print self.pay_check(10, 3.00)

    def test(self):
        print "Hello World"





class Zombie(object):
    def __init__(self):
        self.blood_type = ''
        self.zombie_type = ""
        self.__skin_rot = 0
        self.__teeth = 0

    def print_zombie(self):
        print self.blood_type + self.zombie_type + "The zombie you are fithing has a skin rotting level of" + str(self.__skin_rot) + self.__teeth

    def mic_check(self):
        print "Mic Check"

    def print_out(self):
        print self.__teeth + self.__skin_rot

