from tkinter import *

root = Tk()


class Main:
    entry = Entry(root, width=17, borderwidth=20, font=("MS Sans Serif", 17, "bold"))
    entry1 = Entry(root, width=10, borderwidth=3)
    entry2 = Entry(root, width=10, borderwidth=3)
    entry.grid(row=0, column=0, columnspan=4)
    entry.insert(0, "0")
    entry1.place(x=75, y=75)
    entry2.place(x=75, y=105)

    def __init__(self, master):
        self.title = master.title("Area Calculator")
        self.configure = master.configure(bg="#FAEBD7")
        self.geometry = master.geometry("279x407")
        self.resizable = master.resizable(False, False)
        self.options = [
            "Choose Area",
            "Rectangle",
            "Square",
            "Circle",
            "Triangle"
        ]
        self.click = StringVar()
        self.click.set(self.options[0])
        self.drop = OptionMenu(root, self.click, *self.options)
        self.drop.grid(row=1, column=2, columnspan=3)
        self.buttons()
        self.entry_1 = 0

        self.click_count = 0

        self.entry1.bind("<Button-1>", lambda event, entry_widget=1: self.callback_entry(event, entry_widget))
        self.entry2.bind("<Button-1>", lambda event, entry_widget=2: self.callback_entry(event, entry_widget))

    def callback_entry(self, event, entry_number):
        self.entry_1 = entry_number
        print(entry_number)  # you can remove this line, for debugging purposes only

    def buttons_event(self, number):
        try:
            if self.entry_1 == 1:
                current = self.entry1.get()
                self.entry1.delete(0, END)
                self.entry1.insert(0, str(current) + str(number))
            elif self.entry_1 == 2:
                current = self.entry2.get()
                self.entry2.delete(0, END)
                self.entry2.insert(0, str(current) + str(number))
        except AttributeError as e:
            print(f"[ERROR]: {e}, Please select entry first!")

    def buttons(self):
        self.button1 = Button(root, text="1", padx=25, pady=20, borderwidth=3, command=lambda: self.buttons_event("1"),
                              font=("arial", 10, "bold"), bd=2, bg="#CDCDC1")
        self.button2 = Button(root, text="2", padx=25, pady=20, borderwidth=3, command=lambda: self.buttons_event("2"),
                              font=("arial", 10, "bold"), bd=2)
        self.button3 = Button(root, text="3", padx=25, pady=20, borderwidth=3, command=lambda: self.buttons_event("3"),
                              font=("arial", 10, "bold"), bd=2)
        self.button4 = Button(root, text="4", padx=25, pady=20, borderwidth=3, command=lambda: self.buttons_event("4"),
                              font=("arial", 10, "bold"), bd=2, bg="#CDCDC1")
        self.button5 = Button(root, text="5", padx=25, pady=20, borderwidth=3, command=lambda: self.buttons_event("5"),
                              font=("arial", 10, "bold"), bd=2)
        self.button6 = Button(root, text="6", padx=25, pady=20, borderwidth=3, command=lambda: self.buttons_event("6"),
                              font=("arial", 10, "bold"), bd=2)
        self.button7 = Button(root, text="7", padx=25, pady=20, borderwidth=3, command=lambda: self.buttons_event("7"),
                              font=("arial", 10, "bold"), bd=2, bg="#CDCDC1")
        self.button8 = Button(root, text="8", padx=25, pady=20, borderwidth=3, command=lambda: self.buttons_event("8"),
                              font=("arial", 10, "bold"), bd=2, bg="#CDCDC1")
        self.button9 = Button(root, text="9", padx=25, pady=20, borderwidth=3, command=lambda: self.buttons_event("9"),
                              font=("arial", 10, "bold"), bd=2, bg="#CDCDC1")
        self.button0 = Button(root, text="0", padx=26, pady=19, borderwidth=3, command=lambda: self.buttons_event("0"),
                              font=("arial", 10, "bold"), bd=2, bg="#CDCDC1")

        self.buttonSelect = Button(root, text="Select", command=lambda: self.selectButton())

        self.buttonEquals = Button(root, text="=", padx=58, pady=17, borderwidth=3, command=lambda: self.equalButton(),
                                   font=("arial", 11, "bold"), bd=2, fg="#17161b", bg="#CDCDC1")
        self.buttonDot = Button(root, text=" .", padx=22, pady=16, borderwidth=3, command=lambda: self.buttons_event("."),
                                font=("arial", 13, "bold"), bd=2,fg="#FFFFFF", bg="#17161b")
        self.buttonC = Button(root, text="C", padx=25, pady=54, borderwidth=3, command=lambda: self.clear_event(),
                              font=("arial", 10, "bold"), bd=2, fg="#17161b", bg="#CDCDC1")
        self.buttonBackspace = Button(root, text="<=", padx=15, pady=14, borderwidth=3, state=DISABLED,
                                font=("Helvetica", 14, "bold"), bd=2, fg="#FFFFFF", bg="#17161b")

        self.button1.place(x=2, y=273)
        self.button2.place(x=71, y=273)
        self.button3.place(x=140, y=273)
        self.button4.place(x=2, y=205)
        self.button5.place(x=71, y=205)
        self.button6.place(x=140, y=205)
        self.button7.place(x=2, y=137)
        self.button8.place(x=71, y=137)
        self.button9.place(x=140, y=137)
        self.button0.place(x=70, y=341)
        self.buttonSelect.place(x=200, y=105)
        self.buttonEquals.place(x=140, y=341)
        self.buttonDot.place(x=2, y=342)
        self.buttonC.place(x=208, y=205)
        self.buttonBackspace.place(x=209, y=137)

    def equalButton(self):
        f_num = self.entry1.get()
        l_num = self.entry2.get()
        if self.click.get() == "Rectangle":
            self.entry.delete(0, END)
            self.entry.insert(0, float(f_num) * float(l_num))
        if self.click.get() == "Square":
            self.entry.delete(0, END)
            area_sq = float(f_num or l_num) * float(f_num or l_num)
            self.entry.insert(0, area_sq)
        if self.click.get() == "Circle":
            self.entry.delete(0, END)
            radius = float(f_num) / 2
            squared_r = float(radius ** 2)
            self.entry.insert(0, squared_r * 3.14)
        if self.click.get() == "Triangle":
            self.entry.delete(0, END)
            area_tri1 = float(f_num) / 2
            self.entry.insert(0, float(area_tri1) * float(l_num))

    def selectButton(self):
        if self.click.get() == "Choose Area":
            Label(root, text=" ", padx=25, bg="#FAEBD7").place(x=3, y=77)
            Label(root, text=" ", padx=25, bg="#FAEBD7").place(x=3, y=102)
        if self.click.get() == "Rectangle":
            Label(root, text="Length:   ", bg="#FAEBD7").place(x=3, y=77)
            Label(root, text="Width:  ", bg="#FAEBD7").place(x=3, y=102)
        if self.click.get() == "Square":
            Label(root, text="Side:    ", bg="#FAEBD7").place(x=3, y=77)
            Label(root, text="", padx=32, pady=2, bg="#FAEBD7").place(x=3, y=102)
        if self.click.get() == "Circle":
            Label(root, text="Diameter: ", bg="#FAEBD7").place(x=3, y=77)
            Label(root, text=" ", padx=25, bg="#FAEBD7").place(x=3, y=102)
        if self.click.get() == "Triangle":
            Label(root, text="Base:      ", bg="#FAEBD7").place(x=3, y=77)
            Label(root, text="Height: ", bg="#FAEBD7").place(x=3, y=102)

    def clear_event(self):
        self.entry.delete(0, END)
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry.insert(0, "0")


if __name__ == '__main__':
    main = Main(root)
    root.mainloop()
