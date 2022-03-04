def add(*args):
    sum = 0
    for n in range(len(args)):
        sum += args[n]
    print(sum)

def multiply(*args):
    total = 0
    for n in range(len(args)):
        total *= args[n]
    print(total)


class Calculator:
    def __init__(self, **kw):
        self.direction = kw.get("direction")
        self.first_value = kw.get("first_value")
        self.second_value = kw.get("second_value")
    
    def calculate(self):
        if self.direction == "multiply":
            multiply(self.first_value, self.second_value)
        else:
            add(self.first_value, self.second_value)

class Result(Calculator):
    def __init__(self, **kw):
        super().__init__(**kw)
        pass



choice = input("Do you want to multiply or add : ")
first_value = int(input("Enter first value: "))
second_value = int(input("Enter second value : "))

result = Result(direction=choice, first_value=first_value, second_value=second_value)
result.calculate()