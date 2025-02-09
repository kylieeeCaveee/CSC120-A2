from computer import *

class ResaleShop:
    #this is the class ResaleShop, it has the attribute inventory and the buy and sell and print inventory methods
    inventory: list

    def __init__( self, ivn: list): 
        #this initalizes any new resale shops
        self.inventory= ivn
    
    def buy(self, itm_id: str, des:str, pt:str, hdc: int, mem: int, os: str, ym:int, p: int): 
     
        #this buys the computer and adds it to the stores inventory
        itm_id: Computer = Computer (itm_id, des, pt, hdc, mem, os, ym, p)
        self.inventory.append(itm_id)
        
    
    def sell(self, itm_id: Computer):
        #this sells the computer and removes it from the stores inventory
        if itm_id in self.inventory:
            current_computer_idx=self.inventory.index(itm_id)
            self.inventory.pop(current_computer_idx)
            
            print("Item", end= " ")
            itm_id.get_item_id()
            print("sold!")
        else: 
            print("Item", end=" ")
            itm_id.get_item_id()
            print("not found. Please select another item to sell.")

    def print_inventory(self):
        #this prints out all avalible items in the stores inventory. 
        if self.inventory:
            for item in self.inventory: 
                item.print_details()
        else: 
             print("No inventory to display.")

def main(): 
    computer_zero: Computer= Computer("computer_zero", "Mac Pro 2019", "some processor", 1050, 120, "Newest OS", 2019, 2000)
    myresaleshop: ResaleShop= ResaleShop (ivn=[computer_zero])
    myresaleshop.print_inventory()
    myresaleshop.buy("computer_one", "Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500)
    myresaleshop.print_inventory()
    myresaleshop.sell(computer_zero)
    myresaleshop.print_inventory()
    other_resale_shop: ResaleShop= ResaleShop (ivn=[])
    other_resale_shop.print_inventory()
    other_resale_shop.sell(computer_zero)


if __name__== "__main__": 
    main()

    

