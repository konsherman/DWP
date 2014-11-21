#Konner Sherman
#today
#dynamic-stie
import webapp2
from data import Cat, Black, Orange , Bengal, Burmese #bringing in the cat classes

from pages import Page #impoting page class

class MainHandler(webapp2.RequestHandler):
    def get(self):
        c = Cat()
#------CALLING CLASSES---
        b = Black()
        o = Orange()
        ben = Bengal()
        bur = Burmese()
        p = Page()
        if self.request.GET:
            if self.request.GET['cat'] == 'black': #if the search bar == ?cat=black run this vv
                self.response.write(b.stuff+p.print_out())#printing the cat info + the main page that way the buttons still show up when you view the cat

            if self.request.GET['cat'] == 'orange':
                self.response.write(o.content+p.print_out())

            if self.request.GET['cat'] == 'bengal':
                self.response.write(ben.show()+p.print_out())

            if self.request.GET['cat'] == 'burmese':
                self.response.write(bur.show()+p.print_out())

        else:
            self.response.write(p.print_out()) #else just print it out



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
