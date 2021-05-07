from abc import ABCMeta, abstractmethod

# 目标接口
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass

class Alipay(Payment):
    def pay(self, money):
        print("支付宝支付%d元" % money)

class WechatPay(Payment):
    def pay(self, money):
        print("微信支付%d元" % money)

# 新添加的类和之前的格式不同，名字 参数多少、顺序都可能不同
# 待适配的类
class BankPay:
    def cost(self, money):
        print("银联支付%d元" % money)

class ApplePay:
    def cost(self, money):
        print("苹果支付%d元" % money)

# 此时再使用工厂模式等就会出现不一致的问题
p = WechatPay()
# p = ApplePay()
p.pay(100)


# 适配器
# 所以需要定义适配器，将一个类的接口转换成客户希望的另一个接口，使其兼容
# 一、类适配器 多继承
class NewBankPay(Payment, BankPay):
    def pay(self, money):
        self.cost(money)

# p = WechatPay()
p = NewBankPay() # 此时兼容
p.pay(100)


# 二、好多类都有问题类适配器太麻烦，所以需要对象适配器
class PaymentAdapter(Payment):
    def __init__(self, payment):
        self.payment = payment # 组合

    def pay(self, money):
        self.payment.cost(money)

p = PaymentAdapter(ApplePay())
p.pay(100)


# 复用代码 继承和组合
class A:
    pass
class B:
    def __init__(self): # 组合：在B类的属性中加入A类对象
        self.a = A()