def input_ratio(r):
    def scale_factor(a):
        sequence=tuple([a*r**x for x in range(0,5)])
        return sequence
    return scale_factor

gs3=input_ratio(3)
print(gs3(4))
