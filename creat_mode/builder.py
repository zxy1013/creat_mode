from abc import ABCMeta, abstractmethod

# 产品--玩家对象
class Player:
    def __init__(self, face=None, body=None, arm=None, leg=None):
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg
    def __str__(self):
        return "%s, %s, %s, %s" % (self.face, self.body, self.arm, self.leg)

# 抽象建造者--抽象工厂
class PlayerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_arm(self):
        pass

    @abstractmethod
    def build_leg(self):
        pass

# 具体建造者--具体工厂
# 表示代码
class SexyGirlBuilder(PlayerBuilder):
    def __init__(self):
        # 创建玩家对象
        self.player = Player()

    def build_face(self):
        self.player.face = "漂亮脸蛋"

    def build_body(self):
        self.player.body = "健康"

    def build_arm(self):
        self.player.arm = "漂亮胳膊"

    def build_leg(self):
        self.player.leg = "漂亮腿"

class Monster(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "怪兽脸"

    def build_body(self):
        self.player.body = "怪兽身材"

    def build_arm(self):
        self.player.arm = "怪兽胳膊"

    def build_leg(self):
        self.player.leg = "怪兽腿"

# 指挥者 Director
# 控制组装顺序 必须先有body再后面有躯干
# 构造代码
class PlayerDirector:
    def build_player(self, builder):
        builder.build_body()
        builder.build_face()
        builder.build_arm()
        builder.build_leg()
        return builder.player


# client
builder = Monster()
director = PlayerDirector()
p = director.build_player(builder)
print(p)