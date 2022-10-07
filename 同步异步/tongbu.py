import time
import os

#同步进程阻塞
def rep_a():
    print("开始请求处理rep_a")
    time.sleep(5)
    print("完成处理rep_a")

def rep_b():
    print("开始请求处理rep_b")
    print("完成请求处理rep_b")

def main():
    rep_a()
    rep_b()

if __name__ == "__main__":
    main()