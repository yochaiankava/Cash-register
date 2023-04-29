import json
from utiles import MyShopCategoriesEnum

class Product():   
    def __init__(self, ProductID, ProductName, CategoryID, UnitPrice = 0, amount_in_stock = 0):
        self.ProductID = ProductID
        self.ProductName = ProductName
        self.UnitPrice = UnitPrice
        self.CategoryID = CategoryID
        self.amount_in_stock = amount_in_stock   
               
    def __str__(self):
        return f"""
        Product _id: {self.ProductID},
        Product Name: {self.ProductName},
        Product Category: {self.CategoryID},
        Product Price: {self.UnitPrice},
        Product Amount In Stock: {self.amount_in_stock},
        """

class ProductList():
    
    def __init__(self):  
        self.all_products = []       
        self.load_all_products()  
            
    # load all products from json to all productlist          
    def load_all_products(self):
        try:
            with open("products.json") as f:
                all_file_json = json.load(f)
        except FileNotFoundError:
            print("File not found.")
            return False
        except json.decoder.JSONDecodeError:
            print("Invalid JSON format.")
            return False
        for single_json in all_file_json:
            product = Product(**single_json)
            self.all_products.append(product)
    
    # convert all all_products to a dictionary
    def save_all_products(self):
        new_list = [product.__dict__ for product in self.all_products]
        try:
            with open("products.json", "w") as f:
                 json.dump(new_list, f)
            print("done saving new list on json file")
        except Exception as e:
            print(f"Error occurred while saving file: {e}")
       
    
    def add_product(self, product):
        self.all_products.append(product)
        print("add product ")
        self.save_all_products()
        print()
               
    def delete_product(self, product):        
        self.all_products.remove(product)
        print("product deleted ")
        self.save_all_products()
        print()   
    
    def edit_product_amount(self, ProductID, amount):
        product = self.get_product_by_id(ProductID)
        if product:
            product.amount_in_stock += amount
            self.save_all_products()
            print()
            print(f"Product '{product.ProductName}' amount in stock updated to {product.amount_in_stock}")
        else:
            print(f"Product with ID {ProductID} not found")  
        
    def edit_product_price(self, ProductID, newUnitPrice):
        product = self.get_product_by_id(ProductID)
        if product:
            product.UnitPrice = newUnitPrice
            self.save_all_products()
            print()
            print(f"Product '{product.ProductName}' new amount updated to {product.UnitPrice}")
        else:
            print(f"Product with ID {ProductID} not found")    
          
    def edit_product_category(self, ProductID):
        product = self.get_product_by_id(ProductID)
        if product:
            print(f"{product.ProductName} - {product.CategoryID}")
            newproductcategory = self.product_category()
            if newproductcategory != None:
               product.CategoryID = newproductcategory
            else:
               pass 
            self.save_all_products()
            print()
            print(f"Product '{product.ProductName}' new category updated to {product.CategoryID}")
        else:
            print(f"Product with ID {ProductID} not found") 
    
    def product_category(self):
        while True:
            command = input("what is the product category?\n"
                        "1 - Home Goods.\n"
                        "2 - Meat and Poultry.\n"
                        "3 - Bakery.\n"
                        "4 - Snacks.\n"
                        "5 - Beverages.\n"
                        "6 - Vegetables and fruits.\n"
                        "7 - Cancel. ")
            print()
        
            if command == MyShopCategoriesEnum.HOME_GOODS.value:
                return 1                        
            elif command == MyShopCategoriesEnum.MEAT_AND_POULTRY.value:
                return 2
            elif command == MyShopCategoriesEnum.BAKERY.value:
                return 3  
            elif command == MyShopCategoriesEnum.SNACKS.value:
                return 4
            elif command == MyShopCategoriesEnum.BEVERAGES.value:
                return 5
            elif command == MyShopCategoriesEnum.VEGETABLES_AND_FRUITS.value:
                return 6
            elif command == "":
                print("Please enter a valid input")
            elif command == MyShopCategoriesEnum.CANCEL.value:
                break
            else:
                print("Product category does not exist")
                 
                       
    def get_product_by_id(self, ProductID):              
        for product in self.all_products:
            if product.ProductID == ProductID:
                return product 
        return None     
             
    def get_product_by_name(self, ProductName):        
        result = []
        for product in self.all_products:
            if product.ProductName == ProductName:
               result.append(f"{product.__dict__}\n")             
        return result              
    
    def get_product_by_category(self, CategoryID):        
        result = []
        for product in self.all_products:
            if product.CategoryID == CategoryID:
                result.append(f"{product.ProductID} - {product.ProductName} - {product.UnitPrice} - {product.amount_in_stock}")                
        return result        
            
    def __str__(self):        
        result = ""
        for product in self.all_products:
            result += product.__str__() + "\n"
        return result
    
    
