class Words():
    def __init__(self,array):
        self.array=array
    def prefix(self):
        b=[]
        for word in self.array:
            a=list(word)
            b.append(a)
        z=len(self.array)
        c=0
        f=[]
        for d in b:
            e=len(d)
            f.append(e)
        g=min(f)
        v=[]
        while c<int(g):
            h=[l[c] for l in b]
            j=h[0]
            for k in range(z):
                if j in h:
                    h.remove(j)
            if not h:
                v.append(j)
            c=c+1
        t=''
        for w in v:
            t=t+w
        return t   
x=Words(("flower","flow","flight"))
print(x.prefix())            
y=Words(("apple","application","appendix","appointment"))
print(y.prefix())