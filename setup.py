import logging
import Flaskr
import sys

# app = Flaskr.create_app(None)
# app.run()


def app(environ, start_response):
    data = b"Hello, World!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
