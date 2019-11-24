from . import views

def initializeRoutes(app):
    app.add_url_rule('/test/', view_func=views.test) # methods=['GET']
    app.add_url_rule('/upload/', view_func=views.uploadView)
    app.add_url_rule('/upload/imgs/', view_func=views.uploadImgs, methods=['POST'])
    app.add_url_rule('/view/', view_func=views.view_page)
    app.add_url_rule('/view/more/', view_func=views.view_more, methods=['POST'])