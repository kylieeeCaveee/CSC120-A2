Use this file to record your reflection on this assignment. 

What worked, what didn't, what advice would you give someone taking this course in the future?

The hardest part of the assignment for me was getting the error messages to work. I went from being confused on how to get the proper error message to even occur because I thought that the program just wouldn't compile if you were to put in any of the errors because I assumed that would require putting a non-existent computer object in the sell or update_price methods. However, then I realized that if you created an alternative computer object and used that to trigger the error it would work and still compile. An example of what I mean is featured below. Along with an example of me creating another resale shop that does not contain the created computer_zero object to cause the sell error. 

Calls the "Item not found. Cannot update price.": 
 otherComputer: Computer= Computer("someone elses computer", "other mac","some processor", 1024, 64 ,"old OS", 2013, 1500)
 myComputer.update_price("otherComputer", 2000)

Calls the "Item not found. Please select another item to sell.": 
other_resale_shop: ResaleShop= ResaleShop (ivn=[])
other_resale_shop.sell(computer_zero)

However, after realizing that I ran into antother issue which was how to get the id of the computer in the error message. At the time the computer class did not have any "name" attributes which made it so that any time i tried to acess the name of the computer it would return something along the lines of computer object at *space in memory*. Then i added the item_id attribute to the computer class and a get_item_id function which allowed me to access the item_id from the resale shop class. 

Those were my two major problems that I had to overcome. Aside from that and a few small bug errors like including self with each method and importing the "from typing import Dict, Optional". Everything went pretty smoothly! 

The adivce I would give to someone taking this course is to think about what attributes the computer should have as thinking about what items would be on a like price/feature sticker for that computer. The item_id, price, processor etc. would be on this sticker. However the store inventory would not. Additioanlly methods that would change anything on that sticker should be in the computer class and everything else should be in the resale class. 