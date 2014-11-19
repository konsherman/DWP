#Konner Sherman
#today
#dynamic-stie
import webapp2
from data import Data

class MainHandler(webapp2.RequestHandler):
    def get(self):
        d=Data()
        if self.request.GET:
            self.response.write(d.print_out)

        self.reponse.write(d.print_out)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
