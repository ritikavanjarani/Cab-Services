
from LoginPage import *
from Components.ButtonComponents import GrayButton
from Components.table import *



class Employee():
    def __init__(self, root):
        self.temp_window = Toplevel()
        self.temp_window.title("Employee details")
        self.f = Frame(self.temp_window, height=650, width=1050,bg='light blue')
        self.f.pack()
        self.f.pack_propagate(0)
        self.admin_button = GrayButton(self.f, "Add new Employee",lambda: (self),font=(8) )
        self.admin_button.place(x=30,y=100)

        #this is the reverse of 'zoomed' effect in AdminPage
        #self.add_widgets()


        existing_frame =Frame(self.f, height=600, width=750, bg='light blue')
        existing_frame.place(x=250,y=00)
        Query8 = "Select * from diya.employee"
        ans = DatabaseHelper.get_all_data(Query8)
        my_exisemp_table = SimpleTable(existing_frame, rows=len(ans), columns=len(ans[0]), height=600, width=750)
        my_exisemp_table.place(x=20, y=10)
        my_exisemp_table.grid_propagate(0)
        for i in range(len(ans)):
            for j in range(len(ans[0])):
                my_exisemp_table.set(row=i, column=j, value=ans[i][j])

       # def add_widgets(self):
            #self.admin_button = GrayButton(self.f, "Add new Cab")
            #self.admin_button.place(x=20,y=50)




if(__name__=="__main__"):
    root = Tk()
    emp = Employee(root)
    root.mainloop()
