#!/usr/bin/python

#--------------------------------------------------------------
# imports
#--------------------------------------------------------------
import tkinter as tk
import president

#--------------------------------------------------------------
# globals
#--------------------------------------------------------------
checkbutton_data = (
    ("bdate","Date of Birth"),
    ("ddate","Date of Death"),
    ("bplace","Place of Birth"),
    ("bstate","State of Birth"),
    ("ts_date","Date term stated"),
    ("te_date","Date term ended"),
    ("party","Party Affiliation"),
)

cb = {}

#--------------------------------------------------------------
# functions
#--------------------------------------------------------------
def check_all():
    """ 
    Check status of "Check all" radio button -- if checked, set
    all buttons on; otherwise, set all buttons off
    """
    cb_status =  cb_all_checked.get()
    
    for fld,label in checkbutton_data:
        cb[fld][1].set(cb_status)

def search():
    """
    Fetch data for specified index and redraw the data window
    """
    i = p_index.get()

    i = int(i)

    p = president.President(i)

    tx_data.delete('0.0','end')

    tx_data.insert('end',p.FirstName+ " " + p.last_name+ "\n")

    if cb["bdate"][1].get():
        tx_data.insert('end',str(p.BirthDay)+"\n")

# OR, could add method names to checkbutton_data, and then call 
# methods by name via getattr():
#    meth = "BirthDay"
#    if cb["bdate"][1].get():
#        tx_data.insert('end',str(getattr(p,meth)())+"\n")

    if cb["ddate"][1].get():
        tx_data.insert('end',str(p.DeathDay)+"\n")
    
    if cb["bplace"][1].get():
        tx_data.insert('end',str(p.BirthPlace)+"\n")

    if cb["bstate"][1].get():
        tx_data.insert('end',str(p.BirthState)+"\n")

    if cb["ts_date"][1].get():
        tx_data.insert('end',str(p.TermStart)+"\n")

    if cb["te_date"][1].get():
        tx_data.insert('end',str(p.TermEnd)+"\n")

    if cb["party"][1].get():
        tx_data.insert('end',str(p.Party)+"\n")

def mkrow(row):
    """
    Given an integer, format it as a row index suitable for the Text widget.
    """
    return "%d.0" % row

def build_gui():
    """
    Construct the GUI
    """
    global mwin
    global p_index
    global tx_data
    global cb
    global cb_all
    global cb_all_checked

    mwin = tk.Tk()
    p_index = tk.StringVar(mwin)

    fr_top = tk.Frame(mwin)
    fr_top.pack()
    fr_bottom = tk.Frame(mwin)
    fr_bottom.pack()

    lab_index = tk.Label(fr_top,text="Enter Index (1-43)")
    lab_index.pack(side=tk.LEFT)

    e_index = tk.Entry(fr_top,width=4,textvariable=p_index)
    e_index.pack(side=tk.LEFT)

    cb_all_checked = tk.IntVar(mwin)

    for value,label in checkbutton_data:
        iv = tk.IntVar(mwin)
        cb[value] = (tk.Checkbutton(fr_bottom,text=label,variable=iv),iv)
        cb[value][0].pack(anchor="w")

    cb_all = tk.Checkbutton(fr_bottom,text="All",variable=cb_all_checked,
        command=check_all)
    cb_all.pack(anchor="w")

    bt_find = tk.Button(fr_bottom,text="Search",command=search)
    bt_find.pack()

    tx_data = tk.Text(fr_bottom,width=50,height=20)
    tx_data.pack()
    
    bt_quit = tk.Button(fr_bottom,text="Quit",command=mwin.destroy)
    bt_quit.pack()

#--------------------------------------------------------------
# main program 
#--------------------------------------------------------------
build_gui()

mwin.mainloop()
