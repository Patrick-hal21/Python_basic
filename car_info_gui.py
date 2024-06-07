from tkinter import *
from tkinter import ttk  # for Treeview
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image # to manipulate images
import os
import csv

class EVcars():

    def __init__(self):
        self.window = Tk()
        # icon = ImageTk.PhotoImage(Image.open("./Project/python_ninjas_logo2.jpg")) for .jpg
        icon = PhotoImage(file="./Project/fourninjas with python.png")
        self.window.title("Ninjas EV Trading System")
        self.window.iconphoto(True, icon) #set True to set that icon in all self.window & its descendents
        self.window.geometry("800x600")
        self.window.config(bg="lightblue")
        # created file, load_btn to load file and store it to use in other windows without repeating load_file 
        self.file = None 
        self.datas = None

        self.hist_dict = {} # to store what we type in entry as list # modified place
        self.val_lst = [] # I moved it here
        
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)

        # self.main_frame = Frame(self.window)
        # self.main_frame.grid(row=0, column=0, sticky="nsew")
        # self.main_frame.columnconfigure(0, weight=1)
        # self.main_frame.rowconfigure(0, weight=1)
        
        self.start_page()
        self.createWidgets() #top menu
        self.menuBar.entryconfig(" Home ", state=DISABLED)
        self.window.mainloop()

    def start_page(self):

        self.start_frame = Frame(self.window, bg="lightblue")
        # self.start_frame.pack(fill=BOTH, expand=True)
        self.start_frame.grid(row=0, column=0, sticky="nsew")

        self.start_frame.columnconfigure(0, weight=1)
        self.start_frame.rowconfigure(6, weight=1)

        self.noti_labl = Label(self.start_frame, text="Please load file first!", bg="black", fg="white", font=('', 10, 'bold'))
        self.noti_labl.grid(row=0, column=0, columnspan=2, pady=20, ipadx=5, ipady=5)

        self.load_btn = Button(self.start_frame, relief="raised", text="Load file", activebackground="darkblue", command=self.load_file, bg="blue", fg="white", font=('Consolas', 10))
        self.load_btn.grid(row=1, column=0, pady=5, ipadx=5, ipady=5)

        Button(self.start_frame, text="Show Cars Info", activebackground="darkblue", relief="raised", command=self.show_Info, bg="blue", fg="white", font=('Consolas', 10)).grid(row=2, column=0, pady=20, ipadx=5, ipady=5)

        Button(self.start_frame, text="More..", activebackground="darkblue", relief="raised", command=self.explore_Info, bg="blue", fg="white", font=('Consolas', 10)).grid(row=3, column=0, pady=20, ipadx=5, ipady=5)

        self.info_labl = Label(self.start_frame, text='', fg="red", bg="lightblue")
        self.info_labl.grid(row=4, column=0)  # Adjust row as needed

        Button(self.start_frame, text="Quit", activeforeground="red", relief="raised", bg="blue", fg="white", font=('Consolas', 10), command=self.ask_confirm).grid(row=5, column=0, pady=10)

        Label(self.start_frame, text="Presented by Team-3 (The Python Ninjas)", font=2, bg="lightblue").grid(row=6, column=0, sticky='sw')

        
    def ask_confirm(self):
        response = messagebox.askokcancel("Conirmation", "Are you sure to quit?")
        if response:
            self.window.destroy()
        else:
            pass

    def load_file(self):

        file = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open file", 
        filetypes=(("CSV file", "*.csv"), ("Text file", "*.txt"), ("All file", "*"))
        )
        self.file = file
        if self.file:
            self.info_labl.config(text="File loaded!", fg="green", font=1)
            self.noti_labl.config(text=f"{self.file.split('/')[-1]} is in load.")
            self.load_btn.config(text="Load Another File")
            with open(self.file, newline='') as file:
                csv_reader = csv.reader(file)
                self.datas = [row for row in csv_reader]
            # print(self.datas)
            # if file:
            #     self.display_info()


    # 1st window
    # this create winfo   --> Try it! <--
    def createWidgets(self):
        top = self.window.winfo_toplevel()
        self.menuBar = Menu(top)
        top.config(menu=self.menuBar)
        self.subMenu = Menu(self.menuBar, tearoff=0)

        self.menuBar.add_cascade(label=" About ",activebackground="blue", menu=self.subMenu)
        self.subMenu.add_command(label="Team Logo(example)",activebackground="blue", command=self.aboutUs)

        self.menuBar.add_cascade(label=" Home ", command=self.start_frame.tkraise)
        self.menuBar.add_cascade(label=" Info ", activebackground="blue", command=self.show_cars_info_ico) 
        


    def aboutUs(self):
        about = Toplevel(self.window)
        about.title("About Us")
        # img = ImageTk.PhotoImage(Image.open("./Project/python_ninjas_logo2.jpg")) #1st way this needs to import PIL 
        img = PhotoImage(file="./Project/fourninjas with python.png") #2nd way , .png can be used in both 1 and 2
        # Display the image in a Label
        self.menuBar.entryconfig(" Home ", state="normal")
        img_label = Label(about, image=img)
        img_label.pack()
        about.mainloop()


    # Show all cars info frame 
    def show_Info(self):
        
        if self.file:
            # self.info_labl.config(text="")
            # show_window = Toplevel(self.window)
            # show_window.title("All Cars Info ")
            # show_window.geometry("800x600")
            # show_window.columnconfigure(0, weight=1)
            # show_window.rowconfigure(0, weight=1)
            self.menuBar.entryconfig(" Home ", state = NORMAL)

            self.display_frame = Frame(self.window)
            self.display_frame.grid(row=0, column=0, sticky="nsew")

            back_btn = Button(self.display_frame, relief="sunken", text="<< Back", bg="blue", fg="white", command=lambda: [self.start_frame.tkraise(), self.display_frame.destroy()])
            open_btn = Button(self.display_frame, relief="sunken", text="Show datas", bg="blue", fg="white", command=self.display_info)
            back_btn.pack(anchor=W, padx=10, pady=10)
            open_btn.pack(padx=10, pady=10)

            self.data_info = Label(self.display_frame, text="")
            self.data_info.pack(pady=5)

            # tree view shows columnwide so I created yscroll only
            self.tree = ttk.Treeview(self.display_frame, show="headings")
            self.tree.pack(padx=20, pady=20, fill="both", expand=True)
            yscroll = Scrollbar(self.tree, relief="sunken", orient='vertical', command=self.tree.yview)
            yscroll.pack(side=RIGHT, fill=Y)
            self.tree.config(yscrollcommand=yscroll.set)
            
            # set heading row color
            style = ttk.Style()
            style.theme_use('default')  # try with different theme ('clam', etc..)
            style.configure('Treeview.Heading', background="skyblue")
            # show_window.mainloop()
        
        else:
            self.info_labl.config(text="File is not loaded yet!\nPlease load it!", fg="red")


    def display_info(self):

        try:
            # self.info_labl.config(text="")
            with open(self.file, 'r', newline='') as file:
                csv_reader = csv.reader(file)
                header = next(csv_reader)  # Read the header row
                self.tree.delete(*self.tree.get_children())  # Clear the current data

                brands= [] # to display number of brands
                self.tree["columns"] = header
                for col in header:
                    self.tree.heading(col, text=col)
                    self.tree.column(col, width=100)
                
                # for row colors
                self.tree.tag_configure("oddrow", background="lightblue")
                self.tree.tag_configure("evenrow", background="blanched almond")

                count = 0
                for i, row in enumerate(csv_reader):
                    tags = "evenrow" if i % 2 == 0 else "oddrow"
                    self.tree.insert("", "end", values=row, tag=tags)
                    count += 1 # to count rows
                    if row[0] not in brands:
                        brands.append(row[0]) # can  also use this line only and later use set() to remove duplicates
                # use config to add arguments
                self.data_info.config(text=f"There are {count} {self.__class__.__name__} with {len(brands)} different types.")

        except Exception as e:
            self.data_info.config(text=f"{e}",fg="red")

    # Frame 2  
    def explore_Info(self):

        if self.file:
            # self.info_labl.config(text="")
            # self.info_win = Toplevel(self.window)
            # self.info_win.title("Add & Explore")
            # self.info_win.geometry("800x600")
            self.menuBar.entryconfig(" Home ", state=NORMAL)

            # self.explore_frame = Frame(self.window)
            # self.explore_frame.grid(row=0, column=0, sticky="nsew")
            # #self.explore_frame.tkraise # optional

            # # self.info_win.columnconfigure(0, weight=1)
            # # self.info_win.rowconfigure(0, weight=1)
            # self.explore_frame.columnconfigure(0, weight=0)

            self.num = round(len(self.datas[0])/2)
            self.fst_half = self.datas[0][:self.num+1]  # to display more in 1st half
            self.scd_half = self.datas[0][self.num+1:]

            self.search_frame = Frame(self.window)
            self.search_frame.grid(row=0, column=0, sticky="nsew")
            self.search_frame.columnconfigure(0, weight=1)


            frame1 = Frame(self.search_frame, background="lightblue",borderwidth=10)
            frame1.grid(row=0, rowspan=9, column=0, padx=10, pady=20, columnspan=20, ipadx=100)#,sticky="we")#, 
            self.entries = []
            # value = StringVar()
            

            for i in range(len(self.fst_half)):
                Label(frame1, text=f"{self.fst_half[i]} : ",background="lightblue").grid(row=i, column=0, padx= 20,  pady=5, sticky=W)
                e = Entry(frame1, font=("Consolas", 12))
                e.delete(0, END) # <----- 
                e.grid(row=i, column=1, columnspan=5, pady=5, ipadx=5) # row ends at 7
                self.entries.append(e)

            for i in range(len(self.scd_half)):
                Label(frame1, text=f"{self.scd_half[i]} : ", background="lightblue").grid(row=i, column=10, padx=30, pady=5, sticky=W)
                e = Entry(frame1, font=("Consolas", 12))
                e.grid(row=i, column=11, columnspan=5, pady=5, ipadx=5)
                self.entries.append(e)

            # self.val_lst = [] # to store entry values for many functions ,and this will use in data manipulation
            # self.hist_lst = [] # to store what we type in entry as list   # origin (we moved them cuz destroying widget also delete them)

            # self.option_lst = ["<< Back", "Search", "Add", "Edit", "*Delete", "**Delete All"] 1st usage
            btn_frame = Frame(self.search_frame)
            btn_frame.grid(row=10, column=0, sticky="ns")

            self.option_lst = ["<< Back", "Search", "Add", "Next >>"]
            self.btns = [] ## not used yet
            for i, opt in enumerate(self.option_lst):
                btn = Button(btn_frame, relief="sunken", activebackground="blue", text=opt, command=lambda a=i: self.process_button(a)) # I will go with i instead of opt
                btn.grid(row=1, column=3+i*2, padx=20, pady=5, ipadx=10, ipady=5, sticky="we")
                self.btns.append(btn)

            # self.show_txt = Entry(btn_frame, borderwidth=2, font=("Consolas", 10))
            # self.show_txt.grid(row=2, column=5,sticky="we")#, ipady=5, ipadx=350)

            frame2 = Frame(self.search_frame, background="coral", borderwidth=1)
            frame2.grid(row=17, column=0, columnspan=30, padx=30, ipadx=3, ipady=3, sticky="nswe")
            # # frame2.grid_propagate()

            frame2.columnconfigure(0, weight=1)
            frame2.rowconfigure(0, weight=1)

            self.show_txt = Entry(frame2, borderwidth=2, font=("Consolas", 12), justify="center")
            self.show_txt.grid(row=0, column=0, sticky="we")#, ipady=5, ipadx=350)

            self.tree_search = ttk.Treeview(frame2, show="headings", selectmode='browse')
            self.tree_search.grid(row=1, column=0, sticky="nsew")

            # self.txt_area = Text(frame2, width=100, height=15, wrap=NONE,  font=("Consolas", 12))
            # self.txt_area.grid(row=16,column=1, padx=1, pady=1)
            # txt_area.grid(column=1)
            # txt_area.tag_configure(1, background='beige')
            # txt_area.tag_configure(2, background='white')
            # xscroll= Scrollbar(self.tree_search, orient="horizontal", command=self.tree_search.xview, highlightcolor="blue")
            yscroll= Scrollbar(frame2, orient="vertical",command=self.tree_search.yview, activebackground="skyblue")
            # xscroll.grid(row=17,column=1, sticky=N)#, ipadx=420)
            yscroll.grid(row=1, column=1, sticky=NS)#, ipady=120)

            self.tree_search.config(yscrollcommand=yscroll.set)

            # print(self.entries)
            # print(self.btns)
            # print(self.val_lst)
            
            # self.info_win.mainloop()
            
        else:
            self.info_labl.config(text=f"\nYour data is {self.datas}! Please load the data!")

    def process_button(self, i):
        self.show_txt.config(state="normal")
        self.show_txt.delete(0, END)
        # it will clear entries values list whenever button is clicked
        self.val_lst.clear() 
        temp_lst = [self.option_lst[i]] # to store what we type in entry each button press
        for e in self.entries:
            if self.entries[0] == e:
                value=e.get().upper()
                self.val_lst.append(value) 
                temp_lst.append(value) 
            else:
                # if e.get().isdigit():    still thinking
                #     self.val_lst.append(int(e.get()))
                # else:
                self.val_lst.append(e.get())
                temp_lst.append(e.get())

        if i in [1, 2]:
            # self.show_txt.insert(END, txt)
            # self.show_txt.config(state="readonly")
            # self.opt_labl.config(text=f"To {self.option_lst[i]}..")
            self.hist_dict["Searched"] = temp_lst

        if i == 0:
            self.start_frame.tkraise()
            self.search_frame.destroy()

        elif i == 1:
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
                self.show_txt.config(state="readonly")
        elif i == 2:
            self.add_Info()
        else:
            self.next_Catego()  


        # elif i == 3:
        #     self.edit_Info()
        # elif i == 4:
        #     self.delete_Info()
        # else:
        #     self.delete_AllInfo()

    def search_Info(self): ## need to modify , try to search with index
        
        # self.txt_area.delete(1.0, END) # to del
        self.tree_search.delete(*self.tree_search.get_children())
        header = self.datas[0]
        self.tree_search["columns"] = header
        for col in header:
            self.tree_search.heading(col, text=col)
            self.tree_search.column(col, width=30)

        search_lst = [data for data in self.val_lst if data != ""]
        result = [data for data in self.datas if all(item in data for item in search_lst )]        
        # result = [data for data in self.datas if all(item in data for item in self.val_lst if item != '')]
        # result = [data for data in self.datas if any(item in data for item in self.val_lst if item != '' )]  # prefered one ,    all returns True if bool(x) is  True for all value in iterable
        
        self.show_txt.insert(END, f"{len(result)} results were found")
        self.show_txt.config(state="readonly")

        for row in result:
            self.tree_search.insert("", "end", values=row)
        # self.txt_area.insert(1.0, f"{len(result)} results were found.\n\n") # I omiited brand or model to place in 
        
        # self.txt_area.insert(END, f"{' , '.join(word.strip() for word in self.datas[0])}\n")
        # # self.txt_area.insert(END, '\n')
        # for row in result:
        #     self.txt_area.insert(END, f"{' , '.join(word.strip() for word in row)}\n")


    def add_Info(self):
        # always clear textarea
        # self.txt_area.delete(1.0, END)  we dont need this here
        add_list = []
        for value in self.val_lst:
            if value == "":
                add_list.append("-")
            else:
                add_list.append(value)
        # print(add_list) 
        # self.txt_area.tag_configure("warn", foreground='red')
        # self.txt_area.tag_configure("success", foreground="blue")
        self.tree_search.delete(*self.tree_search.get_children())
        header = self.datas[0]
        self.tree_search["columns"] = header
        for col in header:
            self.tree_search.heading(col, text=col)
            self.tree_search.column(col, width=30, anchor='w')

        # to display brand and model are must fill entries
        if add_list[0] != "" or add_list[1] != "":
            # if same brand and model name in original data, adding data can;t be done.
            if add_list[0] in [data[0] for data in self.datas[1:]] and \
                add_list[1] in [data[1] for data in self.datas[1:]]:

                self.show_txt.config(fg="red")
                self.show_txt.insert("end", f"{self.datas[0][0]} : {add_list[0]}, {self.datas[0][1]} : {add_list[1]} are in your {self.__class__.__name__}.")
                # print(f"Your added data [{add_list[0]}, {add_list[1]}] are already in {self.__class__.__name__}")
            else:
                # self.txt_area.insert(END, f"Your data is added as\n\n {', '.join(word.strip() for word in self.datas[0])}\n", "success")
                # self.txt_area.insert(END, f" {', '.join(item for item in add_list)}", "success")

                self.show_txt.config(fg="green")
                self.show_txt.insert(END, "Your data is added!")
                self.tree_search.insert("", END, values=add_list)
                # print("Your data is added")
        else:   
            if add_list[0] == "":
                self.entries[0].focus_set()
            else:
                self.entries[1].focus_set()
            self.show_txt.config(txt=f"PLease fill both {self.datas[0]} and self{self.datas[1]}!", foreground="red")

    # Edit & Delete Frame 3
    def next_Catego(self):
        # self.next_cat = Toplevel(self.window)
        # self.next_cat.title("Edit, Delete..")
        # self.next_cat.geometry("800x600")
        # self.next_cat.transient(self.window) # to ensure this toplevel is on top of main window when msgbox shows up
        # here I add menu # (draft)

        self.edit_del_frame = Frame(self.window)
        self.edit_del_frame.grid(row=0, column=0, sticky="nswe")
        self.edit_del_frame.columnconfigure(5, weight=1)
        #self.edit_del_frame.tkraise() # (optional) display this frame

        # self.menu2 = Menu(self.window)
        # self.window.config(menu=self.menu2)
        self.menuBar.add_cascade(label="Edit", activebackground="blue", command=self.menu_edit)
        self.menuBar.add_cascade(label="Delete", activebackground="blue", command=self.menu_delete)

        # messagebox.showinfo("Information", f"Be sure to fill *required datas({self.datas[0][0]}, {self.datas[0][1]}) in which {self.datas[0][1]} name must be price.") # test useage
        self.menu_edit()

        # self.next_cat.mainloop()

    
    def menu_edit(self): # to store above codes which are for editing,(draft)
        # first I decided to disable the current menu button(mean I was in that menu)
        self.menuBar.entryconfig("Edit", state="disabled")
        self.menuBar.entryconfig("Delete", state="normal")
        
        try:
            self.frame4.destroy()
        except:
            pass

        self.frame3 = Frame(self.edit_del_frame, background="lightblue", width=500, borderwidth=5)
        self.frame3.grid(row=2, column=5, columnspan=20, rowspan=30, padx=120, pady=20, ipadx=100, ipady=100, sticky="n")
        Label(self.frame3, text="Editing").grid(row=1, column=0)

        self.intro_labl = Label(self.frame3, text="Please fill both of these!")
        self.labl1 = Label(self.frame3, text=f"{self.datas[0][0]}: ", pady=5, font=5) 
        self.ent1 = Entry(self.frame3, takefocus="",  font=("Consolas", 12), state="normal")
        self.ent1.bind("<Button-3>", lambda event: self.popup_fill_val(0, event))
        
        self.labl2 = Label(self.frame3, text=f"{self.datas[0][1]}: ", pady=5, font=5)
        self.ent2 = Entry(self.frame3, font=("Consolas", 12), state="normal")
        self.ent2.bind("<Button-3>", lambda event: self.popup_fill_val(1, event, self.ent1.get()))


        self.cont_btn = Button(self.frame3, relief="sunken", activebackground="blue", text="Continue", command=self.show_up)
        self.back_btn2 = Button(self.frame3, relief="sunken", activebackground="blue", text="<< Back", command=lambda: [self.next_cat.destroy(), self.explore_Info()])

        self.intro_labl.grid(row=4, column=3,sticky=S, pady=10, padx=10)
        self.labl1.grid(row=5, column=2, pady=10, padx=10, sticky=W)
        self.ent1.grid(row=5, column= 3, padx=10, pady=10)
        self.labl2.grid(row=7, column=2, pady=10, padx=10, sticky=W)
        self.ent2.grid(row=7, column= 3, padx=10, pady=10)
        self.back_btn2.grid(row=9, column=1, padx=10, pady=10)
        self.cont_btn.grid(row=9, column=3, padx=10, pady=10)
        # self.menu2.update_idletasks()


    # copied from  ChatGpt and modified it
    def show_up(self, edit=False):

        if edit:
            frame = self.frame4
            func = self.del_vals
        else:
            frame = self.frame3
            func = self.find_edit
        self.vars = [] # to store checkbuttons' var and, by iterating with .get(), we will get value

        self.val_lst.clear() # clear list to have only two values whenever the button is clicked
        self.val_lst.append(self.ent1.get().upper())
        self.val_lst.append(self.ent2.get())

        if "" in self.val_lst:
            self.intro_labl.config(fg="red")

        self.edit_index = 0 # index number of self.datas to edit, iniial value set to 0
        self.check_lst = [data for data in self.datas if all(item in data for item in self.val_lst)]

        if self.check_lst:
            self.intro_labl.config(fg="black")
            self.edit_index = self.datas.index(self.check_lst[0]) # here row index of inserted Brand, Model is added
        # print(self.check_lst)
            # self.warn_labl1.config(text="", bg="lightblue")
            try:   
                self.warn_labl1.destroy() 
            except Exception:
                pass 
            self.ent1.config(state="readonly")
            self.ent2.config(state="readonly")   
            self.canvas1 = Canvas(frame, background="beige", width=100, height=100, borderwidth=5)
            self.canvas1.grid(row=8, column=3,padx=5,sticky=S)

            self.canvas_labl = Label(self.canvas1, text="Please select option(s) to edit...")
            self.canvas_labl.grid(row=2, column=3)
            
            # half1 = len(self.datas[0]) // 2
            for i, item in enumerate(self.datas[0][2:], start=2):
                var = IntVar()  # Create a separate variable for each checkbutton
                # row_offset = i - 1 if i < half1 else i - half1
                chck_btn = Checkbutton(self.canvas1, text=item, justify="left", variable=var, onvalue=i, offvalue=0)
                chck_btn.grid(row=3+i, column=4, padx=5, pady=5, sticky=W)
                self.vars.append(var)
            # print(self.var_lst)

            # self.cont_btn.deletecommand(self.show_up) #  I though to use this to use one continue btn and overwrite the command
            # self.cont_btn1.config(command=self.find_edit)

            self.back_btn3 = Button(self.canvas1, relief="sunken", activebackground="blue", text="..Back", bg="lightgrey", fg="darkblue",
                                     command=lambda:[self.canvas1.destroy(), self.ent1.config(state="normal"), self.ent2.config(state="normal")])
            self.back_btn3.grid(row=16, column=3, sticky=W, padx=5, pady=5)
            self.cont_btn1 = Button(self.canvas1, relief="sunken", activebackground="blue", text="Continue..", bg="lightgrey", fg="darkblue", command=func)
            self.cont_btn1.grid(row=16, column=5, sticky=E, padx=5, pady=5)
        else:
            self.warn_labl1 = Label(frame)
            self.warn_labl1.grid(row=8, column=3)
            self.warn_labl1.config(text="There is no matched data!\n Try some specific values!\nFor more info, check in Show Cars Info", fg="red")
    


    def find_edit(self): # use in button command
        
        # self.canvas1.destroy() 
        self.canvas1.grid_forget() # thinking I should use this now and later(it causes high momory usage), but I use this and grid again its position is just sticky in W
        self.check_var = [c.get() for c in self.vars if c.get() != 0] # this contains index to search

        self.entries.clear() # clear the created list if it needs to use in descendent methods
        self.canvas2 = Canvas(self.frame3, background="beige", width=200, height=100, borderwidth=5)
        self.canvas2.grid(row=8, column=3,padx=5, pady=10, ipadx=5)

        if len(self.check_var) > 0:
            try:
                label.destroy()
            except Exception:
                pass
            finally:
                    for n,index in enumerate(self.check_var, 1): #to increase row number
                        Label(self.canvas2, text=self.datas[0][index]).grid(row=1+n if n < 6 else n-4, column=0 if n < 6 else 3, pady=5, sticky=W)
                        e=Entry(self.canvas2, width=20)     # if we get ""(means user omiited or leaved blank), what will we do?
                        e.grid(row=1+n if n < 6 else n-4, column=1 if n < 6 else 4, pady=5)
                        self.entries.append(e)
                    self.back_btn4 = Button(self.canvas2, relief="sunken", activebackground="blue", text="..Back", bg="lightgrey", fg="darkblue", command=lambda:[self.canvas2.grid_forget(), self.canvas1.grid(row=8, column=3,padx=5,sticky=S)]) # try add frid parameters or better wrap destroy canvas in function
                    self.back_btn4.grid(row=8, column=0, sticky=W+N, padx=5, pady=5)
                    self.cont_btn2 = Button(self.canvas2, text="Continue..", activebackground="blue", bg="lightgrey", fg="darkblue", command=lambda:[self.canvas2.grid_forget(), self.edit_value()])
                    self.cont_btn2.grid(row=8, column=6, sticky=E+N, padx=5, pady=5)
        else:
            label = Label(self.canvas2, text="You didn't select any option. Please select at least one!", fg="red")
            label.grid(row=2, column=2)

            self.back_btn4 = Button(self.canvas2, relief="sunken", activebackground="blue", text="..Back", bg="lightgrey", fg="darkblue", command=lambda:[self.canvas2.grid_forget(), self.canvas1.grid(row=8, column=3,padx=5,sticky=S)]) # try add frid parameters or better wrap destroy canvas in function
            self.back_btn4.grid(row=8, column=0, sticky=W+N, padx=5, pady=5)
        # self.cont_btn2 = Button(self.canvas2, text="Continue..", activebackground="blue", bg="lightgrey", fg="darkblue", command=lambda:[self.canvas2.grid_forget(), self.edit_value()])
        # self.cont_btn2.grid(row=8, column=6, sticky=E+N, padx=5, pady=5)
        
    def edit_value(self): # use in button

        self.val_lst.clear() # clear list first because I will reuse it in this method

        # here I can add if else statement to manipulate empty entry("")
        self.val_lst=[e.get() for e in self.entries] # I can use it directly without clearing its contents
        self.vals_to_edit = [*zip(self.check_var, self.val_lst)] #store zipped two lists(unzip with *) , result will look like eg.(2, value for Battery column)

        # print(self.edit_index)                 #check edit_index is correct
        edit_row = self.datas[self.edit_index]     # <--- if I dont need to use later, I dont add self.           
        self.origin_val = {} # created this for creating revert method in case

        for i, value in self.vals_to_edit:
            self.origin_val[f"row index {i}"] = [edit_row[:2], "origin value -" + edit_row[i], "edited value -" + value] #optional

            edit_row[i] = value

        self.hist_dict["Edited"] = self.origin_val
        # can also add in command of 407line's button
        self.save_datas()
        self.canvas2.destroy() 

        # Should I do followings in messagebox?
        self.canvas3 = Canvas(self.frame3, width=50, height=30)
        self.canvas3.grid(row=8, column=3,padx=5, pady=10, ipadx=5)
        Label(self.canvas3, text="Your data has successfully added!", fg="green").grid(row=2, column=2)
        Label(self.canvas3, text="You can check it by reloading file and in Show Cars Info").grid(row=4, column=2)
        Button(self.canvas3, relief="sunken", activebackground="blue", text="Edit more..", command=self.canvas3.grid_forget).grid(row=7, column=0, sticky=W+N, padx=5, pady=5)
        Button(self.canvas3, relief="sunken", activebackground="blue", text="Ok", command=self.next_cat.destroy).grid(row=7, column=6, sticky=E+N, padx=5, pady=5)


    def menu_delete(self):
        # first I decided to disable the current menu button(mean I was in that menu)
        self.menuBar.entryconfig("Delete", state="disabled")
        self.menuBar.entryconfig("Edit", state="normal")
        # self.menu2.update_idletasks()
        #4/6/24
        try:
            self.frame3.destroy()
        except:
            pass
        self.frame4 = Frame(self.edit_del_frame, background="lightblue", width=500, borderwidth=5)
        self.frame4.grid(row=2, column=5, columnspan=20, rowspan=30, padx=120, pady=30, ipadx=100, ipady=100, sticky="n")
        Button(self.frame4, text="Delete whole file", fg="red", command=self.delete_file).grid(row=1, column=3, ipadx=5, ipady=5, sticky="s")
        Label(self.frame4, text="Deleting...").grid(row=1, column=0, pady=5)
        self.delete_fram()

    def del_msg_box(self):

        self.val_lst.clear() # clear list to have only two values whenever the button is clicked
        self.val_lst.append(self.ent1.get().upper())
        self.val_lst.append(self.ent2.get())

        self.delete_index = 0 # index number of self.datas to edit, iniial value set to 0
        self.check_lst = [data for data in self.datas if all(item in data for item in self.val_lst)]
        self.delete_index = self.datas.index(self.check_lst[0])

        response = messagebox.askquestion("How", "1. Do you want to delete column value(s)?")
        if response == "yes":
            self.show_up(True)
        else:
            response1 = messagebox.askquestion("How", "2. Do you want to delete row?")
            if response1 == "yes":
                self.delete_row()
            else:
                pass
        

        
    def delete_fram(self):
        # messagebox.showinfo("Information", f"Be sure to fill *required datas({self.datas[0][0]}, {self.datas[0][1]}) in which {self.datas[0][1]} name must be precise.") # try useage

        # I use same variable names as in next_cat(menu_edit) cuz we will only use one at a time,  can also use diff variable names in this
        # self.frame3 = Frame(self.next_cat, background="lightblue", width=500, borderwidth=5)
        # self.frame3.grid(row=2, column=5, columnspan=20, rowspan=30, ipadx=100, ipady=100)

        self.intro_labl = Label(self.frame4, text="Please fill both of these!")
        self.labl1 = Label(self.frame4, text=f"{self.datas[0][0]}: ", pady=5, font=5) 
        self.ent1 = Entry(self.frame4, takefocus="",  font=("Consolas", 12), state="normal")
        self.ent1.bind("<Button-3>", lambda event: self.popup_fill_val(0, event))

        self.labl2 = Label(self.frame4, text=f"{self.datas[0][1]}: ", pady=5, font=5)
        self.ent2 = Entry(self.frame4, font=("Consolas", 12), state="normal")
        self.ent2.bind("<Button-3>", lambda event: self.popup_fill_val(1, event, self.ent1.get()))

        self.cont_btn = Button(self.frame4, relief="raised", activebackground="blue", text="Continue", command=self.del_msg_box)
        self.back_btn2 = Button(self.frame4, relief="raised", activebackground="blue", text="<< Back", command=lambda: [self.frame4.grid_forget(), self.explore_Info()])

        self.intro_labl.grid(row=4, column=3,sticky=S, pady=10, padx=10)
        self.labl1.grid(row=5, column=2, pady=10, padx=10, sticky=W)
        self.ent1.grid(row=5, column= 3, padx=10, pady=10)
        self.labl2.grid(row=7, column=2, pady=10, padx=10, sticky=W)
        self.ent2.grid(row=7, column= 3, padx=10, pady=10)
        self.back_btn2.grid(row=9, column=1, padx=10, pady=10)
        self.cont_btn.grid(row=9, column=3, padx=10, pady=10)

    def del_vals(self):
        self.canvas1.grid_forget() # thinking I should use this now and later(it causes high momory usage), but I use this and grid again its position is just sticky in W
        self.check_var = [c.get() for c in self.vars if c.get() != 0] # this contains index to search

        self.canvas2 = Canvas(self.frame4, background="beige", width=200, height=100, borderwidth=5)
        self.canvas2.grid(row=8, column=3,padx=5, pady=10, ipadx=5)

        if len(self.check_var) > 0:
            try:
                label.destroy()
            # except Exception:
            #     pass
            finally:
                    for n in self.check_var:
                        self.hist_dict["deleted_vals(s)"] = self.datas[0][n] + " - " + self.datas[self.delete_index][n]

                        if self.datas[self.delete_index][n].replace(" ", "").isalpha():
                            self.datas[self.delete_index][n] = ""
                        else:
                            self.datas[self.edit_index][n] = "0"
                            
                    Label(self.canvas2, text="Process Completed!", font=('', 13)).grid(row=1, column=1, sticky="we", padx=5, pady=5)
                    Button(self.canvas2, text="Cancel", command=lambda : [self.canvas2.grid_forget(), self.canvas1.grid(row=8, column=3,padx=5,sticky=S)]).grid(row=2, column=0, padx=10, sticky="w")
                    Button(self.canvas2, text="Ok", command=lambda: [self.save_datas(), self.menu_edit()]).grid(row=2, column=5, sticky="e", padx=10, pady=10)
        else:
            label = Label(self.canvas2, text="You didn't select any option. Please select at least one!", fg="red")
            label.grid(row=2, column=2)      

    def delete_row(self):

        self.hist_dict["deleted_row"] = self.datas[self.delete_index]        

        # self.edit_index contains index number to delete
        self.datas.pop(self.delete_index)
        
        self.canvas2 = Canvas(self.frame4, background="beige", width=200, height=100, borderwidth=5)
        self.canvas2.grid(row=8, column=3,padx=5, pady=10, ipadx=5)

        Label(self.canvas2, text="Process Completed!", font=('', 13)).grid(row=1, column=1, sticky="we", padx=5, pady=5)
        Button(self.canvas2, text="Cancel", command=lambda : [self.canvas2.grid_forget(), self.canvas1.grid(row=8, column=3,padx=5,sticky=S)]).grid(row=2, column=0, padx=10, sticky="w")
        Button(self.canvas2, text="Ok", command=lambda: [self.save_datas(), self.menu_edit()]).grid(row=2, column=5, sticky="e", padx=10, pady=10)
    
    
    def delete_file(self):
        messagebox.showwarning("Alert", "You are about to delete whole file")
        confirm = messagebox.askokcancel("Confirmation", "Are you sure to delete whole file?")
        if confirm:
            self.datas.clear()
            os.remove(self.file)

            self.hist_dict["Deleted File"] = self.file

    

    # for popup fill
    def set_value(self, value, index):
        if index == 0:
            self.ent1.delete(0, END)
            self.ent1.insert(0, value)
        else:
            self.ent2.delete(0, END)
            self.ent2.insert(0, value)


    def popup_fill_val(self, index, event, ent1_val=None): # it was a bit messy cuz I wrapped some funcs in it
        # self.fill_val = None
        # if index == 0:
        self.menu3 = Menu(self.next_cat, tearoff=0)
        if ent1_val:
            self.fill_val = [row[1] for row in self.datas if ent1_val in row]
        else:
            self.fill_val=set(row[index] for row in self.datas[1:])  # I used set() to get unduplicated data

        for value in self.fill_val:
            self.menu3.add_command(label=value, command=lambda v=value, i=index: self.set_value(v, i))

        try:
            self.menu3.tk_popup(event.x_root, event.y_root)
        finally:
            self.menu3.grab_release()


    # Cars logo frame
    def show_cars_info_ico(self):
        if self.datas:
            # self.info_labl.config(text="")
            # self.root = Toplevel()
            # self.root.geometry("800x600")
            # self.root.columnconfigure(0, weight=1)
            # self.root.rowconfigure(0, weight=1)
            self.menuBar.entryconfig(" Home ", state=NORMAL)
            self.menuBar.entryconfig(" Info ", state=DISABLED)

            self.brands_main_frame = Frame(self.window)
            self.brands_main_frame.grid(row=0, column=0, sticky="nsew")
            self.brands_main_frame.columnconfigure(0, weight=1)

            self.brands_main_frame.tkraise() # (optional)Even if we don't add this, it works as intended

            # self.brands_main_frame.rowconfigure(0, weight=1)
            Button(self.brands_main_frame, text="< Back", command=lambda: [self.start_frame.tkraise(), self.brands_main_frame.destroy(), self.menuBar.entryconfig(" Info ", state=NORMAL), self.menuBar.entryconfig(" Home ", state=DISABLED)])\
                .grid(row=0, column=0, padx=5, pady=5, ipadx=5, ipady=5, sticky="w")

        
            self.cars_img = ["./Project/brands/bmw.png", "./Project/brands/nissan.png", "./Project/brands/tesla.png", "./Project/brands/ford.png", "./Project/brands/rolls-royce.png", "./Project/brands/mercedes-benz.png", "./Project/brands/toyota.png", "./Project/brands/audi.png"]

            self.ico_frame = Frame(self.brands_main_frame, background="skyblue", relief="raised")
            self.ico_frame.grid(row=1, column=0, columnspan=10, rowspan=10, ipadx=10, ipady=100, padx=150, sticky="n")

            names = [name.split("/")[-1][:-4].upper() for name in self.cars_img]
            images = [PhotoImage(file=image) for image in self.cars_img]

            for i, car in enumerate(images):
                label =Label(self.ico_frame, image=car, background="skyblue", relief="solid", cursor="hand2")
                label.grid(row=i//3, column= i%3, padx=10, pady=5, ipadx=10, ipady=40, sticky="nswe")
                label.bind("<Button-1>", lambda event,a=i: self.show_icon(names[a]))
            # self.window.mainloop()
        else:
            self.info_labl.config(text="Your data is empty.\n File is not loaded yet!")
        self.window.mainloop() # if I don't add this logos will not display

    def show_icon(self,name):
        self.brands_main_frame.grid_forget()

        self.ico_main_frame = Frame(self.window)
        self.ico_main_frame.grid(row=0, column=0, sticky="nsew")
        self.ico_main_frame.columnconfigure(7, weight=1)
        # self.ico_main_frame.rowconfigure(5, weight=1)

        models_count = len([row[1] for row in self.datas[1:] if name in row])

        self.ico_back = Button(self.ico_main_frame, text="<< Back", bg="blue",fg="white", command=lambda: [self.ico_main_frame.destroy(), self.show_cars_info_ico()])
        self.ico_back.grid(row=0, column=0, padx=5, pady=5, ipadx=5, ipady=5, sticky=W)

        self.brand_name = Label(self.ico_main_frame, text=f"{name} ({models_count})" , font=('', 12, 'bold'))
        self.brand_name.grid(row=0, column=7, padx=5, pady=5, sticky=S) 

        path = "./Project/models/" + name.lower() +"/"
        # print(os.path.exists(path))
        self.load_images(path)
        self.img_counter = 0
        self.image_display() # 6/3/24

    def image_display(self): # 6/3/24
        self.model = [row for row in self.datas[1:] if self.img_modl[self.img_counter][1] in row] # [[]]

        # Button(self.root, text=" < ", font=('', 10, 'bold'), background="skyblue", command=self.prev_ico).grid(row=2, column=4, padx=5, pady=5, ipadx=5, ipady=5)
        # Button(self.root, text=" > ", font=('', 10, 'bold'), background="skyblue", command=self.next_ico).grid(row=2, column=7, padx=5, pady=5, ipadx=5, ipady=5, sticky=W)

        self.ico_frame1 = Frame(self.ico_main_frame, width=50, height=20, background="skyblue", borderwidth=2, relief="solid")
        self.ico_frame1.grid(row=1, column=7, padx=40, pady=10, sticky="s")
        self.ico_frame1.columnconfigure([7,8], weight=2)

        self.ico = Label(self.ico_frame1, image=self.img_modl[self.img_counter][0], background="skyblue", cursor="hand2")
        self.ico.grid(row=1, column=7, pady=10, sticky=NSEW)
        # self.ico.bind("<Button-1>", lambda event, a=self.img_modl[self.img_counter][1]: self.img_info(a))
        self.action_on = False # to toggle button
        self.ico.bind("<Button-1>", lambda event: self.img_info())
 
        Button(self.ico_frame1, text=" < ", font=('', 15, 'bold'), activebackground="skyblue", command=self.prev_ico).grid(row=2, column=0, padx=5, pady=5, ipadx=5, ipady=5, sticky=W)
        
        self.ico_name = Label(self.ico_frame1, text=f"{self.img_counter+1}.   {self.img_modl[self.img_counter][1]} ( ${int(self.model[0][-1]):,.0f} )", background="skyblue", font=7)
        self.ico_name.grid(row=2, column=7, sticky="s") 

        Button(self.ico_frame1, text=" > ", font=('', 15, 'bold'), activebackground="skyblue", command=self.next_ico).grid(row=2, column=8, padx=5, pady=5, ipadx=5, ipady=5, sticky=E)

        self.txt_frame = Frame(self.ico_main_frame, width=80, borderwidth=2, relief="solid", background="skyblue")
        self.txt_frame.grid(row=5, column=5, padx= 10, ipadx=20, sticky=EW)

        for i, column in enumerate(self.datas[0][1:7]):
            Label(self.txt_frame, text=column, justify='left',background="skyblue").grid(row=i , column=0, sticky=W, padx=5, pady=5)
            Label(self.txt_frame, text=f"- {self.model[0][i]}", justify='left',background="skyblue", wraplength=100).grid(row=i, column=1, sticky=W, padx=20,pady=5)
          
        for i, column in enumerate(self.datas[0][7:]):
            Label(self.txt_frame, text=column, background="skyblue").grid(row=i, column=3, sticky=E, padx=20, pady=5)
            Label(self.txt_frame, text=f"- {self.model[0][7:][i]}", justify='left', background="skyblue").grid(row=i, column=4, sticky=W, pady=5)
        
        self.txt_frame.grid_forget()
        # self.root.mainloop()

    def img_info(self):
        self.action_on = not self.action_on # toggling using boolean
        if self.action_on:
            self.txt_frame.grid(row=4, column=7, ipadx=50)
        else:
            self.txt_frame.grid_forget()

    def next_ico(self):

        self.img_counter += 1
        if self.img_counter == len(self.img_modl):
            self.img_counter = 0

        self.ico_frame.destroy()
        self.txt_frame.destroy()
        self.image_display() # 6/3/24
        

    def prev_ico(self):
        if 0 < self.img_counter < len(self.img_modl):
            self.img_counter -= 1
        else:
            self.img_counter = len(self.img_modl) - 1

        self.ico_frame.destroy()
        self.txt_frame.destroy()
        self.image_display() # 6/3/24
        # print(self.img_counter)

    def load_images(self, path):
        images_dir = os.listdir(path)
        images = []
        model_names = []
        for image in images_dir:
            # I didn't use this for now yet
            Image.open(path+image).resize((420,270)).save(path+image) # to automatically resize but you will need PIL module
            
            images.append(PhotoImage(file=path+image))
            model_names.append(image[:-4])
        self.img_modl = [*zip(images, model_names)]


    def save_datas(self):
        with open(self.file, 'w', newline='') as f:
            reWriter = csv.writer(f)
            reWriter.writerows(self.datas)
        
        with open(os.curdir+"/Project/log", "a") as l:
            for x, value in self.hist_dict.items():
                l.write(x +" - " + str(value) + "\n")

EVcars()
