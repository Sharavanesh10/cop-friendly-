import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox,simpledialog
conn=sqlite3.connect('mydatabse.db')
c=conn.cursor()
c.execute("DROP TABLE IF EXISTS log")
c.execute("CREATE TABLE log(City char(20),Cop_name char(20),Cop_phno int,Branch_name char(20),Area_name char(20),Station_name char(20))")
c.execute("INSERT INTO log VALUES('Trichy','SNS',7531598246,'KKnagar','KKnagar','T-5')")
c.execute("INSERT INTO log VALUES('Trichy','Np',8246791350,'Srirangam','Ammamandapam road','T-7')")
c.execute("INSERT INTO log VALUES('Trichy','Ram',4682135795,'Woraiyur','Big sowrasthra road','T-2')")
c.execute("INSERT INTO log VALUES('Trichy','Sangi',9825364172,'Palakarai','Sangliyandapuram','T-12')")
c.execute("INSERT INTO log VALUES('Madurai','SNS',7531598246,'Southgate','Palace road','M-5')")
c.execute("INSERT INTO log VALUES('Madurai','Np',8246791350,'Jaihindpuram','Jaihindpuram 2nd mainroad','M-7')")
c.execute("INSERT INTO log VALUES('Madurai','Ram',4682135795,'Karimedu','Mela ponnagaram','M-2')")
c.execute("INSERT INTO log VALUES('Madurai','Sangi',9825364172,'Subramaniyapuram','Pallivasal N Ln','M-12')")
conn.commit()
    
def copfriend():
    city=city_input.get()
    city=city.capitalize()
    
    c.execute("SELECT Cop_name,Cop_phno,Branch_name,Area_name,Station_name FROM log WHERE City=?",[city])
    stu=c.fetchall()
    
    for widget in log_frame.winfo_children():
        widget.destroy()

    searched_header=tk.Label(nw,text="Searched city =>",font=("Copperplate Gothic Bold",30,"bold"))
    searched_header.place(relx=0.4,rely=0.2,anchor='center')

    searched_op=tk.Label(nw,text=""+city,font=("Fugaz One",20,"bold"))
    searched_op.place(relx=0.6,rely=0.2,anchor='center')
        
    copname_header=tk.Label(log_frame,text="Cop name",font=("Copperplate Gothic Bold",20,"bold"))
    copname_header.grid(row=0,column=0,padx=10,pady=5)
    
    copno_header=tk.Label(log_frame,text="Cop Phno",font=("Copperplate Gothic Bold",20,"bold"))
    copno_header.grid(row=0,column=1,padx=10,pady=5)
    
    brname_header=tk.Label(log_frame,text="Branch",font=("Copperplate Gothic Bold",20,"bold"))
    brname_header.grid(row=0,column=2,padx=10,pady=5)
    
    arname_header=tk.Label(log_frame,text="Area",font=("Copperplate Gothic Bold",20,"bold"))
    arname_header.grid(row=0,column=3,padx=10,pady=5)
    
    stname_header=tk.Label(log_frame,text="Station",font=("Copperplate Gothic Bold",20,"bold"))
    stname_header.grid(row=0,column=4,padx=10,pady=5)

    for i,cop in enumerate(stu):
        copname_label=tk.Label(log_frame,text=cop[0],font=('calibri',22))
        copname_label.grid(row=i+1,column=0,padx=10,pady=5)

        copno_label=tk.Label(log_frame,text=cop[1],font=('calibri',22))
        copno_label.grid(row=i+1,column=1,padx=10,pady=5)

        brname_label=tk.Label(log_frame,text=cop[2],font=('calibri',22))
        brname_label.grid(row=i+1,column=2,padx=10,pady=5)

        arname_label=tk.Label(log_frame,text=cop[3],font=('calibri',22))
        arname_label.grid(row=i+1,column=3,padx=10,pady=5)

        stname_label=tk.Label(log_frame,text=cop[4],font=('calibri',22))
        stname_label.grid(row=i+1,column=4,padx=10,pady=5)

        log_frame.configure(bd=2,relief='groove')

def nextwin():
    global log_frame
    global nw
    nw=tk.Toplevel(root)
    nw.attributes('-fullscreen',True)
    nw.title("Your search")
    log_frame=tk.Frame(nw)
    log_frame.place(relx=0.5,rely=0.5,anchor='center')
    copfriend()

def go_back():
    # Define the action to be performed when the back button is clicked
    # Switch to the first tab
    city_label=tk.Label(root,text="Where are you located now ?",font=('Copperplate Gothic Bold',50))
    city_label.place(relx=0.5,rely=0.3,anchor='center')

    city_input=tk.Entry(root,font=('Cascadia Mono',40))
    city_input.place(relx=0.5,rely=0.5,anchor='center')

    disp_button=tk.Button(root,text="Search",font=('lemon',25),command=nextwin)
    disp_button.place(relx=0.5,rely=0.7,anchor='center')

    back_button = tk.Button(nextwin, text="Back",font=('lemon',25), command=go_back)
    back_button.place(relx=0.5,rely=0.9,anchor='center')
    go_back()
#root = tk.Tk()
#root.title("Tabbed Interface")

# Create a tabbed interface



root=tk.Tk()
#tab_control = tk.(root)
root.attributes('-fullscreen',True)
root.title("Cop Friendly")
city_label=tk.Label(root,text="Where are you located now ?",font=('Copperplate Gothic Bold',50))
city_label.place(relx=0.5,rely=0.3,anchor='center')

city_input=tk.Entry(root,font=('Cascadia Mono',40))
city_input.place(relx=0.5,rely=0.5,anchor='center')

disp_button=tk.Button(root,text="Search",font=('lemon',25),command=nextwin)
disp_button.place(relx=0.5,rely=0.7,anchor='center')

back_button = tk.Button(nextwin, text="Back",font=('lemon',25), command=go_back)
back_button.place(relx=0.5,rely=0.9,anchor='center')

#tab_control.pack(expand=1, fill='both')

root.mainloop()

conn.close()

#import tkinter as tk
#from tkinter import ttk

"""def go_back():
    # Define the action to be performed when the back button is clicked
    tab_control.select(0)  # Switch to the first tab

#root = tk.Tk()
#root.title("Tabbed Interface")

# Create a tabbed interface
tab_control = tk.Notebook(root)"""

# Create the first tab
#tab1 = ttk.Frame(tab_control)
#tab_control.add(tab1, text='Tab 1')

# Create the second tab
#tab2 = ttk.Frame(tab_control)
#tab_control.add(tab2, text='Tab 2')

# Add a back button to the second tab


# Pack the tab control widget


#root.mainloop()

    
    
