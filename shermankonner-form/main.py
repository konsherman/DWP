#Konner Sherman
#Nov 9, 2014
#DWP
import webapp2
from Page import Page
class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()

        if self.request.GET:
            self.response.write(p.head + p.close)
            self.response.write(self.request.GET['fName']+"</br>")
            self.response.write(self.request.GET['lName']+"</br>")
            self.response.write(self.request.GET['age']+"</br>")
            self.response.write(self.request.GET['gender']+"</br>")
            self.response.write(self.request.GET['com']+"</br>")

        else:
            self.response.write(p.print_out())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
