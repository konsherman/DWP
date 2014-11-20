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
</head>
<body>
'''
        self.body = '''
        <ul>
            <li><a href="?cat=orange">Orange Cat</a></li>
            <li><a href='?cat=black'>Black Cat</a></li>
            <li><a href='?cat=bengal'>Bengal Cat</a></li>
            <li><a href='?cat=burmese'>Burmese Cat</a></li>
        </ul>
        '''
        self.content = '''

        '''
        self.close = '''
</body>
</html>
'''

    def print_out(self):
        return self.head + self.body + self.content + self.close