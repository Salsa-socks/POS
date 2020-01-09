from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import re

# holds all the rules and functions of layout of screen
class SigninWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate_user(self):
        errors = ''
        user = self.ids.username_field
        password = self.ids.pwd_field
        info = self.ids.info

        uname = user.text
        pwd = password.text

        if uname == '' or pwd == '':
            errors += 'Username and Password are required to sign in.\n'
        elif uname != 'admin' or pwd != 'admin':
            errors += 'Invalid Username or Password'

        if errors:
            info.text = (f'[color=#FF0000]{errors}[/color]')
        else:
            if uname == 'admin' and pwd == 'admin':
                info.text = (f'[color=#5DD300]Thank You. Logging you in[/color]')
# takes care of displaying layout of application
#kv file needs to be the same name as App class ie: everythin in signinwindow (.py) will be in <signinwindow> (.kv)
class SigninApp(App):
    def build(self):
        return SigninWindow()

if __name__ == "__main__":
    sa = SigninApp()
    sa.run()