#konner
#simpleformlek
#today
import webapp2
from page import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        p.title = "Welcome..............."
        self.response.write(p.print_out())
        if self.request.GET:
            print "Yut"
            self.response.write(self.request.GET['f_name'] + "<br/>")
            self.response.write(self.request.GET['l_name'])


        else:
            print "nope"







app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
