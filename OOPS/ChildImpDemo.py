# INHERITANCE - acquiring the properties of parent class.
from OOPS.OOPSDemo import Calculator


class ChildImpDemo(Calculator):
    number2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def getCompleteData(self):
        return self.number2 + self.num + self.summation()


obj = ChildImpDemo()
print(obj.getCompleteData())
