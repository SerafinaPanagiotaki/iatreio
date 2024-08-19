import os
import csv
import msvcrt as m
import time
import datetime
import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter.scrolledtext import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile

def main(): #(2 επιλογές: Είσοδος στο σύστημα - Έξοδος-->τερματισμός προγ/τος)
    global root
    global firstFrame
    global false
    global miss
    global mainFrame
    root=Tk()
    miss=0
    false=0
    photo = PhotoImage(file = "unesco_logo_4.png") #window icon
    root.iconphoto(False, photo)
    width = root.winfo_screenwidth() #get your Windows width size 
    height = root.winfo_screenheight() #get your Windows height size     
    root.geometry("%dx%d+0+0" % (width, height)) #full size Tkinter
    root.resizable(False,False)    
    root.state('zoomed')  #full screen window'''
    root.option_add("*Button.Background", "#000080") #attribute για όλα τα Buttons
    root.option_add("*Button.Foreground", "#ffffff")  #attribute για όλα τα Buttons
    root.option_add("*Button.cursor", "hand2")  #attribute για όλα τα Buttons, cursor="hand2" --> cursor: pointer    
    mainFrame=LabelFrame(root, bd=0)#, bg="#000080")
    mainFrame.grid(row=0, column=0, columnspan=10)
    my_img=ImageTk.PhotoImage(Image.open("unesco_logo_2.jpg"))
    my_label=Label(mainFrame, image=my_img)
    my_label.grid(row=0, padx=0, column=0, columnspan=2)
    my_img2=ImageTk.PhotoImage(Image.open("espaLogo_3.jpg"))
    my_label2=Label(mainFrame, image=my_img2) 
    my_label2.grid(row=0, padx=0, column=9, columnspan=2)
    root.title("Όμιλος για την Unesco Πειραιώς και Νήσων - Πρόγραμμα παρακολούθησης ιατρικών ραντεβού - ΙΣΤΟΡΙΚΟ v.1.02 (Υφιστάμενη δομή)") #Υφιστάμενη δομή
    #root.title("Όμιλος για την Unesco Πειραιώς και Νήσων - Πρόγραμμα παρακολούθησης ιατρικών ραντεβού - ΙΣΤΟΡΙΚΟ v.1.02  (Νέα δομή)")    #Νέα δομή
    label00= Label(mainFrame, bg="#000080", fg="#ffffff", padx=10, pady=0, text="Όμιλος για την Unesco Πειραιώς και Νήσων", font=('bold', 18), bd=40)
    label00.grid(row=0, column=2, columnspan=7, sticky=W+E, pady=0)
    my_img0=ImageTk.PhotoImage(Image.open("doctor2.jpg"))
    my_label=Label(mainFrame, image=my_img0)#, bg="#000080")
    my_label.grid(row=1, padx=0, column=3, sticky=E)
    label01= Label(mainFrame, fg="#000080", text="ΙΣΤΟΡΙΚΟ", font=('bold', 40))#bg="#000080", 
    label01.grid(row=1, column=4, columnspan=3, sticky=W)
    label02= Label(mainFrame, fg="#000080", text="Πρόγραμμα καταγραφής και παρακολούθησης ιατρικών ιστορικών και μετρήσεων", font=('bold', 14))#, bd=7)bg="#000080", 
    label02.grid(row=2, column=0, columnspan=10, sticky=N)    
    label= Label(mainFrame, fg="#000080", padx=511, pady=5, text="ΙΣΤΟΡΙΚΟ v.1.02  - powered by Python v.3.10.5")#bg="#000080", 
    label.grid(row=3, column=0, columnspan=10, sticky=N, pady=0)   
    root.bind('<Escape>', lambda event: root.destroy())
    root.bind('<F11>', lambda event: exec('ΙΑΤΡΕΙΟ.py'))
    root.bind('<Return>', lambda event: logIn())
    messagebox.showinfo('Ενημέρωση:', 'Καλωσήρθατε στο "ΙΣΤΟΡΙΚΟ"!\n\nΠιέστε "OK" για να μεταβείτε στο κεντρικό μενού')
    menu_new("")    
    root.mainloop() 

def greetings(y): #μήνυμα τερματισμού του προγ/τος (το πρόγραμμα σε αυτό το σημείο είναι ανενεργό αλλά το παράθυρό του (root()) κλείνει ΜΟΝΟ με κλικ στο κουμπί "Κλείσιμο παράθυρου")
    if y!="":
        y.grid_forget()
    global finish
    global Frame0
    global x
    global status
    status=1
    #mainFrame.grid_forget()
    Frame0=LabelFrame(root, bd=0)
    Frame0.grid(row=4, column=0, columnspan=18)  
    label0= Label(Frame0, text="Ευχαριστούμε πολύ που χρησιμοποιήσατε την εφαρμογή!\n\nProgrammed, designed and developed by Shery Panagiotaki, @copyright 2022\n\n\nContact info:\n\nTel.: (+30) 6976929404\n\nE-mail: sherypanagiotaki@yahoo.com,\n             sherypamagiotaki@gmail.com", bd=0)
    label0.grid(row=700, column=0, columnspan=18, pady=15, sticky=W+E)
    Frame00=LabelFrame(Frame0, bd=0)
    Frame00.grid(row=15, column=0, columnspan=18)
    image4 = Image.open("iatreio_logo2.jpg")
    photo4 = ImageTk.PhotoImage(image4)
    shery_pic = Label(Frame0, image = photo4, bd=0)
    shery_pic.image = photo4
    shery_pic.grid(row=9, column=0, columnspan=52, pady=15)    
    finish=Button(Frame0, text="Κλείσιμο παράθυρου", padx=22, pady=11, command=lambda: root.destroy()) 
    again=Button(Frame0, text="Επανείσοδος", padx=42, pady=11, command=lambda: exec('ΙΑΤΡΕΙΟ.py'))
    info=Button(Frame0, text="Contact Service", padx=37, pady=11, command=fire)
    again.grid(row=16, column=8, padx=35, pady=35)
    finish.grid(row=16, column=9, padx=35, pady=35)
    info.grid(row=16, column=10, padx=35, pady=35)    
    if currentDate()[-2:]in ['01', '15', '30']:  #--> ενημέρωση αντιγράφων ασφαλείας κάθε 1η, 15η, και 30η αυτόματα στο τέλος του προγ/τος (θα γίνεται και μέσω χρήστη)
        restart.grid(row=16, column=8, padx=65, pady=35)
        finish.grid(row=16, column=9, padx=65, pady=35)
        status=0
        #update() ΝΑ ΤΗΝ ΕΝΕΡΓΟΠΟΙΗΣΩ ΟΤΑΝ ΕΙΝΑΙ ΕΤΟΙΜΑ ΤΑ ΑΡΧΕΙΑ ΠΟΥ ΔΙΑΧΕΙΡΙΖΕΤΑΙ!!!
    else:
        backupButton=Button(Frame0, text="Αντίγραφα ασφαλείας", padx=16, pady=11, command=lambda: update()) #goto(3)
        backupButton.grid(row=16, column=7, padx=35, pady=35)
        message="Δεν έγινε αυτόματη ενημέρωση των αντιγράφων ασφαλείας."
        messagebox.showwarning('Σημαντικό:', message)

def exec(x):
    root.destroy()
    os.system(x)

def currentDate():#υπολογισμός τρέχουσας ημ/νίας και δημιουργία string.
    x = str(datetime.date.today())  #current date
    x=x.split('-')
    x="".join(x)                    #current date as one string!
    return x        

