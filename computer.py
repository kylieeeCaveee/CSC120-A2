class Computer:
    #This is the computer class- it has the attributes: desciption, processor_type, hard_drive_capactiy, 
    # memory, operating_system, year_made, price. It contains the methods update_price, update_OS, 
    # and refurbish.
    description:str
    processor_type:str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made:int
    price: int
   
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(des:str, pt:str, hdc: int, mem: int, os: str, ym:int, p: int):
        #this initializes a new computer and all of it's corresponding variables
        self.description= des
        self.processor_type= pt
        self.hard_drive_capacity=hdc
        self.memory= mem
        self.operating_system= os
        self.year_made= ym
        self.price= p
    
    def update_price(new_price: int): 
        #this updates the price of the computer to the price given to the function
        self.price= new_price
        
    def update_OS(new_OS: str): 
        #this updates the OS of the computer to the new OS given
        self.operating_system= new_OS

    def refurbish(new_OS, new_price): 
        #this function refurbishes the computer which updates the OS and the price
        update_price(new_price)
        update_OS (new_OS)

def main(): 
    myComputer: Computer= Computer("my mac","some processor", 1024, 64 ,"old OS", 2013, 1500)
    print (myComputer)
    myComputer.update_price("1000000")
    myComputer.update_OS("newest OS")
    print (myComputer)

if __name__== "__main__": 
    main()

    # What methods will you need?