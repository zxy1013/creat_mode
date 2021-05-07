from abc import ABCMeta, abstractmethod

# 抽象实体
class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self, content):
        pass

# 实体
class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        f = open(filename, 'r', encoding='utf-8')
        print("读取文件内容")
        self.content = f.read()
        f.close()

    def get_content(self):
        return self.content

    def set_content(self, content):
        f = open(self.filename, 'w', encoding='utf-8')
        f.write(content)
        f.close()


# subj = RealSubject("test.txt") # 只要实例化了 即使以后不执行subj.get_content() content属性也会一直存在 从而占用很大内存


# 代理
# 虚代理 实现Subject接口 目的是和RealSubject保持一致
# 构造对象时不占用空间存储content 只有当调用get_content()方法时才真正从文件中读取信息
class VirtualProxy(Subject):
    def __init__(self, filename):
        self.filename = filename # 构建时只是存储了一个文件名的字符串
        self.subj = None

    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename) # 创建真实对象 读取文件内容
        return self.subj.get_content()

    def set_content(self, content):
        if not self.subj:
            self.subj = RealSubject(self.filename)
            print(1111) # set_content("abc")时不打印
        return self.subj.set_content(content)


# subj1 = VirtualProxy("test.txt")
# print(subj1.get_content()) # 读取文件内容 嘻嘻
# subj1.set_content("abc")


# 保护代理
class ProtectedProxy(Subject):
    def __init__(self, filename):
        self.subj = RealSubject(filename) # 复用RealSubject的代码

    def get_content(self):
        return self.subj.get_content()

    def set_content(self, content): # 可以写入验证代码
        raise PermissionError("无写入权限")

# 只有读的权限 没有写的权限
subj = ProtectedProxy("test.txt")
print(subj.get_content())
subj.set_content("abc") # PermissionError: 无写入权限