def count_numbers(f):
    def count(*args):
        i = 0
        print("The numbers are:")
        f(*args) #在这里要保持参数个数相同！
        i= len(args)
        print("There are " + str(i) + " numbers.")
    return count #关键理解点

@count_numbers
def numbers(*args):
    print(args)

numbers(1,2,3,4)
