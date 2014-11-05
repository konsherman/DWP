#Konner Sherman
#DWP
#Nov 4, 2014

from library import Library


class MainHandler(object):
    def __init__(self):
        stuff = Library()
        stuff.age = raw_input("age")
        print stuff.age





#NO MORE GLOBAL VAR'S
#GLOBAL VARS ARE THE DEVIL
web_app = MainHandler()