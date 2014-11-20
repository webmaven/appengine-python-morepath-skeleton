"""`main` is the top level module for your Morepath application."""

# Import the Morepath Framework
import morepath
from webob.exc import HTTPNotFound, HTTPInternalServerError


class App(morepath.App):
    pass

@App.path('')
class Root(object):
    pass


@App.html(model=Root)
def hello_world(self, request):
    """Return a friendly HTML greeting."""
    return '<p>Hello World!</p>'


@App.view(model=HTTPNotFound)
def notfound_custom(self, request):
    """Return a custom 404 error"""
    def set_status_code(response):
        response.status = self.code  # pass along 404
    request.after(set_status_code)
    return "Sorry, Nothing at this URL."


@App.view(model=HTTPInternalServerError)
def servererror_custom(self, request):
    def set_status_code(response):
        response.status = self.code  # pass along 500
    request.after(set_status_code)
    return "Sorry, unexpected error: {}".format(self.detail)

app = App()
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.
config = morepath.setup()
config.scan()
config.commit()
