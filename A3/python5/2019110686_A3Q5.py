class Num():
    def __init__(self,nums):
        self.nums=nums
    def sip(self,num):
        if num in self.nums:
            a=0
            for n in self.nums:
                if n==num:
                    return a
                a=a+1
        else:
            a=0
            for n in self.nums:
                if num<n:
                    return a
                a=a+1
x=Num((1,2,5,8,13,19))
print(x.sip(5))            
x=Num((1,2,5,8,13,19))
print(x.sip(15))
