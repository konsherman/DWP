#Konner Sherman
#today
#dynamic-stie

class Page(object):
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
        self.close = '''
</body>
</html>
'''

    def print_out(self):
        return self.head + self.body + self.content + self.close