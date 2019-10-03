"""
`````````````````````````````````````````````````````````````````````````````````````````````````````````
    [League Tracker va3.00, Conor Fitzgerald, [03/09/2018]]
`````````````````````````````````````````````````````````````````````````````````````````````````````````    

    This Build includes a GUI with a functional Treeview Table built with Tkinter

    Elements that work include:
    - Selecting a Name from a Listbox and Adding a number of Wins and Losses to the Table updating from an inital value.
    - Exporting to and Updating the Table from a file.
    - Adding New Names to the Table via the GUI
    - A Functioning Help Button


    Element that do not yet work include:
    - Calculating Values by use of the Table.    

"""
##Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import *
from datetime import *
import csv
from math import sqrt

##Definitions and presets

backgroundColour = '#f6ddff'
ribbonColour = '#e0a3ff' #Imports colours to be used throughout the program

names = [] # An empty list is set here the names of users entered into the system will be stored
wins = [] # An empty list is set to store users wins
losses = [] # An empty list is set that will store users losses
wldiff = [] # An empty list is set it will be used to store the differnces in wins and losses for each user

root = Tk()
root.title("League Tracker")
root.geometry('458x568')
root.wm_iconbitmap("icon.ico") #sets an icon for the window
root.configure(background=backgroundColour) #sets the window colour to backgroundColour
root.resizable(False, False)

treeview = ttk.Treeview(root)
treeview.pack()
treeview.config(height = 10)
treeview.config(columns = ('Wins','Losses','WL Difference'))
treeview.place(x=98,y=62)
treeview.column('#0', width = 100, anchor = 'center')
treeview.heading('#0', text = 'Name')
treeview.column('Wins', width = 50, anchor = 'center')
treeview.heading('Wins', text = 'Wins')
treeview.column('Losses', width = 50, anchor = 'center')
treeview.heading('Losses', text = 'Losses')
treeview.column('WL Difference', width = 50, anchor = 'center')
treeview.heading('WL Difference', text = 'WL Diff')
selectmode='extended'	

def Help():

    messagebox.showinfo("Help","Please read \n `readme.txt`") # A message box that will be used when an Error Occurs

def error():

    messagebox.showerror("Error", "An Error has Occured") # A message box that will be used when an Error Occurs

