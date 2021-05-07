from abc import ABCMeta, abstractmethod

# 抽象订阅者
class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, notice): # notice是一个Notice类的对象
        pass


# 抽象发布者
class Notice:
    def __init__(self):
        self.observers = [] # 存储订阅者

    def attach(self, obs):
        self.observers.append(obs)

    def detach(self, obs):
        self.observers.remove(obs)

    def notify(self): # 向订阅者推送
        for obs in self.observers:
            obs.update(self)


# 具体发布者
class StaffNotice(Notice): # 继承
    def __init__(self, company_info=None):
        super().__init__()
        self.__company_info = company_info #__***表示私有

    @property
    def company_info(self):
        return self.__company_info

    @company_info.setter
    def company_info(self, info):
        self.__company_info = info
        self.notify() # 推送


notice = StaffNotice("初始公司信息")
# print(notice.__company_info) # 外部不可访问私有成员
# 加 @property 表示可读
print(notice.company_info) # 此时可访问 初始公司信息
# 加 @company_info.setter 表示可写
notice.company_info ='123' # 将self.__company_info设置为123
print(notice.company_info) # 123


# 具体订阅者
class Staff(Observer):
    def __init__(self):
        self.company_info = None

    def update(self, notice):
        self.company_info = notice.company_info


# Client
notice = StaffNotice("初始公司信息")
s1 = Staff()
s2 = Staff()
notice.attach(s1)
notice.attach(s2)
notice.company_info = "公司给大家发奖金！！！"
print(s1.company_info)
print(s2.company_info)
notice.detach(s2) # 取消订阅
notice.company_info = "公司明天放假！！！"
print(s1.company_info)
print(s2.company_info)