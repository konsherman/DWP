#Konner Sherman
#Nov 9, 2014
#DWP
import webapp2
from Page import Page #importing the page class
class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()

        if self.request.GET:
            #if the url has does not have stuff submited "GET" this will print
            self.response.write(p.head)
            self.response.write(self.request.GET['fName']+"</br>")
            self.response.write(self.request.GET['lName']+"</br>")
            self.response.write(self.request.GET['age']+"</br>")
            self.response.write(self.request.GET['gender']+"</br>")
            self.response.write(self.request.GET['com']+"</br>"+p.close)

        else:
            # if nothing in the URL this will print the forum and everything
            self.response.write(p.print_out())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
