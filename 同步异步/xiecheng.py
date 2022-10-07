import time
from threading import Thread

#全局生成器，供long_io使用
gen = None

def long_io():
    def fun():
        print("开始执行IO操作")
        global gen
        time.sleep(5)
        try:
            print("完成IO操作，并sent结果唤醒挂起程序继续执行")
            gen.send("io result")
        except Exception as e:
            pass
    t=Thread(target=fun,args=())
    t.start()

def req_a():
    print("开始处理请求rep_a")
    ret = yield long_io()
    print("ret: %s "%ret)
    print("完成处理请求rep_a")

def req_b():
    print("开始请求处理req_b")
    time.sleep(2)
    print("完成处理rep_b")

def main():
    global gen
    gen=req_a()
    next(gen)
    req_b()
    # while 1:
    #     pass

if  __name__ == "__main__":

    main()
        