from abc import ABCMeta,abstractmethod

# 抽象策略
class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, data):
        pass


# 具体策略
class FastStrategy(Strategy):
    def execute(self, data):
        print("用较快的策略处理%s" % data)

class SlowStrategy(Strategy):
    def execute(self, data):
        print("用较慢的策略处理%s" % data)


# 上下文类
class Context:
    def __init__(self, strategy, data):
        self.data = data
        self.strategy = strategy

    def set_strategy(self, strategy): # 切换策略
        self.strategy = strategy

    def do_strategy(self): # 执行策略
        self.strategy.execute(self.data)


# Client 需要知道不同的策略优缺点 才能知道如何转换策略
data = "[...]"
s1 = FastStrategy()
s2 = SlowStrategy()
context = Context(s1, data)
context.do_strategy()
context.set_strategy(s2)
context.do_strategy()