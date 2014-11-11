class Page(object):
    def __init__(self):
        self.title = ''
        self.head = ''''<!DOCTYPE html>
<head>
    <title>{self.title}</title>
    <link href="css/styles.css" rel="stylesheet" type="text/css" />
</head>
<body>'''
        #format() method
        #format() method cannot use private attributes
        self.content = 'Welcome'
        self.close = '''</body>
        </html>'''
        self.all = ''
        self.form = '''
        <form method="GET" action="">
            <input type="text" placeholer="First Name" name="f_name" />
            <input type="text" placeholder="LastName" name="l_name" />
            <input type="submit" value="Submit" />
        </form>
        '''


    def update(self):

        self.all = self.head + self.content + self.form + self.close
        #**locals() function that represents all accessible variables
        self.all = self.all.format(**locals())


    def print_out(self):
        self.update()
        return self.all

