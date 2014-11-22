from page import Page
from data import Data
import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        d = Data()

        if self.request.GET:
            if self.request.GET['n']:
                self.response.write(p.print_out)

        else:
            self.response.write(p.print_out)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)