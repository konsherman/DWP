from data import Data
class Page(object):
    def __init__(self):

        self.head = '''
<html>
<title>Hello</title>
<body>
                '''

        self.content = '''
        <a href="n" name="Lan" value="lan">Lannister</a>
        <a href="n" name="Stark">Stark</a>
        <a href="n" name="GreyJoey">GreyJoy</a>
        <a href="n" name="Targaryen">Targaryen</a>
        <a href="n" name="Tully">"Tully"</a>
        '''
        self.houses = Data
        self.close = '''
</body>
</html>
                '''

    def print_out(self):

        return self.head + self.content + self.close







