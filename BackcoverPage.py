from tkinter import *
from PIL import Image, ImageTk

class BackcoverPage:
    def __init__(self, root):
        self.root = root
        self.root.iconbitmap('images/CarLogo.ico')
        self.root.title('Cab Services')
        # ensure that size of image is same as/greater than size of frame
        self.f = Frame(root, width=900, height=600)
        self.f.pack()

        self.raw_image = Image.open("images/BackCover2.jpeg")
        # define the size of the image, which will also determine the size of the button
        self.raw_image = self.raw_image.resize((900, 600))
        self.img = ImageTk.PhotoImage(self.raw_image)

        self.panel = Label(self.f, image=self.img)
        self.panel.pack()
        self.panel.pack_propagate(0)
        # Add the message saying "Cab"
        self.m = Message(self.f, width=600, font=("Monotype Corsiva", 20, "bold", "italic"), text="CAB SERVICES",
                         bg="white", relief=SOLID, borderwidth=2)
        self.m.place(x=520, y=20)
        # The footer at the bottom
        self.footer = Label(self.panel, bg="ivory3", height=1,
                            text="@Copyright 2022 Cab services. All rights reserved")
        self.footer.pack(side=BOTTOM, fill=X)
        self.footer.tkraise()
        self.f.pack_propagate(0)
       # self.f.destroy()

    def destroy(self):
        self.f.destroy()

if (__name__ == "__main__"):
    root = Tk()
    d = BackcoverPage(root)
    root.mainloop()


"""
The file which is executed, uska __name__ ==> "__main__"
All the other file which are not executed, uska __name__ ==> "filename"
"""
