import csv
import os
# I will create class later

def loadFile():
    datas = []
    with open ('./Project/toughestsports_1.csv', newline='') as f:
        lines = f.readlines()
        for line in lines:
            datas.append(line.strip().split(',')) 
    return datas
    # return lines

# I named funcs general names
def dataInfo():
    datas = loadFile()
    for row in datas:
        print(row)

def numberOfDatas():
    datas = loadFile()
    print("There are", len(datas[1:]), "Types of sport.")

def addNewData():
    datas = loadFile()
    print("\n To Add Sport Type--")
    needs = datas[0] # can use directly in input with datas[0][i]
    new_type = []
    for i in range(11):
        if i == 0:
            info = str(input(f"Enter {needs[i]} name: "))
        else:
            try:
                info = float(input(f"Enter {needs[0]}'s {needs[i]}(0-10): "))
            except ValueError or (info < 0 and info > 10):
                print("The value must be integer or float and between 0 and 10!")
                # info = 0
                info = float(input(f"Enter {needs[0]}'s {needs[i]}: "))
        new_type.append(str(info))
    new_type.append(sum(float(data) for data in new_type[1:11]))
    # for rank(need to make better)
    new_type.append(len(datas[1:])+1)
    # if new_type[0] not in [row[0] for row in datas]:
    datas.append(new_type)
    # should I wrap this code in separate func?
    with open("./Project/toughestsports_1.csv", 'a', newline='') as f:
        # quotechar removes quotes of lines and repeat the give word
        # if it presents in each line(my opinion)
        newWrite = csv.writer(f, quotechar='|')
        # checking is there a same data type
        if new_type[0] not in [row[0] for row in datas]:
            newWrite.writerow(new_type)
        else:
            print(f"There is already a same {needs[0]} type that you had tried to add!")
            # # f.write(str(datas))
        # for line in datas:
        #     f.write(str(line))

# def searchDataInfo():
#     datas = loadFile()
#     print("Here is category to find the datas"+"\n")
#     print(*("i "+str(col)+"\n" for i,col in datas[0]))
#     data_to_find = input("Enter the name ")


def searchDataInfo():
    datas = loadFile()
    num_to_search, data_to_search = askMenu()
    if num_to_search == 1:
        for row in datas[1:]:
            if data_to_search in row:
                print(*(f"{datas[0][i]} - {word}\n" for i, word in enumerate(row)))
    else:
        # print(f"{datas[0][0]} , {datas[0][num_to_search-1]}")
        # eg if data_to_search is 4 , this will return all rows that contain 
        # at least 4 in that specific column[num_to_search-1]

        # I needed to add [0] in condition to check very 1st number 
        # bcu all of datas are string (eg if 5 in 1.5 results True)
        print(*(f"{datas[0][0]} - {row[0]}\n {datas[0][num_to_search-1]} - {row[num_to_search-1]}\n\n" 
                for row in datas[1:] if data_to_search in row[num_to_search-1][0]))


def askMenu(quest_type="search", edit=False):
    # I added parameter to make sense in input
    datas = loadFile()
    print(f"Here is the category you can {quest_type}--- \n")
    print(*(f"{i}. {column}\n" for i,column in enumerate(datas[0], 1)))

    try:
        num = int(input(f"Enter the serial No. you want to {quest_type}: "))
    except ValueError:
        print("Please provide the number only!")
        num
    # lame codes below , still solving
    if edit ==  True:
        index1, index2 = findIndex(datas, num)
        data = input(f"Enter {datas[0][num-1]}'s name/value to {quest_type}: ")
        return num, data, index1, index2
    else:
        data = input(f"Enter {datas[0][num-1]}'s name/value to {quest_type}: ")
        return num, data

def editDataInfo():
    datas = loadFile() # this is repeat in every func, need to pack in main func or in class
    num_to_edit, data_to_edit, index1, index2 = askMenu("edit", True)
    # index1, index2 = findIndex(datas, num_to_edit)
    # this only edits one value, need to find ways to edit multiple values
    datas[index1][index2] = data_to_edit
    reWriteCsv('./Project/toughestsports_1.csv', datas)
    # dataInfo() test code

def delDataInfo():
    datas = loadFile()
    num_to_del, data_to_del = askMenu("delete")
    index1, index2 = findIndex(datas, num_to_del, True, data_to_del)
    # I made it 0 if it delete column values
    # if data_to_del in [row for row in datas]:
    if index2 > 0:
        datas[index1][index2] = 0
    else:
        datas.pop(index1)                         
    reWriteCsv('./Project/toughestsports_1.csv', datas)
    dataInfo()


def delFile(filename):
    datas =loadFile() # here it comes, calling this func always doesnt make sense
    delAllInfo = int(input("Do you want to delete the whole file?\n 1. Yes 2. No : "))
    if delAllInfo == 1:
        datas.clear()
        os.remove(filename)
    else:
        pass # thinking....


def findIndex(datas, num, toDel = False, delData=None):
    # added parameters to make sense for both edit and delete functions
    sportName = input(f"Enter {datas[0][0]}'s name to track: ")
    if toDel == True:
        existing_data = delData
    else:
        existing_data = input(f"Enter the {sportName}'s {datas[0][num-1]} existing value/name: ")
    
    for row in datas[1:]:
        if sportName in row[0]:
            if existing_data in row[num-1]:
                index1 = datas.index(row)
                index2 = num-1
            else:
                print(f"{existing_data} is not present in {sportName}'s {datas[0][num-1]}")
    return index1, index2

def reWriteCsv(filename, datas):
    with open(filename, 'w', newline='') as f:
        reWriter = csv.writer(f, quotechar='|')
        reWriter.writerows(datas)

dataInfo()
# numberOfDatas()
# addNewData() 
# searchDataInfo()
# editDataInfo()
# delDataInfo()
# delFile('./Project/toughestsports_1.csv')
