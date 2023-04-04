class Num():
    def __init__(self,numbers):
        self.numbers = numbers
        
    def sip(self,y):
        i = 0
        for number in self.numbers:
            if y == number:
                return i
                break
            elif y < number:
                return i
                break
            else:
                i += 1

x=Num((1,2,5,8,13,19))
print(x.sip(15))
