from tkinter import *
from tkinter import messagebox
import webbrowser
import os
import sys
pro=Tk()
pro.geometry("800x400")
pro.resizable(False,False)
pro.title("miraschool")
pro.iconbitmap("miraschool.ico")
title=Label(pro,text="miraschool",fg="gold",bg="black",font=('tajawel',16,'bold'))
title.pack(fill=X)
u1='https://www.facebook.com/profile.php?id=100010354231680'
def open1():
    webbrowser.open_new(u1)
def verif():
    user=Enl.get()
    passw=En2.get()
    if user=='aziz' and passw=="12345678":
        messagebox.showinfo('welcome',"user et mot de passe sont correct")
        import mira
        mypage=Mira.mira
        page=mypage.get()
        print(page)
    else:
        messagebox.showerror('eurror',"mot de passe et user ne sont pas correct")
F1=Frame (pro, width=230, height=420 ,bg='yellow')
F1.place(x=570,y=30)
title3 =Label(F1,text='contact :',bg='yellow',fg='black',font=("tajawal",12,'bold'))
title3.place(x=76,y=90)
B1=Button(F1, text='facebook account',width=26,fg='black',bg='yellow',font=('tajawal',11,'bold'),command=open1)
B1.place(x=2,y=130)
title4 =Label(F1,text='telephone:51098640',bg='yellow',fg='black',font=("tajawal",12,'bold'))
title4.place(x=40,y=170)
B2=Button(F1, text='fermer le systéme',width=26,fg='black',bg='yellow',font=('tajawal',11,'bold'),command=quit)
B2.place(x=30,y=330)
photo=PhotoImage(file="miraschool.png")
imo=Label(pro,image=photo)
imo.place(x=0,y=30,height=300,width=600)
F2=Frame (pro, width=570, height=120,bg='yellow')
F2.place(x=0,y=330)
l1=Label(F2,text='le nom de utilisateur',fg='black',bg='yellow',font=("tajawal",12))
l1.place(x=20,y=10)
l2=Label(F2,text='le mot de passe',fg='black',bg='yellow',font=("tajawal",12))
l2.place(x=20,y=40)
Enl =Entry (F2 ,font=('tajawal',12), justify='center')
Enl.place (x=170,y=10)
En2 = Entry (F2 ,font=('tajawal',12), justify='center')
En2.place(x=170,y=40)
b=Button(F2,text='login',fg='black',bg='yellow',font=("tajawal",12),command=verif)
b.place(x=400,y=15)

pro.mainloop()