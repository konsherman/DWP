#konner Sherman
#friday nov 4
#DWP

import webapp2
from count import Count

class MainHandler(webapp2.RequestHandler):
    def get(self):
        c = Count() #bring in the count class

        if self.request.GET: #when GET print the self.content and evyerhitng
            c.count = int(self.request.GET['n'])


        self.response.write(c.print_out())
        #else just print out what its got


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
