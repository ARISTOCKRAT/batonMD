# # # import tkinter as tk
# # # from tkinter import ttk
# # #
# # # root = tk.Tk()
# # # root.geometry('600x800')
# # # container = ttk.Frame(root)
# # # canvas = tk.Canvas(container)
# # # scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
# # # scrollable_frame = ttk.Frame(canvas)
# # #
# # # scrollable_frame.bind(
# # #     "<Configure>",
# # #     lambda e: canvas.configure(
# # #         scrollregion=canvas.bbox("all")
# # #     )
# # # )
# # #
# # # canvas.create_window((150, 150), window=scrollable_frame, anchor="nw")
# # #
# # # canvas.configure(yscrollcommand=scrollbar.set)
# # #
# # # for i in range(50):
# # #     ttk.Label(scrollable_frame, text="Sample scrolling label").pack()
# # #
# # # container.pack()
# # # canvas.pack(side="left", fill="both", expand=True)
# # # scrollbar.pack(side="right", fill="y")
# # #
# # # root.mainloop()
# #
# # from tkinter import *
# #
# # def data():
# #     for i in range(50):
# #        Label(frame,text=i).grid(row=i,column=0)
# #        Label(frame,text="my text"+str(i)).grid(row=i,column=1)
# #        Label(frame,text="..........").grid(row=i,column=2)
# #
# # def myfunction(event):
# #     canvas.configure(scrollregion=canvas.bbox("all"),width=600,height=600)
# #
# # root=Tk()
# # sizex = 800
# # sizey = 600
# # posx  = 100
# # posy  = 100
# # root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
# #
# # myframe=Frame(root,relief=GROOVE,width=50,height=100,bd=1)
# # myframe.place(x=10,y=10)
# #
# # canvas=Canvas(myframe)
# # frame=Frame(canvas)
# # myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
# # canvas.configure(yscrollcommand=myscrollbar.set)
# #
# # myscrollbar.pack(side="right",fill="y")
# # canvas.pack(side="left")
# # canvas.create_window((0,0),window=frame,anchor='nw')
# # frame.bind("<Configure>", myfunction)
# # data()
# # root.mainloop()
#
# a = "askdgashdjasjdasj"
# print(
#     a[a.find('dj'):]
# )
#
# input()

import tkinter as tk
import webbrowser

def callback(event):
    webbrowser.open_new(event.widget.cget("text"))

root = tk.Tk()
lbl = tk.Label(root, text=r"http://www.google.com", fg="blue", cursor="hand2")
lbl.pack()
lbl.bind("<Button-1>", callback)
root.mainloop()