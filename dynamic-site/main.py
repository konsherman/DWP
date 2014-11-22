#Konner Sherman
#today
#dynamic-stie
import webapp2
from data import Cat,Data

from pages import Page #impoting page class

class MainHandler(webapp2.RequestHandler):
    def get(self):
        c = Cat()
#------CALLING CLASSES---
        d = Data()

        p = Page()
        if self.request.GET:
            if self.request.GET['cat'] == 'black': #if the search bar == ?cat=black run this vv
                p.cat = d.b

                self.response.write(p.print_out())#printing the cat info + the main page that way the buttons still show up when you view the cat

            if self.request.GET['cat'] == 'orange':
                p.cat = d.o
                self.response.write(p.print_out())

            if self.request.GET['cat'] == 'bengal':
                p.cat = d.ben
                self.response.write(p.print_out())

            if self.request.GET['cat'] == 'burmese':
                p.cat = d.bur
                self.response.write(p.print_out())


        else:
            self.response.write(p.print_out2()) #else just print it out



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
