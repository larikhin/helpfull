class MyFirstClass:
    print('scaning of MyFirstClass, once, before using.')


class MySecondClass:
    print('scaning of MySecondClass, once, before using.')


class MyThirdClass:
    print('scaning of MyThirdClass, once, before using.')
    i=0
    print('Setting attrbutes i in MyThirdClass =' + str(i))
    def def_1(self):
        print('def_1 of MyThirdClass, it appears only after call it')
    def def_2(self):
        print('def_2 of MyThirdClass')
print('_______________________________________\n')


print('creates new instance of MySecondClass()')
two = MySecondClass()
print('_______________________________________\n')

print('creates new instance of MyThirdClass()')
tree = MyThirdClass()
print('p = tree.def_1')
p = tree.def_1
print('call method def_1 in instatnce MyThirdClass()')
p()
print('call MyThirsClass and call def_2 method')
p = MyThirdClass().def_2
p()

MyThirdClass().def_2()

print('______________________________________\n')

class MyFourth_1_Class:
    print('scaning of MyFourth_1_Class, once, before using.')
    i=0
    print('Setting attrbutes i = 0 in MyFourth_1_Class')
   # def __init__(self):
   #     print('__init__ in MyFourth_1_Class')
    def def_1(self):
        print('def_1 of MyFourth_1_Class, it appears only after call it')
    def def_2(self):
        print('def_1 of MyFourth_1_Class')


print('Create new instatnce of Fourth_1_Class')
four = MyFourth_1_Class()
print('call method def_1 in MyFourth_1_Class ')
four.def_1()


print('_______________________________________\n')
class MyFourth_2_Class:
    print('scaning of MyFourth_2_Class, once, before using.')
    i=0
    print('Setting attrbutes i = 0 in MyFourth_2_Class')
    def __init__(self, name):
        print('__init__ in MyFourth_2_Class')
        self.name = name
    def def_1(self):
        print('def_1 of MyFourth_2_Class, it appears only after call it')
    def def_2(self):
        print(self.name)


print('Create new instatnce of Fourth_2_Class')
four2 = MyFourth_2_Class('Some_name')
print('call method def_1 in MyFourth_2_Class ')
four2.def_1()
print('call method def_2 in MyFourth_2_Class ')
four2.def_2()
