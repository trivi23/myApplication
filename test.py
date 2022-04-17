import sqlite3
from tkinter import *
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
data = pd.read_csv("data.csv")
x = data.iloc[:, :-1].values
y = data.iloc[:, -1].values
sc = StandardScaler()
x = sc.fit_transform(x)
# training dataset
lr = LinearRegression()
lr.fit(x, y)
# Creating database
connect = sqlite3.connect('my.db')
crsr = connect.cursor()
try:
    crsr.execute(
        """create table student(roll_number text primarykey,first_name text NOT NULL ,last_name text NOT NULL, father_name text NOT NULL,course text NOT NULL, contact integer NOT NULL)"""
    )
except:
    pass
try:
    crsr.execute(
        """create table marks(roll text REFERENCES student(roll_number) ON delete CASCADE ON update CASCADE, python integer NOT NULL, c integer NOT NULL, java integer NOT NULL, algorithms integer NOT NULL,
        dbms integer NOT NULL, os integer NOT NULL, cn integer NOT NULL, verbal integer NOT NULL, aptitude integer NOT NULL,math integer NOT NULL);"""
    )
except sqlite3.Error as error:
    pass
try:
    crsr.execute(
        """create table company(roll REFERENCES student(roll_number) ON delete CASCADE ON update CASCADE,cid integer NOT NULL, cname text NOT NULL, cpos text NOT NULL);""")
except sqlite3.Error as error:
    pass
connect.close()


window = Tk()
window.geometry("720x720")
window.title("training and placement")

stlist = ["Enter roll number", "Enter first name", "Enter last name",
          "Enter father name", "Enter Course", "Enter Contact"]
marklist = ["Enter roll number","Enter pyhton marks","Enter C marks","Enter java maraks","Enter DataStructures marks","Enter Dbms Marks","Enter Os marks","Enter Cn marks","Enter Verbal Marks","Enter Aptitude Marks","Enter Math Marks"]
clist = ["Enter roll number","Enter Company id","Enter Company Name","Enter Position hired"]

# Student
def s_top():
    entries = []
    top = Toplevel(window)
    top.geometry("900x750")
    top.resizable(width=0, height=0)
    for j in range(6):
        l = Label(top,text=stlist[j])
        l.grid(row=j, column=1,padx=5,pady=20)
    for i in range(6):
        entry = Entry(top)
        entry.grid(row=i, column=2, padx=5, pady=20)
        entries.append(entry)
    def insert():
        connect = sqlite3.connect("my.db")
        crsr = connect.cursor()
        crsr.execute("INSERT INTO student values(:roll,:fname,:lname,:faname,:cname,:phno)",
                 {
                     'roll': entries[0].get(),
                     'fname': entries[1].get(),
                     'lname': entries[2].get(),
                     'faname': entries[3].get(),
                     'cname': entries[4].get(),
                     'phno': entries[5].get()})
        entries[0].delete(0, END)
        entries[1].delete(0, END)
        entries[2].delete(0, END)
        entries[3].delete(0, END)
        entries[4].delete(0, END)
        entries[5].delete(0, END)
        l.config(text="Insertion success...!")
        connect.commit()
        connect.close()

    def update_entries():
        connect = sqlite3.connect("my.db")
        crsr = connect.cursor()
        crsr.execute("UPDATE student SET first_name = :fname, last_name = :lname, father_name = :faname, course = :cname, contact = :phno WHERE roll_number = :roll",
                     {
                         'roll': entries[0].get(),
                         'fname': entries[1].get(),
                         'lname': entries[2].get(),
                         'faname': entries[3].get(),
                         'cname': entries[4].get(),
                         'phno': entries[5].get()})
        entries[0].delete(0, END)
        entries[1].delete(0, END)
        entries[2].delete(0, END)
        entries[3].delete(0, END)
        entries[4].delete(0, END)
        entries[5].delete(0, END)
        l.config(text="Updated...!")
        connect.commit()
        connect.close()
    bInsert = Button(top, text="Insert", command=insert)
    bInsert.grid(row=7, column=1)
    bUpdate = Button(top, text="update", command=update_entries)
    bUpdate.grid(row=8, column=1)
    l = Label(top, text="")
    l.grid(row=9, column=1)

