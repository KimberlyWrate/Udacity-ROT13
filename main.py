#Kimberly Wrate
#URL: https://udacity-rot13-144021.appspot.com/
#Translate input to a web form via ROT13, and print the output
#Preserves punctuation, whitespace, and caps
#Accounts for escape html

from string import maketrans   # Required to call maketrans function.
import cgi # Required for HTML escape characters

# form stuff:
import webapp2

form="""
<form method="post">
    Enter text to get transformed by ROT13:
    <br>
    <textarea name="text">%(val)s</textarea>
    <br>
    <input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def escape_html(self, s):
        return cgi.escape(s, quote = True)

    def write_form(self, s=' '):
        self.response.out.write(form % {"val":s})
    
    def ROT_translate(self, s):
        intab = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        outtab = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
        trantab = maketrans(intab, outtab)
        return str(s).translate(trantab)

    def get(self):
        self.write_form()

    def post(self):
        user_text = self.request.get('text')
        user_text = self.ROT_translate(user_text)
        user_text = self.escape_html(user_text)

        self.write_form(user_text)

        #self.redirect("/")
app = webapp2.WSGIApplication([('/', MainPage)],
                                debug=True)   
        
