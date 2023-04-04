def count_numbers(fun_tobe_deco):
    def fun_deco(*args):
        print("The numbers are:")
        fun_tobe_deco(*args)
        c=len(args)
        print("There are "+str(c)+" numbers.")
    return(fun_deco)

@count_numbers
def numbers(*args):
    print(args)

numbers(1,2,3,4)
