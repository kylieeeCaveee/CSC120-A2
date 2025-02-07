import computer

class ResaleShop:
    #this is the class ResaleShop, it has the attribute inventory and the buy and sell and print inventory methods
    inventory: list

    def __init__( self, ivn: list): 
        #this initalizes any new resale shops
        self.inventory= ivn
    
    def buy(self,comp: computer): 
        #this buys the computer and adds it to the stores inventory
        self.inventory.append(comp)
        return self.inventory.index(comp)
    
    def sell(self,comp: computer):
        #this sells the computer and removes it from the stores inventory
        if comp in self.inventory:  
            self.inventory.pop(comp)
            print("Item", comp, "sold!")
        else: 
            print("Item", comp, "not found. Please select another item to sell.")

    def print_inventory(self):
        #this prints out all avalible items in the stores inventory. 
        if self.inventory:
            for item in self.inventory: 
                print( item, item.print_details())
        else: 
             print("No inventory to display.")

    # What methods will you need?- buy method, sell method, print inventory method