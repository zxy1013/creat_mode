from abc import ABCMeta, abstractmethod

# 形状是抽象 颜色是实现
# 形状接口
class Shape(metaclass=ABCMeta):
    def __init__(self, color): # 使用组合实现代码复用 松耦合 两个维度都可以自由扩展
        self.color = color

    @abstractmethod
    def draw(self):
        pass

# 颜色接口
class Color(metaclass=ABCMeta):
    @abstractmethod
    def paint(self, shape):
        pass

# 具体形状
class Rectangle(Shape):
    name = "长方形"
    def draw(self):
        # 长方形逻辑
        self.color.paint(self)

class Circle(Shape):
    name = "圆形"
    def draw(self):
        # 圆形逻辑
        # print(self.name) # 圆形
        self.color.paint(self)

# 具体颜色
class Red(Color):
    def paint(self, shape):
        print("红色的%s" % shape.name)

class Green(Color):
    def paint(self, shape):
        print("绿色的%s" % shape.name)

class Blue(Color):
    def paint(self, shape):
        print("蓝色的%s" % shape.name)

# 客户端
shape2 = Circle(Green())
shape2.draw()



# 线条维度的扩展符合开闭原则
class Line(Shape):
    name = "直线"
    def draw(self):
        # 直线逻辑
        self.color.paint(self)

shape = Line(Blue())
shape.draw()