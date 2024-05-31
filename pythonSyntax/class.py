class Simple:
    pass
a = Simple()

class Service:
    secret = "hello"
    def sum(self, a, b):
        result = a + b
        print("%s + %s = %s" % (a, b, result))
        print(self)
    
# pey = Service()
# print(pey.sum(1,2))
# print(pey.secret)

class fCal():
    def setData(self, a, b):
        self.a = a
        self.b = b
    def sum1(self):
        result = self.a + self.b
        return result
    def sup(self):
        result = self.a - self.b
        return result
    def mul(self):
        result = self.a * self.b
        return result
    def div(self):
        result = self.a / self.b
        return result
    
# c = fCal()
# c.setData(1,12)
# print(c.sum1(), c.sup(), c.div(), c.mul())

class Travel:
    firstname = "kim"
    def __init__(self, name):
        self.name = name
    def travel(self, where, day):
        print(self.firstname+self.name+where+str(day))
hasung = Travel("hasung")
hasung.travel("독도", 3)