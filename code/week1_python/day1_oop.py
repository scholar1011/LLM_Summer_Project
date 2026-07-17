import sys
print(sys.executable)
class Student:
    def __init__(self,name,age,stu_id):
        self.name=name
        self.age=age
        self.stu_id=stu_id
    def introduce(self):
        print(f'姓名：{self.name}，年龄：{self.age}，学号：{self.stu_id}')
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print('动物发出声音')
class Dog(Animal):
    def __init__ (self,name):
        super().__init__(name)
    def speak(self):
        print('小狗汪汪叫')
class Demo:
    testname="三类测试"
    def __init__(self,hao):
        self.hao=hao

    def p (self):
        print(f"{self.hao}{Demo.testname}")
    @classmethod
    def p1 (cls) :
        print(f'{Demo.testname}')
    @staticmethod
    def p2 ():
        print("欢迎使用")