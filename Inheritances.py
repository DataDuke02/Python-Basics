class app1:

    def v1(self):
        print("I am from app1 class")

class app2(app1):

    def v2(self):
        print("i am from app2")

    def v1(self):
        print("i now belongs to app2 as well")

a1 = app1()
a2 = app2()
a2.v1()
a2.v2()


class Dad:
    def house(self):
        print("White House".upper())

d= Dad()
d.house()
