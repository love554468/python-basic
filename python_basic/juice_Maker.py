class Juice:
    def __init__(self,name,capacity) -> None:
        self.name = name
        self.capacity = capacity
    def __add__(self,other):
        return self.name +"&"+other.name+"\n"+str(self.capacity+other.capacity)

a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)
result = a + b
print(result)