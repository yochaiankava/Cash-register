# Cash-register
20.3.2023
Yochai Ankava

My Shop Project
The software manages sales, products, and customers in the store
The operations are carried out by 5 different programs:

1.Utiles
holds the classes:
class MyShopMenuEnum 
- Holds the Enum values of the menu in the main program
class MyShopCategoriesEnum
- Holds the Enum values of the categories menu in the customer program

2.Customer
holds the classes:
class customer
methods inside class:
-def__init__ - constructor method
-def __str__ - print customer details
Class customerList
methods inside class:
-def __init - Initializes the customer list and the load all customers method
-def __load all customers – load the customers list from the customers json file
-def __save all customers – save the data\changes on the json customers json file
-def __add customer – add customer to json file\customers list
-def__remove customer - remove customer from json file\customers list
-def__add to purchaseid - adds a purchase number to the customer shopping history list
-deff__get customer by phone number
-def__get customer by name
-def__customer by last name 
-def_check credentials - Checks the correctness of the user's username and password, which is necessary before deleting a customer from the customer list
def__str__ – print the customers list

3.Product
holds the classes:
class product
methods inside class:
-def__init__- constructor method
-def__str__ - print the customer details
Class ProductList
methods inside class:
-def __init - Initializes the product list and the load all customers method
-def __load all customers – load the products list from the products json file
-def __save all products – save the data\changes on the json products json file
-def __add product – add product to json file\products list
-def__remove product - remove product from json file\products list
-def__edit_product_amount – updates the number of units/kg in stock for the product
-def edit_product_price 
-def edit_product_category - updates the category of the product according to the selection from the existing options
-def product_category – categories menu
-def get_product_by_id
- def get_product_by_name
-def get_product_by_category - generates a list of products for a selected category
-def __str__ -print the products list

4.purchase
holds the classes:
class Purchase
methods inside class:
-def__init__- constructor method
-def__str__ - print the purchase details
class PurchaseList
methods inside class:
-def __init - Initializes the all purchase list and the load all purchases method
-def __load all purchases – load the purchases list from the purchases json file
-def __save all purchases – save the new data\changes on the json purchases json file
-def __add purchase – add new purchase to json file\all purchases list
-def new_purchase - generates a new customer purchase
-def get_purchase_by_id
-def find_last_purchase_id - finds the number of the last purchase in the list to determine the next purchase number
-def find_purchases_between_dates - finds all purchases between selected dates and summarizes the total price for the purchases

5.main
The program holds all the methods for selecting the execution of the actions in the main menu:
-def menu_add_customer
-def menu_delete_customer
-def menu_find_customer_by_phone_number
-def menu_add_product
-def menu_delete_product
-menu_find_product_by_id
-def menu_find_product_by_name
-def menu_find_product_by_category
-def manu_edit_product_price
-def manu_edit_product_amount
-def manu_edit_product_category
-def menu_add_purchase
-def manu_find_purchase_by_id
-def menu_find_purchases_between_dates

