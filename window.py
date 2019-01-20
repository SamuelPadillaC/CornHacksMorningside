from Tkinter import *
root=Tk()
root.geometry("1000x1000") 

def var_states():
   print("option1: %d,noption2: %d,\noption3: %d".center(200) % (var1.get(), var2.get(), var3.get()))

Label(root, text="Your option:".center(200)).grid(row=0, sticky=W)
var1 = IntVar()
Checkbutton(root, text="option1", variable=var1).grid(row=1)
var2 = IntVar()
Checkbutton(root, text="option2", variable=var2).grid(row=2)
var3 = IntVar()
Checkbutton(root, text="option3", variable=var3).grid(row=3)

Button(root, text='cancle', command=root.quit).grid(row=4, pady=4)
Button(root, text='Go', command=var_states).grid(row=5,pady=4)

mainloop()
