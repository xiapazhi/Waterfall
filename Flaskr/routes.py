from . import views

def initializeRoutes(app):
    app.add_url_rule('/test/', view_func=views.test)