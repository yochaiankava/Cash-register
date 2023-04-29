
import json
from datetime import datetime, timedelta


class Purchase():    
    __purchaseid = 1
    def __init__(self,  customer, products = None, purchaseid = None, date = datetime.now().isoformat(), total_price = 0):
        self.date = date
        self.purchaseid = purchaseid 
        Purchase.__purchaseid += 1
        self.customer = customer        
        self.products = products if products is not None else []
        self.total_price = total_price        
            
    def __str__(self):           
         return f"""
             {self.date}
             {self.customer} 
             {self.products}
             {self.total_price}"""
             
class PurchaseList(): 
    def __init__(self):
        self.all_purchases = []         
        self.load_all_purchases()        
    
    # load all purchases
    def load_all_purchases(self):
        # reading the file
        with open("purchases.json") as f:
            all_file_json = json.load(f)
        print("done reading")
        # turn into objects
        for single_json in all_file_json:
            purchase = Purchase(**single_json)
            self.all_purchases.append(purchase)
            
    # convert all all_purchases to a dictionary  
    def save_all_purchases(self):
        new_list = []
        for purchase in self.all_purchases:
            new_list.append(purchase.__dict__)
        with open("purchases.json","w") as f:        
            json.dump(new_list, f)                   
        
    def add_purchase(self, purchase):
        self.all_purchases.append(purchase)
        print("add purchase ")
        self.save_all_purchases()
        print()  
             
    def new_purchase(self):
        from customer import CustomerList
        from product import ProductList
        customers_list = CustomerList()
        products_list = ProductList()
        try:   
            customer_Phone_numebr = int(input("what is the customer Phone_Number? "))            
            customer = customers_list.get_customer_by_phone_number(customer_Phone_numebr)                       
            print()                             
            if customer:               
                print(f"{customer.name} - {customer.last_name}")
                purchase_products = []                
                purchase_total_price = 0
                while True:
                    order = input("to complete a purchase press e ")
                    if order != "e":
                        ProductID = int(input("what is the ProductID? "))
                        product = products_list.get_product_by_id(ProductID)
                        if product:
                            print(product)
                            amount = float(input("what is the ammount?"))
                            if product.amount_in_stock >= amount:                        
                                    price = product.UnitPrice * amount
                                    purchase_total_price += price
                                    purchase_products.append(f"{product.ProductName}-{amount}-{price}") 
                                    products_list.edit_product_amount(ProductID, -amount)                                                          
                                    print(f"{product.ProductName}-{amount}-{price}") 
                                    print()
                            else:
                                print("The product is out of stock ")   
                                print()
                                 
                        else:
                            print("product not in products list ")
                            print()
                    else:
                        self.find_last_purchase_id()
                        purchase = Purchase(purchaseid = Purchase.__purchaseid, customer = customer.phone_number, products = purchase_products, total_price = purchase_total_price)
                        self.add_purchase(purchase)                                                           
                        customers_list.add_to_purchaseID(customer_Phone_numebr, purchase.purchaseid)                  
                        self.save_all_purchases()                                   
                        for line in purchase_products: 
                            print(f"{line}")
                        print()    
                        print(f"Payment summary - {purchase_total_price}") 
                        print()
                        break             
            else:
                print("Phone number does not exist\n"
                    "For casual customers press - 0") 
                print()                
        except Exception as e:
                print(f"product data is mising: {e}")  
                print()          
    
    def get_purchase_by_id(self, purchaseid):               
        for purchase in self.all_purchases:
            if purchase.purchaseid == purchaseid:
                return purchase 
        return None                 
    
    def find_last_purchase_id(self):
        last_purchase_id = 0
        for purchase in self.all_purchases:
            if purchase.purchaseid > last_purchase_id:
                last_purchase_id = purchase.purchaseid
        Purchase.__purchaseid = last_purchase_id + 1    
    
    def find_purchases_between_dates(self, start_date, end_date = ""):                   
            purchases_between_dates = []
            Total_between_dates = 0
            next_day = timedelta(days=1)
            
            start_datetime = datetime.strptime(start_date, '%d/%m/%Y').date()
            # convert start_date to ISO format
            start_date_iso = start_datetime.isoformat()
            if end_date is not "":
                end_datetime = datetime.strptime(end_date, '%d/%m/%Y').date() + next_day
                # convert end_date to ISO format
                end_date_iso = end_datetime.isoformat() 
            else:
                end_datetime = start_datetime + next_day 
                end_date_iso = end_datetime.isoformat()
                
            for purchase in self.all_purchases:
                if start_date_iso <= purchase.date <= end_date_iso:
                    purchases_between_dates.append(purchase)
                    Total_between_dates += purchase.total_price
            print()        
            print(f"Total income between dates - {Total_between_dates}")                    
            return purchases_between_dates

        