# Company
def c_top():
    top=Toplevel(window)
    top.geometry("900x750")
    top.resizable(width=0,height=0)
    entries = []
    for j in range(4):
        l = Label(top, text=clist[j])
        l.grid(row=j, column=1, padx=5, pady=20)
    for i in range(4):
        entry = Entry(top)
        entry.grid(row=i, column=2, padx=5, pady=20)
        entries.append(entry)

    def insert():
        connect = sqlite3.connect("my.db")
        crsr = connect.cursor()
        crsr.execute("INSERT INTO company values(:roll,:cid,:cname,:cpos)",
                     {
                         'roll': entries[0].get(),
                         'cid': entries[1].get(),
                         'cname': entries[2].get(),
                         'cpos': entries[3].get()})
        entries[0].delete(0, END)
        entries[1].delete(0, END)
        entries[2].delete(0, END)
        entries[3].delete(0, END)
        l.config(text="Insertion success...!")
        connect.commit()
        connect.close()

    def update_entries():
        connect = sqlite3.connect("my.db")
        crsr = connect.cursor()
        crsr.execute("UPDATE company SET cid = :fname, cname = :lname, cpos = :faname WHERE roll = :roll",
                        {
                         'roll': entries[0].get(),
                         'fname': entries[1].get(),
                         'lname': entries[2].get(),
                         'faname': entries[3].get(),
                        })
        entries[0].delete(0, END)
        entries[1].delete(0, END)
        entries[2].delete(0, END)
        entries[3].delete(0, END)
        l.config(text="Updated...!")
        connect.commit()
        connect.close()
    bInsert = Button(top, text="Insert", command=insert)
    bInsert.grid(row=7, column=1)
    bUpdate = Button(top, text="update", command=update_entries)
    bUpdate.grid(row=8, column=1)
    l = Label(top, text="")
    l.grid(row=9, column=1)

# Marks

def m_top():
    top=Toplevel(window)
    top.geometry("900x900")
    top.resizable(width=0,height=0)
    entries = []
    for j in range(11):
        l = Label(top, text=marklist[j])
        l.grid(row=j, column=1, padx=5, pady=20)
    for i in range(11):
        entry = Entry(top)
        entry.grid(row=i, column=2, padx=5, pady=20)
        entries.append(entry)

    def insert():
        connect = sqlite3.connect("my.db")
        crsr = connect.cursor()
        crsr.execute("INSERT INTO marks values(:roll,:python,:c,:java,:ds,:dbms,:os,:cn,:verbal,:aptitude,:math)",
                     {
                         'roll': entries[0].get(),
                         'python': entries[1].get(),
                         'c': entries[2].get(),
                         'java': entries[3].get(),
                         'ds': entries[4].get(),
                         'dbms':entries[5].get(),
                         'os': entries[6].get(),
                         'cn': entries[7].get(),
                         'verbal': entries[8].get(),
                         'aptitude': entries[9].get(),
                         'math': entries[10].get()})
        entries[0].delete(0, END)
        entries[1].delete(0, END)
        entries[2].delete(0, END)
        entries[3].delete(0, END)
        entries[4].delete(0, END)
        entries[5].delete(0, END)
        entries[6].delete(0,END)
        entries[7].delete(0, END)
        entries[8].delete(0, END)
        entries[9].delete(0, END)
        entries[10].delete(0, END)
        l2.config(text="Insertion success...!")
        connect.commit()
        connect.close()

    def update_entries():
        connect = sqlite3.connect("my.db")
        crsr = connect.cursor()
        crsr.execute(""" UPDATE marks SET python = :python, c = :c, java = :java, algorithms = :ds,
                     dbms = :dbms, os = :os, cn = :cn, verbal = :verbal, aptitude = :aptitude, math = :math  WHERE roll = :roll""",
                    {
                         'roll': entries[0].get(),
                         'python': entries[1].get(),
                         'c': entries[2].get(),
                         'java': entries[3].get(),
                         'ds': entries[4].get(),
                         'dbms': entries[5].get(),
                         'os': entries[6].get(),
                         'cn': entries[7].get(),
                         'verbal': entries[8].get(),
                         'aptitude': entries[9].get(),
                         'math': entries[10].get()
                    })
        entries[0].delete(0, END)
        entries[1].delete(0, END)
        entries[2].delete(0, END)
        entries[3].delete(0, END)
        entries[4].delete(0, END)
        entries[5].delete(0, END)
        entries[6].delete(0, END)
        entries[7].delete(0, END)
        entries[8].delete(0, END)
        entries[9].delete(0, END)
        entries[10].delete(0, END)
        l2.config(text="Updated...!")
        connect.commit()
        connect.close()
    bInsert = Button(top, text="Insert", command=insert)
    bInsert.grid(row=13, column=1)
    bUpdate = Button(top, text="update", command=update_entries)
    bUpdate.grid(row=14, column=1)
    l = Label(top, text="")
    l.grid(row=15, column=1)

