
import webapp2
from pages import Page
class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()

        p.title = "Content"
        p.css = "css/styles.css"
        if self.request.GET:
            p.content = self.request.GET['n']

        self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
