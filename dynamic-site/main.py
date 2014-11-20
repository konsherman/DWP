#Konner Sherman
#today
#dynamic-stie
import webapp2
from data import Cat, Black, Orange , Bengal, Burmese

from pages import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        c = Cat()
        b = Black()
        o = Orange()
        ben = Bengal()
        bur = Burmese()
        p = Page()
        if self.request.GET:
            if self.request.GET['cat'] == 'black':
                self.response.write(p.print_out())
                self.response.write(b.show())

            if self.request.GET['cat'] == 'orange':
                self.response.write(p.print_out())
                self.response.write(o.show())
            if self.request.GET['cat'] == 'bengal':
                self.response.write(p.print_out())
                self.response.write(ben.show())
            if self.request.GET['cat'] == 'burmese':
                self.response.write(p.print_out())
                self.response.write(bur.show())
        else:
            self.response.write(p.print_out())







app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
