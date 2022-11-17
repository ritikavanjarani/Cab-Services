from tkinter import *

root = Tk()
root.title("EmployeeSignUp Page")
root.geometry('500x500')

signup_frame = Frame(root, height=500, width=500, bg='gray')
signup_frame.pack()

firstname_label = Label(signup_frame, text='FirstName', font=('calibre', 10, 'bold'))
firstname_label.place(x=35, y=25)
firstname = Entry(signup_frame)
firstname.place(x=150, y=75)

lastname_label = Label(signup_frame, text='LastName', font=('calibre', 10, 'bold'))
lastname_label.place(x=35, y=75)
lastname = Entry(signup_frame)
lastname.place(x=150, y=125)

empid_label = Label(signup_frame, text='Emp Id', font=('calibre', 10, 'bold'))
empid_label.place(x=35, y=125)
empid = Entry(signup_frame)
empid.place(x=150, y=25)


branch_label = Label(signup_frame, text='Branch', font=('calibre', 10, 'bold'))
branch_label.place(x=35, y=175)
branch = Entry(signup_frame)
branch.place(x=150, y=175)


street_label = Label(signup_frame, text='Street', font=('calibre', 10, 'bold'))
street_label.place(x=35, y=225)
street = Entry(signup_frame)
street.place(x=150, y=225)

city_label = Label(signup_frame, text='City', font=('calibre', 10, 'bold'))
city_label.place(x=35, y=275)
city = Entry(signup_frame)
city.place(x=150, y=275)

pincode_label = Label(signup_frame, text='Pin Code', font=('calibre', 10, 'bold'))
pincode_label.place(x=35, y=325)
pincode = Entry(signup_frame)
pincode.place(x=150, y=325)

contactno_label = Label(signup_frame, text='Contact No', font=('calibre', 10, 'bold'))
contactno_label.place(x=35, y=375)
contactno = Entry(signup_frame)
contactno.place(x=150, y=375)

emailid_label = Label(signup_frame, text='Email', font=('calibre', 10, 'bold'))
emailid_label.place(x=35, y=425)
emailid = Entry(signup_frame)
emailid.place(x=150, y=425)

ok = Button(signup_frame, text="OK", font=('calibre', 10, 'bold'))
ok.place(x=100, y=470)


root.mainloop()