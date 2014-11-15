class Count(object):
    def __init__(self):
        self.__count = 0
        self.__number = 0

    @property
    def add(self):
        #convert mi to mk
        self.__count + 1

    @add.setter
    def abc(self,new_count):
        self.__count = new_count

    def print_out(self):
        num = self.__count
        num = num.format(**locals())

        return num

