import tornado.web
import tornado.ioloop

class IndexHanler(tornado.web.RequestHandler):
    #主页处理类
    def get(self):
        #get请求方式
        self.write("hello,world！")


if __name__ == "__main__":
    #先声明一个类
    app = tornado.web.Application([(r"/",IndexHanler)]);
    app.listen(8080);#绑定到8000端口
    tornado.ioloop.IOLoop.current().start();