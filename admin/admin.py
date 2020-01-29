from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from collections import OrderedDict
from pymongo import MongoClient

class AdminWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_users(self): 
        client = MongoClient()
        db = client.silverpos
        users = db.users
        _users = OrderedDict(
            first_names = {},
            last_names = {},
            user_names = {},
            passwords = {},
            designations = {}
        )
        first_names = []
        last_names = []
        user_names = []
        passwords = []
        designations = []
        
        for user in users.find():
            first_names.append(user['first_name'])
            last_names.append(user['last_name'])
            user_names.append(user['user_name'])
            passwords.append(user['password'])
            designations.append(user['designation'])
        users_len = len(first_names)
        idx = 0
        while idx < users_len:
            _users['first_names'][idx] = first_names[idx]
            _users['last_names'][idx] = last_names[idx]
            _users['user_names'][idx] = user_names[idx]
            _users['passwords'][idx] = passwords[idx]
            _users['designations'][idx] = designations[idx]
            idx += 1
            
        return _users

    def get_products(self): 
        client = MongoClient()
        db = client.silverpos
        products = db.stocks
        _stocks = OrderedDict()
        _stocks['product_code'] = {}
        _stocks['product_name'] = {}
        _stocks['product_weight'] = {}
        _stocks['in_stock'] = {}
        _stocks['sold'] = {}
        _stocks['order'] = {}
        _stocks['last_purchase'] = {}
        
        product_code = []
        product_name = []
        product_weight = []
        in_stock = []
        sold = []
        order = []
        last_purchase = []
        
        for product in products.find():
            product_code.append(user['product_code'])
            product_name.append(user['product_name'])
            product_weight.append(user['product_weight'])
            in_stock.append(user['in_stock'])
            sold.append(user['sold'])
            order.append(user['order'])
            last_purchase.append(user['last_purchase'])
            
        products_len = len(first_names)
        idx = 0
        while idx < products_len:
            _stocks['product_code'][idx] = product_code[idx]
            _stocks['product_name'][idx] = product_name[idx]
            _stocks['product_weight'][idx] = product_weight[idx]
            _stocks['in_stock'][idx] = in_stock[idx]
            _stocks['sold'][idx] = sold[idx]
            _stocks['order'][idx] = order[idx]
            _stocks['last_purchase'][idx] = last_purchase[idx]
            idx += 1
            
        return _users

class AdminApp(App):
    def build(self):
        return AdminWindow()
    
if __name__ == '__main__':
    AdminApp().run()