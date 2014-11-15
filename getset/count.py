class Count(object):
    def __init__(self):
        self.__count = 0
        self.__number = 0
        self.__content = "<p href='?n={self.count}'>{self.__count}</p>"





    @property
    def count(self):
        it = self.__count = self.__number + 1
        return it

    @count.setter
    def count(self, new_count):
        self.__count = int(new_count)


    def print_out(self):
        all = self.__content + str(self.__number)
        all = all.format(**locals())
        return all



