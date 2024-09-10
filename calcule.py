from tkinter import *
import math, random , os
from tkinter import messagebox
from tkinter import ttk
class cal:
    def __init__ (self,root):
        self.root=root
        self.root.geometry ('1300x700+30+10')
        self.root.title('calcule de moyenne')
        self.root.resizable (False,False)
        self.root.iconbitmap("miraschool.ico")
        title = Label (self.root, text='miraschool', fg='yellow',bg="black",font=("tajawal",12))
        title.pack (fill=X)
        F1=Frame(self.root,bg='red',width=400,height=550)
        F1.place(x=450,y=25)
        F2=Frame(self.root,bg='yellow',width=400,height=550)
        F2.place(x=450,y=550)
        def calculmath():
            x=enmath.get()
            y=semath.get()
            s=(int(x)+int(y))/2
            t='le moyenne est '
            ms=t+str(s)
            messagebox.showinfo("le moyenne",ms)
        
        def calculphy():
            x=enphy.get()
            y=sephy.get()
            s=(int(x)+int(y))/2
            t='le moyenne est '
            ms=t+str(s)
            messagebox.showinfo("le moyenne",ms)

        def calculfra():
            x=enfra.get()
            y=sefra.get()
            s=(int(x)+int(y))/2
            t='le moyenne est '
            ms=t+str(s)
            messagebox.showinfo("le moyenne",ms)
        
        def calculeng():
            x=eneng.get()
            y=seeng.get()
            s=(int(x)+int(y))/2
            t='le moyenne est '
            ms=t+str(s)
            messagebox.showinfo("le moyenne",ms)
        
        def calcularab():
            x=enarab.get()
            y=searab.get()
            s=(int(x)+int(y))/2
            t='le moyenne est '
            ms=t+str(s)
            messagebox.showinfo("le moyenne",ms)
        def moygen():
            a=enmath.get()
            b=semath.get()
            s1=(int(a)+int(b))/2
            c=enphy.get()
            d=sephy.get()
            s2=(int(c)+int(d))/2
            e=enfra.get()
            f=sefra.get()
            s3=(int(e)+int(f))/2
            g=enarab.get()
            h=searab.get()
            s4=(int(g)+int(h))/2
            i=eneng.get()
            j=seeng.get()
            s5=(int(i)+int(j))/2
            sg=(s1+s2+s3+s4+s5)/5
            tg='le mogenne génerale est '+ str(sg)
            messagebox.showinfo("le moyenne",tg)




        math=Label(F1,bg='red',fg='black',font=("tajawal",12),text=' controle math')
        math.place(x=10,y=20)
        enmath=Entry(F1,font=("tajawal",12),width=5)
        enmath.place(x=120,y=20)
        smath=Label(F1,bg='red',fg='black',font=("tajawal",12),text=' synthése math')
        smath.place(x=170,y=20)
        semath=Entry(F1,font=("tajawal",12),width=5)
        semath.place(x=280,y=20)
        mym=Button(F1,text='calculer moyenne',bd=2,command=calculmath)
        mym.place(x=15,y=50)

        phy=Label(F1,bg='red',fg='black',font=("tajawal",12),text=' controle phy')
        phy.place(x=10,y=80)
        enphy=Entry(F1,font=("tajawal",12),width=5)
        enphy.place(x=120,y=80)
        sphy=Label(F1,bg='red',fg='black',font=("tajawal",12),text=' synthése physique')
        sphy.place(x=160,y=80)
        sephy=Entry(F1,font=("tajawal",12),width=5)
        sephy.place(x=300,y=80)
        mym=Button(F1,text='calculer moyenne',bd=2,command=calculphy)
        mym.place(x=15,y=110)

        fra=Label(F1,bg='red',fg='black',font=("tajawal",12),text=' controle fra')
        fra.place(x=10,y=150)
        enfra=Entry(F1,font=("tajawal",12),width=5)
        enfra.place(x=120,y=150)
        sfra=Label(F1,bg='red',fg='black',font=("tajawal",12),text=' synthése francais')
        sfra.place(x=160,y=150)
        sefra=Entry(F1,font=("tajawal",12),width=5)
        sefra.place(x=300,y=150)
        mym=Button(F1,text='calculer moyenne',bd=2,command=calculfra)
        mym.place(x=15,y=190)

        eng=Label(F1,bg='red',fg='black',font=("tajawal",12),text=' controle ang')
        eng.place(x=10,y=220)
        eneng=Entry(F1,font=("tajawal",12),width=5)
        eneng.place(x=120,y=220)
        seng=Label(F1,bg='red',fg='black',font=("tajawal",12),text=' synthése anglais')
        seng.place(x=160,y=220)
        seeng=Entry(F1,font=("tajawal",12),width=5)
        seeng.place(x=300,y=220)
        mym=Button(F1,text='calculer moyenne',bd=2,command=calculeng)
        mym.place(x=15,y=260)

        
        arab=Label(F1,bg='red',fg='black',font=("tajawal",12),text=' controle arabe')
        arab.place(x=10,y=290)
        enarab=Entry(F1,font=("tajawal",12),width=5)
        enarab.place(x=120,y=290)
        sarab=Label(F1,bg='red',fg='black',font=("tajawal",12),text=' synthése arabe')
        sarab.place(x=160,y=290)
        searab=Entry(F1,font=("tajawal",12),width=5)
        searab.place(x=300,y=290)
        mym=Button(F1,text='calculer moyenne',bd=2,command=calcularab)
        mym.place(x=15,y=320)




        bmoyen=Button(F2,text='moyenne génerale',bg='red',fg='black',bd=2,command=moygen)
        bmoyen.place(x=15,y=50)
        exist=Button(F2,text="fermer l'application",bg='red',fg='black',bd=2,command=quit)
        exist.place(x=250,y=50)





root =Tk()     
ob = cal(root)
root.mainloop ()     