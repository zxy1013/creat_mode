from abc import ABCMeta, abstractmethod
from time import sleep

# 抽象类
class Window(metaclass=ABCMeta):
    @abstractmethod
    def start(self): # 原子操作/钩子操作 不变的东西Window写了 变的东西还需要子类实现
        pass

    @abstractmethod
    def repaint(self): # 窗口重新绘制
        pass

    @abstractmethod
    def stop(self): # 原子操作/钩子操作
        pass

    def run(self):  # 模板方法
        self.start()
        while True:
            try:
                self.repaint()
                sleep(1)
            except  KeyboardInterrupt: # terminal 运行 python template_method.py ctrl+c终止
                break
        self.stop()


# 具体类
class MyWindow(Window): # 接口+继承
    def __init__(self, msg):
        self.msg = msg

    def start(self):
        print("窗口开始运行")

    def stop(self):
        print("窗口结束运行")

    def repaint(self):
        print(self.msg)


MyWindow("Hello...").run()