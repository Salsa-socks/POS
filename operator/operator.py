from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import re

class OperatorWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(). __init__(**kwargs)
        
        self.cart = [] #contains all items selected
        self.qty = []
        self.total = 0.00
        
    def update_purchases(self):
        pcode = self.ids.code_inp.text
        qty = self.ids.qty_inp.text
        name = self.ids.code_inp.text
        disc = self.ids.disc_inp.text
        price = self.ids.price_inp.text
        total = self.ids.total_inp.text
        
        products_container = self.ids.products
        if pcode =='1234' or pcode == '2345': #needs some kind of validation checks eg: numbers inputted, range for percs
            details = BoxLayout(size_hint_y=None, height=30, pos_hint={'top':1})
            products_container.add_widget(details)
            
            code = Label(text=pcode, size_hint_x=.2, color=(.06, .45, .45, 1))
            name = Label(text='Product', size_hint_x=.3, color=(.06, .45, .45, 1))
            qty = Label(text=qty, size_hint_x=.1, color=(.06, .45, .45, 1))
            disc = Label(text=f'{disc}%', size_hint_x=.1, color=(.06, .45, .45, 1))
            price = Label(text=f'R{price}', size_hint_x=.1, color=(.06, .45, .45, 1))
            total = Label(text=f'R{total}', size_hint_x=.2, color=(.06, .45, .45, 1))
            
            details.add_widget(code)
            details.add_widget(name)
            details.add_widget(qty)
            details.add_widget(disc)
            details.add_widget(price)
            details.add_widget(total)
            
            # update Preview
            pname = "Product One"
            if pcode == '2345':
                pname = 'Product Two'
            pprice = 1.00
            pqty = str(1)
            self.total += pprice
            preview = self.ids.receipt_preview
            prev_text = preview.text
            purchase_total = '`\n\nTotal\t\t\t\t' + str(self.total)
            self.ids.curr_product.text = pname
            self.ids.curr_price.text = str(pprice)
            _prev = prev_text.find('`')
            if _prev > 0:
                prev_text = prev_text[:_prev]           
            
            ptarget = -1
            for i,c in enumerate(self.cart):
                if c == pcode:
                    ptarget = i
                    
            if ptarget >= 0:
                pqty = self.qty[ptarget]+1
                self.qty[ptarget] = pqty
                expr = '%s\t\tX\d\t'%(pname)
                rexpr = pname+'\t\tX'+str(pqty)+'\t'
                new_text = re.sub(expr, rexpr, prev_text)
                preview.text = new_text + purchase_total
            else:
                self.cart.append(pcode)
                self.qty.append(1)
                new_preview = '\n'.join([prev_text, pname+'\t\tX'+pqty+'\t\t'+str(pprice),purchase_total])
                preview.text = new_preview

class OperatorApp(App):
        def build(self):
            return OperatorWindow()

if __name__ == "__main__":
    oa = OperatorApp()
    oa.run()