def update(): #NA ΦΤΙΑΞΩ ΤΑ ΣΩΣΤΑ ΑΡΧΕΙΑ (ΟΝΟΜΑΤΑ)!!!
    global message
    global copyPrevious
    global copyCurrent
    global copyFuture
    global copyPast
    global copyPassword
    copyPrevious=[]
    copyCurrent=[]
    copyFuture=[]
    copyPast=[]
    copyPassword=[]
    with open("previous.csv", "r", encoding="utf-8", newline="") as file:
        ro=csv.reader(file, delimiter='$')
        for i in ro:
            copyPrevious.append(i)
        with open("..\\..\\backup_previous.csv", "w", encoding="utf-8", newline="") as file:
            wo=csv.writer(file, delimiter='$')
            for i in copyPrevious:
                wo.writerow(i)                    
    with open("current.csv", "r", encoding="utf-8", newline="") as file:
        ro=csv.reader(file, delimiter='$')
        for i in ro:
            copyCurrent.append(i)                  
        with open("..\\..\\backup_current.csv", "w", encoding="utf-8", newline="") as file:
            wo=csv.writer(file, delimiter='$')
            for i in copyCurrent:
                wo.writerow(i)
    with open("future.csv", "r", encoding="utf-8", newline="") as file:
        ro=csv.reader(file, delimiter='$')
        for i in ro:
            copyFuture.append(i)                  
        with open("..\\..\\backup_future.csv", "w", encoding="utf-8", newline="") as file:
            wo=csv.writer(file, delimiter='$')
            for i in copyFuture:
                wo.writerow(i)
    with open("past.csv", "r", encoding="utf-8", newline="") as file:
        ro=csv.reader(file, delimiter='$')
        for i in ro:
            copyPast.append(i)                  
        with open("..\\..\\backup_past.csv", "w", encoding="utf-8", newline="") as file:
            wo=csv.writer(file, delimiter='$')
            for i in copyPast:
                wo.writerow(i)
    with open("password.csv", "r", encoding="utf-8", newline="") as file:
        ro=csv.reader(file, delimiter='$')
        for i in ro:
            copyPassword.append(i)
        if len(copyPassword)==0:
            message="Παρακαλώ πολύ επικοινωνήστε με την προγραμματίστρια, κωδικός σφάλματος: EMPTY_PASSWORD_0"
            messagebox.showwarning('Σφάλμα:', message)
        else:
            with open("..\\..\\backup_password.csv", "w", encoding="utf-8", newline="") as file:
                wo=csv.writer(file, delimiter='$')
                for i in copyPassword:
                    wo.writerow(i)
                if status ==0:
                    message="Αυτόματη ενημέρωση αντιγράφων ασφαλείας: επιτυχής."
                else:
                    message="Ενημέρωση αντιγράφων ασφαλείας: επιτυχής."
                messagebox.showinfo('Σημαντικό:', message)        

def menu_new(x):#Κεντρικό μενού
    if x!="":
        x.grid_forget()
    global mainMenu   
    mainMenu=LabelFrame(root, padx=5, pady=10, bd=0)
    mainMenu.grid(row=5, column=0, columnspan=10, padx=10, pady=15)                           
    epilogi4=Button(mainMenu, bg="#000080", fg="white", text="Ιστορικό", padx=67, pady=11, command=lambda: istoriko(mainMenu))
    epilogi4.grid(row=7, column=0, padx=33, pady=15)
    epilogi5=Button(mainMenu, bg="#000080", fg="white", text="Παραπεμπτικό σημείωμα", padx=21, pady=11, command=lambda: parapemptiko(mainMenu))
    epilogi5.grid(row=7, column=2, padx=33, pady=15)
    epilogi8=Button(mainMenu, bg="#000080", fg="white", text="Ιστορικό ενεργειών (follow-up)", padx=7, pady=11, command=lambda: follow-up(mainMenu))
    epilogi8.grid(row=7, column=4, padx=33, pady=15)   
    epilogi6=Button(mainMenu, bg="#000080", fg="white", text="Διάγραμμα αρτηριακής πίεσης\n- μετρήσεις γλυκόζης", padx=8, pady=3, command=lambda: diagramma(mainMenu))
    epilogi6.grid(row=7, column=6, padx=33, pady=15)                               
    epilogi7=Button(mainMenu, bg="#000080", fg="white", text="Έξοδος", padx=68, pady=11, command=lambda: greetings(mainMenu))
    epilogi7.grid(row=7, column=8, padx=33, pady=15)
    mainMenu2=LabelFrame(mainMenu, bd=0)
    mainMenu2.grid(row=20, column=0, columnspan=10, pady=50)
    other=Label(mainMenu2, text="ΑΛΛΑ ΔΙΑΘΕΣΙΜΑ ΠΡΟΓΡΑΜΜΑΤΑ: ", bg="#000080", fg="#ffffff", pady=10, font=('bold', 12))
    other.grid(row=20, column=0, columnspan=10)
    image5 = Image.open("rantevou.jpg")
    photo5 = ImageTk.PhotoImage(image5)
    label5 = Button(mainMenu2, image = photo5, command=lambda: exec('ΡΑΝΤΕΒΟΥ_v.3.02.5.py'))
    label5.image = photo5
    label5.grid(row=25, column=6, pady=25)

def fire(): #μήνυμα στοιχείων επικοινωνίας για service.
    messagebox.showinfo('Service - Πληροφορίες επικοινωνίας:', 'Programmer / Developer: Shery Panagiotaki\n\nContact info:\n\nTel.: (+30) 6976929404\n\nE-mail: sherypanagiotaki@yahoo.com,\n             sherypamagiotaki@gmail.com')          

def exec(x):
    root.destroy()
    os.system(x)

def diagramma(x):
    if x!="":
        x.grid_forget()
    diagr1=LabelFrame(root, bd=0)
    diagr1.grid(row=5, column=0, columnspan=12)
    FrameForScroll=LabelFrame(diagr1, bd=0) #scrollbar attempt!!!
    FrameForScroll.grid(row=5, column=0, columnspan=12)
    Frame100=LabelFrame(FrameForScroll, bd=0)
    Frame100.grid(row=500, column=0, columnspan=12)
    #ΝΑ ΕΛΕΓΞΩ ΤΙΣ ΔΙΑΣΤΑΣΕΙΣ ΤΟΥ MONITOR ΓΙΑ ΝΑ ΓΙΟΥΝ ADJUSTMENTS ΣΤΗΝ ΕΠΟΜΕΝΗ ΓΡΑΜΜΗ(HEIGHT, WIDTH)!!!
    canvas=Canvas(FrameForScroll, bd=0, height=480, width=1220) 
    canvas.grid(row=0, column=0, columnspan=12, sticky=N+S+E+W)    
    diagr2=LabelFrame(canvas, bd=0)
    scrollbar = Scrollbar(FrameForScroll, orient="vertical", command=canvas.yview)
    scrollbar.grid(row=0, column=12, sticky=N+S)
    diagr2.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=diagr2, anchor="nw", width=1220)
    canvas.configure(yscrollcommand=scrollbar.set)
    title0=Label(diagr2, text="ΔΙΑΓΡΑΜΜΑ ΑΡΤΗΡΙΑΚΗΣ ΠΙΕΣΗΣ - ΜΕΤΡΗΣΕΙΣ ΓΛΥΚΟΖΗΣ", fg="#000080", bg="#d9d9d9", font=('bold', 15), pady=15)
    title0.grid(row=5, column=0, columnspan=12, sticky=W+E)
    blank1=Label(diagr2, text="")
    blank1.grid(row=7, column=0, columnspan=12, sticky=W+E)#, pady=5)    
    title1=Label(diagr2, text="ΑΡΤΗΡΙΑΚΗ ΠΙΕΣΗ", fg="#000080", bg="#d9d9d9", pady=10, bd=1, relief=SUNKEN)
    title1.grid(row=10, column=0, columnspan=6, sticky=W+E)
    title2=Label(diagr2, text="ΚΛΙΜΑΚΑ ΓΛΥΚΟΖΗΣ", fg="#000080", bg="#d9d9d9", pady=10, bd=1, relief=SUNKEN)
    title2.grid(row=10, column=6, columnspan=6, sticky=W+E)
    #blank2=Label(diagr2, text="")
    #blank2.grid(row=12, column=0, columnspan=12, sticky=W+E)#, pady=15)
    inside1=LabelFrame(diagr2, bd=0)
    inside1.grid(row=15, column=0, columnspan=6)
    title3=Label(inside1, text="120", bg="#000080", fg="#ffffff", pady=10, padx=35)
    title3.grid(row=15, column=0, sticky=W+E)
    title4=Label(inside1, text="ΣΥΣΤΟΛΙΚΗ", fg="#000080", bg="#d9d9d9", pady=10, padx=15)
    title4.grid(row=15, column=2, sticky=W+E)    
    title5=Label(inside1, text="80", bg="#000080", fg="#ffffff", pady=10, padx=36)
    title5.grid(row=20, column=0, sticky=W+E, pady=5)
    title6=Label(inside1, text="ΔΙΑΣΤΟΛΙΚΗ", fg="#000080", bg="#d9d9d9", pady=10, padx=16)
    title6.grid(row=20, column=2, sticky=W+E, pady=5)
    title7=Label(inside1, text=">170, <90", bg="#000080", fg="#ffffff", pady=10, padx=36)
    title7.grid(row=15, column=4, sticky=W+E, pady=5)
    title8=Label(inside1, text=">110, <50", bg="#000080", fg="#ffffff", pady=10, padx=36)
    title8.grid(row=20, column=4, sticky=W+E, pady=5)
    for i in range(2):
        blankCell=Label(inside1, text="")
        blankCell.grid(row=15+5*i, column=1+2*i, sticky=W+E)    
    global inside2
    inside2=LabelFrame(diagr2, bd=0)
    inside2.grid(row=15, column=6, columnspan=6)        
    for i in range(3):
        if i==0:
            txt1="70"
            txt2="ΧΑΜΗΛΗ"
        elif i==1:
            txt1="100"
            txt2="ΦΥΣΙΟΛΟΓΙΚΗ"
        else:
            txt1="150"
            txt2="ΥΨΗΛΗ"
        title9=Label(inside2, text=txt1, bg="#000080", fg="#ffffff", pady=10, padx=16)
        title9.grid(row=15, column=6+2*i, sticky=W+E, pady=5)
        title10=Label(inside2, text=txt2, fg="#000080", bg="#d9d9d9", pady=10, padx=16)
        title10.grid(row=20, column=6+2*i, sticky=W+E, pady=5)
        if i<2:
            blankCell2=Label(inside2, text="")
            blankCell2.grid(row=15, column=7+2*i, sticky=W+E)       
    global j
    for j in range(3): 
        #global name
        #global space
        #global size
        global k
        for k in range(10):
            if k==0:
                name="Ημερομηνία"
                space=2
                size=10
            elif k==1:
                name="Ώρα"
                space=2
                size=10
            elif k==2:
                name="Γεγονός"
                space=5
                size=20
            elif k==3:
                name="Συστολική"
                space=2
                size=15
            elif k==4:
                name="Διαστολική"
                space=2
                size=15
            elif k==5:
                name="Σφύξεις"
                space=2
                size=15
            elif k==6:
                name="Γλυκόζη"
                space=2
                size=15
            elif k==7:
                name="Επίπεδο"
                space=2
                size=15
            elif k==8:
                name="Κατάσταση"
                space=2
                size=15
            elif k==9:
                name="Σημειώσεις"
                space=2
                size=60
            legend=Label(diagr2, text=name, fg="#000080", bg="#d9d9d9", pady=10, padx=space, bd=1, relief=SUNKEN)
            legend.grid(row=25, column=k, sticky=W+E)
            global field
            field=Entry(diagr2, width=size, bd=1, relief=SUNKEN)
            field.grid(row=30+j, column=k, sticky=W+E+N)
            if j%3==0:
                field.config(rowspan=3)
            
            reg = root.register(callback)
            if k==0 and (j%3==0 or j%3==1):
                field.config(validate ="focusout",validatecommand =(reg, '%s'))


             
