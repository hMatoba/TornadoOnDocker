import os

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
}

def main():
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()