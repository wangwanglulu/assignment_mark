class Food():
    def __init__(self,name,price):
        self.name=name
        self.price=price
        
    def get_info(self):
        print(self.name+" has a price of "+str(self.price)+".")
    
    def update_price(self,num):
        self.price=num

food_1 = Food('Hot Dog', 15)
food_1.get_info()
food_1.update_price(20)
food_1.get_info()

class Fruit(Food):
    def __init__(self,name,price,area):
        self.name=name
        self.price=price
        self.area=area
    
    def show_area(self):
        print(self.name+" is produced in "+self.area+".")

fruit_1 = Fruit('Orange', 5, 'California')
fruit_1.show_area()
