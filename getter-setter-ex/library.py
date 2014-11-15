class Library(object):
    def __init__(self):
        self.__mi = 0
        self.__km = 0

    def convert_km(self):
        #convert mi to mk
        self.__km = self.__mi/.62137

    @property
    def km(self):
        it = round(self.__km,3)
        return it

    @km.setter
    def km(self, new_km):
        self.__km = new_km



    @property
    def mi(self):
        pass

    @mi.setter
    def mi(self, new_mi):
        self.__mi = new_mi
        self.convert_km()



