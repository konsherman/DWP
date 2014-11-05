#Konner Sherman
#day2 classes
# from <<file>> import <<class>>

from character import Character

class MainHandler(object):
    def __init__(self):

        self.yoda=Character()

        self.yoda.name = "Yoda"
        self.yoda.hometown = "dagoba"
        self.yoda.age = 900
        self.yoda.occupation = "Jedi Master"


        leia = Character()

        leia.name = "Leia Organa"
        leia.age = 19
        leia.hometown = "Alderan"
        leia.occupation = "Princess"

        luke = Character()

        luke.name = "Luke"
        luke.age = leia.age
        luke.occupation = "Jedi Knight"
        luke.hometown = "Tatooine"
        self.print_out()

    def print_out(self):
        print self.yoda.age


#NO MORE GLOBAL VAR'S
#GLOBAL VARS ARE THE DEVIL
web_app = MainHandler()