def callback(input):
    if not input is "":
        print(input)
        #for i in range(1, 3):
        field.insert(INSERT, input)
        field.grid(row=30+j, column=0, sticky=W+E+N)
        return True



    
    
def parapemptiko(x):
    x.grid_forget()
    para1=LabelFrame(root, bd=0)
    para1.grid(row=5, column=0, columnspan=10)

    FrameForScroll=LabelFrame(para1, bd=0) #scrollbar attempt!!!
    FrameForScroll.grid(row=11, column=0, columnspan=10)
    Frame100=LabelFrame(FrameForScroll, bd=0)
    Frame100.grid(row=500, column=0, columnspan=10)
    #ΝΑ ΕΛΕΓΞΩ ΤΙΣ ΔΙΑΣΤΑΣΕΙΣ ΤΟΥ MONITOR ΓΙΑ ΝΑ ΓΙΟΥΝ ADJUSTMENTS ΣΤΗΝ ΕΠΟΜΕΝΗ ΓΡΑΜΜΗ(HEIGHT, WIDTH)!!!
    canvas=Canvas(FrameForScroll, bd=0, height=480, width=1220) 
    canvas.grid(row=0, column=0, columnspan=10, sticky=N+S+E+W)    
    para2=LabelFrame(canvas, bd=0)
    scrollbar = Scrollbar(FrameForScroll, orient="vertical", command=canvas.yview)
    scrollbar.grid(row=0, column=10, sticky=N+S)
    para2.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=para2, anchor="nw", width=1220)
    canvas.configure(yscrollcommand=scrollbar.set)
    title0=Label(para2, text="ΠΑΡΑΠΕΜΠΤΙΚΟ ΣΗΜΕΙΩΜΑ", font=('bold', 13), bg="#d9d9d9", fg="#000080", pady=45, padx=300)
    title0.grid(row=5, column=1, columnspan=7, sticky=W+E)
    image7 = Image.open("parapemptiko1.jpg")
    photo7 = ImageTk.PhotoImage(image7)
    label7 = Label(para2, image = photo7, bd=0)
    label7.image = photo7
    label7.grid(row=5, column=0, pady=25, sticky=E)
    image8 = Image.open("parapemptiko2.jpg")
    photo8 = ImageTk.PhotoImage(image8)
    label8 = Label(para2, image = photo8, bd=0)
    label8.image = photo8
    label8.grid(row=5, column=9, pady=25, sticky=W) 
    keimeno1=Label(para2, text='''Διευκρινίζεται πως συμφώνως με το ΦΕΚ 1336/12-5-2016 « οι απαραίτητες εξετάσεις των προς ένταξη ωφελουμένων και
η αντίστοιχη ιατρική εκτίμηση,πραγματοποιούνται στην οικεία Δομή του ΠΕΔΥ και στα Δημοτικά ιατρεία άμεσα και
κατά προτεραιότητα» . Επίσης, σε περίπτωση εισαγωγής σε νοσoκομείο, κατά την έξοδό τους από αυτό, πρέπει «…να
είναι αυτοεξυπηρετούμενοι με ιατρικά προσδιορισμένο χρόνο oλοκλήρωσης της αποθεραπείας τους…» να αναγράφεται
είτε στο ενημερωτικό σημείωμα είτε σε ιατρική γνωμάτευση, αφού πρώτα έχει ενημερωθεί ο υπεύθυνος της δομής. Σε
περίπτωση εισαγωγής σε ψυχιατρική κλινική, να επισυνάπτεται ιατρική γνωμάτευση, που να πιστοποιεί ότι ο ωφελούμενος :
«δεν έχει έκπτωση της λειτουργικότητας ή διαταραχή της συμπεριφοράς του, λόγω σοβαρής ψυχιατρικής διαταραχής, η
οποία καθιστά αδύνατη την ένταξή του στη δομή.» ΤΗΛΕΦΩΝΑ ΕΠΙΚΟΙΝΩΝΙΑΣ : 210- 4122037 &216-8003076/77.''', justify='left')
    keimeno1.grid(row=15, column=0, columnspan=10, sticky=W+E, pady=15)   
    pros1=Label(para2,  text="ΠΡΟΣ: ")
    pros1.grid(row=20, column=0, pady=5, sticky=E)
    pros2=Entry(para2,width=140, bd=1, relief=SUNKEN)
    pros2.grid(row=20, column=1, columnspan=9, pady=5, sticky=W)
    onomaeponumo1=Label(para2,  text="ΟΝΟΜΑΤΕΠΩΝΥΜΟ: ")
    onomaeponumo1.grid(row=25, column=0, pady=5, sticky=E)
    onomaeponumo2=Entry(para2,width=140, bd=1, relief=SUNKEN)
    onomaeponumo2.grid(row=25, column=1, columnspan=9, pady=5, sticky=W)
    amka1=Label(para2,  text="ΑΜΚΑ: ")
    amka1.grid(row=30, column=0, pady=5, sticky=E)
    amka2=Entry(para2,width=140, bd=1, relief=SUNKEN)
    amka2.grid(row=30, column=1, columnspan=9, pady=5, sticky=W)
    hlikia1=Label(para2,  text="ΗΛΙΚΙΑ: ")
    hlikia1.grid(row=35, column=0, pady=5, sticky=E)
    hlikia2=Entry(para2,width=140, bd=1, relief=SUNKEN)
    hlikia2.grid(row=35, column=1, columnspan=9, pady=5, sticky=W)
    anamnhstiko1=Label(para2,  text="ΑΤΟΜΙΚΟ ΑΝΑΜΝΗΣΤΙΚΟ: ")
    anamnhstiko1.grid(row=40, column=0, pady=5, sticky=E)
    anamnhstiko2=Entry(para2,width=140, bd=1, relief=SUNKEN)
    anamnhstiko2.grid(row=40, column=1, columnspan=9, pady=5, sticky=W)
    varEmvolio=StringVar()
    new_Emvolio1=Label(para2, text="ΕΜΒΟΛΙΑΣΜΟΣ COVID-19: ", pady=15)
    new_Emvolio1.grid(row=45, column=0, sticky=E) #with radio buttons
    new_Emvolio2=Radiobutton(para2, padx=45, text='ΝΑΙ /YES', variable=varEmvolio, value='ΝΑΙ') #command=?
    new_Emvolio2.grid(row=45, column=1,sticky=W+E)
    new_Emvolio2=Radiobutton(para2, padx=45, text='ΟΧΙ /NO', variable=varEmvolio, value='ΟΧΙ') #command=?
    new_Emvolio2.grid(row=45, column=2,sticky=W+E)
    varNosisi=StringVar()
    new_Nosisi1=Label(para2, text="ΝΟΣΗΣΗ COVID-19: ", pady=5) 
    new_Nosisi1.grid(row=45, column=5, sticky=E) #with radio buttons
    new_Nosisi2=Radiobutton(para2, padx=45, text='ΝΑΙ /YES', variable=varNosisi, value='ΝΑΙ') #command=?
    new_Nosisi2.grid(row=45, column=6,sticky=W+E)
    new_Nosisi2=Radiobutton(para2, padx=45, text='ΟΧΙ /NO', variable=varNosisi, value='ΟΧΙ') #command=?
    new_Nosisi2.grid(row=45, column=7,sticky=W+E)     
    new_Farmaka1=Label(para2, text="ΦΑΡΜΑΚΕΥΤΙΚΗ ΑΓΩΓΗ: ", pady=5)
    new_Farmaka1.grid(row=55, column=0, sticky=E) #with radio buttons
    new_Farmaka2=Text(para2, width=105, height=3, pady=5, bd=3, relief=SUNKEN)
    new_Farmaka2.grid(row=55, column=1, columnspan=9, sticky=W) #with radio buttons
    new_Parapompi1=Label(para2, text="ΑΙΤΙΑ ΠΑΡΑΠΟΜΠΗΣ: ", pady=5) 
    new_Parapompi1.grid(row=60, column=0, sticky=E) #with radio buttons
    new_Parapompi2=Text(para2, width=105, height=3, pady=5, bd=3, relief=SUNKEN)
    new_Parapompi2.grid(row=60, column=1, columnspan=9, sticky=W) #with radio buttons
    new_Info1=Label(para2, text="ΚΛΙΝΙΚΕΣ ΠΛΗΡΟΦΟΡΙΕΣ: ", pady=5)
    new_Info1.grid(row=65, column=0, sticky=E) #with radio buttons
    new_Info2=Text(para2, width=105, height=3, pady=5, bd=3, relief=SUNKEN)
    new_Info2.grid(row=65, column=1, columnspan=9, sticky=W) #with radio buttons
    para3=LabelFrame(para2, bd=0)
    para3.grid(row=85, column=0, columnspan=10)    
    new_Iatros1=Label(para3, text="Ο ΙΑΤΡΟΣ/Η ΝΟΣΗΛΕΥΤΡΙΑ ", pady=10) 
    new_Iatros1.grid(row=70, column=9, sticky=W+E) 
    new_Iatros2=Text(para3, width=50, height=1, pady=5, bd=3, relief=SUNKEN)
    new_Iatros2.grid(row=75, column=9, sticky=W)     
    image10 = Image.open("parapemptiko3.jpg")
    photo10 = ImageTk.PhotoImage(image10)
    label10 = Label(para3, image = photo10, bd=0)
    label10.image = photo10
    label10.grid(row=80, column=0, columnspan=10, pady=10, sticky=W+E)
    image11 = Image.open("espaLogo_3.jpg")
    photo11 = ImageTk.PhotoImage(image11)
    label11 = Label(para3, image = photo11, bd=0)
    label11.image = photo11
    label11.grid(row=85, column=0, sticky=W)
    image12 = Image.open("parapemptiko4.jpg")
    photo12 = ImageTk.PhotoImage(image12)
    label12 = Label(para3, image = photo12, bd=0)
    label12.image = photo12
    label12.grid(row=85, column=9, sticky=E)   
    new_Submit=Button(Frame100, text="<<Επιστροφή", fg="#ffffff", bg="#000080", padx=35, pady=11, command=lambda:menu_new(para1))
    new_Submit.grid(row=500, column=4, padx=100, pady=25)
    new_Submit=Button(Frame100, text="Καταχώρηση", fg="#ffffff", bg="#000080", padx=35, pady=11, command=lambda:menu(para1))
    new_Submit.grid(row=500, column=5, padx=100, pady=25)
    

