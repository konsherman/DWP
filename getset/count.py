class Count(object):
    def __init__(self):
        self.__count = 1  
        self.__content = "<a href='?n={self.count}'>{self.count}</a>"



    def counter(self):
        self.__count += 1


    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, new_count):
        self.__count = new_count
        self.counter()

    def print_out(self):
        stuff = self.__content
        stuff = stuff.format(**locals())
        return stuff



