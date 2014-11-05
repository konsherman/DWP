__author__ = 'Konner'

from utility import Utility

class MainHandler(object):
    def __init__(self):

        self.area = Utility()

        print self.area.calc_area(100,100)













#only global variable allowed
web_app = MainHandler()