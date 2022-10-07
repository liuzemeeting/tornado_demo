from tornado.web import RequestHandler


class MainHandler2(RequestHandler):
    def get(self):
        data = {"d": "test2"}
        self.write(data)

