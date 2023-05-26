from tkinter import*
from tkcalendar import Calendar,DateEntry

screen=Tk()
screen.geometry('700x600')
screen.minsize(450,450)
screen.maxsize(700,600)
screen.title("Registration Form")

a=StringVar()
b=StringVar()
c=StringVar()
d=StringVar()
e=StringVar()
f=StringVar()
gender=IntVar()
lang1=IntVar()
lang2=IntVar()
def data():
    import sqlite3 as sq
    p=a.get()
    q=b.get()
    r=c.get()
    s=d.get()
    t=e.get()
    u=f.get()
    v=DateOfBirthPiker.get()
    ge=gender.get()
    if ge==0:
        ge1="Male"
        
    else:
        ge1="Female"
    la1=lang1.get()
    la2=lang2.get()
    if la1 and la2:
        lan="English & Hindi"
    elif la2:
        lan="Hindi"
    else:
        lan="English"
    print(lan)
    
    con=sq.connect("Registraton_Form1.db")
    cur=con.cursor()

    cur.execute("create table if not exists RegistrationForm(Name text,FatherName text,MotherName text,Email_Id text,Mobile_No text,Address text,Date_Of_Birth text,Language text,Gender text)")

    cur.execute("insert into RegistrationForm values(?,?,?,?,?,?,?,?,?)",[p,q,r,s,t,u,v,lan,ge1])

    con.commit()
    con.close()
    
    
l=Label(screen,text='Registration form for Admission',bg='orange',font=('Arial',22,'bold'),width=70)
l.pack(side=TOP)

candidate=Label(screen,text="Candidate Name:-",bg='orange',font=('Arial',16,'bold'))
candidate.place(x=50,y=70)

cInput=Entry(screen,text=a,font=('Arial',16,'bold'))
cInput.place(x=350,y=70)


FatherName=Label(screen,text="Candidate FatherName:-",bg='orange',font=('Arial',16,'bold'))
FatherName.place(x=50,y=120)

FatherNameInput=Entry(screen,font=('Arial',16,'bold'),text=b)
FatherNameInput.place(x=350,y=120)


MotherName=Label(screen,text="Candidate MotherName:-",bg='orange',font=('Arial',16,'bold'))
MotherName.place(x=50,y=170)

MotherNameInput=Entry(screen,font=('Arial',16,'bold'),text=c)
MotherNameInput.place(x=350,y=170)


Email=Label(screen,text="Email-id:-",bg='orange',font=('Arial',16,'bold'))
Email.place(x=50,y=220)

EmailInput=Entry(screen,font=('Arial',16,'bold'),text=d)
EmailInput.place(x=350,y=220)


MobileNo=Label(screen,text="Mobile-No:-",bg='orange',font=('Arial',16,'bold'))
MobileNo.place(x=50,y=270)

MobileNoInput=Entry(screen,font=('Arial',16,'bold'),text=e)
MobileNoInput.place(x=350,y=270)

Address=Label(screen,text="Address:-",bg='orange',font=('Arial',16,'bold'))
Address.place(x=50,y=320)

AddressInput=Entry(screen,font=('Arial',16,'bold'),text=f)
AddressInput.place(x=350,y=320)

DateOfBirth=Label(screen,text="Date Of Birth:-",bg='orange',font=('Arial',16,'bold'))
DateOfBirth.place(x=50,y=370)

DateOfBirthPiker= DateEntry(screen,width=19,font=('Arial',16,'bold'))
DateOfBirthPiker.place(x=350,y=370)

Lang=Label(screen,text="Language:-",bg='orange',font=('Arial',16,'bold'))
Lang.place(x=50,y=420)

Lang_Check1=Checkbutton(screen,text='English',onvalue=1,offvalue=0,height=2,width=10 ,variable=lang1)
Lang_Check1.place(x=330,y=420)

Lang_Check2=Checkbutton(screen,text='Hindi',onvalue=1,offvalue=0,height=2,width=10,variable=lang2)
Lang_Check2.place(x=450,y=420)

Gender=Label(screen,text='Gender:-',bg='orange',font=('Arial',16,'bold'))
Gender.place(x=50,y=470)

G_Male=Radiobutton(screen,text='Male', value=0,variable=gender)
G_Male.place(x=350,y=470)


G_Female=Radiobutton(screen,text='Female',value=1 ,variable=gender)
G_Female.place(x=470,y=470)

Btn=Button(screen,text="Submit",font=('Arial',16,'bold'),command=data)
Btn.place(x=300,y=550)



screen.mainloop()

