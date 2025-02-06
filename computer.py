class Computer:
    #This is the computer class- it has the attributes: desciption, processor_type, hard_drive_capactiy, 
    # memory, operating_system, year_made, price. It contains the methods update_price, update_OS, 
    # and refurbish, and print_details. 
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

    def refurbish(new_os: Optional[str] = None): 
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
    
    def print_details(): 
        #this function prints all the attributes of a computer
        print ("Description:", self.description, "Proccessor:", self.processor, "Hard Drive Capacity:", self.hard_drive_capacity, "Memory", self.memory, "Operating System:", self.operating_system, "Year:", self.year_made, "Price:", self.price)

def main(): 
    myComputer: Computer= Computer("my mac","some processor", 1024, 64 ,"old OS", 2013, 1500)
    print (myComputer)
    myComputer.update_price("1000000")
    myComputer.update_OS("newest OS")
    print(myComputer)
    myComputer.refurbish("epic OS")
    print (myComputer)

if __name__== "__main__": 
    main()

   