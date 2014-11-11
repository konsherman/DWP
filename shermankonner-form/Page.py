class Page(object):
    def __init__(self):

        self.head = '''<!DOCTYPE html>
<head>
    <title>Simple Form</title>
    <link href="css/main.css" rel="stylesheet" type="text/css" />
</head>
<body>'''

        self.close = '''</body>
        </html>'''
        self.all = ''
        self.form = '''
	<form method="GET" action="">
		<input type="text" placeholder="First Name" name="fName">
		<input type="text" placeholder="Last Name" name="lName">
		<input type="number" placeholder="Age" name="age">
		<select name="gender">
			<option value="Male">Male</option>
			<option value="Female">Female</option>
		</select>
		<textarea rows="4" cols="50" placeholder="Comments" name="com">
		</textarea>
        <input type="submit" value="Submit">
	</form>
        '''


    def update(self):

        self.all = self.head  + self.form + self.close
        #**locals() function that represents all accessible variables
        self.all = self.all.format(**locals())


    def print_out(self):
        self.update()
        return self.all