# Delete Function


def delete():
    connect = sqlite3.connect("my.db")
    crsr = connect.cursor()
    crsr.execute("DELETE FROM student WHERE roll_number = :roll",
                 {
                     'roll': entri.get()})
    crsr.execute("DELETE FROM company WHERE roll = :roll",
                 {
                     'roll': entri.get()})
    crsr.execute("DELETE FROM marks WHERE roll = :roll",
                 {
                     'roll': entri.get()})
    entri.delete(0, END)
    l2.config(text="Delete success...!")
    connect.commit()
    connect.close()

# For prediction
def prediction():
    top = Toplevel(window)
    top.geometry("900x900")
    top.resizable(width=0, height=0)
    entries = []
    for j in range(11):
        l = Label(top, text=marklist[j])
        l.grid(row=j, column=1, padx=5, pady=20)
    for i in range(11):
        entry = Entry(top)
        entry.grid(row=i, column=2, padx=5, pady=20)
        entries.append(entry)
    l = Label(top,text="")
    l.grid(row=13,column=1)
    def pred():
        roll = entries[0].get()
        python = entries[1].get()
        c = entries[2].get()
        java = entries[3].get()
        ds = entries[4].get()
        dbms = entries[5].get()
        os = entries[6].get()
        cn = entries[7].get()
        verbal = entries[8].get()
        aptitude = entries[9].get()
        math = entries[10].get()
        entries[0].delete(0, END)
        entries[1].delete(0, END)
        entries[2].delete(0, END)
        entries[3].delete(0, END)
        entries[4].delete(0, END)
        entries[5].delete(0, END)
        entries[6].delete(0, END)
        entries[7].delete(0, END)
        entries[8].delete(0, END)
        entries[9].delete(0, END)
        entries[10].delete(0, END)
        pred = lr.predict([[int(python),int(c),int(java),int(ds),int(dbms),int(os),int(cn),int(verbal),int(aptitude),int(math)]])[0]
        if pred == 0:
            l.config(text=roll+" you need to improve")
        else :
            l.config(text = roll + " you may select")
    btt = Button(top,text="predict",command=pred)
    btt.grid(row=12,column=1)
# Entering Details
bLabel = LabelFrame(window, text="Enter Records : ")
bLabel.pack(fill="both", expand="yes")
sButton = Button(bLabel,text="Student", command=s_top)
sButton.pack()
mButton = Button(bLabel,text="Marks", command=m_top)
mButton.pack()
cButton = Button(bLabel,text="Company", command=c_top)
cButton.pack()
# Deleting details
dLabel = LabelFrame(window,text="Delete Records : ")
dLabel.pack(fill="both", expand="yes")
dButton = Button(dLabel,text="delete",command=delete)
dButton.pack()
deletel = Label(dLabel,text="Enter Roll Number")
deletel.pack()
entri = Entry(dLabel)
entri.pack()
l2 = Label(dLabel,text="")
l2.pack()
# Prediction
pLabel = LabelFrame(window,text="Predict Your Placement")
pLabel.pack(fill="both",expand="yes")
pButton = Button(pLabel,text="predict",command=prediction)
pButton.pack()
window.mainloop()
