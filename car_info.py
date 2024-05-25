import csv
import os
from tkinter import *

class EVcars():
    def __init__(self, filename):
        self.filename = filename # str(input("Enter filename/path: ") or name.get() for GUI
        self.datas = self.loadFile()
        self.prices = []
        # self.dataInfo(self.datas)
        # self.mainMenu()

        # # for GUI
        # window = Tk()
        # window.geometry("300x150")
        # label = Label(window, text="Enter the file name or path: ")
        # name = StringVar()
        # entry = Entry(window, textvariable=name)
        # btn = Button(window, text="Ok", command=self.loadFile)
        # label.pack()
        # entry.pack()
        # btn.pack()
        # window.mainloop()

    def loadFile(self):
        with open (self.filename, 'r', newline='') as f:
            fileReader = csv.reader(f)
            datas = [row for row in fileReader] # this just works well in terminal
        return datas 


    def dataInfo(self):
        # try to get input number of lines to display even if it won't work well with textarea(GUI)

        # for row in self.datas[1:]: # try datas[1:5] to test
        #     # I used unpacking instead of using nested for loop and printing
        #     print(*(f"\n{self.datas[0][i]} - {value}" for i, value in enumerate(row))) # this display column - values
        brands=[] 
        # line = 0 # I used self.datas so created line to remove first row
        for row in self.datas:
            print(', '.join(word.strip() for word in row)) # this shows line by line 
            # following code was solved by just using brands[1:]
            # if line == 0:
            #     line += 1
            # elif row[0] not in brands:
            #     brands.append(row[0])

            if row[0] not in brands:
                brands.append(row[0])
        print(f"\nThere are {len(brands[1:])} brands of {self.__class__.__name__}.")
            
    def numberOfData(self):
        print("\nThere are", len(self.datas[1:]), "Types of datas.\n") # I used datas for general purpose

    def addInfo(self):
        print(f"\n To Add {self.__class__.__name__} Type--")
        print("\n Type carefully!")
        needs = self.datas[0] # can use directly in input with datas[0][i]
        new_data = self.datas
        new_type = []
        for i in range(len(needs)):
            if i == 0:
                info = input(f"Enter {needs[i]} name: ").upper()
            else:
                info = input(f"Enter {needs[i]}'s value/name: ")
            new_type.append(str(info))

        #check added Brands' models exist in datas (same data type?) , if True func wont add that new type
        if new_type[:2] not in [row[:2] for row in self.datas[1:]]:
            # should I wrap this code in separate func?
            with open(self.filename, 'a', newline='') as f:
                newAppend = csv.writer(f, quotechar='|')
                newAppend.writerow(new_type)
            print("\nNew info has added!\n")

        else:
            print(f"\nThere is already a same {needs[0], needs[1] } type that you had tried to add!")
            print("Try to add some new info!\n")


    def searchInfo(self):
        num_to_search, data_to_search = self.askMenu()
        count = 0
        if num_to_search == 1:
            for row in self.datas[1:]:
                if data_to_search.upper() in row:
                    print(*(f"{self.datas[0][i]} - {word}\n" for i, word in enumerate(row)))
                    count += 1
        else:
        # print(f"{self.datas[0][0]} , {self.datas[0][num_to_search-1]}")
        # eg if data_to_search is 4 , this will return all rows that contain 
        # at least 4 in that specific column[num_to_search-1]

        # I needed to add [0] in condition to check very 1st number 
        # bcu all of datas are string (eg if 5 in 1.5 results True)
            print(*(f"{self.datas[0][0]} - {row[0]}\n {self.datas[0][num_to_search-1]} - {row[num_to_search-1]}\n\n" 
                    for row in self.datas[1:] if data_to_search in row[num_to_search-1][0]))
        print(f"{count} results found.")

    def editInfo(self):
        num_to_edit, data_to_edit, index1, index2 = self.askMenu("edit", True)
        # index1, index2 = findIndex(datas, num_to_edit)
        # this only edits one value, need to find ways to edit multiple values
        self.datas[index1][index2] = data_to_edit
        self.reWriteCsv(self.datas)

    def delInfo(self):
        num_to_del, data_to_del = self.askMenu("delete")
        index1, index2 = self.findIndex(num_to_del, True, data_to_del)

        # I made it 0 if it delete column values
        # if data_to_del in [row for row in datas]:
        if index2 > 0:
            self.datas[index1][index2] = 0
        else:
            self.datas.pop(index1)                         
        self.reWriteCsv(self.datas)

    def delFile(self):
        delAllInfo = int(input("Do you want to delete the whole file?\n 1. Yes 2. No : "))
        if delAllInfo == 1:
            self.datas.clear()
            os.remove(self.filename)

    def mainMenu(self):
        menu = ["Info", "Number", "Adding New Info", "Searching Info", "Editing Info", "Deleting Info", "* Deleting All Datas/File"]
        func = [self.dataInfo, self.numberOfData, self.addInfo, self.searchInfo, self.editInfo, self.delInfo, self.delFile]
        # menu = zip(quest, func)  I treid to zip it and later access with index

        print("<--Here is a category-->")
        for i, mn in enumerate(menu, 1):
            print(f"{i}. {mn} of {self.__class__.__name__}") # I used special attr self.__class__.__name__ to get class name
        print("\n")

        choice = int(input(f"Enter No. of category: "))
        for i in range(len(menu)): 
            if choice == i+1:
                func[i]()

    def askMenu(self, quest_type="search", edit=False):
    # I added parameter to make sense in input
        datas = self.datas
        print(f"Here is the category you can {quest_type}--- \n")
        print(*(f"{i}. {column}\n" for i,column in enumerate(datas[0], 1)))

        try:
            num = int(input(f"Enter number to {quest_type}: "))
        except ValueError:
            print("Please provide the number only!")
            num

        # lame codes below , still solving
        if edit ==  True:
            index1, index2 = self.findIndex(num)
            if num == 1:
                data = input(f"Enter {datas[0][num-1]}'s name/value to {quest_type}: ").upper()
            else:
                data = input(f"Enter {datas[0][num-1]}'s name/value to {quest_type}: ")
            return num, data, index1, index2
        else:
            if num == 1:
                data = input(f"Enter {datas[0][num-1]}'s name/value to {quest_type}: ").upper()
            else:
                data = input(f"Enter {datas[0][num-1]}'s name/value to {quest_type}: ")
            return num, data
        
    def findIndex(self, num, toDel=False, delData=None):
    # added parameters to make sense for both edit and delete functions
        brandName = input(f"Enter {self.datas[0][0]}'s name to track: ").upper() # to find index
        target_data = None # to use as variable for existing_data and modelName in condition

        if brandName in [row[0]for row in self.datas[1:]]:
            if num == 1 or sum(1 for row in self.datas[1:] if row[0] == brandName) > 1: # check if datas contains brandname more than 1 time
                print("\n Please provide more!")
                modelName = input(f"Enter the {self.datas[0][1]} value/name: ") # to make specific
            else:#sum(1 for row in self.datas[1:] if row[0] == brandName) > 1:
                modelName = input(f"Enter the {self.datas[0][1]} value/name: ")
            #     existing_data = input(f"Enter the {modelName}'s existing {self.datas[0][num-1]} value/name: ")
            # else:
            #     existing_data = input(f"Enter the {brandName}'s existing {self.datas[0][num-1]} value/name: ")

            # simple way
            # value_indx = input(f"Enter {self.datas[0][num-1]}'s value/name: ")
            # index1 = [*(self.datas.index(row) for row in self.datas[1:] if existing_data in row[num-1])]
            # index2 = num-1  

            # for row in self.datas[1:]:
            # if brandName in [row[0]for row in self.datas[1:]]:
            # I used [0] after list comprehension to access inside list, 
                if toDel == True:
                    target_data = delData
                    # model specific
                    index1 = self.datas.index([row for row in self.datas[1:] if target_data in row[num-1] and modelName in row[1] and len(modelName) == len(row[1])][0])
                    index2 = num-1
                    return index1, index2
                else:
                    target_data = modelName

                    # this gets index list that can be used to remove duplicate values
                    # index1 = [self.datas.index(row) for row in self.datas[1:] if modelName in row[1]] #and len(modelName) == len(row[1])]
                    # model_list = [m[1] for m in self.datas[1:] if modelName in m[1]] this can again be used as options
                    # option = zip(index1, model_list) like ((1, 'Model 3'), (2, Model Y) if modelName = "model"

                    # model specific
                    index1 = self.datas.index([row for row in self.datas[1:] if modelName in row[1] and len(modelName) == len(row[1])][0])
                    # same result -> index1 = self.datas.index(*(i for i in[row for row in self.datas[1:] if modelName in row[1] and len(modelName) == len(row[1])]))
                    index2 = num-1

                    return index1, index2

        else:
            print(f"{brandName} is not present in {self.datas[0][0]}")
        # print(sum(1 for row in self.datas[1:] if row[0] == brandName))
        

    def reWriteCsv(self, datas):
        with open(self.filename, 'w', newline='') as f:
            reWriter = csv.writer(f, quotechar='|')
            reWriter.writerows(datas)

    def expensiveness(self):
        for row in self.datas[1:]:
            self.prices.append((int(row[-1]), (row[0] + ', ' + row[1])),)  
        self.prices.sort(reverse=True)
        print(*(f"{data[1]} --> {data[0]}$\n" for data in self.prices))

evInfo = EVcars('./Project/evcars_subset.csv')
evInfo.expensiveness()

# print(evInfo.datas)

# evInfo.findIndex(1)
# print(index1)
# for i in index1:
#     print(evInfo.)
