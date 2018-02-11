import time
from threading import Thread
import threading
def long_io(callback):
    def fun(cb):
        print("开始执行IO操作...");
        time.sleep(5);
        print("完成IO操作，并执行回调函数...")
        #执行回调函数
        cb("io result")
    #开区线程执行耗时操作
    t=Thread(target=fun,args=(callback,))
    t.start()

def on_finish(ret):
    print("开始执行回调函数on_finish")
    # ret=yield long_io()
    print("ret: %s "% ret);
    print("完成执行回调函数on_finish")

def rep_a():
    print("开始处理请求rep_a");
    long_io(on_finish);
    print("离开处理请求rep_a");

def rep_b():
    print("开始处理请求rep_b")
    time.sleep(2);
    print("完成处理请求rep_b")

def main():
    rep_a();
    rep_b();
    while 1:
        pass;


if __name__ == "__main__":
    main()