#konner Sherman
#friday nov 4
#DWP

import webapp2
from count import Count

class MainHandler(webapp2.RequestHandler):
    def get(self):
        c = Count()




        if self.request.GET:
            c.print_out()
            self.response.write('<a href="">Count</a>')

        c.print_out()


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
