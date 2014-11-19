#Konner Sherman
#today
#dynamic-stie

class Data(object):
    def __init__(self):
        self.__cat_one = "<a href='?n=cat_one'>Cat one</a>"
        self.__cat_two = "<a href='?n=cat_two'>cat two</a>"
        self.__cat_three = "<a href='?n=cat_three'>cat three</a>"
        self.__cat_four = "<a href='?n=cat_four'>cat four</a>"
        self.__cat_five = "<a href='?n=cat_five'>cat five</a>"

    def print_out(self):
        all = self.__cat_five + self.__cat_four + self.__cat_one + self.__cat_two + self.__cat_three
        return all
