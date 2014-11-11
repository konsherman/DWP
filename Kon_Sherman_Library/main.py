#Konner Sherman
#DWP
#Nov 4, 2014

from library import Library
from library import Printer



class MainHandler(object):
    def __init__(self):

        calculations = Library()
        name1= raw_input("Name")
        name2= raw_input("Name")
        name3= raw_input("Name")
        name4= raw_input("Name")

        weight1 = int(raw_input("Enter Weight"))
        weight2 = int(raw_input("Enter Weight"))
        weight3 = int(raw_input("Enter Weight"))
        weight4 = int(raw_input("Enter Weight"))
        thePrinter = Printer()
        thePrinter.printstuff("The Average Weight of "+ name1 +" "+name2 + " " +name3 + " " +"and"+ name4 + " "+"Is", calculations.calc_info(weight1,weight2,weight3,weight4))



        






web_app = MainHandler()