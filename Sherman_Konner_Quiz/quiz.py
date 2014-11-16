class Student(object):
    def __init__(self):
        #----Public----

        self.hair = ""
        self.gender = ""

        #^^^^public^^^^
        #-------------
        #---PROTECTED----

        self._age = ""

        #^^^PROTECTED^^
        #--------------
        #----PRIVATE----

        self.__height = ""

    def full_student(self):
        #gets the student and adds it into one big student
        all = self.hair + self.gender + self._age + self.__height
        return all


class Custodian(object):
    def __init__(self):
        self.position = ''
        self.hair_color = ''
        self._hours = 0
        self.__name = ''

    def pay_check(self, hours, pay_rate):
        #this method calulates how much money the person is going to make
        money = self._hours * 3.00
        return money



class Zombie(object):
    def __init__(self):
        self.blood_type = ''
        self.zombie_type = ""
        self.__skin_rot = 0
        self.__teeth = ""

    def print_zombie(self):
        print self.blood_type + self.zombie_type + "The zombie you are fithing has a skin rotting level of" + str(self.__skin_rot) + self.__teeth

