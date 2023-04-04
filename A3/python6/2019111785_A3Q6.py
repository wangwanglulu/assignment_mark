class Words():
    def __init__(self,args):
        self.args=args
    
    def prefix(self):
        s=0
        for i in range(len(self.args)):
            if len(self.args[i])<len(self.args[s]):
                s=i
        strs=""
        for j in range(len(self.args[s])):
            strs=self.args[s][:j]
            for k in range(len(self.args)):
                if strs!=self.args[k][:j]:
                    r=self.args[s][:j-1]
                    return(r)
                    break


x=Words(("flower","flow","flight"))
print(x.prefix())

y=Words(("apple","application","appendix","appointment"))
print(y.prefix())