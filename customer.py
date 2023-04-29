
import json

class Customer:
    def __init__(self, name, last_name, phone_number, purchaseid_history=None):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.purchaseid_history = purchaseid_history  if purchaseid_history is not None else []          
                                    
    def __str__(self):           
         return f"""
                Customer Name: {self.name},
                Last Name: {self.last_name},
                Phone Number: {self.phone_number},
                Purchase history ID: {self.purchaseid_history}"""       
               
class CustomerList():    
    def __init__(self):
        self.customers = []       
        self.load_all_customers()
        
    # load all customers    
    def load_all_customers(self):
        # reading the file
        with open("customers.json") as f:
            all_file_json = json.load(f)
        print("done reading")
        # turn into objects
        for single_json in all_file_json:
            customer = Customer(**single_json)
            self.customers.append(customer)
            
    # convert all customers to a dictionary  
    def save_all_customers(self):
        new_list = []
        for customer in self.customers:
            new_list.append(customer.__dict__)
        with open("customers.json","w") as f:        
            json.dump(new_list, f)          
                
    def add_customer(self, customer):
        self.customers.append(customer)
        self.save_all_customers()
        
    def remove_customer(self, customer):
        self.customers.remove(customer)             
        self.save_all_customers()
    
    def add_to_purchaseID(self, phone_number, newpurchaseID):             
        customer = self.get_customer_by_phone_number(phone_number)      
        if customer:                   
            customer.purchaseid_history.append(newpurchaseID)       
            self.save_all_customers()          
            print()
            print(f"customer {customer.name} customer purchase history updated {customer.purchaseid_history}")
            print()
        else:
            print(f"customer with phone number {phone_number} not found") 
               
    def get_customer_by_phone_number(self, phone_number):
        for customer in self.customers:
            if customer.phone_number == phone_number:
                return customer
        return None  
      
    def get_customer_by_name(self, name):
        result = []
        for customer in self.customers:
            if customer.name == name:
                result.append(customer)
        return result
        
    def get_customer_by_last_name(self, last_name):
        result = []
        for customer in self.customers:
            if customer.last_name == last_name:
                result.append(customer)
        return result       
                
        # Function to check if the username and password are valid
    def check_credentials(self, username, password):
        credentials = {'user1': 'password1', 'user2': 'password2', 'user3': 'password3'}    

        if username in credentials and credentials[username] == password:
            return True
        else:
            return False
    
    def __str__(self):
        result = ""
        for customer in self.customers:
            result += customer.__str__() + "\n"
        return result    