with open('data.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    for row in reader:

        name = row[0]
        win = row[1]
        loss = row[2]
        names.append(name)
        wins.append(win)
        losses.append(loss)

for i in range(0,len(names)):

    currentName = (names[i])
    currentWin = (wins[i])
    currentLoss = (losses[i])
    currentWin = int(currentWin)
    currentLoss = int(currentLoss)
    
    treeview.insert('', '0', currentName, text =currentName)
    treeview.set(currentName, 'Wins',wins[i])
    treeview.set(currentName, 'Losses',losses[i])
    treeview.set(currentName, 'WL Difference',(currentWin - currentLoss))

i = 0

def delete():

    selected_item = treeview.selection()[0] ## Det selected item

    print(selected_item, 'has been removed from the table')

    i= names.index(selected_item) #Finds where the name matching the selected item is in the names list
    del names[i] # Deletes the selected item from the names list

    treeview.delete(selected_item) # The Item Currently Selected is Deleted from the list

    personlist.delete(0,END) 
    personlist.insert(END, *names) # On this line and the line above it the personlist listbox is updated to remove the name which was deleted from the names list
    i = 0

def Add_to_table(): 

    Name_to_add = personlist.get(ANCHOR)
    i = names.index(Name_to_add)
    Wins_to_add = int(WinsEntry.get())
    Losses_to_add = int(LossesEntry.get())
    
    toDelete = names[i]
    treeview.delete(toDelete)
    
    wins[i] = (int(wins[i]) + int(Wins_to_add))
    losses[i] =(int(losses[i]) + int(Losses_to_add))
    treeview.insert('', '0', Name_to_add, text =Name_to_add)
    treeview.set(Name_to_add, 'Wins',wins[i])
    treeview.set(Name_to_add, 'Losses',losses[i])
    treeview.set(Name_to_add, 'WL Difference',(wins[i] - losses[i]))

    i = 0

def Export():
    for i in range(0,len(names)):
        wins[i] = str(wins[i])
        losses[i] = str(losses[i])
        
    rows = zip(names,wins,losses)
    
    with open("data.csv",'w', newline='') as outputFile:
        wr = csv.writer(outputFile, dialect='excel')
        for row in rows:
            wr.writerow(row)
    i = 0

def New_Name():
    UserAdd = str(userEntry.get())
    if UserAdd == (''):
        i = 0
    else:
        names.append(UserAdd)
        wins.append(int('0'))
        losses.append(int('0'))

        treeview.insert('', '0', UserAdd, text =UserAdd)
        treeview.set(UserAdd, 'Wins','0')
        treeview.set(UserAdd, 'Losses','0')
        treeview.set(UserAdd, 'WL Difference','0')

        personlist.delete(0,END) 
        personlist.insert(END, *names)
        userEntry.delete(0,END)


def Standard_Deviation():
    global mAverage
    global sd
    num_ofItems = len(chosenList)

    mAverage = (sum(chosenList) / num_ofItems)
    differences = [x - mAverage for x in chosenList]
    sq_differences = [d ** 2 for d in differences]
    ssd = sum(sq_differences)
    variance = ssd / num_ofItems
    sd = sqrt(variance)
    

def Calculate():
    if selectFunction.get() == ('Mean'):
        Standard_Deviation()
        print(mAverage)
    
    
    
    
    
       
##Select Person List
selectpersonLabel = Label(text='Select a Person: ')
selectpersonLabel.place(x=28, y=300)
personlist=Listbox()
personlist.insert(END, *names)
personlist.place(x=28,y=328)

##Add Wins Entry Box
AddWinsLabel = Label(text='Add Wins: ')
AddWinsLabel.place(x=158, y=300)
WinsEntry=Entry()
WinsEntry.place(x=158,y=328)

##Add Losses Entry Box
AddLossesLabel = Label(text='Add Losses: ')
AddLossesLabel.place(x=158, y=352)
LossesEntry=Entry()
LossesEntry.place(x=158,y=380)                        

##Add To Table Button
AddButton = Button(text='Add To Table',command = Add_to_table)
AddButton.place(x=158,y=408,width=80,height=25)

##label1(Ribbon)
LabelRibbon = Label(text='V:a3.000', fg='white', bg=ribbonColour, anchor=E, justify=RIGHT)
LabelRibbon.place(x=0, y=0, width=458, height=35)  # make a label with said dimensions

#helpButton
helpButton = Button(text='Help', bg=ribbonColour, command=Help)
helpButton.place(x=10, y=5, width=75, height=25)

LabelFunction1 = Label(text='Calculate the:', bg=backgroundColour, justify=RIGHT)
LabelFunction1.place(x=308,y=382,)
#makes a label to instruct the user.

selectFunction = StringVar(root)
selectFunction.set("Select a Function")
FunctionList = OptionMenu(root, selectFunction, "Mean","Standard Deviation")
FunctionList.place(x=308,y=402)
#creates an options list of different functions by which the data can be manipulated

LabelFunction1 = Label(text='Of:', bg=backgroundColour, justify=RIGHT)
LabelFunction1.place(x=308,y=435,)
#makes a label to instruct the user.

selectVar = StringVar(root)
selectVar.set("Chose one")
VarList = OptionMenu(root, selectVar, "wins","losses","wldiff")
VarList.place(x=308,y=455)
#shows the different variables which can be manipulated 

CalculateButton = Button(text='Calculate', command = Calculate)
CalculateButton.place(x=28, y=502, width=125, height=25)
#a button is created with the purpose of calculating the function that the user has set via the GUI

ExportButton = Button(text='Export Table',command = Export)
ExportButton.place(x=158, y=436, width=80, height=25)
#a button is made to let the user export the table in it's current for to a txt file

DeleteButton = Button(text='Delete Record',command = delete)
DeleteButton.place(x=158, y=464, width=80, height=25)
#a button is made to let the manually delete a selected row

#Add User
addUserLabel = Label(text='Add New User:',justify=RIGHT) #makes a label to instruct the user where they can add a new user to the database.
addUserLabel.place(x=308,y=300,)
userEntry=Entry()
userEntry.place(x=308,y=328)
userButton = Button(text='Add',command = New_Name)
userButton.place (x=308, y=352, height=25, width=125)

root.mainloop()
