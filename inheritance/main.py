#Konner Sherman
#lab ex

import webapp2
from vehicle import Car, Vehicle, Boat

class MainHandler(webapp2.RequestHandler):
    def get(self):
        subaru = Car()
        subaru.crash()

        island_gypsy = Boat()
        island_gypsy.float()


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
