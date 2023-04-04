def count_numbers(fune):
    def decorate(*args):
        print("The numbers are:")
        fune(*args)
        print("There are",len(args),"numbers.")
    return decorate
@count_numbers
def numbers(*args):
    print(args)
numbers(1,2,3,4)
