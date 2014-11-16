class Page(object):
    def __init__(self):
        #public
        self.title = ''
        self.css = ''
        #not public
        self._head = '''
        <html>
<head>
	<meta charset="UTF-8">
	<title>{self.title}</title>
	<link rel="stylesheet" href="{self.css}">
</head>
<body>
        '''
        self._close = '''
</body>
</html>
        '''
        self._nav ='''
         <a href="?n=mickey">Mickey</a></br>
         <a href="?n=minie">Minie</a></br>
         <a href="?n=pluto">Pluto</a></br>
         <a href="?n=don">Don</a></br>

         '''
        self._content = "" # makes attr private

    @property #treat it like avariable in other classes #write only
    def content(self):#getter getters always return
        # return self.__content
        pass

    #setter function #read only
    @content.setter
    def content(self,new_content):
        self._content = new_content

    def print_out(self):
        all = self._head + self._content + self._nav + self._close
        all = all.format(**locals())#replaces {variables} with values
        return all

class FormPage(Page):
    def __init__(self):
        Page.__init__(self)
        self.__form_open = "<form>"
        self.__form_body = '''
            <input type="text" name="f_name" placeholder="first name"/>
            <input type="text" name="email" placehodler="email"/>
            <input type="submit" value="Submit infor"/>
            '''
        self.__form_close = "</form>"

    def print_out(self):
        all = self._head + self._nav + self.__form_open + self.__form_body + self.__form_close +self._content + self._close
        all = all.format(**locals())
        return all