def istoriko(x):
    x.grid_forget()
    global istoriko1
    root.unbind('<Return>')
    istoriko1=LabelFrame(root, bd=0)
    istoriko1.grid(row=5, column=0, columnspan=10, padx=10, pady=15)   
    epilogi1=Button(istoriko1, bg="#000080", fg="white", text="Καταχώρηση ιστορικού", padx=30, pady=10, command=lambda: new_entry(istoriko1))
    epilogi1.grid(row=7, column=1, padx=33, pady=15)
    epilogi2=Button(istoriko1, bg="#000080", fg="white", text="Τροποποίηση ιστορικού", padx=30, pady=10, command=lambda: changePass(2))
    epilogi2.grid(row=7, column=3, padx=33, pady=15)
    epilogi3=Button(istoriko1, bg="#000080", fg="white", text="Αναζήτηση ιστορικού", padx=36, pady=10, command=lambda: changePass(3))
    epilogi3.grid(row=7, column=5, padx=33, pady=15)    
    epilogi9=Button(istoriko1, bg="#000080", fg="white", text="Διαγραφή ιστορικού", padx=39, pady=10, command=lambda:transition(7))
    epilogi9.grid(row=7, column=7, padx=33, pady=15)
    istoriko2=LabelFrame(istoriko1, bd=0)
    istoriko2.grid(row=8, column=0, columnspan=10, padx=10, pady=15)    
    epilogi9=Button(istoriko2, bg="#000080", fg="white", text="Επιστροφή", padx=65, pady=10, command=lambda:menu_new(istoriko1))
    epilogi9.grid(row=8, column=1, padx=33, pady=15)
    epilogi9=Button(istoriko2, bg="#000080", fg="white", text="Κεντρικό μενού", padx=55, pady=10, command=lambda:transition(7))
    epilogi9.grid(row=8, column=4, padx=33, pady=15)
    epilogi9=Button(istoriko2, bg="#000080", fg="white", text="Έξοδος", padx=75, pady=10, command=lambda:transition(7))
    epilogi9.grid(row=8, column=7, padx=33, pady=15)

