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

# 抽象工厂角色
# 工厂类的接口
class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass

# 具体工厂角色
class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay()

class WechatPayFactory(PaymentFactory):
    def create_payment(self):
        return WechatPay()

class HuabeiFactory(PaymentFactory):
    def create_payment(self):
        return Alipay(use_huabei=True)


# client客户端
# 根据需要的方法创建工厂 参数也不需要加
pf = HuabeiFactory()
p = pf.create_payment()
p.pay(100)


# 添加新的支付方式也不需要修改原先的代码 只是再添加一个类即可
class CardPay(Payment):
    def pay(self, money):
        print("银行卡支付%d元" % money)

class CardPayFactory(PaymentFactory):
    def create_payment(self):
        return CardPay()