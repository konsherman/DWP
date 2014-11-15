class Page(object):
    def __init__(self):
        #public
        self.title = ''
        self.css = ''
        #not public
        self.__head = '''
        <html>
<head>
	<meta charset="UTF-8">
	<title>{self.title}</title>
	<link rel="stylesheet" href="{self.css}">
</head>
<body>
        '''
        self.__close = '''
</body>
</html>
        '''
        self.nav ='''
         <a href="?n=mickey">Mickey</a></br>
         <a href="?n=minie">Minie</a></br>
         <a href="?n=pluto">Pluto</a></br>
         <a href="?n=don">Don</a></br>

         '''
        self.__content = "" # makes attr private

    @property #treat it like avariable in other classes #write only
    def content(self):#getter getters always return
        # return self.__content
        pass

    #setter function #read only
    @content.setter
    def content(self,new_content):
        self.__content = new_content

    def print_out(self):
        all = self.__head + self.__content + self.nav + self.__close
        all = all.format(**locals())#replaces {variables} with values
        return all
