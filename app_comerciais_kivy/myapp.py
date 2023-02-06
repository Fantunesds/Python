from tkinter import*
from tkinter import ttk


# cores-------------------------------------------
cor1 = '#00FA9A' #SpringGreen


myApp = Tk()
myApp.title("MyApp")
myApp.iconbitmap("img/Kit.ico")
myApp.geometry("800x450")
myApp.resizable(width='False',height='False')
myApp.configure(bg="#00FA9A")
#myApp.wm_maxsize(width=1000,height=500)
#myApp.wm_minsize(width=500,height=250)

label = ttk.Label(myApp, text=" Hello World!").place(x=1)




myApp.mainloop()

