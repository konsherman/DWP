class Vehicle(object):
    def __init__(self):
        self.engine = ""
        self.speed = 0
        self.mpg = 0
        self.color = ""
        self.year = 0
        self.make = ""
        self.fuel_type = ""

    def accelerate(self):
        print "Accelerating"

    def decelerate(self):
        print "Decelrating"

    def crash(self):
        print "BANG YOU CRASHED"

    def start_ignition(self):
        print "VRRRRROOOOOMMMMM"

    def sink(self):
        print "sinking"



class Car(Vehicle):
    def __init__(self):
        Vehicle.__init__(self) #this call the super class construtor
        self.num_windows = 0
        self.num_axles = 0

    def burn_out(self):
        print "*smoke* *burning out*"

    def crash(self):#over righting the function
        print "BOOM"



class Boat(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.waterline = 0
        self.inboard_engine = ""
        self.out_board_engine = ""
        self.name = ""

    def float(self):
        print "Floating"

    def cast_anchor(self):
        print "Casting anchor"
