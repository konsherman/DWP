#konner Sherman
#quiz
#nov 18th

class Reptile(object): #super class of reptile
    def __init__(self):
        self.color = ""
        self.weight = 0
        self.gender = ""
        self.age = 0


    def poop(self): #super functions
        print "Reptile is pooping"

    def pee(self):
        print "Reptile is peeing"

    def eat(self):
        print "Reptile is eating"




class Snake(Reptile): #new reptile
    def __init__(self):
        Reptile.__init__(self) #calls the super class
        self.name = "Mr.Snake"
        self.type= "Python" #two attributes


    def bite(self):
        print "snake bites"

    def shed_skin(self):#overwriting functions
        print "snake is shedding skin"





class Turtle(Reptile): #new reptile
    def __init__(self):
        Reptile.__init__(self)#calls the superclass
        self.name = "Mr.Tuuurtle"
        self.shel_type = "soft" #two attributes


    def swim(self):
        print "turtle is swimming" #overwriting functions

    def get_in_shell(self):
        print "turtle goes back into his shell"