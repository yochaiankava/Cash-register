from enum import Enum
    
class MyShopMenuEnum(Enum):
    ADD_CUSTOMER = "1"
    DELETE_CUSTOMER = "2"
    FIND_CUSTOMER_BY_PHONE_NUMBER = "3"
    NEW_PURCHASE = "4"
    ADD_NEW_PRODUCT = "5"
    DELETE_PRODUCT = "6"
    FIND_PRODUCT_BY_ID = "7"
    FIND_PRODUCT_BY_NAME = "8"
    FIND_PRODUCTS_AT_CATGORY = "9"
    EDIT_PRODUCT_UNIT_PRICE = "10"
    EDIT_PRODUCT_AMOUNT = "11"
    EDIT_PRODUCT_CATEGORY = "12"
    FIND_PURCHASE_BY_ID = "13"
    FIND_PURCHASE_BETWEEN_DATES = "14"
    EXIT = "20"

class MyShopCategoriesEnum(Enum):
    HOME_GOODS ="1"
    MEAT_AND_POULTRY = "2"
    BAKERY = "3"
    SNACKS = "4"
    BEVERAGES = "5"    
    VEGETABLES_AND_FRUITS = "6"
    CANCEL = "7"
                        

