# 简单工厂模式
from abc import ABCMeta, abstractmethod

# 抽象产品角色
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass

# 具体产品角色
class Alipay(Payment):
    def __init__(self, use_huabei=False):
        self.use_huabei = use_huabei

    def pay(self, money):
        if self.use_huabei:
            print("花呗支付%d元" % money)
        else:
            print("支付宝余额支付%d元" % money)

class WechatPay(Payment):
    def pay(self, money):
        print("微信支付%d元" % money)

# 工厂角色
# 工厂类生产对象---支付对象
class PaymentFactory:
    def create_payment(self, method):
        if method == 'alipay':
            return Alipay()
        elif method == 'wechat':
            return WechatPay()
        elif method == 'huabei':
            return Alipay(use_huabei=True) # 可以传一些不需要用户自己传入的参数或隐藏一些功能 否则需要用户自己将代码读完，自己实现
        else:
            raise TypeError("No such payment named %s" % method)

# client代码--高层代码
pf = PaymentFactory()
p = pf.create_payment('huabei') # 免去了用户了解use_huabei参数的作用
p.pay(100)