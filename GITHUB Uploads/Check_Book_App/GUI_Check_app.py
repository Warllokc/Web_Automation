from tkinter import *
from os import path
from csv import writer
import tkinter.messagebox

# CREATING A GUI WINDOW/TITLE
master = Tk()
master.title('Check Tracking App')
e = Entry(master)
mystring = StringVar()

# CREATING LABELS
first = Label(master, text="FIRST NAME", font = 'Mistral 12 bold').grid(row=2)
last = Label(master, text="LAST NAME", font = 'Mistral 12 bold').grid(row=3)
date = Label(master, text="DATE", font = 'Mistral 12 bold').grid(row=4)
Check_num = Label(master, text="CHECK NUMBER", font = 'Mistral 12 bold').grid(row=5)
check_anoumt = Label(master, text="CHECK AMOUNT", font = 'Mistral 12 bold').grid(row=6)
purpose = Label(master, text="PURPOSE", font = 'Mistral 12 bold').grid(row=7)

# DEFINING THE FUNCTIONS
def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

def creating_csv_file():
    import csv
    # IF FILE DOES NOT EXIST, CREATE ONE
    if not path.isfile('../Alex_expenses.csv'):
            global rows
            global exampleDictWriter

            exampleFIle = open('../Alex_expenses.csv', 'w', newline='')
            # Crating columns in CSV file
            exampleDictWriter = csv.DictWriter(exampleFIle, ['First name', 'Last name', 'Date', 'Check Number',
                                                     'Check Amount', 'Purpose'])
            # Creating  a header row "Otherwise, skip calling writeheader() to omit a header row from the file"
            exampleDictWriter.writeheader()

            rows=exampleDictWriter.writerow({'First name': entry_row1.get(), 'Last name': entry_row2.get(), 'Date': entry_row3.get(),
                 'Check Number': entry_row4.get(), 'Check Amount': entry_row5.get(),'Purpose': entry_row6.get()})

            # Write each row of the CSV file
    # IF FILE EXIST APPEND OPEN AND APPEND DATA INPUTS
    elif path.isfile('../Alex_expenses.csv'):
            rows=(entry_row1.get()),(entry_row2.get()),(entry_row3.get()),(entry_row4.get()),(entry_row5.get()),(entry_row6.get())

            append_list_as_row('../Alex_expenses.csv', rows)

def callback():
    entry_row1.delete(first=0,last=50)
    entry_row2.delete(first=0,last=50)
    entry_row3.delete(first=0,last=50)
    entry_row4.delete(first=0,last=50)
    entry_row5.delete(first=0,last=50)
    entry_row6.delete(first=0,last=50)

def submit():
    num1 = entry_row4.get()
    num2 = entry_row5.get()
    req1 = entry_row1.get()
    req2 = entry_row2.get()
    if (entry_row1.get() and entry_row2.get()) and (num1.isdigit() and num2.isdigit()) and (not req1.isdigit() and  not req2.isdigit()):
        Label(master, text="                ", fg="red").grid(row=3, column=2)
        Label(master, text="                ", fg="red").grid(row=2, column=2)
        Label(master, text="                    ", fg="red").grid(row=5, column=2)
        Label(master, text="                    ", fg="red").grid(row=6, column=2)

        # the user entered data in  the mandatory entry: proceed to next step
        global sumbit_lab
        print(mystring.get())
        creating_csv_file()
        callback()
        Button(master, text="CLEAR", font='Mistral 10 bold', fg="black", command=callback2).grid(row=0, column=2)
        sumbit_lab = Label(master, text="      SUBMITED     ", font='Mistral 12 bold').grid(row=0, column=1)
        return sumbit_lab


    else:
        req1=Label(master, text="* required", fg="red")
        req1.grid(row=3, column=2)
        req2=Label(master, text="* required", fg="red")
        req2.grid(row=2, column=2)
        req3=Label(master, text="* digits only", fg="red")
        req3.grid(row=5, column=2)
        req4=Label(master, text="* digits only", fg="red")
        req4.grid(row=6, column=2)
        tkinter.messagebox.showwarning('Wrong data', 'Requiered fields are not compleated as requered:'
                                                     '                      - no digits on  First and Last Name fields'
                                                     '                                     - just digits on Check Amount and Check number fields')
        # the mandatory field is empty
        print("mandatory data missing")

def callback2():
    global sumbit_lab2
    sumbit_lab2 = Label(master, text="WRITE A NEW ONE", font='Mistral 12 bold').grid(row=0, column=1)

# CREATING BUTTONS
button_Submit = Button(master, text="SUBMIT", font= 'Mistral 12 bold', fg="blue", command=submit).grid(row=8, column=1)
button_Quit = Button(master, text="QUIT", font= 'Mistral 12 bold', fg="red", command=quit).grid(row=8)
button_Clear = Button(master, text="CLEAR", font= 'Mistral 10 bold', fg="black",command= submit, state='disabled').grid(row=0, column= 2)

# DEFINING TYPES OF OBJECTS
entry_row1 = Entry(master)
entry_row2 = Entry(master)
entry_row3 = Entry(master)
entry_row4 = Entry(master)
entry_row5 = Entry(master)
entry_row6 = Entry(master)

# CREATING AND LOCATING TEXT FIELDS
entry_row1.grid(row=2, column=1)
entry_row2.grid(row=3, column=1)
entry_row3.grid(row=4, column=1)
entry_row4.grid(row=5, column=1)
entry_row5.grid(row=6, column=1)
entry_row6.grid(row=7, column=1)

print('  *' 
      '\n*\t*' 
      '\n*****' 
      '\n*  \t*' 
      '\n*  \t*')

master.mainloop()

