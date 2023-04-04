def input_ratio(r):
    def difi(x):
        return(x,x*r,x*r**2,x*r**3,x*3**4)
    return difi
gs3=input_ratio(3)
print(gs3(4))
