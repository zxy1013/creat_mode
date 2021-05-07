# 接口 普通实现(不好) 因为不调用时不报错
class Payment:
    def pay(self, money):
        # 报没有实现的异常
        raise NotImplementedError

class Alipay(Payment):
    # 不调用时不报错
    pass

class WechatPay(Payment):
    def pay(self, money):
        print("微信支付%d元" % money)

def payfinish(p,money):
    # 由于wechat和alipay的pay方法相同才可以直接使用. 否则需要判断 非常麻烦 所以需要接口
    p.pay(money)

# 不调用时不报错
p = Alipay()
# p.pay(100) # 此时报错NotImplementedError




# 接口 抽象类实现(好) 必须实现抽象类里的方法
from abc import ABCMeta, abstractmethod

class Payment(metaclass=ABCMeta): # abstract class
    @abstractmethod # abstract method
    def pay(self, money):
        pass

class Alipay(Payment):
    pass

# class Alipay(Payment):
#     def pay(self, money):
#         print("支付宝支付%d元." % money)

class WechatPay(Payment):
    def pay(self, money):
        print("微信支付%d元." % money)

# p = Alipay() # 不调用时也报错 Can't instantiate abstract class Alipay with abstract methods pay




# 面向对象设计SOLID原则
# 里氏替换原则
from abc import ABCMeta, abstractmethod
class User:
    def show_name(self):
        pass

class VIPUser(User):
    def show_name(self):
        pass

def show_user(u):
    res = u.show_name()
    # 拿到结果做统一处理 所以需要两个u对象的参数以及返回值类型相同
    # 即传User对象不报错的情况下 传VIPUser对象也不能报错




# 接口隔离原则
from abc import ABCMeta, abstractmethod
class Animal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass
    @abstractmethod
    def swim(self):
        pass
    @abstractmethod
    def fly(self):
        pass

class Tiger(Animal):
    def walk(self):
        print("老虎走路")

# p = Tiger() # 报错Can't instantiate abstract class Tiger with abstract methods fly, swim但是老虎不会飞
# 所以需要将总接口拆分成多个专门的接口


class LandAnimal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass
class WaterAnimal(metaclass=ABCMeta):
    @abstractmethod
    def swim(self):
        pass
class SkyAnimal(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass

class Tiger(LandAnimal):
    def walk(self):
        print("老虎走路")
p = Tiger()

# 用多继承实现多个接口
class Frog(LandAnimal, WaterAnimal):
    pass