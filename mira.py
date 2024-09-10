from tkinter import *
import math, random , os
from tkinter import messagebox
from tkinter import ttk
import pymysql
import mysql.connector
class Mira:
    def __init__ (self,root):
        self.root=root
        self.root.geometry ('1300x700+30+10')
        self.root.title('miraschool')
        self.root.resizable (False, False)
        self.root.iconbitmap("miraschool.ico")
        def enrg():
            x=En_name.get() 
            s=x+" est bien enrigistré"
            messagebox.showinfo("liste d'éleves",s)
        def calcule():
            import calcule
            mypage=calcule.cal
            page=mypage.get()
            print(page)


        title = Label (self.root, text='miraschool', fg='yellow',bg="black",font=("tajawal",12))
        title.pack (fill=X)
        F1 =Frame(root, bd=2 ,width=338, height=320, bg='red')
        F1.place(x=0,y=25)
        tit = Label (F1, text="les donnés d'éleves",fg='black',bg='yellow',font=('tajawal',13, 'bold'))
        tit.place (x=0,y=0)
        his_name = Label(F1 ,text="mon d'eleve", font=('tajawal',10),bg='red')
        his_name.place (x=6, y=40)
        his_phone = Label(F1, text='numero de téléphone', font=('tajawal',10),bg='red')
        his_phone.place (x=6, y=70)
        his_num = Label (F1, text="carte d'identité", font=('tajawal',10), bg='red')
        his_num.place (x=6,y=100)
        his_mail = Label (F1, text="email", font=('tajawal',10), bg='red')
        his_mail.place (x=6,y=130)
        his_nv = Label (F1, text="niveau scolaire", font=('tajawal',10), bg='red')
        his_nv.place (x=6,y=160)
        his_ad = Label (F1, text="adresse", font=('tajawal',10), bg='red')
        his_ad.place (x=6,y=190)
        lbl_certi=Label(F1,text='le genre',bg='red',font=('tajawal',10))
        lbl_certi.place(x=6,y=220)
        combo=ttk.Combobox(F1)
        combo['value']=('homme','femme')
        combo.place(x=130,y=220)
        En_name =Entry (F1 ,font=('tajawal',12), justify='center')
        En_name.place (x=130,y=40)
        En_phone =Entry (F1 ,font=('tajawal',12), justify='center')
        En_phone.place (x=130,y=70)
        En_id =Entry(F1 ,font=('tajawal',12))
        En_id.place (x=130,y=100)
        En_mail =Entry(F1 ,font=('tajawal',12))
        En_mail.place (x=130,y=130)
        En_nv =Entry(F1 ,font=('tajawal',12))
        En_nv.place (x=130,y=160)
        En_ad=Entry(F1 ,font=('tajawal',12))
        En_ad.place (x=130,y=190)
        valid=Button(F1,bg="yellow",fg="black",text="enrigister",command=enrg)
        valid.place (x=130,y=280)
        F2 =Frame(root, bd=2 ,width=338, height=400, bg='gold')
        F2.place(x=0,y=340)
        tit1 = Label (F2, text="controle barre",fg='black',bg='yellow',font=('tajawal',13, 'bold'))
        tit1.place(x=0,y=0)
        badd=Button(F2,text="ajoute un eleve",bg='yellow',fg='black',command=add_student)
        badd.place(x=50,y=75)
        bsup=Button(F2,text="supprimer un eleve",bg='yellow',fg='black')
        bsup.place(x=50,y=120)
        bmod=Button(F2,text="modifier les informations",bg='yellow',fg='black')
        bmod.place(x=50,y=180)
        bcal=Button(F2,text="calcule de moyenne",bg='yellow',fg='black',command=calcule)
        bcal.place(x=200,y=120)
        bqu=Button(F2,text="fermer l'application",bg='yellow',fg='black',command=quit)
        bqu.place(x=200,y=180)
        F3 =Frame(root, bd=2 ,width=960, height=50, bg='gold')
        F3.place(x=340,y=25)
        rch=Label(F3,text='rechercher un eleve avec sans id',fg='black',bg='gold',font=('tajawal',13, 'bold'))
        rch.place(x=25,y=15)
        rche=Entry(F3,font=('tajawal',13, 'bold'))
        rche.place(x=350,y=15)
        rchb=Button(F3,text="recharcher",bg='red',fg='black')
        rchb.place(x=600,y=15)
        Dietals_Frame=Frame(self.root,bg='#F2F4F4')
        Dietals_Frame.place(x=340,y=100,width=960,height=600)
        scroll_x=Scrollbar(Dietals_Frame, orient=HORIZONTAL)
        scroll_y=Scrollbar(Dietals_Frame, orient=VERTICAL)
        self.student_table=ttk.Treeview(Dietals_Frame,
        columns=('nom','adresses','mail','phone','niveau scolaire','id'),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set)
        self.student_table.place(x=18,y=1,width=960,height=580)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=LEFT,fill=Y)
        scroll_x.config(command=self.student_table.xview)

        self.student_table['show']='headings'
        self.student_table.heading('nom',text="nom d'eleve")
        self.student_table.heading('adresses',text="adresses d'eleve")
        self.student_table.heading('mail',text="email")
        self.student_table.heading('phone',text="télephone")
        self.student_table.heading('niveau scolaire',text="niveau scolaire")
        self.student_table.heading('id',text="id")
        self.student_table.column('nom',width=60)
        self.student_table.column('adresses',width=60)
        self.student_table.column('id',width=10)
        self.student_table.column('mail',width=120)
        self.student_table.column('niveau scolaire',width=10)
        self.name_var=StringVar()
        self.adrese_var=StringVar()
        self.mail_var=StringVar()
        self.nv_var=StringVar()
        self.id_var=StringVar()
        self.phone_var=StringVar()

        self.name_var=En_name.get()
        self.adrese_var=En_ad.get()
        self.mail_var=En_mail.get()
        self.phone_var=En_phone.get()
        self.nv_var=En_nv.get()
        self.id_var=En_id.get()
def add_student(self):
        con=pymysql.connect(host='localhost',user ='root@localhost',password='',database='student')
        cur=con.cursor()
        cur.execute("insert into st values(%s,%s,%s,%s,%s,%s)",(
                                                              self.id_var.get(),
                                                              self.nv_var.get(),
                                                              self.phone_var.get(),
                                                              self.mail_var.get(),
                                                              self.adrese_var.get(),
                                                              self.name_var.get()
                                                              ))
        con.commit()
        con.close()
        




        
    

    
       
    
        
           







        





    
        




root =Tk()
ob = Mira(root)
root.mainloop ( )     