from product import Product, ProductList
from customer import Customer, CustomerList
from utiles import MyShopMenuEnum
from purchase import PurchaseList

# starting program ------------
customers_list = CustomerList()
products_list = ProductList()
purchase_list = PurchaseList()

def menu_add_customer(customers_list):
    print("adding customer")
    try:
        phone_number = int(input("what is the customer phone number?"))
        if customers_list.get_customer_by_phone_number(phone_number) == None:
            name = input("what is the customer name?")
            last_name = input("what is the customer last name?")
            # creating a new customer object!
            customer = Customer(name = name, last_name = last_name, phone_number = phone_number)
            customers_list.add_customer(customer)
            print(customer)
            print()
        else:
            print("there is alredy customer with this phone_number ")   
            print()     
    except Exception as e:
            print(f"customer data is mising: {e}")  
            print()  
                      
def menu_delete_customer(customers_list):
    input_username = input("Enter your username: ")
    input_password = input("Enter your password: ")  
    print()  
    if customers_list.check_credentials(input_username, input_password):
        print("Login successful!")
        print()
        phone_number = int(input("what is the customer phone number?"))
        customer = customers_list.get_customer_by_phone_number(phone_number)
        phone_number = customers_list.get_customer_by_phone_number(customers_list)
        if customer != None:
            print(customer)
            print()   
            delete = input("do you want to delete this customer? press - y to delete ")
            print()  
            if delete == "y":
                customers_list.remove_customer(customer)
                print("customer is deleted from customers list ")
                print()            
            else:
                pass
        else:
            print("phone_number not in customers list")
            print()
    else:
        print("Invalid username or password.")
        print()     
           
def menu_find_customer_by_phone_number(customers_list):
    try:
        phone_number = int(input("what is the phone_number? "))
        print()
        customer = customers_list.get_customer_by_phone_number(phone_number)
        if customer != None:
            print(customer)
            print()
        else:
            print("phone_number not in customer list")
            print()
    except Exception as e:
        print(f"{e}")    
        print()
                   
def menu_add_product(products_list):
    print("adding product")
    try:
        ProductID = int(input("what is the ProductID?"))
        if products_list.get_product_by_id(ProductID) == None:   
            ProductName = input("what is the ProductName?")
            UnitPrice = float(input("what is the product UnitPrice?"))
            CategoryID = products_list.product_category()
            amount_in_stock = float(input("what is the Product amount_in_stock?"))
            # creating a new product object!
            product = Product(ProductID = ProductID, ProductName = ProductName, CategoryID = CategoryID, UnitPrice = UnitPrice or 0, amount_in_stock = amount_in_stock or 0)
            products_list.add_product(product)
            print(product)
            print()            
        else:
            print("there is alredy product with this ID ") 
            print()   
    except Exception as e:
            print(f"product data is mising: {e}")    
            print()
            
def menu_delete_product(products_list):
    try:
        ProductID = int(input("what is the ProductID? "))
        print()
        product = products_list.get_product_by_id(ProductID)
        if product:
            print(product)   
            delete = input("do you want to delete this product? press - y to delete ")  
            print()
            if delete == "y":
                products_list.delete_product(product) 
                print("product deleted from products list") 
                print()          
            else:
                pass
        else:
            print("ID not in products list")
            print()
    except Exception as e:
        print(f"{e}")    
        print()
             
def menu_find_product_by_id(products_list):
    try:
        ProductID = int(input("what is the ProductID? "))
        print()
        product = products_list.get_product_by_id(ProductID)
        if product != None:
            print(product)
            print()
        else:
            print("product id does not exist")
            print()
    except Exception as e:
        print(f"{e}")    
        print()
            
def menu_find_product_by_name(products_list):
    try:
        ProductName = input("what is the Name?")
        print()
        product = products_list.get_product_by_name(ProductName)
        print(product) 
        print() 
    except Exception as e:
        print(f"{e}")    
        print()
        
def menu_find_product_by_category(products_list):
    try:
        CategoryID = int(input("what is the category?"))
        print()
        result = products_list.get_product_by_category(CategoryID)
        for r in result:
            print(r)            
        print()  
    except Exception as e:
        print(f"{e}")    
        print()
              
