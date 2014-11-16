
import webapp2
from pages import FormPage,Page
class MainHandler(webapp2.RequestHandler):
    def get(self):
        f = FormPage()
        p = Page()

        f.title = "Enter your info"
        f.css = "css/styles.css"
        if self.request.GET:
            # p.content = self.request.GET['n']
            self.response.write(p.print_out())
        else:
            self.response.write(f.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
