from tkinter import *
from tkinter import ttk  # for Treeview
from tkinter import filedialog
from PIL import ImageTk, Image # to add image in About us window, I will use this for .jpg only
import csv

class EVcars():

    def __init__(self):
        self.window = Tk()
        # icon = ImageTk.PhotoImage(Image.open("./Project/python_ninjas_logo2.jpg")) for .jpg
        icon = PhotoImage(file="./Project/fourninjas with python.png")
        self.window.title("Ninjas EV Trading System")
        self.window.iconphoto(True, icon) #set True to set that icon in all self.window & its descendents
        self.window.geometry("300x300")
        # created file, load_btn to load file and store it to use in other windows without repeating load_file 
        self.file = None 
        self.datas = None

        load_labl = Label(self.window, text="Please load file first!")
        load_btn = Button(self.window, text="Load file", command=self.load_file) 
        show_btn = Button(self.window, text="Show Cars Info", command=self.show_Info)
        more_btn = Button(self.window, text="More..", command=self.explore_Info)

        load_labl.pack(side=TOP, pady=20)
        load_btn.pack()
        show_btn.pack(pady=20)
        more_btn.pack(pady=20)

        self.info_labl = Label(self.window, text='', fg="red")
        self.info_labl.pack()

        self.createWidgets() #top menu
        self.window.mainloop()

    # 1st window
    # this create winfo   --> Try it! <--
    def createWidgets(self):
        top = self.window.winfo_toplevel()
        self.menuBar = Menu(top)
        top["menu"] = self.menuBar
        self.subMenu = Menu(self.menuBar)
        self.menuBar.add_cascade(label="About", menu=self.subMenu)
        self.subMenu.add_command(label="Team Logo(example)", command=self.aboutUs) 


    def aboutUs(self):
        about = Toplevel(self.window)
        about.title("About Us")
        # img = ImageTk.PhotoImage(Image.open("./Project/python_ninjas_logo2.jpg")) #1st way this needs to import PIL 
        img = PhotoImage(file="./Project/fourninjas with python.png") #2nd way , .png can be used in both 1 and 2
        # Display the image in a Label
        img_label = Label(about, image=img)
        img_label.pack()
        about.mainloop()

    def show_Info(self):
        show_window = Toplevel(self.window)
        show_window.title("All Cars Info ")
        show_window.geometry("500x500")

        open_btn = Button(show_window, text="Show datas", command=self.display_info)
        open_btn.pack(padx=10, pady=10)

        self.data_info = Label(show_window, text="")
        self.data_info.pack(pady=5)

        # tree view shows columnwide so I created yscroll only

        self.tree = ttk.Treeview(show_window, show="headings")
        self.tree.pack(padx=20, pady=20, fill="both", expand=True)
        yscroll = Scrollbar(self.tree, orient='vertical', command=self.tree.yview)
        yscroll.pack(side=RIGHT, fill=Y)
        self.tree.config(yscrollcommand=yscroll.set)
        # set heading row color
        style = ttk.Style()
        style.theme_use('default')  # try with different theme ('clam', etc..)
        style.configure('Treeview.Heading', background="skyblue")
        show_window.mainloop()





    def load_file(self):
        file = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open file", 
        filetypes=(("CSV file", "*.csv"), ("Text file", "*.txt"), ("All file", "*"))
        )
        self.file = file
        with open(self.file, newline='') as file:
            csv_reader = csv.reader(file)
            self.datas = [row for row in csv_reader]
        # print(self.datas)
        # if file:
        #     self.display_info()

    def display_info(self):
        
        try:
            with open(self.file, 'r', newline='') as file:
                csv_reader = csv.reader(file)
                header = next(csv_reader)  # Read the header row
                self.tree.delete(*self.tree.get_children())  # Clear the current data

                brands= [] # to display number of brands
                self.tree["columns"] = header
                for col in header:
                    self.tree.heading(col, text=col)
                    self.tree.column(col, width=100)
                
                count = 0
                for row in csv_reader:
                    self.tree.insert("", "end", values=row)
                    count += 1 # to count rows
                    if row[0] not in brands:
                        brands.append(row[0])
                # use config to add arguments
                self.data_info.config(text=f"There are {count} {self.__class__.__name__} with {len(brands)} different types.")

        except Exception as e:
            self.data_info.config(text=f"{e}",fg="red")

    # 2nd window
    def explore_Info(self):
        try:
            info_win = Toplevel(self.window)
            info_win.title("Add & Explore")

            n = round(len(self.datas[0])/2)
            fst_half = self.datas[0][:n+1]  # to display more in 1st half
            scd_half = self.datas[0][n+1:]

            frame1 = Frame(info_win, background="lightblue",borderwidth=10)
            frame1.grid(row=0, rowspan=10, column=0, columnspan=20, padx=10, pady=20, ipadx=100)
            self.entries = []
            # value = StringVar()
            

            for i in range(len(fst_half)):
                Label(frame1, text=f"{fst_half[i]} : ",background="lightblue").grid(row=i, column=0, padx= 20,  pady=5)
                e = Entry(frame1, font=("Consolas", 12))
                e.delete(0, END) # <----- 
                e.grid(row=i, column=1, columnspan=5, pady=5, ipadx=5) # row ends at 7
                self.entries.append(e)

            for i in range(len(scd_half)):
                Label(frame1, text=f"{scd_half[i]} : ", background="lightblue").grid(row=i, column=10, padx=20, pady=5)
                e = Entry(frame1, font=("Consolas", 12))
                e.grid(row=i, column=11, columnspan=5, pady=5, ipadx=5)
                self.entries.append(e)

            self.val_lst = [] # to store entry values for many functions ,and this will use in data manipulation
            self.hist_lst = [] # to store what we type in entry as list

            self.option_lst = ["Search", "Add", "Edit", "*Delete", "**Delete All"]
            self.btns = [] ## not used yet
            for i, opt in enumerate(self.option_lst):
                btn = Button(info_win, text=opt, command=lambda a=i: self.process_button(a)) # I will go with i instead of opt
                btn.grid(row=12, column=3+i*2, columnspan=3, padx=15, pady=10, ipadx=5, ipady=5)
                self.btns.append(btn)

            self.opt_labl=Label(info_win, text="")
            self.opt_labl.grid(row=15, column=1)
            self.show_txt = Entry(info_win, borderwidth=2, font=("Consolas", 12))
            self.show_txt.grid(row=15, rowspan=2, column=4, columnspan=8, pady=10, ipady=5, ipadx=350)

            frame2 = Frame(info_win, background="coral", height= 10, borderwidth=1)
            frame2.grid(row=17, column=0, columnspan=30, padx=30, ipadx=3, ipady=3)

            self.txt_area = Text(frame2, width=100, height=17, wrap=NONE)
            self.txt_area.grid(row=17,column=1, padx=1, pady=1)
            # txt_area.grid(column=1)
            # txt_area.tag_configure(1, background='beige')
            # txt_area.tag_configure(2, background='white')
            xscroll= Scrollbar(frame2, orient="horizontal", command=self.txt_area.xview, highlightcolor="blue")
            yscroll= Scrollbar(frame2, orient="vertical",command=self.txt_area.yview, activebackground="skyblue")
            xscroll.grid(column=1, sticky=N, ipadx=376)
            yscroll.grid(row=17, column=2, sticky=E, ipady=111)

            self.txt_area.config(xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

            # print(self.entries)
            # print(self.btns)
            # print(self.val_lst)
            
            info_win.mainloop()
            
        except Exception as e:
            self.info_labl.config(text=f"{e} \nYour data is {self.datas}! Please load the data!")

    def process_button(self, i):
        self.show_txt.delete(0, END)
        self.val_lst.clear() 
        temp_lst = [self.option_lst[i]] # to store what we type in entry each button press
        txt=""
        for e in self.entries:
            if self.entries[0] == e:
                value=e.get().upper()
                self.val_lst.append(value) 
                temp_lst.append(value) 
                txt += value + ", "
            else:
                # if e.get().isdigit():    still thinking
                #     self.val_lst.append(int(e.get()))
                # else:
                self.val_lst.append(e.get())
                temp_lst.append(e.get())
                txt += e.get() + ", "

        self.hist_lst.append(temp_lst)
        self.show_txt.insert(END, txt)
        self.opt_labl.config(text=f"To {self.option_lst[i]}..")

        if i == 0:
            show_all = 0 # to check each entry is empty or not, 0 means empty 
            for value in self.val_lst:
                show_all += len(value)
            # print(self.val_lst)
            # print(show_all)
            # print(self.hist_lst)
            if show_all == 0: # that means all entry are empty(string)
                self.show_Info() # it will search all data files(i.e.show all datas)
            else:
                self.search_Info()
        # elif i == 1:
        #     self.add_Info()
        # elif i == 2:
        #     self.edit_Info()
        # elif i == 3:
        #     self.delete_Info()
        # else:
        #     self.delete_AllInfo()

    def search_Info(self):
        self.txt_area.delete(1.0, END)
        result = [data for data in self.datas if all(item in data for item in self.val_lst if item != '')]
        self.txt_area.insert(1.0, f"{len(result)} results were found.\n\n") # I omiited brand or model to place in 
        self.txt_area.insert(END, f"{', '.join(word.strip() for word in self.datas[0])}\n")
        # self.txt_area.insert(END, '\n')
        for row in result:
            self.txt_area.insert(END, f"{', '.join(word.strip() for word in row)}\n")


EVcars()
