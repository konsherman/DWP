
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #all code starts in this get function
        #self.response attribute of main handler
        #to the browser


        self.response.write('Hello world!')

        #from the browser
        #self.request atrribute of mainhandler

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

