from page import Page #importing page
from data import Data #importing data
import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page() #calling the page
        d = Data()

        if self.request.GET:
            if self.request.GET['n']:
                for i in d.houses[1]:
                    self.response.write(i)

        else:
            self.response.write(p.print_out)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
