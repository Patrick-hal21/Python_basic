from tkinter import *
from tkinter import filedialog
from tkinter.font import Font
import csv
                                                                                                                                                                                                                                                                                                                                                                                                #banana color                                          brick color                              cobalt    cobaltgrey  cobalgreen
# colors = ['green', 'blue', 'alice blue', 'red', 'cyan', 'magenta', 'yellow', 'white', "lightblue", "lightgrey", "pink", "lightgreen","violet", "skyblue", "gold", "aqua", "bisque", "beige","aquamarine", "azure", "blanched almond", "chocolate", "blue violet", "cadet blue", "brown", "chartreuse", "burlywood", "coral","antique white", "cornflower blue", "antique white2", "aquamarine4", "#E3CF57", "antique white4", "brown2", "cadetblue1", "#9C661F", "cadetblue4", "chartreuse2", "#3D59AB", "#808A87", "#3D9140", "coral2", "#CDC8B1","darkgoldenrod2", "cornsilk4", "darkolivegreen3", "darkorchid1", "lawngreen", "mediumpurple3", "#33A1C9", "powderblue", "seagreen1", "seagreen4", "wheat", "tomato1"]
# tag_nums = [i for i  in range(0, 55)]
def openFile():
    # filedialog.askopenfilename()
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open  file", 
        filetypes=(("CSV file", "*.csv"), ("Text file", "*.txt"), ("All file", "*"))
    )
    pathh.insert(END, tf)
    # datas = [] better not to assign
    # brands = []
    if tf: # it will read file only if tf is True(ie. file was chosed)
        with open(tf, 'r', newline='') as f:
            fileReader = csv.reader(f) # without delimiter=' ', textarea show {str} if str contains space
            num_counter = 0
            brands = []
            # print(len(colors))
            # color_tags(colors)
            for row in fileReader:
                #datas.append(row)  we should append if we had used delimiter parameter in reader cuz it will split with ' '
                # txtarea.insert(END, (', '.join(word.strip() for word in row))) 
                # txtarea.config(state=NORMAL)
                txtarea.tag_configure(1, background='beige')
                txtarea.tag_configure(2, background='skyblue')
                # txtarea.config(state=NORMAL)
                # print(row)

                # coloring each brand but, I got erroe in 1st two lines
                '''
                i = 0
                if row[0] not in brands:
                    brands.append(row[0])
                    i += 1
                    add_data_color(', '.join(word.strip() for word in row), tag_nums[i-1])
                else:
                    add_data_color(', '.join(word.strip() for word in row), tag_nums[brands.index(row[0])])
                '''

                if num_counter % 2 == 0:
                    txtarea.insert(END, ', '.join(word.strip() for word in row), 2, '\n')
                else:
                    txtarea.insert(END, ', '.join(word.strip() for word in row), 1, '\n')
                num_counter += 1

                if row[0] not in brands:
                    brands.append(row[0])
                # txtarea.insert(END, "\n")
                # txtarea.config(state=DISABLED)

            # bold_font = Font(family="Helvetica", size=14, weight="bold")
            # txtarea.configure("BOLD", font=bold_font) #trying to add BOLD
            txtarea.insert(1.0, f"There are {len(brands)} brands of EV cars.\n\n")
            # txtarea.tag_add("BOLD", 1.0, END)

                # txtarea.config(state=DISABLED)
                # print((', '.join(word.strip() for word in row))) # it shows

    # tf = open(tf)  # or tf = open(tf, 'r')
    # data = tf.read()
    # txtarea.insert(END, data)
    # tf.close()
# def color_tags(colors):
#     for i, color in enumerate(colors):
#         txtarea.tag_configure(i, background=color) # colors tags will be (0-55)
# txtarea.tag_configure('odd', background='grey')
# txtarea.tag_configure('even', background='lightblue')
# def add_data_color(brand_data, tag):
    #  i = 0
    #  while i < len(tag):
    # txtarea.insert(END, brand_data, tag, "\n")



ws = Tk()
ws.title("File Reader")
ws.geometry("500x400")
ws['bg']='#00f'

txt_frame = Frame(ws, width=50, height=20, bd=1, borderwidth=5)
txt_frame.pack(side='top', fill=BOTH)

xscroll = Scrollbar(txt_frame, orient='horizontal')
yscroll = Scrollbar(txt_frame, orient='vertical')
xscroll.pack(side=BOTTOM, ipadx=250)
yscroll.pack(side=RIGHT, fill=Y)

txtarea = Text(txt_frame, width=60, height=20, wrap='none', xscrollcommand=xscroll.set, yscrollcommand=yscroll.set) # wrap ='none' to be able to set xscroll
# txtarea.config(state='disabled') # might test to use in function to disable previous shown words
txtarea.pack(pady=20) #if this sets here, any method needs before=txtarea parameter to be viewable
xscroll.config(command=txtarea.xview)
yscroll.config(command=txtarea.yview)

# xscroll = Scrollbar(ws, orient='horizontal', command=txtarea.xview)
# yscroll = Scrollbar(ws, orient='vertical', command=txtarea.yview)
#xscroll.grid(row=0, column=1, sticky=NS) # north to south direction
# xscroll.pack(side=BOTTOM, fill=X, anchor=S)
#yscroll.grid(row=0, column=1, sticky=EW) # east to west direction 
# yscroll.pack(side=RIGHT, fill=Y, anchor=E, after=txtarea)
# txtarea['xscrollcommand'] = xscroll.set
# txtarea['yscrollcommand'] = yscroll.set
# txtarea.pack(pady=20)

pathh = Entry(ws)
pathh.pack(side=LEFT, expand=True, fill=X, padx=20)
# Button(ws, text="Open").pack(side=RIGHT, padx = 60)
Button(
    ws, 
    text="Open File", 
    command=openFile
    ).pack(side=RIGHT, expand=True, padx=20) # fill=X,


ws.mainloop()
