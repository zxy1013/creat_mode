# 单例
class Singleton:
    # 保证一个类只有一个实例
    # 重写new方法 给整个对象初始化
    def __new__(cls, *args, **kwargs):
        # 看class有没有_instance属性 如果没有说明类没有实例化
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        # 如果有直接返回实例
        return cls._instance

class MyClass(Singleton):
    def __init__(self, a):
        self.a = a


a = MyClass(10) # 创建实例 self.a = 10
b = MyClass(20) # 已经存在实例，直接返回 更新 self.a = 20

print(a.a) # 20 因为ab指向同一个实例 b后面更改了self.a = 20
print(b.a) # 20
print(id(a), id(b)) # 相等 2064314853832