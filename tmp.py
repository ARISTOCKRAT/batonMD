import tkinter
from tkinter import ttk
tkwindow = tkinter.Tk()
chk = ttk.Checkbutton(tkwindow, text="foo")
chk.state(['selected'])  # check the checkbox
# chk.state(['!selected']) # clear the checkbox
# chk.state(['disabled'])  # disable the checkbox
# chk.state(['!disabled','selected']) # enable the checkbox and put a check in it!
chk.grid(column=0, row=0)

tkwindow.mainloop()