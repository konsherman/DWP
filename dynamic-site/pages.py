#Konner Sherman
#today
#dynamic-stie
from data import Cat
class Page(object): #page class this is going to spit the whole page out
    def __init__(self):

        self.head = '''
<html>
<head>
	<meta charset="UTF-8">
	<title>Cats</title>
	<link rel="stylesheet" type="text/css" href="css/main.css">
	<link href='http://fonts.googleapis.com/css?family=Sniglet' rel='stylesheet' type='text/css'>
</head>
<body>
'''
        self.body = '''
        <div id="wrapper">
        <ul>
            <li><a href="?cat=orange">Orange Cat</a></li>
            <li><a href='?cat=black'>Black Cat</a></li>
            <li><a href='?cat=bengal'>Bengal Cat</a></li>
            <li><a href='?cat=burmese'>Burmese Cat</a></li>
        </ul>
        </div>
        '''
        self.content = '''


        '''
        self.cat = Cat()
        self.close = '''
</body>
</html>
'''

    def print_out(self): #just printing everything out

        return self.head + self.body +"<p>"+self.cat.cat_name+"</p>"+"<p>"+self.cat.cat_color+"</p>"+"<p>"+self.cat.cat_type+"</p>"+self.cat.cat_image+self.content + self.close

    def print_out2(self): #just printing everything out
        return self.head + self.body + self.content + self.close

