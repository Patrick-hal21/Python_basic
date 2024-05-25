from tkinter import *
from tkinter import ttk  # for Treeview
from tkinter import filedialog
from PIL import ImageTk, Image # to add image in About us window
import csv

class EVcars():

    def __init__(self):
        self.window = Tk()
        self.window.title("Main Page")
        self.window.geometry("300x300")
        # created file, load_btn to load file and store it to use in other windows without repeating load_file 
        self.file = None 
        load_labl = Label(self.window, text="Please load file first!")
        load_btn = Button(self.window, text="Load file", command=self.load_file) 
        show_btn = Button(self.window, text="Show Cars Info", command=self.show_Info)

        load_labl.pack(side=TOP, pady=20)
        load_btn.pack()
        show_btn.pack(pady=20)

        self.createWidgets() #top menu
        self.window.mainloop()

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
        img = ImageTk.PhotoImage(Image.open("./Project/fourninjas with python.png"))
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
        self.info_labl = Label(show_window, text='')
        self.info_labl.pack()

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
                self.info_labl.config(text=f"There are {count} {self.__class__.__name__} with {len(brands)} different types.")

        except Exception as e:
            self.info_labl.config(text=f"Error: {str(e)}")


EVcars()