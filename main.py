"""`main` is the top level module for your Morepath application."""

# Import the Morepath Framework
import morepath
from webob.exc import HTTPNotFound, HTTPInternalServerError

app = morepath.App(name='Hello')
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

@app.path('')
class Root(object):
    pass

@app.view(model=Root)
def hello_world(self, request):
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

@app.view(model=HTTPNotFound)
def notfound_custom(self, request):
    """REturn a custom 404 error"""
    def set_status_code(response):
        response.status = self.code # pass along 404
    request.after(set_status_code)
    return "Sorry, Nothing at this URL."

@app.view(model=HTTPInternalServerError)
def servererror_custom(self, request):
    def set_status_code(response):
        response.status = self.code # pass along 500
    request.after(set_status_code)
    return "Sorry, unexpected error: {}".format(self.detail)

config = morepath.setup()
config.scan()
config.commit()
