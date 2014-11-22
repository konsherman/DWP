from data import Data
class Page(object):
    def __init__(self):

        self.__head = '''
<html>
<title>Hello</title>
<body>
                '''

        self.__content = '''
        <a href="?n" name="Lan">Lannister</a>
        <a href="?n" name="Stark">Stark</a>
        <a href="?n" name="GreyJoey">GreyJoy</a>
        <a href="?n" name="Targaryen">Targaryen</a>
        <a href="?n" name="Tully">"Tully"</a>
        '''
        self.data = Data
        self.data = self.data.houses
        self.__close = '''
</body>
</html>
                '''
    def print_2(self):
        print self.data.houses
    @property
    def print_out(self):
        return self.__head + self.__content + self.__close







