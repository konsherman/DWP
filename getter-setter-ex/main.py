
import webapp2
from library import Library

class MainHandler(webapp2.RequestHandler):
    def get(self):

        i = Library()
        '''
        i.km = 5 #writing
        i.km = i.km + 1 #reading and writing
        '''''
        i.mi = 5
        self.response.write(i.km)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
