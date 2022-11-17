
from tkinter import messagebox
from Components.ButtonComponents import GrayButton

from DBHelper import *
from Components.MessageComponents import WhiteMessage
from Components.table import *
from SignUpPage import *
from LoginPage import *
from PIL import Image, ImageTk



class EmployeePage:
    def __init__(self,root, result):
        self.temp_window = Toplevel()
        self.temp_window.title("Cab details")
        self.f = Frame(self.temp_window, height=600, width=900)
        self.f.pack()
        self.f.pack_propagate(0)

        self.raw_image = Image.open("images/EmployeePage5.jpeg")
        # define the size of the image, which will also determine the size of the button
        self.raw_image = self.raw_image.resize((900, 600))
        self.img = ImageTk.PhotoImage(self.raw_image)

        self.panel = Label(self.f, image=self.img)
        self.panel.pack()
        self.panel.pack_propagate(0)


        #this is the reverse of 'zoomed' effect in AdminPage
        self.add_widgets(result)





    def add_widgets(self,uid):

        self.shared_button = GrayButton(self.f, "Shared Cab", lambda: Shared(self))
        self.shared_button.place(x=450,y=250)
        self.personal_button = GrayButton(self.f, "Personal Cab", lambda: Personal(self))
        self.personal_button.place(x=450,y=350)
        self.status_button = GrayButton(self.f, "Check Status", lambda: Check(self))
        self.status_button.place(x=650,y=300)

        #username = Login.e_username.get()
        Query = "Select * from diya.Employee where Uid= %s"
       # Query="Select employee.EmpFirstName,employee.EmpLastName,employee.EmpPincode from employee inner join user on employee.EmpFirstName=user.UserName"
        parameters = (uid)
        result = DatabaseHelper.get_all_data(Query, parameters)
        # Query = "Select * from diya.cab_booking where Uid= %s"

        self.my_emp_table = SimpleTable(self.f, rows=len(result), columns=len(result[0]), height=100, width=650)
        self.my_emp_table.place(x=200, y=20)
        self.my_emp_table.grid_propagate(0)
        for i in range(len(result)):
            for j in range(len(result[0])):
                self.my_emp_table.set(row=i, column=j, value=result[i][j])
        resultDict = DatabaseHelper.get_data(Query, parameters)
        print(result)
        location = resultDict.get('EmpPincode')
        print(location)


        #resultDictcab=DatabaseHelper.get_data(Query1)
        #loc=resultDictcab.get('Location')
        #print(loc)
        def Shared(self):
            Query1 = "Select * from diya.cab_booking"
            result1 = DatabaseHelper.get_all_data(Query1)
            print(result1)
            Query2="Select * from diya.cab_booking where Location=%s"
            parameter=(location)
            resultcab = DatabaseHelper.get_all_data(Query2, parameter)
            resultcabDict = DatabaseHelper.get_data(Query2, parameter)
            print(resultcab)
            #sharetype = resultDictcab.get('CabType')
            cabID=resultcabDict.get('CabId')
            #print(sharetype)
            if(resultcab is not None):
                Query3 = "Update diya.cab_booking set CurrentCap=CurrentCap+1,IsBooked = If(CurrentCap=MaxCapacity,1,0)  where CabId=%s order by CabId desc limit 1"
                print(cabID)
                parameter = (cabID)
                DatabaseHelper.execute_query(Query3, parameter)
                #print(Query3)
                #print(resultCabBooking)

            else:
                CurrentCap=1
                MaxCapacity=3
                IsBooked=0
                Cabtype='Shared'
                Query4= "Insert into Cab_Booking(Location, CurrentCap, MaxCapacity, IsBooked, CabType) Values (%s,%s,%s,%s,%s)"
                parameter=(location, CurrentCap, MaxCapacity,IsBooked,Cabtype)
                DatabaseHelper.execute_query(Query4, parameter)

        def Personal(self):
            CurrentCap = 1
            MaxCapacity = 3
            IsBooked = 1
            Cabtype = 'personal'
            DriverName = 'Jerry'
            CarNo = 'Mh-02-0302'
            Query5 = "Insert into Cab_Booking(Location, CurrentCap, MaxCapacity, IsBooked, CabType, DriverName, CarNo) Values (%s,%s,%s,%s,%s,%s,%s)"
            parameter = (location, CurrentCap, MaxCapacity, IsBooked, Cabtype, DriverName, CarNo)
            DatabaseHelper.execute_query(Query5, parameter)

            Query8 = "Select * from cab_booking where Location=%s and CabType='personal'"

            result2 = DatabaseHelper.get_all_data(Query8, location)
            self.my_cab1_table = SimpleTable(self.f, rows=len(result2), columns=len(result2[0]), height=100, width=460)
            self.my_cab1_table.place(x=400, y=450)
            self.my_cab1_table.grid_propagate(0)
            for i in range(len(result2)):
                for j in range(len(result2[0])):
                    self.my_cab1_table.set(row=i, column=j, value=result2[i][j])

        def Check(self):


            Query6= "Select * from cab_booking where Location=%s"

            result1 = DatabaseHelper.get_all_data(Query6,location)
            self.my_cab_table = SimpleTable(self.f, rows=len(result1), columns=len(result1[0]), height=100, width=460)
            self.my_cab_table.place(x=400, y=450)
            self.my_cab_table.grid_propagate(0)
            for i in range(len(result1)):
                for j in range(len(result1[0])):
                    self.my_cab_table.set(row=i, column=j, value=result1[i][j])



if(__name__=="__main__"):
    root = Tk()
    e = EmployeePage(root)
    root.mainloop()

