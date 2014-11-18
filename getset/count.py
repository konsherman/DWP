class Count(object):
    def __init__(self):
        self.__count = 1  #count starts at 1 because the computer starts at 0
        self.__content = "<a href='?n={self.count}'>{self.count}</a>" #content that will print on the page



    def counter(self): #the counter function that adds one to the self.__count
        self.__count += 1


    @property #getter
    def count(self):
        return self.__count #getting self._count

    @count.setter #setter
    def count(self, new_count):
        self.__count = new_count
        self.counter() #run the counter function

    def print_out(self):
        stuff = self.__content
        stuff = stuff.format(**locals()) #making it so the vars will work in the content {like.this}
        return stuff #returning the stuff



