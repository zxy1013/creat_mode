import time
from abc import ABCMeta, abstractmethod

# 抽象组件
class Graphic(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass


# 简单图形 叶子组件
class Point(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "点(%s, %s)" % (self.x, self.y)

    def draw(self):
        print(str(self))


# 叶子组件
class Line(Graphic):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return "线段[%s, %s]" % (self.p1, self.p2)

    def draw(self):
        print(str(self))

l = Line(Point(3,4), Point(6,7))
# print(l) # 直接调用str函数 输出：线段[点(3, 4), 点(6, 7)]


# 复杂图形 复合组件
class Picture(Graphic):
    def __init__(self, iterable):
        self.children = [] # 将简单图形添加到叶子结点
        for g in iterable:
            self.add(g)

    def add(self, graphic):
        self.children.append(graphic)

    def draw(self):
        print("------复合图形------")
        for g in self.children:
            g.draw()
            # time.sleep(2)
        print("------复合图形------")


# 客户端
# 复杂图形一
p1 = Point(2,3)
l1 = Line(Point(3,4), Point(6,7))
l2 = Line(Point(1,5), Point(2,8))
pic1 = Picture([p1, l1, l2])

# 复杂图形二
p2 = Point(4,4)
l3 = Line(Point(1,1), Point(0,0))
pic2 = Picture([p2, l3])

# 将一二组合
pic = Picture([pic1, pic2])
pic.draw()