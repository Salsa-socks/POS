from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class OperatorWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(). __init__(**kwargs)
        
    def update_purchases(self):
        code = self.ids.code_inp.text
        qty = self.ids.qty_inp.text
        name = self.ids.code_inp.text
        disc = self.ids.disc_inp.text
        price = self.ids.price_inp.text
        total = self.ids.total_inp.text
        
        products_container = self.ids.products
        if code and qty and name: #needs some kind of validation checks eg: numbers inputted, range for percs
            details = BoxLayout(size_hint_y=None, height=30, pos_hint={'top':1})
            products_container.add_widget(details)
            
            code = Label(text=code, size_hint_x=.2, color=(.06, .45, .45, 1))
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
            pname = self.ids.code_inp.text
            pprice = f'R{self.ids.price_inp.text}'
            preview = self.ids.receipt_preview
            prev_text = preview.text
            _prev = prev_text.find('`')
            if _prev > 0:
                prev_text = prev_text[:_prev]
            purchase_total = '`\n\nTotal\t\t\t\t0.00'
            new_preview = '\n'.join([prev_text, pname+'\t\t\t\t'+str(pprice),purchase_total])
            preview.text = new_preview

class OperatorApp(App):
        def build(self):
            return OperatorWindow()

if __name__ == "__main__":
    oa = OperatorApp()
    oa.run()