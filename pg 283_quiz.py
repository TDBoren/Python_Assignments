x = 10.50
print(x)
print(type(x))
 
x = float("10.50")
print(x)
print(type(x))
 
 
class Data:
    id = 0.0
 
    def __init__(self, i):
        self.id = i
 
    def __float__(self):
        return float(self.id)
 
 
d = Data(10.50)
 
x = float(d)
print(x)
print(type(x))
 
d = Data(10)
x = float(d)
print(x)
print(type(x))
