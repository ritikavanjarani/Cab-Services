from BackcoverPage import *
from tkinter import messagebox
from Components.ButtonComponents import GrayButton
from DBHelper import *
from Components.MessageComponents import WhiteMessage
from SignUpPage import *
from LoginPage import *



class MainPages(BackcoverPage):
    def __init__(self,root):
        #Calls the parent BackgroundPage and now MainPage adds its own widgets using add_widgets()
        super().__init__(root)
        self.root.geometry('900x600')
        #this is the reverse of 'zoomed' effect in AdminPage
        self.root.state('normal')
        self.add_widgets()


    def add_widgets(self):
        # Add 2 buttons-> Admin and user
        # Add 1 button-> new user
        # Add contact details
        self.admin_button = GrayButton(self.panel, "Admin login", lambda: Login("Admin", self), font=(10))
        self.admin_button.place(x=520, y=200)
        self.user_button = GrayButton(self.panel, "User login", lambda: Login("User", self), font=(10))
        self.user_button.place(x=520, y=320)
        #self.new_user_button = GrayButton(self.panel, "New user? Sign up here",SignUp, borderwidth=2, relief=RIDGE)
        #self.new_user_button.place(x=550, y=220)


    def redirect_to_page(self, result, login_type):
        self.f.destroy()
        if login_type == "Admin":
            import AdminPage as admin
            admin.AdminPage(self.root)

        elif login_type == "User":
            self.f.destroy()
            BackcoverPage.destroy(self)
            print(result)
            import EmployeePage as emp
            emp.EmployeePage(self.root, result)



if(__name__=="__main__"):
    root = Tk()
    m = MainPages(root)
    root.mainloop()
