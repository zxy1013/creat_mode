from abc import ABCMeta, abstractmethod

# 抽象处理者
class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handle_leave(self, day):
        pass


# 具体处理者
# 总经理处理十天之内的假期
class GeneralManager(Handler):
    def handle_leave(self, day):
        if day <= 10:
            print("总经理准假%d天"%day)
        else:
            print("总经理说：你还是辞职吧")

# 部门经理处理5天之内的假期
class DepartmentManager(Handler):
    def __init__(self):
        self.next = GeneralManager()

    def handle_leave(self, day):
        if day <= 5:
            print("部门经理准假%s天"%day)
        else:
            print("部门经理职权不足")
            self.next.handle_leave(day)

# 项目主管
class ProjectDirector(Handler):
    def __init__(self):
        self.next = DepartmentManager()

    def handle_leave(self, day):
        if day <= 3:
            print("项目主管准假%d天"%day)
        else:
            print("项目主管职权不足")
            self.next.handle_leave(day)


# Client只向第一级主管提出申请 当职权不足时由此对象自动向上级继续提出申请
# Client不需要知道是谁处理的
day = 7
h = ProjectDirector()
h.handle_leave(day)