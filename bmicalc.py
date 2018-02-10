
# coding: utf-8

# In[8]:


from tkinter import *

def show_entry_fields():
    inweight = float(e1.get())
    inheight = float(e2.get())
    sqinheight = inheight**2
    bmi = (inweight / sqinheight)*703

    if bmi < 18.5:
        e3.delete(0, END)
        e4.delete(0, END)
        e3.insert(0, ("%.2f" % bmi))
        e4.insert(0, "Underweight")
    elif (bmi >= 18.5) and (bmi < 25):
        e3.delete(0, END)
        e4.delete(0, END)
        e3.insert(0, ("%.2f" % bmi))
        e4.insert(0, "Normal Weight")
    elif (bmi >= 25) and (bmi < 30):
        e3.delete(0, END)
        e4.delete(0, END)
        e3.insert(0, ("%.2f" % bmi))
        e4.insert(0, "Overweight")
    else:
        e3.delete(0, END)
        e4.delete(0, END)
        e3.insert(0, ("%.2f" % bmi))
        e4.insert(0, "Obese")

master = Tk()
Label(master, text="Weight: ").grid(row=0)
Label(master, text="Height: ").grid(row=1)
Label(master, text="BMI: ").grid(row=2)
Label(master, text="Status: ").grid(row=3)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)



Button(master, text='Calculate BMI', command=show_entry_fields).grid(row=4, column=1, sticky=W, pady=4)

master.title("BMI")
master.iconbitmap(r'./scale.ico')
master.minsize(width=198, height=119)
master.maxsize(width=198, height=119)
master.resizable(0, 0)

mainloop( )