def manu_edit_product_price(products_list):
    try:
        ProductID = int(input("what is the ProductID? "))
        newUnitPrice = float(input("what is the newUnitPrice? "))
        products_list.edit_product_price(ProductID, newUnitPrice)
        print()
    except Exception as e:
        print(f"{e}")    
        print()
        
def manu_edit_product_amount(products_list):
    try:
        ProductID = int(input("what is the ProductID? "))
        amount = float(input("What is the amount to add? "))
        products_list.edit_product_amount(ProductID, amount)
        print()
    except Exception as e:
        print(f"{e}")    
        print()
        
def manu_edit_product_category(products_list):
    try:
        ProductID = int(input("what is the ProductID? "))    
        products_list.edit_product_category(ProductID)
        print()
    except Exception as e:
        print(f"{e}")    
        print()            
    
def menu_add_purchase(purchase_list):
    try:
        print("new purchase ")
        purchase_list.new_purchase()
    except Exception as e:
        print(f"{e}")    
        print()
    
def manu_find_purchase_by_id(purchase_list):
    try:
        purchaseid = int(input("what_is_the_purchase_id? "))
        print()
        purchase = purchase_list.get_purchase_by_id(purchaseid)
        if purchase != None:
            print(purchase)
            print()
        else:
            print("purchase id does not exist ")
            print()
    except Exception as e:
        print(f"{e}")    
        print()
        
def menu_find_purchases_between_dates(purchase_list):
    try:
        start_date = input("Please enter a start date in this format-dd/mm/yyyy- ")
        end_date = input("Please enter an end date in this format-dd/mm/yyyy- ") 
        purchases_data = purchase_list.find_purchases_between_dates(start_date, end_date)   
        for purchase in purchases_data:
            print(purchase) 
        print()              
    except Exception as e:
                print(f"{e} - wrong date format")  
                print() 
                                         
while True:
    command = input("what is the command?\n"
                     "1 - add new customer.\n"
                     "2 - delete customer from list.\n"
                     "3 - find customer by phone number.\n"
                     "4 - new purchase.\n"
                     "5 - add new product.\n"
                     "6 - delete product.\n"
                     "7 - find product by id\n"
                     "8 - find product by name\n"
                     "9 - find product by category\n"
                     "10 - edit product unit price\n"
                     "11 - edit product amount\n"
                     "12 - edit product category\n"
                     "13 - find_purchase_by_id\n"
                     "14 - find_purchases_between_dates\n"
                     "20 - exit ")
    print()
                     
    if command == MyShopMenuEnum.ADD_CUSTOMER.value:
        menu_add_customer(customers_list)        
    elif command == MyShopMenuEnum.DELETE_CUSTOMER.value:
        menu_delete_customer(customers_list)
    elif command == MyShopMenuEnum.FIND_CUSTOMER_BY_PHONE_NUMBER.value:
        menu_find_customer_by_phone_number(customers_list)    
    elif command == MyShopMenuEnum.NEW_PURCHASE.value:
        menu_add_purchase(purchase_list)
    elif command == MyShopMenuEnum.ADD_NEW_PRODUCT.value:
        menu_add_product(products_list)  
    elif command == MyShopMenuEnum.DELETE_PRODUCT.value:
        menu_delete_product(products_list)       
    elif command == MyShopMenuEnum.FIND_PRODUCT_BY_ID.value:
        menu_find_product_by_id(products_list)       
    elif command == MyShopMenuEnum.FIND_PRODUCT_BY_NAME.value:
        menu_find_product_by_name(products_list)
    elif command == MyShopMenuEnum.FIND_PRODUCTS_AT_CATGORY.value:
        menu_find_product_by_category(products_list)
    elif command == MyShopMenuEnum.EDIT_PRODUCT_UNIT_PRICE.value:
        manu_edit_product_price(products_list) 
    elif command == MyShopMenuEnum.EDIT_PRODUCT_AMOUNT.value:
        manu_edit_product_amount(products_list) 
    elif command == MyShopMenuEnum.EDIT_PRODUCT_CATEGORY.value:
        manu_edit_product_category(products_list)     
    elif command == MyShopMenuEnum.FIND_PURCHASE_BY_ID.value:
        manu_find_purchase_by_id(purchase_list)   
    elif command == MyShopMenuEnum.FIND_PURCHASE_BETWEEN_DATES.value:
        menu_find_purchases_between_dates(purchase_list)                             
    elif command == MyShopMenuEnum.EXIT.value:         
        break











