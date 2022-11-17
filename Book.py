from BackcoverPage import *

from Components.ButtonComponents import GrayButton
from DBHelper import *
from Components.MessageComponents import WhiteMessage
from SignUpPage import *
from LoginPage import *
from Cab import *
from Employee import *



class AdminPage(BackcoverPage):
    def __init__(self,root):
        #Calls the parent BackgroundPage and now MainPage adds its own widgets using add_widgets()
        super().__init__(root)
        self.root.geometry('900x600')
        #this is the reverse of 'zoomed' effect in AdminPage
        self.root.state('normal')
        self.add_widgets()


    def add_widgets(self):

        self.cab_button = GrayButton(self.panel, "Cabs", lambda: Cab(self.root), font=(10))
        self.cab_button.place(x=520, y=200)
        self.employee_button = GrayButton(self.panel, "Employee", lambda: Employee(self.root), font=(10))
        self.employee_button.place(x=520, y=320)


    def redirect_to_page(self, select_type):
        self.f.destroy()
        if select_type == "Cabs":
            import Cab as c
            c.Cab(self.root,)
        elif select_type == "Employee":
            import Employee as emp
            emp.Employee(self.root,)


if(__name__=="__main__"):
    root = Tk()
    a = AdminPage(root)
    root.mainloop()

