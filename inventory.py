#This is a Python program to prepare a presentation using a text file
#The class Shoe is defined and within that the attributes for the init method are defined

class Shoe:
    def __init__(self,country,code,product,cost,quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

#This method will return the cost of each shoe

    def get_cost(self):
        return self.cost

#This method will return the quantity of each shoe

    def get_quantity(self):
        return self.quantity

#This method uses repr and will be used when appending objects to the text file 

    def __repr__(self):
        return ("{0},{1},{2},{3},{4}".format(self.country,self.code,self.product,self.cost,self.quantity))

#This method uses the str and will be used when appending objects to the list and printing to the screen.

    def __str__(self):
        return (" Country: {0} \n Code: {1}\n Product: {2}\n Cost: {3}\n Quantity: {4}\n".format(self.country,self.code,self.product,self.cost,self.quantity))

warehouse_stock = []   #This is the empty list where objects will be appended

#This function reads the data from the text file and appends it to the list
#The user is asked to enter the text file name and using error handling if the file does not exist, a message will be displayed
#and the user will be asked to try again

def read_shoes_data():
    while True:
        try:
            file_name = input("What is the name of the file you want to view:")
            text_file_name = file_name + ".txt"
            with open(text_file_name,"r+") as f:
                for line in f:
                    object_new = list(line)
                    if "\n" in object_new:
                        object_new.remove("\n")
                    object_new2 = ''.join(object_new)
                    object_new3 = object_new2.split(",")
                    country = object_new3[0]
                    code = object_new3[1]
                    product = object_new3[2]
                    cost = object_new3[3]
                    quantity = object_new3[4]
                    stock = Shoe(country,code,product,cost,quantity)
                    warehouse_stock.append(stock)
                break
        except IOError:
            print("The file that you are trying to open does not exist.")

    warehouse_stock.remove(warehouse_stock[0])

#This function captures a new shoe and appends it to the list   
            
def capture_shoes():
    country = input("Which country is the shoe made? ")
    code = input("What is the code? ")
    product = input("What is the product name? ")
    cost = input("What is the price of the shoe? ")
    quantity = input("How many are in stock? ")
    
    stock = Shoe(country,code,product,cost,quantity)
    warehouse_stock.append(stock)
    print("") 

#This function is to output all the shoes in the text file to the user by iterating through the list using the FOR loop

def view_all():
    for stock in warehouse_stock:
        print(str(stock))
    print("") 

#This function is to return the stock with the lowest quantity
#The user is then asked if they want to add to that stock
#From there the new quantity is updated and the text file is updated 

def re_stock():
    min_stock = []
    
    for stock in warehouse_stock:
        min_stock.append(int(stock.quantity))
    
    minimum_value = min(min_stock)
    min_index = min_stock.index(minimum_value)
    min_item = warehouse_stock[min_index]
    print(min_item)
    
    restock = input("Do you want to add to the quantity? (Yes/No)")
    restock_lower = restock.lower()
    print("")
    
    if restock_lower == "yes":
        
        while True:         #This while loop is used for when the user updated the quantity and if they enter a wrong value an error message is returned and they try again
            try:
                quant = int(input("How much stock are you adding?"))
                break
            except ValueError:
                print("Invalid entry. Please try again.")
                
        new_quantity = minimum_value + quant
        min_item.quantity = str(new_quantity)
        
    elif restock_lower == "no":
        print("Okay. Returning to main menu")

    with open("inventory.txt","w+") as f:              #This is where the text file is updated using the write method
        first_line = ("Country,Code,Product,Cost,Quantity")
        f.write(first_line + "\n")
        for stock in warehouse_stock:
            f.write(repr(stock) + "\n")
    print("")

#This function is to display the object from the list when the shoe code is entered using the FOR loop

def search_shoe():
    i = 0
    while i <= 1:    #This while loop is only executed once, which is when the user enters an invalid shoe code
        if i >= 1:
            print("Item code is not valid.")
            break
        i += 1
        shoe_code = input("What is the code of the shoe you would like to see: ")
        print("") 
        for item in warehouse_stock:
            if shoe_code == item.code:
                print(item)
                i += 1
    print("")

#This is a function which returns the value for each item
#Using the get_cost and get_quantity methods defined above and the FOR loop
#Multiplying these two together will return the value for each item

def value_per_item():
    
    print("value = cost * quantity")
    for stock in warehouse_stock:
        x = int(stock.get_cost())
        y = int(stock.get_quantity())
        z = x * y
        print("The value of the shoe", str(stock.code), "is" , str(z))
    print("")

#This function returns the item that has the highest quantity and prints out that this item is on sale.  

def highest_qty():
    
    max_stock = []
    for stock in warehouse_stock:         #Thie FOR loop is to get the quantity of each item and append it to the max_stock list
        max_stock.append(int(stock.quantity))
    
    maximum_value = max(max_stock)
    max_index = max_stock.index(maximum_value)
    max_item = warehouse_stock[max_index]
    print(max_item)
    print("")
    print("This item is on SALE!")
    print("") 

#This function is to define the main menu.
#Before the main menu is displayed which is in the WHILE loop, the read_shoes_data function is called
#so that the object list is generated

def main():
    read_shoes_data() 
    while True:

#This is the main menu displayed to the user

        menu_option = input('''What would you like to          
1 - capture shoes
2 - view the inventory
3 - re_stock
4 - search for a shoe
5 - view the value per item
6 - put items on sale
7 - exit
:''')

#If the user selects "1", the capture_shoes function is called

        if menu_option == "1":
            capture_shoes()

#If the user selects "2", the view_all function is called

        elif menu_option == "2":
            view_all()

#If the user selects "3", the re_stock function is called

        elif menu_option == "3":
            re_stock()

#If the user selects "4", the search_shoe function is called

        elif menu_option == "4":
            search_shoe()

#If the user selects "5", the value_per_item function is called

        elif menu_option == "5":
            value_per_item()

#If the user selects "6", the highest_qty function is called as this returns that the item is on sale.

        elif menu_option == "6":
            highest_qty()

#If the user selects "7", the program is terminated
#but first the user is asked if they want to update in the text file
#I added this part in because if the user captures a shoe, only the list is updated and not the file
#so if the user wants all the objects in the list ti be in the text file, it is also updated here

        elif menu_option == "7":
            
            update = input("Would you like to update the inventory file? (Yes/No)")
            update_lower = update.lower()
            print("")
            
            if update_lower == "yes":                   #This is where the text file is updated. 
                with open("inventory.txt","w+") as f:
                    first_line = ("Country,Code,Product,Cost,Quantity")
                    f.write(first_line + "\n")
                    for stock in warehouse_stock:
                        f.write(repr(stock) + "\n")
                
                print("File updated. Goodbye")
                exit()
            else:
                print("Goodbye")
                exit()

        else:
            print("You have made an invalid entry. Please try again.")


main()
            






            
