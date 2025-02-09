from typing import Dict, Optional
class Computer:
    #This is the computer class- it has the attributes: item_id, desciption, processor_type, hard_drive_capactiy, 
    # memory, operating_system, year_made, price. It contains the methods update_price, update_OS, 
    # and refurbish, print_details, and get_name() function.
    item_id: str
    description:str
    processor_type:str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made:int
    price: int
    
   
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, itm_id: str, des:str, pt:str, hdc: int, mem: int, os: str, ym:int, p: int):
        #this initializes a new computer and all of it's corresponding variables
        self.item_id=itm_id
        self.description= des
        self.processor_type= pt
        self.hard_drive_capacity=hdc
        self.memory= mem
        self.operating_system= os
        self.year_made= ym
        self.price= p
        
    
    def update_price(self, itm_id: str, new_price: int): 
        #this updates the price of the computer to the price given to the function
        if itm_id== self.item_id: 
            self.price= new_price
        else: 
             print("Item", itm_id , "not found. Cannot update price.")
        
    def update_OS(self,new_OS: str): 
        #this updates the OS of the computer to the new OS given
        self.operating_system= new_OS

    def refurbish(self, new_os: Optional[str] = None): 
        #this function refurbishes the computer which updates the OS and the price
        if self.year_made < 2000:
             self.price = 0 # too old to sell, donation only
        elif self.year_made < 2012:
             self.price= 250 # heavily-discounted price on machines 10+ years old
        elif self.year_made < 2018:
             self.price = 550 # discounted price on machines 4-to-10 year old machines
        else:
             self.price= 1000 # recent stuff

        if new_os is not None:
             self.operating_system = new_os # update details after installing new OS
    
    def print_details(self): 
        #this function prints all the attributes of a computer
        print ("-----", self.item_id, "-------", "\n" "Description:", self.description, "\n" "Proccessor:", self.processor_type, "\n" "Hard Drive Capacity:", self.hard_drive_capacity, "\n" "Memory", self.memory, "\n" "Operating System:", self.operating_system, "\n" "Year:", self.year_made, "\n" "Price:", self.price, "\n" "---------------------")

    def get_item_id(self):
        #this method prints out the item_id of the computer
        print (self.item_id, end= " ")
        

def main(): 
    myComputer: Computer= Computer("my computer", "my mac","some processor", 1024, 64 ,"old OS", 2013, 1500)
    myComputer.print_details()
    myComputer.update_price("my computer", 10000)
    myComputer.update_OS("newest OS")
    myComputer.print_details()
    myComputer.refurbish("epic OS")
    myComputer.print_details()
    otherComputer: Computer= Computer("someone elses computer", "other mac","some processor", 1024, 64 ,"old OS", 2013, 1500)
    myComputer.update_price("otherComputer", 2000)
    myComputer.get_name()
    print("test")

if __name__== "__main__": 
    main()

   