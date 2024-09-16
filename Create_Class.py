#create a computer class


#类的使用

# class Computer:
#         #赋值语句描述电脑类的两个属性
#         CPU = True
#         screen = True
#         #def 方法名(self)创建实例方法
#         def start(self):
#             print('正在开机中……')
#             #调用电脑类
# my_computer = Computer()
# print(my_computer.CPU)
# print(my_computer.screen)


# #类的两个关键点：
#         #特殊参数self,所有实力的替身，实例对象创建后，实例会代替self运行
#           #只要在类中用def创建语法时，就必须把第一个参数位置留给self,并在调用时忽略它.
# class Chinese: 
#     name = '张三'
#     def say(self):
#         print(self.name + '是中国人')

# person = Chinese()
# print(person.name)
# person.say()
#         #初始化方法

        #def __init __(self):
        #作用：当每个实例对象创建的时候，该方法内的代码不需要调用就可以自动运行
# class Chinese:
#     def __init__(self):
#         self.mouth = 1
#         self.eye = 2
#     def body(self):
#         print(f"我有{self.mouth}张嘴巴")
#         print("我有{}只眼睛".format(self.eye))
# person = Chinese()
# person.body()


# #electrcity_class
class Dog:
    def ___init__(self,name,gender,energy,weight):
        self.name = name
        self.gender = gender
        self.energy = energy
        self.weight = weight
        print(f'你好，我的名字时{self.name},我是{self.gender},很高兴成为你的小伙伴')
    def eat(self,food):
        if food == 'hamberger':
            self.energy += 10
            self.weight =+ 5
            print('汉堡包真好吃')
        else:
            self.weight += 2
            print('美味')
    def run(self):
        pass
    def display(self):
        print(f'我当前的能量值为{self.energy}')
        print(f'我当前的体重为{self.weight}')
        if self.energy <40:
            print('需要补充energy')
        elif self.weight > 50:
            print('weight_out')
        else:
            print('i am very healthy')
haha = Dog('卡尔',"男孩",50,20)
haha.display()
haha.eat('hamberger')



