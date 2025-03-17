from computer import *

class ResaleShop:
    #this is the class ResaleShop, it has the attribute inventory and the buy and sell and print inventory methods
    inventory: list

    def __init__( self, ivn: list): 
        #this initalizes any new resale shops
        self.inventory= ivn
    
    def buy(self, c: Computer): 
        #this buys the computer and adds it to the stores inventory
        self.inventory.append(c)
        
    
    def sell(self, c: Computer):
        #this sells the computer and removes it from the stores inventory
        if c in self.inventory:
            current_computer_idx=self.inventory.index(c)
            self.inventory.pop(current_computer_idx)
            
            print("Item", end= " ")
            print(c)
            print("sold!")
        else: 
            print("Item", end=" ")
            print(c)
            print("not found. Please select another item to sell.")

    def print_inventory(self):
        #this prints out all avalible items in the stores inventory. 
        if self.inventory:
            for item in self.inventory: 
                item.print_details()
        else: 
             print("No inventory to display.")

def main(): 
    computer_zero: Computer= Computer("Mac Pro 2019", "some processor", 1050, 120, "Newest OS", 2019, 2000)
    computer_one: Computer= Computer("my mac","some processor", 1024, 64 ,"old OS", 2013, 1500)
    myresaleshop: ResaleShop= ResaleShop (ivn=[computer_zero])
    myresaleshop.print_inventory()
    myresaleshop.buy(computer_one)
    myresaleshop.print_inventory()
    myresaleshop.sell(computer_zero)
    myresaleshop.print_inventory()
    other_resale_shop: ResaleShop= ResaleShop (ivn=[])
    other_resale_shop.print_inventory()
    other_resale_shop.sell(computer_zero)


if __name__== "__main__": 
    main()

    

