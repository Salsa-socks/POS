from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

# holds all the rules and functions of layout of screen
class SigninWindow(BoxLayout):
    pass

# takes care of displaying layout of application
#kv file needs to be the same name as App class ie: everythin in signinwindow (.py) will be in <signinwindow> (.kv)
class SigninApp(App):
    def build(self):
        return SigninWindow()

if __name__ == "__main__":
    sa = SigninApp()
    sa.run()