from BackcoverPage import *
from tkinter import messagebox
from Components.ButtonComponents import GrayButton
from DBHelper import *
from Components.MessageComponents import WhiteMessage
from Components.table import *
from SignUpPage import *
from LoginPage import *
from Components.ButtonComponents import GrayButton



class Cab():
    def __init__(self, root):
        self.temp_window = Toplevel()
        self.temp_window.title("Cab details")
        self.f = Frame(self.temp_window, height=600, width=900,bg='light blue')
        self.f.pack()
        self.f.pack_propagate(0)
        self.admin_button = GrayButton(self.f, "Add new Cab",lambda: (self), font=(10))
        self.admin_button.place(x=50,y=100)

        #this is the reverse of 'zoomed' effect in AdminPage
        #self.add_widgets()


        existing_frame =Frame(self.f, height=600, width=600, bg='light blue')
        existing_frame.place(x=250,y=00)
        Query7 = "Select * from diya.cab"
        res = DatabaseHelper.get_all_data(Query7)
        my_exiscab_table = SimpleTable(existing_frame, rows=len(res), columns=len(res[0]), height=450, width=370)
        my_exiscab_table.place(x=50, y=50)
        my_exiscab_table.grid_propagate(0)
        for i in range(len(res)):
            for j in range(len(res[0])):
                my_exiscab_table.set(row=i, column=j, value=res[i][j])

       # def add_widgets(self):
            #self.admin_button = GrayButton(self.f, "Add new Cab")
            #self.admin_button.place(x=20,y=50)




if(__name__=="__main__"):
    root = Tk()
    c = Cab(root)
    root.mainloop()
