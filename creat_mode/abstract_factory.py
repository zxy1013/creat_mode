from abc import abstractmethod, ABCMeta

# 抽象产品
class PhoneShell(metaclass=ABCMeta):
    @abstractmethod
    def show_shell(self):
        pass

class CPU(metaclass=ABCMeta):
    @abstractmethod
    def show_cpu(self):
        pass

class OS(metaclass=ABCMeta):
    @abstractmethod
    def show_os(self):
        pass

# 抽象工厂
class PhoneFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_shell(self):
        pass

    @abstractmethod
    def make_cpu(self):
        pass

    @abstractmethod
    def make_os(self):
        pass

# 具体产品
class SmallShell(PhoneShell):
    def show_shell(self):
        print("普通手机小手机壳")

class BigShell(PhoneShell):
    def show_shell(self):
        print("普通手机大手机壳")

class AppleShell(PhoneShell):
    def show_shell(self):
        print("苹果手机壳")

class SnapDragonCPU(CPU):
    def show_cpu(self):
        print("骁龙CPU")

class MediaTekCPU(CPU):
    def show_cpu(self):
        print("联发科CPU")

class AppleCPU(CPU):
    def show_cpu(self):
        print("苹果CPU")

class Android(OS):
    def show_os(self):
        print("Android系统")

class IOS(OS):
    def show_os(self):
        print("iOS系统")

# 具体工厂
# 当 MiFactory只有SnapDragonCPU Android BigShell的三者组合时就可以用此方法
# 每个工厂生产一套对象
class MiFactory(PhoneFactory):
    def make_cpu(self):
        return SnapDragonCPU()

    def make_os(self):
        return Android()

    def make_shell(self):
        return BigShell()

class HuaweiFactory(PhoneFactory):
    def make_cpu(self):
        return MediaTekCPU()

    def make_os(self):
        return Android()

    def make_shell(self):
        return SmallShell()

class IPhoneFactory(PhoneFactory):
    def make_cpu(self):
        return AppleCPU()

    def make_os(self):
        return IOS()

    def make_shell(self):
        return AppleShell()

# 客户端 将其链接起来变为手机对象
class Phone:
    def __init__(self, cpu, os, shell):
        self.cpu = cpu
        self.os = os
        self.shell = shell

    def show_info(self):
        print("手机信息:")
        self.cpu.show_cpu()
        self.os.show_os()
        self.shell.show_shell()

def make_phone(factory):
    cpu = factory.make_cpu()
    os = factory.make_os()
    shell = factory.make_shell()
    return Phone(cpu, os, shell)

# 参数传递 IPhoneFactory() HuaweiFactory() MiFactory()
p1 = make_phone(MiFactory())
p1.show_info()