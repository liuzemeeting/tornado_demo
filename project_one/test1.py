import asyncio

from tornado.httpclient import AsyncHTTPClient
from tornado import gen
from test2 import MainHandler2
import tornado

from tornado.web import Application, RequestHandler, authenticated


class MainHandler(RequestHandler):

    def get_current_user(self):
        return self.get_secure_cookie("username")

    @tornado.web.authenticated
    def get(self):
        # res = async_fetch_gen("http://www.baidu.com")
        # print(res, "res")
        data = {"d": "test"}
        res = self.get_secure_cookie("username")
        print("res", res)
        self.write(data)


class LoginMainHandler(RequestHandler):

    # def get(self):
    #     res = async_fetch_gen("http://www.baidu.com")
    #     print(res, "res")
    #     data = {"login": "login"}
    #     self.write(data)

    def get(self):
        # res = async_fetch_gen("http://www.baidu.com")
        # print(res, "res")
        data = {"login": "login"}
        res = self.set_secure_cookie('username', "test")
        print(res, "rrrr")
        # self.set_current_user('username')
        # self.redirect(self.get_argument("next", "/"))
        self.write(data)


class AuthLogoutHandler(RequestHandler):
    def get(self):
        self.clear_cookie("test_user")
        self.redirect(self.get_argument("next", "login"))

def make_app():
    return Application([
        (r"/", MainHandler),
        (r"/login", LoginMainHandler),
        (r"/loginout", AuthLogoutHandler),
        (r"/test2", MainHandler2)
    ], **settings)

settings = {
    "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    "login_url": "/login",
}

async def main():
    print("sssssssssssss")
    app = make_app()
    app.listen(8008)
    await asyncio.Event().wait()


if __name__ == '__main__':
    asyncio.run(main())
