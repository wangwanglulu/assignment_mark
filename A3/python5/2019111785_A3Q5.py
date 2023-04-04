class Num():
    def __init__(self,args):
        self.args=args
    
    def sip(self,target):
        l=0
        for i in self.args:
            l=l+1
        j=0
        while j<=l:
            if target<=self.args[j]:
                return(j)
            j=j+1

x=Num((1,2,5,8,13,19))
print(x.sip(5))
                
x=Num((1,2,5,8,13,19))
print(x.sip(15))
