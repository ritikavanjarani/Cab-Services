from tkinter import *

root = Tk()
root.title("EmployeeSignUp Page")
root.geometry('500x500')

signup_frame = Frame(root, height=500, width=500, bg='gray')
signup_frame.pack()

drivername_label = Label(signup_frame, text='DriverName', font=('calibre', 10, 'bold'))
drivername_label.place(x=35, y=25)
drivername = Entry(signup_frame)
drivername.place(x=150, y=25)

cabno_label = Label(signup_frame, text='Cab-No', font=('calibre', 10, 'bold'))
cabno_label.place(x=35, y=75)
cabno = Entry(signup_frame)
cabno.place(x=150, y=75)

model_label = Label(signup_frame, text='Model', font=('calibre', 10, 'bold'))
model_label.place(x=35, y=125)
model = Entry(signup_frame)
model.place(x=150, y=125)


Capacity_label = Label(signup_frame, text='Arrival Time', font=('calibre', 10, 'bold'))
time_label.place(x=35, y=175)
time = Entry(signup_frame)
time.place(x=150, y=175)

contactno_label = Label(signup_frame, text='Contact No', font=('calibre', 10, 'bold'))
contactno_label.place(x=35, y=225)
contactno = Entry(signup_frame)
contactno.place(x=150, y=225)


ok = Button(signup_frame, text="OK", font=('calibre', 10, 'bold'))
ok.place(x=120, y=300)


root.mainloop()