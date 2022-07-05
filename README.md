# Inventory #
## Overview ##
This is a Python program to read a text file data (inventory.txt) and display certain aspects of the data from the text file when called, as well as update the inventory
file if new shoes have been added. This program makes use of classes, the class name for this program is called Shoe and has the following attributes:
1. country
2. code
3. product
4. cost
5. quantity

The class also has the follwoing methods:
1. get_cost - return the cost of that particular shoe
2. get_quantity - returns the quantity of that particular shoe
3. repr - this is to display the shoe object in a specific format
4. str - this is to display the shoe object in a different format to __repr__

The data which is read from the text file is stored in a list named warehouse_stock. This is to allow for easy access to the data when performing operations in the 
program. The program has the following methods which are separate from the class methods:
1. read_shoes_data - this method reads the data from the text file and appends it to the list. The user is asked to enter the text file name and using error handling
if the file does not exist, a message will be displayed and the user will be asked to try again.
2. capture_shoes - this method captures a new shoe and appends it to the list
3. view_all - this method is to output all the objects in the text file to the user by iterating through the list.
4. re_stock - This method is to return the stock with the lowest quantity, the user is then asked if they want to add to that stock. From there the new quantity
is updated and the text file is updated
5. search_shoe - this method is to display the object from the list when the shoe code is entered by the user. 
6. value_per_item - this is a method which returns the value for each item, using the get_cost and get_quantity methods defined above. Multiplying these two
together will return the value for each item
7. highest_qty - this method returns the item with the highest quantity. 
8. main - this is the menu that is displayed to the user and calls the methods above depending on the users choice.

In the main, the first method which is called is the read_shoes_data, this is to have the items in the list for ease of access. The main method has the following 
menu option displayed to the user:
1. capture shoes - this calls the capture_shoes method
2. view the inventory - this calls the view_all method
3. re_stock - this calls the re_stock method
4. search for a shoe - this calls the search_shoe method
5. view the value per item - this calls the value_per_item method
6. put items on sale - this calls the highest_qty method
7. exit - this will exit the program, but first giving the user the option to update the inventory.txt file. 

## Motivation ##
This program was design for my final capstone project using Python in my software engineering course 

## Build status ##
This program was developed with no errors or bugs. If there is any it is something that I have missed and did not correct.

## Installation ##
To run this program, Python has to be installed on the users laptop or computer. Thereafter, right-click on the program and select "Edit with IDLE", to run the 
program press F5. Where ever user input is required, enter what is required and press "Enter". 