def new_entry(x):
    x.grid_forget()
    global newEntry
    global kwdikos2
    global hmeromhnia2
    global sumvoulos2
    global paratiriseis2
    global ekthesi2
    global FrameForScroll
    temp=LabelFrame(root, bd=0)
    temp.grid(row=5, column=0, columnspan=10)
    FrameForScroll=LabelFrame(temp, bd=0) #scrollbar attempt!!!
    FrameForScroll.grid(row=5, column=0, columnspan=18)
    #ΝΑ ΕΛΕΓΞΩ ΤΙΣ ΔΙΑΣΤΑΣΕΙΣ ΤΟΥ MONITOR ΓΙΑ ΝΑ ΓΙΟΥΝ ADJUSTMENTS ΣΤΗΝ ΕΠΟΜΕΝΗ ΓΡΑΜΜΗ(HEIGHT, WIDTH)!!!
    canvas=Canvas(FrameForScroll, bd=0, height=420, width=1220) #height=420 -->laptop, 680-->desktop
    canvas.grid(row=0, column=0, columnspan=18, sticky=N+S+E+W)
    newEntry=LabelFrame(canvas, bd=0)
    scrollbar = Scrollbar(FrameForScroll, orient="vertical", command=canvas.yview)
    scrollbar.grid(row=0, column=18, sticky=N+S)
    newEntry.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=newEntry, anchor="nw", width=2000)
    canvas.configure(yscrollcommand=scrollbar.set)
    Frame100=LabelFrame(FrameForScroll, bd=0)
    Frame100.grid(row=500, column=0, columnspan=18) 
    image5 = Image.open("unesco_form_1.jpg")
    photo5 = ImageTk.PhotoImage(image5)
    top_logo = Label(newEntry, image = photo5, bd=0)
    top_logo.image = photo5
    top_logo.grid(row=6, column=0, rowspan=3, sticky=W+S)
    kwdikos1=Label(newEntry, text="ΚΩΔΙΚΟΣ ΩΦΕΛΟΥΜΕΝΟΥ", pady=3)
    kwdikos1.grid(row=6, column=14, sticky=E)
    kwdikos2=Entry(newEntry, width=35, bd=1, relief=SUNKEN)
    kwdikos2.grid(row=6, column=15, sticky=E, pady=3)
    hmeromhnia1=Label(newEntry, text="ΗΜΕΡΟΜΗΝΙΑ", pady=3)
    hmeromhnia1.grid(row=7, column=14, sticky=E)
    hmeromhnia2=Entry(newEntry, width=35, bd=1, relief=SUNKEN)
    hmeromhnia2.grid(row=7, column=15, sticky=E, pady=3)
    sumvoulos1=Label(newEntry, text="ΙΑΤΡΟΣ / ΝΟΣΗΛΕΥΤΗΣ (ΥΠΟΓΡΑΦΗ)", pady=3)
    sumvoulos1.grid(row=8, column=14, sticky=E)
    sumvoulos2=Entry(newEntry, width=35, bd=1, relief=SUNKEN)
    sumvoulos2.grid(row=8, column=15, sticky=E, pady=3)
    blankRow=Label(newEntry, text="", padx=7, pady=5)
    blankRow.grid(row=9, column=0, columnspan=15, sticky=W+E)
    titlos=Label(newEntry, text=" ΦΟΡΜΑ ΚΑΤΑΓΡΑΦΗΣ ΙΑΤΡΙΚΟΥ ΙΣΤΟΡΙΚΟΥ\n\nPERSONAL HEALTH RECORD", font=("bolder", 10), fg="#000080", bg= "#d9d9d9", padx=7, pady=15)
    titlos.grid(row=10, column=0, columnspan=16, sticky=W+E)
    titlos2=Label(newEntry, text="ΚΑΤΑΧΩΡΗΣΗ ΑΣΘΕΝΟΥΣ / PATIENT REGISTRATION", fg="#ffffff", bg="#000080", pady=5, font=("bolder", 10))
    titlos2.grid(row=11, column=0, columnspan=16, sticky=W, pady=5)
    new_Name1=Label(newEntry, text="1. Όνομα / First Name", pady=5)
    new_Name1.grid(row=13, column=0, columnspan=3, sticky=W)
    new_Name2=Entry(newEntry, width=146, bd=1, relief=SUNKEN)
    new_Name2.grid(row=13, column=3, columnspan=13, sticky=W)
    new_Surname1=Label(newEntry, text="2. Επώνυμο / Family Name ", pady=5) 
    new_Surname1.grid(row=14, column=0, columnspan=3, sticky=W)
    new_Surname2=Entry(newEntry, width=146, bd=1, relief=SUNKEN)
    new_Surname2.grid(row=14, column=3, columnspan=13, sticky=W)
    new_Fathername1=Label(newEntry, text="3. Όνομα Πατρός / Father's Name ", pady=5)
    new_Fathername1.grid(row=15, column=0, columnspan=3, sticky=W)
    new_Fathername2=Entry(newEntry, width=146, bd=1, relief=SUNKEN)
    new_Fathername2.grid(row=15, column=3, columnspan=13, sticky=W)
    new_Phone1=Label(newEntry, text="4. Τηλέφωνο ή κινητό / Telephone or Mobile Number ", pady=5) 
    new_Phone1.grid(row=16, column=0, columnspan=3, sticky=W)
    new_Phone2=Entry(newEntry, width=146, bd=1, relief=SUNKEN)
    new_Phone2.grid(row=16, column=3, columnspan=13, sticky=W)
    new_Phone3=Label(newEntry, text="5. Τηλέφωνο ή κινητό αντίκλητου / Telephone\nor Mobile Number of representative", pady=5)
    new_Phone3.grid(row=17, column=0, columnspan=3, sticky=W)
    new_Phone4=Entry(newEntry, width=146, bd=1, relief=SUNKEN)
    new_Phone4.grid(row=17, column=3, columnspan=13, sticky=W)
    new_Amka1=Label(newEntry, text="6. Α.Μ.Κ.Α. ", pady=5)
    new_Amka1.grid(row=18, column=0, columnspan=3, sticky=W)
    new_Amka2=Entry(newEntry, width=146, bd=1, relief=SUNKEN)
    new_Amka2.grid(row=18, column=3, columnspan=13, sticky=W)
    blankRow=Label(newEntry, text="", padx=7, pady=5)
    blankRow.grid(row=19, column=1, columnspan=16, sticky=W+E)
    titlos3=Label(newEntry, text="ΙΑΤΡΙΚΟ ΙΣΤΟΡΙΚΟ / MEDICAL HISTORY ", pady=5, fg="#ffffff", bg="#000080", font=("bolder", 10))
    titlos3.grid(row=20, column=0, columnspan=16, sticky=W, pady=5)
    varSurgical=StringVar()    
    new_Surgical1=Label(newEntry, text="1. Χειρουργικές Επεμβάσεις / Surgical Interventions", pady=5) 
    new_Surgical1.grid(row=21, column=0, columnspan=3, sticky=W) #with radio buttons
    new_Surgical2=Radiobutton(newEntry, padx=45, text='ΝΑΙ /YES', variable=varSurgical, value='ΝΑΙ') #command=?
    new_Surgical2.grid(row=21, column=3,sticky=W)
    new_Surgical3=Radiobutton(newEntry, padx=45, text='ΟΧΙ /NO', variable=varSurgical, value='ΟΧΙ')
    new_Surgical3.grid(row=21, column=6, sticky=W)   
    varHeart=StringVar()
    new_Heart1=Label(newEntry, text="2. Καρδιακό Νόσημα / υψηλή αρτηριακή πίεση /\n Heart disease or high blood pressure", pady=5)
    new_Heart1.grid(row=22, column=0, columnspan=3, sticky=W) #with radio buttons
    new_Heart2=Radiobutton(newEntry, padx=45, text='ΝΑΙ /YES', variable=varHeart, value='ΝΑΙ') #command=?
    new_Heart2.grid(row=22, column=3,sticky=W)
    new_Heart3=Radiobutton(newEntry, padx=45, text='ΟΧΙ /NO', variable=varHeart, value='ΟΧΙ')
    new_Heart3.grid(row=22, column=6, sticky=W)
    varNeuro=StringVar()
    new_Neuro1=Label(newEntry, text="3. Νευρολογική ασθένεια / Neurological disease", pady=5)
    new_Neuro1.grid(row=23, column=0, columnspan=3, sticky=W) #with radio buttons
    new_Neuro2=Radiobutton(newEntry, padx=45, text='ΝΑΙ /YES', variable=varNeuro, value='ΝΑΙ') #command=?
    new_Neuro2.grid(row=23, column=3,sticky=W)
    new_Neuro3=Radiobutton(newEntry, padx=45, text='ΟΧΙ /NO', variable=varNeuro, value='ΟΧΙ')
    new_Neuro3.grid(row=23, column=6, sticky=W)
    varMental=StringVar()
    new_Mental1=Label(newEntry, text="4. Ψυχική ασθένεια / Mental illness/problems", pady=5)
    new_Mental1.grid(row=24, column=0, columnspan=3, sticky=W) #with radio buttons
    new_Mental2=Radiobutton(newEntry, padx=45, text='ΝΑΙ /YES', variable=varMental, value='ΝΑΙ') #command=?
    new_Mental2.grid(row=24, column=3,sticky=W)
    new_Mental3=Radiobutton(newEntry, padx=45, text='ΟΧΙ /NO', variable=varMental, value='ΟΧΙ')
    new_Mental3.grid(row=24, column=6, sticky=W)
    varDrug=StringVar()
    new_Drug1=Label(newEntry, text="5. Χρήση ουσιών / Drug Use", pady=5) 
    new_Drug1.grid(row=25, column=0, columnspan=3, sticky=W) #with radio buttons
    new_Drug2=Radiobutton(newEntry, padx=45, text='ΝΑΙ /YES', variable=varDrug, value='ΝΑΙ') #command=?
    new_Drug2.grid(row=25, column=3,sticky=W)
    new_Drug3=Radiobutton(newEntry, padx=45, text='ΟΧΙ /NO', variable=varDrug, value='ΟΧΙ')
    new_Drug3.grid(row=25, column=6, sticky=W)
    varLiver=StringVar()
    new_Liver1=Label(newEntry, text="6. Ηπατική η νεφρική νόσος / Liver or Kidney disease", pady=5)
    new_Liver1.grid(row=26, column=0, columnspan=3, sticky=W) #with radio buttons
    new_Liver2=Radiobutton(newEntry, padx=45, text='ΝΑΙ /YES', variable=varLiver, value='ΝΑΙ') #command=?
    new_Liver2.grid(row=26, column=3,sticky=W)
    new_Liver3=Radiobutton(newEntry, padx=45, text='ΟΧΙ /NO', variable=varLiver, value='ΟΧΙ')
    new_Liver3.grid(row=26, column=6, sticky=W)
    varDiabetes=StringVar()
    new_Diabetes1=Label(newEntry, text="7. Διαβήτης ή άλλη ενδοκρινική διαταραχή /\n Diabetes or other endocrine disorder", pady=5)
    new_Diabetes1.grid(row=27, column=0, columnspan=3, sticky=W) #with radio buttons
    new_Diabetes2=Radiobutton(newEntry, padx=45, text='ΝΑΙ /YES', variable=varDiabetes, value='ΝΑΙ') #command=?
    new_Diabetes2.grid(row=27, column=3,sticky=W)
    new_Diabetes3=Radiobutton(newEntry, padx=45, text='ΟΧΙ /NO', variable=varDiabetes, value='ΟΧΙ')
    new_Diabetes3.grid(row=27, column=6, sticky=W)
    varHematologic=StringVar()
    new_Hematologic1=Label(newEntry, text="8. Αιματολογική νόσος / Hematologic disease", pady=5)
    new_Hematologic1.grid(row=28, column=0, columnspan=3, sticky=W) #with radio buttons
    new_Hematologic2=Radiobutton(newEntry, padx=45, text='ΝΑΙ /YES', variable=varHematologic, value='ΝΑΙ') #command=?
    new_Hematologic2.grid(row=28, column=3,sticky=W)
    new_Hematologic3=Radiobutton(newEntry, padx=45, text='ΟΧΙ /NO', variable=varHematologic, value='ΟΧΙ')
    new_Hematologic3.grid(row=28, column=6, sticky=W)
    varTuberculosis=StringVar()
    new_Tuberculosis1=Label(newEntry, text="9. Φυματίωση / Tuberculosis (lung/πνευμονική)", pady=5)
    new_Tuberculosis1.grid(row=29, column=0, columnspan=3, sticky=W) #with radio buttons
    new_Tuberculosis2=Radiobutton(newEntry, padx=45, text='ΝΑΙ /YES', variable=varTuberculosis, value='ΝΑΙ') #command=?
    new_Tuberculosis2.grid(row=29, column=3,sticky=W)
    new_Tuberculosis3=Radiobutton(newEntry, padx=45, text='ΟΧΙ /NO', variable=varTuberculosis, value='ΟΧΙ')
    new_Tuberculosis3.grid(row=29, column=6, sticky=W)    
    varWeight=StringVar()
    new_Weight1=Label(newEntry, text="10. Άλλο νόσημα του αναπνευστικού συστήματος /\n Other lung disease", pady=5)
    new_Weight1.grid(row=30, column=0, columnspan=3, sticky=W) #with radio buttons
    new_Weight2=Radiobutton(newEntry, padx=45, text='ΝΑΙ /YES', variable=varWeight, value='ΝΑΙ') #command=?
    new_Weight2.grid(row=30, column=3,sticky=W)
    new_Weight3=Radiobutton(newEntry, padx=45, text='ΟΧΙ /NO', variable=varWeight, value='ΟΧΙ')
    new_Weight3.grid(row=30, column=6, sticky=W)
    varSexual=StringVar()
    new_Sexual1=Label(newEntry, text="11. Σημαντική απώλεια βάρους (κατά τους \nπροηγούμενους έξι μήνες) /\n Significant weight loss (in the past 6 months)", pady=5)
    new_Sexual1.grid(row=31, column=0, columnspan=3, sticky=W) #with radio buttons
    new_Sexual2=Radiobutton(newEntry, padx=45, text='ΝΑΙ /YES', variable=varSexual, value='ΝΑΙ') #command=?
    new_Sexual2.grid(row=31, column=3,sticky=W)
    new_Sexual3=Radiobutton(newEntry, padx=45, text='ΟΧΙ /NO', variable=varSexual, value='ΟΧΙ')
    new_Sexual3.grid(row=31, column=6, sticky=W)
    varSexual=StringVar()
    new_Sexual1=Label(newEntry, text="12. Σεξουαλικώς μεταδιδόμενα νοσήματα / \nSexually transmitted infections", pady=5) 
    new_Sexual1.grid(row=32, column=0, columnspan=3, sticky=W) #with radio buttons
    new_Sexual2=Radiobutton(newEntry, padx=45, text='ΝΑΙ /YES', variable=varSexual, value='ΝΑΙ') #command=?
    new_Sexual2.grid(row=32, column=3,sticky=W)
    new_Sexual3=Radiobutton(newEntry, padx=45, text='ΟΧΙ /NO', variable=varSexual, value='ΟΧΙ')
    new_Sexual3.grid(row=32, column=6, sticky=W)
    varTorture=StringVar()
    new_Torture1=Label(newEntry, text="13. Ιστορικό βασανισμών, βίας / History of torture, violence", pady=5)
    new_Torture1.grid(row=33, column=0, columnspan=3, sticky=W) #with radio buttons
    new_Torture2=Radiobutton(newEntry, padx=45, text='ΝΑΙ /YES', variable=varTorture, value='ΝΑΙ') #command=?
    new_Torture2.grid(row=33, column=3,sticky=W)
    new_Torture3=Radiobutton(newEntry, padx=45, text='ΟΧΙ /NO', variable=varTorture, value='ΟΧΙ')
    new_Torture3.grid(row=33, column=6, sticky=W)
    varSkin=StringVar()
    new_Skin1=Label(newEntry, text="14. Δερματικές παθήσεις (π.χ. εξάνθημα) \n/ Skin condition (e.g. rash)", pady=5)
    new_Skin1.grid(row=34, column=0, columnspan=3, sticky=W) #with radio buttons
    new_Skin2=Radiobutton(newEntry, padx=45, text='ΝΑΙ /YES', variable=varSkin, value='ΝΑΙ') #command=?
    new_Skin2.grid(row=34, column=3,sticky=W)
    new_Skin3=Radiobutton(newEntry, padx=45, text='ΟΧΙ /NO', variable=varSkin, value='ΟΧΙ')
    new_Skin3.grid(row=34, column=6, sticky=W)
    newEntry2=LabelFrame(newEntry, bd=0)
    newEntry2.grid(row=35, column=0, columnspan=16, sticky=W+E)                   
    new_Medication1=Label(newEntry2, text="15. Τρέχουσα φαρμακευτική αγωγή (να προσδιοριστεί          \n/ Current medications (specify)    ", pady=5)
    new_Medication1.grid(row=37, column=0, columnspan=3, sticky=W)
    new_MedicTitle2=Label(newEntry2, text="ΦΑΡΜΑΚΟ", pady=5, fg="#ffffff", bg="#000080")
    new_MedicTitle2.grid(row=36, column=4, columnspan=3, sticky=W+E)
    new_MedicTitle3=Label(newEntry2, text="ΠΡΩΙ", pady=5, fg="#ffffff", bg="#000080")
    new_MedicTitle3.grid(row=36, column=7, columnspan=3, sticky=W+E)
    new_MedicTitle4=Label(newEntry2, text="ΜΕΣΗΜΕΡΙ", pady=5, fg="#ffffff", bg="#000080")
    new_MedicTitle4.grid(row=36, column=10, columnspan=3, sticky=W+E)
    new_MedicTitle5=Label(newEntry2, text="ΒΡΑΔΙ", pady=5, fg="#ffffff", bg="#000080")
    new_MedicTitle5.grid(row=36, column=13, columnspan=3, sticky=W+E)
    new_Medication2=Text(newEntry2, width=50, bd=3, relief=SUNKEN, height=5)
    new_Medication2.grid(row=37, column=4, columnspan=3, pady=5, sticky=W)    
    new_Medication3=Text(newEntry2, width=19, bd=3, relief=SUNKEN, height=5)
    new_Medication3.grid(row=37, column=7, columnspan=3, pady=5, sticky=W)
    new_Medication4=Text(newEntry2, width=19, bd=3, relief=SUNKEN, height=5)
    new_Medication4.grid(row=37, column=10, columnspan=3, pady=5, sticky=W)
    new_Medication5=Text(newEntry2, width=19, bd=3, relief=SUNKEN, height=5)
    new_Medication5.grid(row=37, column=13, columnspan=3, pady=5, sticky=W)    
    varAllergy=StringVar()
    new_Allergy1=Label(newEntry, text="16. Αλλεργίες (συμπ. αλλεργιών σε φάρμακα) / Allergies", pady=5) 
    new_Allergy1.grid(row=360, column=0, columnspan=3, sticky=W) #with radio buttons
    new_Allergy2=Radiobutton(newEntry, padx=45, text='ΝΑΙ /YES', variable=varAllergy, value='ΝΑΙ') #command=?
    new_Allergy2.grid(row=360, column=3,sticky=W)
    new_Allergy3=Radiobutton(newEntry, padx=45, text='ΟΧΙ /NO', variable=varAllergy, value='ΟΧΙ')
    new_Allergy3.grid(row=360, column=6, sticky=W)
    varSmoking=StringVar()
    new_Smoking1=Label(newEntry, text="17. Κάπνισμα / Smoking", pady=5)
    new_Smoking1.grid(row=370, column=0, columnspan=3, sticky=W) #with radio buttons
    new_Smoking2=Radiobutton(newEntry, padx=45, text='ΝΑΙ /YES', variable=varSmoking, value='ΝΑΙ') #command=?
    new_Smoking2.grid(row=370, column=3,sticky=W)
    new_Smoking3=Radiobutton(newEntry, padx=45, text='ΟΧΙ /NO', variable=varSmoking, value='ΟΧΙ')
    new_Smoking3.grid(row=370, column=6, sticky=W)
    varAlcohol=StringVar()
    new_Alcohol1=Label(newEntry, text="18. Αλκοόλ / Alcohol", pady=5)
    new_Alcohol1.grid(row=380, column=0, columnspan=3, sticky=W) #with radio buttons
    new_Alcohol2=Radiobutton(newEntry, padx=45, text='ΝΑΙ /YES', variable=varAlcohol, value='ΝΑΙ') #command=?
    new_Alcohol2.grid(row=380, column=3,sticky=W)
    new_Alcohol3=Radiobutton(newEntry, padx=45, text='ΟΧΙ /NO', variable=varAlcohol, value='ΟΧΙ')
    new_Alcohol3.grid(row=380, column=6, sticky=W)
    new_Pregnant1=Label(newEntry, text="19. Εγκυμοσύνες (αριθμός) / Pregnancies (number)", pady=5)
    new_Pregnant1.grid(row=390, column=0, columnspan=3, sticky=W) #with radio buttons
    new_Pregnant2=Text(newEntry, width=20, bd=3, relief=SUNKEN, height=1)
    new_Pregnant2.grid(row=390, column=3, columnspan=13, pady=5, sticky=W)    
    varCurrent=StringVar()
    new_Current1=Label(newEntry, text="20 Τρέχουσα εγκυμοσύνη / Current Pregnancy", pady=5)
    new_Current1.grid(row=400, column=0, columnspan=3, sticky=W) #with radio buttons
    new_Current2=Radiobutton(newEntry, padx=45, text='ΝΑΙ /YES', variable=varCurrent, value='ΝΑΙ') #command=?
    new_Current2.grid(row=400, column=3,sticky=W)
    new_Current3=Radiobutton(newEntry, padx=45, text='ΟΧΙ /NO', variable=varCurrent, value='ΟΧΙ')
    new_Current3.grid(row=400, column=6, sticky=W)     
    titlos4=Label(newEntry, text="ΚΛΙΝΙΚΗ ΕΚΤΙΜΗΣΗ / EXAM FINDINGS ", pady=5, fg="#ffffff", bg="#000080", font=("bolder", 10))
    titlos4.grid(row=410, column=0, columnspan=16, sticky=W, pady=5)
    titlos5=Label(newEntry, text="ΣΥΣΤΗΜΑ / SYSTEM\t\t\t           ", font=("bolder", 10))
    titlos5.grid(row=420, column=0, columnspan=3, sticky=W)
    titlos6=Label(newEntry, text="ΕΥΡΗΜΑΤΑ / FINDINGS", font=("bolder", 10))
    titlos6.grid(row=420, column=3, columnspan=13, sticky=W+E)
    titlos5.config(bg="#d9d9d9")
    titlos6.config(bg="#d9d9d9")
    new_Respiratory1=Label(newEntry, text="Αναπνευστικό / Respiratory", pady=5)
    new_Respiratory1.grid(row=430, column=0, columnspan=3, sticky=W) #with radio buttons
    new_Respiratory2=Text(newEntry, width=110, bd=3, relief=SUNKEN, height=5)
    new_Respiratory2.grid(row=430, column=3, columnspan=13, pady=5, sticky=W)
    new_Gastro1=Label(newEntry, text="ΓΕΣ / Gastrointestinal", pady=5)
    new_Gastro1.grid(row=440, column=0, columnspan=3, sticky=W) #with radio buttons
    new_Gastro2=Text(newEntry, width=110, bd=3, relief=SUNKEN, height=5)
    new_Gastro2.grid(row=440, column=3, columnspan=13, pady=5, sticky=W)
    new_Circulatory1=Label(newEntry, text="Κυκλοφορικό / Circulatory", pady=5)
    new_Circulatory1.grid(row=450, column=0, columnspan=3, sticky=W) #with radio buttons
    new_Circulatory2=Text(newEntry, width=110, bd=3, relief=SUNKEN, height=5)
    new_Circulatory2.grid(row=450, column=3, columnspan=13, pady=5, sticky=W)
    new_Genital1=Label(newEntry, text="Ουροποιογεννητικό / Genitourinary", pady=5)#padx=7, 
    new_Genital1.grid(row=460, column=0, columnspan=3, sticky=W) #with radio buttons
    new_Genital2=Text(newEntry, width=110, bd=3, relief=SUNKEN, height=5)
    new_Genital2.grid(row=460, column=3, columnspan=13, pady=5, sticky=W)
    new_Nervous1=Label(newEntry, text="Νευρολογικό / Nervous System", pady=5)
    new_Nervous1.grid(row=460, column=0, columnspan=3, sticky=W) #with radio buttons
    new_Nervous2=Text(newEntry, width=110, bd=3, relief=SUNKEN, height=5)
    new_Nervous2.grid(row=460, column=3, columnspan=13, pady=5, sticky=W)    
    titlos7=Label(newEntry, text="ΕΡΓΑΣΤΗΡΙΑΚΕΣ / ΑΛΛΕΣ ΕΞΕΤΑΣΕΙΣ / LABORATORY TESTS ", pady=5, fg="#ffffff", bg="#000080", font=("bolder", 10))
    titlos7.grid(row=470, column=0, columnspan=16, sticky=W, pady=5)
    titlos8=Label(newEntry, text="ΕΞΕΤΑΣΗ / ΤΕΣΤ / ΜΕΘΟΔΟΣ / TEST\t           ", font=("bolder", 10))
    titlos8.grid(row=480, column=0, columnspan=3, sticky=W)
    titlos9=Label(newEntry, text="ΑΠΟΤΕΛΕΣΜΑΤΑ / RESULTS", font=("bolder", 10))
    titlos9.grid(row=480, column=3, columnspan=13, sticky=W+E)
    titlos8.config(bg="#d9d9d9")
    titlos9.config(bg="#d9d9d9")
    new_PregTest1=Label(newEntry, text="1. Τεστ εγκυμοσύνης / Pregnancy Test", pady=5)
    new_PregTest1.grid(row=490, column=0, columnspan=3, sticky=W) #with radio buttons
    new_PregTest2=Text(newEntry, width=110, bd=3, relief=SUNKEN, height=5)
    new_PregTest2.grid(row=490, column=3, columnspan=13, pady=5, sticky=W)
    new_Mantoux1=Label(newEntry, text="2. Τεστ Mantoux / Mantoux Test", pady=5)
    new_Mantoux1.grid(row=500, column=0, columnspan=3, sticky=W) #with radio buttons
    new_Mantoux2=Text(newEntry, width=110, bd=3, relief=SUNKEN, height=5)
    new_Mantoux2.grid(row=500, column=3, columnspan=13, pady=5, sticky=W)
    new_Malaria1=Label(newEntry, text="3. Γρήγορο Τεστ ελονοσίας / Malaria Rapid Test", pady=5) 
    new_Malaria1.grid(row=510, column=0, columnspan=3, sticky=W) #with radio buttons
    new_Malaria2=Text(newEntry, width=110, bd=3, relief=SUNKEN, height=5)
    new_Malaria2.grid(row=510, column=3, columnspan=13, pady=5, sticky=W)
    new_Urine1=Label(newEntry, text="4. Ανάλυση ούρων / Urinanalysis", pady=5)
    new_Urine1.grid(row=520, column=0, columnspan=3, sticky=W) #with radio buttons
    new_Urine2=Text(newEntry, width=110, bd=3, relief=SUNKEN, height=5)
    new_Urine2.grid(row=520, column=3, columnspan=13, pady=5, sticky=W)
    new_Urine1=Label(newEntry, text="5. Γενική αίματος / Blood Test", pady=5)
    new_Urine1.grid(row=530, column=0, columnspan=3, sticky=W) #with radio buttons
    new_Urine2=Text(newEntry, width=110, bd=3, relief=SUNKEN, height=5)
    new_Urine2.grid(row=530, column=3, columnspan=13, pady=5, sticky=W)
    new_HBsAg1=Label(newEntry, text="6. Εργαστηριακή Εξέταση για HBsAg / Laboratory: HBsAg", pady=5)
    new_HBsAg1.grid(row=540, column=0, columnspan=3, sticky=W) #with radio buttons
    new_HBsAg2=Text(newEntry, width=110, bd=3, relief=SUNKEN, height=5)
    new_HBsAg2.grid(row=540, column=3, columnspan=13, pady=5, sticky=W)
    new_HCV1=Label(newEntry, text="7. Εργαστηριακή Εξέταση για HCV / Laboratory: HCV", pady=5)
    new_HCV1.grid(row=550, column=0, columnspan=3, sticky=W) #with radio buttons
    new_HCV2=Text(newEntry, width=110, bd=3, relief=SUNKEN, height=5)
    new_HCV2.grid(row=550, column=3, columnspan=13, pady=5, sticky=W)
    new_HIV1=Label(newEntry, text="8. Εργαστηριακή Εξέταση για HIV / Laboratory: HIV", pady=5)
    new_HIV1.grid(row=560, column=0, columnspan=3, sticky=W) #with radio buttons
    new_HIV2=Text(newEntry, width=110, bd=3, relief=SUNKEN, height=5)
    new_HIV2.grid(row=560, column=3, columnspan=13, pady=5, sticky=W)
    new_Syphilis1=Label(newEntry, text="9. Εργαστηριακή Εξέταση για Σύφιλη \n/ Laboratory: Syphilis, VDRL", pady=5)
    new_Syphilis1.grid(row=570, column=0, columnspan=3, sticky=W) #with radio buttons
    new_Syphilis2=Text(newEntry, width=110, bd=3, relief=SUNKEN, height=5)
    new_Syphilis2.grid(row=570, column=3, columnspan=13, pady=5, sticky=W)
    new_Teberculosis1=Label(newEntry, text="10. Φυματίωση (επίχρισμα πτυέλων, κ/α) \n/ Laboratory: Teberculosis (sputum smear/culture)", pady=5)
    new_Teberculosis1.grid(row=580, column=0, columnspan=3, sticky=W) #with radio buttons
    new_Teberculosis2=Text(newEntry, width=110, bd=3, relief=SUNKEN, height=5)
    new_Teberculosis2.grid(row=580, column=3, columnspan=13, pady=5, sticky=W)        
    titlos10=Label(newEntry, text="ΘΕΡΑΠΕΥΤΙΚΗ ΑΓΩΓΗ / Treatment ", pady=5, fg="#ffffff", bg="#000080", font=("bolder", 10))
    titlos10.grid(row=590, column=0, columnspan=16, sticky=W, pady=5)
    therapeia=Text(newEntry, width=150, bd=3, relief=SUNKEN, height=5)
    therapeia.grid(row=600, column=0, columnspan=16, pady=5, sticky=W)
    new_Therapy1=Label(newEntry, text="Χορήγηση Θεραπείας (αιτία, δοσολογία, διαρκεια \nχορηγούμενης αγωγής \n/ Therapy (cause, dosage, duration of the prescribed \ntreatment)", pady=5)#padx=7, 
    new_Therapy1.grid(row=610, column=0, columnspan=3, sticky=W) #with radio buttons
    new_Therapy2=Text(newEntry, width=110, bd=3, relief=SUNKEN, height=5)
    new_Therapy2.grid(row=610, column=3, columnspan=13, pady=5, sticky=W)
    new_Referral1=Label(newEntry, text="Παραπομπή / Medical referral", pady=5)
    new_Referral1.grid(row=620, column=0, columnspan=3, sticky=W) #with radio buttons
    new_Referral2=Text(newEntry, width=110, bd=3, relief=SUNKEN, height=5)
    new_Referral2.grid(row=620, column=3, columnspan=13, pady=5, sticky=W)
    titlos11=Label(newEntry, text="ΕΝΗΜΕΡΩΤΙΚΟ ΣΗΜΕΙΩΜΑ", pady=5, fg="#ffffff", bg="#000080", font=("bolder", 10))
    titlos11.grid(row=630, column=0, columnspan=16, sticky=W+E, pady=5)
    notes=Text(newEntry, width=151, bd=3, relief=SUNKEN, height=15)
    notes.grid(row=640, column=0, columnspan=16, pady=5, sticky=W)    
    titlos12=Label(newEntry, text="ΕΚΚΡΕΜΟΤΗΤΕΣ ΑΣΘΕΝΗ", pady=5, fg="#ffffff", bg="#000080", font=("bolder", 10))
    titlos12.grid(row=650, column=0, columnspan=16, sticky=W+E, pady=5)
    titlos15=Label(newEntry, text="ΕΞΕΤΑΣΗ / ΡΑΝΤΕΒΟΥ", font=("bolder", 10), bg="#d9d9d9")
    titlos15.grid(row=660, column=0, columnspan=2, sticky=W+E)
    titlos16=Label(newEntry, text="ΠΡΑΓΜΑΤΟΠΟΙΗΘΗΚΕ", font=("bolder", 10), bg="#d9d9d9")
    titlos16.grid(row=660, column=2, columnspan=2, sticky=W+E)
    titlos17=Label(newEntry, text="ΠΑΡΑΤΗΡΗΣΕΙΣ", font=("bolder", 10), bg="#d9d9d9")
    titlos17.grid(row=660, column=4, columnspan=12, sticky=W+E)     
    for i in range(12):
        randevou=Text(newEntry, width=10, bd=3, relief=SUNKEN, height=2)
        randevou.grid(row=670+i, column=0, columnspan=2, pady=5, sticky=W+E)
        varDone=StringVar()
        new_Done2=Radiobutton(newEntry, padx=45, text='ΝΑΙ /YES', variable=varDone, value='ΝΑΙ') #command=?
        new_Done2.grid(row=670+i, column=2, sticky=W)
        new_Done3=Radiobutton(newEntry, padx=45, text='ΟΧΙ /NO', variable=varDone, value='ΟΧΙ')
        new_Done3.grid(row=670+i, column=3, sticky=W)
        new_notes=Text(newEntry, width=90, bd=3, relief=SUNKEN, height=2)
        new_notes.grid(row=670+i, column=4, columnspan=12, pady=5, sticky=W)        
    titlos13=Label(newEntry, text="Ο Ιατρός της Δομής\n\n(Ονοματεπώνυμο)", font=("bolder", 10))
    titlos13.grid(row=800, column=0, columnspan=3, sticky=W+E)
    titlos14=Label(newEntry, text="Ο/Η νοσηλευτής/ρια\n\n(Ονοματεπώνυμο)", font=("bolder", 10))
    titlos14.grid(row=800, column=13, columnspan=3, sticky=W+E)
    docName=Text(newEntry, width=40, bd=3, relief=SUNKEN, height=1)
    docName.grid(row=810, column=0, columnspan=3, pady=5, sticky=W+E)
    nurseName=Text(newEntry, width=40, bd=3, relief=SUNKEN, height=1)
    nurseName.grid(row=810, column=14, columnspan=2, pady=5, sticky=W+E)
    backMemo=Button(Frame100, text="<<Επιστροφή", padx=30, pady=11, fg="#ffffff", bg="#000080", command=lambda: istoriko(temp)) 
    backMemo.grid(row=1000, column=3, pady=15, padx=80)       
    saveAs=Button(Frame100, text="Αποθήκευση", padx=33, pady=11, fg="#ffffff", bg="#000080", command=lambda: goto(125)) 
    saveAs.grid(row=1000, column=8, pady=15, padx=80)
    returnMenu=Button(Frame100, text="Κεντρικό μενου", padx=27, pady=11, fg="#ffffff", bg="#000080", command=lambda: menu_new(temp))
    returnMenu.grid(row=1000, column=13, pady=15, padx=80) 
    image6 = Image.open("unesco_form_2.jpg")
    photo6 = ImageTk.PhotoImage(image6)
    bottom_logo = Label(Frame100, image = photo6, bd=0)
    bottom_logo.image = photo6
    bottom_logo.grid(row=1100, column=8, columnspan=2)    


main()

#Να φτιάξω τα σωστά ονόματα αρχείων για το update() (αντίγραφα ασφαλείας).
#ΔΟΥΛΕΥΩ ΜΕΣΑ ΣΤΗΝ def diagramma(), θέλω να βρω τρόπο να κάνω rowspan στην πρώτη στήλη ή να χρησιμοποιήσω την function που έχω ηδη βρει ώστε όταν γίνεται πέρασμα από το χρήστη, να
#αντιγράφεται η τιμή στα 2 επόμενα κελιά (κάθετα).
