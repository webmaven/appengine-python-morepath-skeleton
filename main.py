"""`main` is the top level module for your Morepath application."""

# Import the Morepath Framework
import morepath

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

config = morepath.setup()
config.scan()
config.commit()

#@app.errorhandler(404)
#def page_not_found(e):
    #"""Return a custom 404 error."""
    #return 'Sorry, Nothing at this URL.', 404


#@app.errorhandler(500)
#def page_not_found(e):
    #"""Return a custom 500 error."""
    #return 'Sorry, unexpected error: {}'.format(e), 500
