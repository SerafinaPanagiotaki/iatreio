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
    root.title("Όμιλος για την Unesco Πειραιώς και Νήσων - Πρόγραμμα παρακολούθησης ιατρικών ραντεβού - ΡΑΝΤΕΒΟΥ v.3.02.5 (Υφιστάμενη δομή)") #Υφιστάμενη δομή
    #root.title("Όμιλος για την Unesco Πειραιώς και Νήσων - Πρόγραμμα παρακολούθησης ιατρικών ραντεβού - ΡΑΝΤΕΒΟΥ v.3.02.5  (Νέα δομή)")    #Νέα δομή
    label00= Label(mainFrame, bg="#000080", fg="#ffffff", padx=10, pady=0, text="Όμιλος για την Unesco Πειραιώς και Νήσων", font=('bold', 18), bd=40)
    label00.grid(row=0, column=2, columnspan=7, sticky=W+E, pady=0)
    my_img0=ImageTk.PhotoImage(Image.open("doctor2.jpg"))
    my_label=Label(mainFrame, image=my_img0)#, bg="#000080")
    my_label.grid(row=1, padx=0, column=3, sticky=E)
    label01= Label(mainFrame, fg="#000080", text="ΡΑΝΤΕΒΟΥ", font=('bold', 40))#bg="#000080", 
    label01.grid(row=1, column=4, columnspan=3, sticky=W)
    label02= Label(mainFrame, fg="#000080", text="Πρόγραμμα παρακολούθησης ιατρικών ραντεβού", font=('bold', 14))#, bd=7)bg="#000080", 
    label02.grid(row=2, column=0, columnspan=10, sticky=N)    
    label= Label(mainFrame, fg="#000080", padx=511, pady=5, text="ΡΑΝΤΕΒΟΥ v.3.02.5  - powered by Python v.3.10.5")#bg="#000080", 
    label.grid(row=3, column=0, columnspan=10, sticky=N, pady=0)   
    root.bind('<Escape>', lambda event: root.destroy())
    root.bind('<F11>', lambda event: exec('ΙΑΤΡΕΙΟ.py'))
    root.bind('<Return>', lambda event: logIn())
    messagebox.showinfo('Ενημέρωση:', 'Καλωσήρθατε στο "ΡΑΝΤΕΒΟΥ"!\n\nΠιέστε "OK" για να μεταβείτε στο κεντρικό μενού')
    menu()
    root.mainloop()    

def fire(): #μήνυμα στοιχείων επικοινωνίας για service.
    messagebox.showinfo('Service - Πληροφορίες επικοινωνίας:', 'Programmer / Developer: Shery Panagiotaki\n\nContact info:\n\nTel.: (+30) 6976929404\n\nE-mail: sherypanagiotaki@yahoo.com,\n             sherypamagiotaki@gmail.com')
    
'''def greetings(): #μήνυμα τερματισμού του προγ/τος (το πρόγραμμα σε αυτό το σημείο είναι ανενεργό αλλά το παράθυρό του (root()) κλείνει ΜΟΝΟ με κλικ στο κουμπί "Κλείσιμο παράθυρου")
    global finish
    wait(.2)
    firstFrame.grid_forget()
    exitFrame=LabelFrame(root, bd=0)
    exitFrame.grid(row=4, column=0, columnspan=10)
    label4= Label(exitFrame, fg="#000080", text="Ευχαριστούμε πολύ που χρησιμοποιήσατε την εφαρμογή!\n\nProgrammed, designed and developed by Shery Panagiotaki, @copyright 2022\n\n\nContact info:\n\nTel.: (+30) 6976929404\n\nE-mail: sherypanagiotaki@yahoo.com,\n", bd=0)
    label4.grid(row=50, column=0, columnspan=10, pady=40)
    finish=Button(exitFrame, text="Κλείσιμο παράθυρου", padx=30, pady=11, fg="#ffffff", bg="#000080", command=lambda: root.destroy()) #κουμπί που κλείνει το παράθυρο του προγ/τος
    finish.grid(row=60, column=6, padx=45)
    info=Button(exitFrame, fg="#ffffff", bg="#000080", text="Contact Service", padx=37, pady=11, command=fire)    
    info.grid(row=60, column=7, padx=45)'''




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




        
    
def wait(s): #'παγώνει' το πρόγραμμα κατά (s) δευτερόλεπτα
    time.sleep(s)

def menu():#Κεντρικό μενού
    wait(0)
    global mainMenu   
    mainMenu=LabelFrame(root, padx=5, pady=10, bd=0)
    mainMenu.grid(row=5, column=0, columnspan=10, padx=10, pady=15)                           
    epilogi4=Button(mainMenu, bg="#000080", fg="white", text="Καταχώρηση ραντεβού", padx=30, pady=10, command=lambda: insert(mainMenu, 1))
    epilogi4.grid(row=6, column=1, padx=33, pady=15)
    epilogi5=Button(mainMenu, bg="#000080", fg="white", text="Διόρθωση ραντεβού", padx=39, pady=10, command=lambda: insert(mainMenu, 2))
    epilogi5.grid(row=6, column=3, padx=33, pady=15)
    epilogi6=Button(mainMenu, bg="#000080", fg="white", text="Ακύρωση ραντεβού", padx=40, pady=10, command=lambda: insert(mainMenu, 3))
    epilogi6.grid(row=6, column=5, padx=33, pady=15)                               
    epilogi7=Button(mainMenu, bg="#000080", fg="white", text="Αναζήτηση ραντεβού", padx=37, pady=10, command=lambda: insert(mainMenu, 7))
    epilogi7.grid(row=6, column=7, padx=33, pady=15)
    epilogi1=Button(mainMenu, bg="#000080", fg="white", text="Προσθήκη Λογαριασμού", padx=28, pady=10, command=lambda: changePass(1))
    epilogi1.grid(row=7, column=1, padx=33, pady=15)
    epilogi2=Button(mainMenu, bg="#000080", fg="white", text="Κατάργηση Λογαριασμού", padx=26, pady=10, command=lambda: changePass(2))
    epilogi2.grid(row=7, column=3, padx=33, pady=15)
    epilogi3=Button(mainMenu, bg="#000080", fg="white", text="Αλλαγή Λογαριασμού", padx=36, pady=10, command=lambda: changePass(3))
    epilogi3.grid(row=7, column=5, padx=33, pady=15)    
    epilogi9=Button(mainMenu, bg="#000080", fg="white", text="Έξοδος", padx=74, pady=10, command=lambda:greetings(mainMenu))
    epilogi9.grid(row=7, column=7, padx=33, pady=15)
    mainMenu2=LabelFrame(mainMenu, bd=0)
    mainMenu2.grid(row=20, column=0, columnspan=10, pady=50)
    other=Label(mainMenu2, text="ΑΛΛΑ ΔΙΑΘΕΣΙΜΑ ΠΡΟΓΡΑΜΜΑΤΑ: ", bg="#000080", fg="#ffffff", pady=10, font=('bold', 12))
    other.grid(row=20, column=0, columnspan=10)#, sticky=W+E)
    image5 = Image.open("istoriko.jpg")#ή "shery_pic_3.jpg"
    photo5 = ImageTk.PhotoImage(image5)
    label5 = Button(mainMenu2, image = photo5, command=lambda: exec('ΙΣΤΟΡΙΚΟ_v.1.02.py'))
    label5.image = photo5
    label5.grid(row=25, column=6, pady=25)#, padx=100)
    #epilogi10=Button(temp, bg="#000080", fg="white", text='Μετάβαση στο πρόγραμμα:\n\n"ΙΣΤΟΡΙΚΟ"', padx=20, pady=10, command=lambda:exec('ΙΣΤΟΡΙΚΟ_v.1.02.py'))
    #epilogi10.grid(row=8, column=0, columnspan=10, pady=60)

def exec(x):
    root.destroy()
    os.system(x)    
    
def logIn(): #Είσοδος στο πρόγραμμα
    global checkLogin
    global miss
    firstFrame.grid_forget()
    checkLogin=[]
    checkIn=[]
    miss=0
    if false>0:       
        Frame11.grid_forget()    
    with open("password.csv", "r", newline="", encoding="utf-8") as file:
        ro=csv.reader(file, delimiter='$')
        for row in ro:
            checkLogin.append(row)
        if len(checkLogin)==0:
            errorMessage=Label(root, text="Παρακαλώ πολύ επικοινωνήστε με την προγραμματίστρια, κωδικός σφάλματος: EMPTY_PASSWORD_0", pady=15, fg="#000080")
            errorMessage.grid(row=5, column=0, columnspan=7)
            wait(5)
            epilogi9=Button(root, bg="#000080", fg="white", text="Έξοδος", padx=74, pady=10, command=root.destroy)
            epilogi9.grid(row=7, column=3, pady=15)             
        else:
            global verify 
            global enterUsername2
            global enterPassword2
            global submit
            verify=LabelFrame(root, pady=10, bd=0)
            verify.grid(row=5, column=0, columnspan=10, padx=5, pady=20)
            enterUsername1=Label(verify, text="Username: ", pady=15, fg="#000080")
            enterUsername1.grid(row=6, column=4)
            enterUsername2=Entry(verify, width=50, bg= "#d9d9d9", fg="#000080", borderwidth=5)
            enterUsername2.grid(row=6, column=5)
            enterPassword1=Label(verify, text="Password: ", pady=15, fg="#000080")
            enterPassword1.grid(row=7, column=4)
            enterPassword2=Entry(verify, width=50, bg= "#d9d9d9", fg="#000080", borderwidth=5)
            enterPassword2.grid(row=7, column=5)                           
            submit=Button(verify, text="Υποβολή", padx=45, pady=10, bg="#000080", fg="white", command=lambda: checkMiss(miss, checkLogin)) 
            submit.grid(row=8, column=0, columnspan=9, pady=15)                                                                               
            choice2=enterUsername2.get()
            choice2=choice2.strip()
            choice3=enterPassword2.get()
            choice3=choice3.strip()
    root.bind('<Return>', lambda event: checkMiss(miss, checkLogin))            
            
def checkMiss(miss, checkLogin): #βοηθητική function της logIn(), παίρνει 2 παραμέτρους, miss--> αρ. αποτυχημένων προσπαθειών και checkLogin--> λίστα με κωδικούς εισόδου                              
    choice2=enterUsername2.get()
    choice2=choice2.strip()
    choice3=enterPassword2.get()
    choice3=choice3.strip()
    checkIn=[choice2.upper(), choice3.upper()]
    global counter #δείκτης --> πριν την είσοδο στο πρόγραμμα και πριν εκυπωθεί για πρώτη φορά η αρχική οθόνη εχει τιμή 0. Για όλες τις άλλες φορές που επιστρέφουμε στην αρχική
    counter=0      #οθόνη παίρνει τιμή 1, για να μην τυπωθεί το μήνυμα της επιτυχημένης εισόδου μετά από κωδικό.
    for x in checkLogin:
        if checkIn==x:
            verify.grid_forget()
            #gotoMenu.grid_forget()
            show()
            break
        elif x==checkLogin[-1]: #τρεις προσπάθειες εισόδου αλλιώς τερματισμός του προγ/τος.            
            verify.grid_forget()
            submit.grid_forget()
            global Frame11
            global false  
            Frame11=LabelFrame(root, bd=0)
            Frame11.grid(row=4, column=0, columnspan=18)
            if false==2:
                strikeThree=Label(Frame11, pady=35, text="Λανθασμένοι κωδικοί χρήστη, το πρόγραμμα τερματίστηκε.\n\n\nProgrammed, designed and developed by Shery Panagiotaki, @copyright 2022", fg="#000080")
                strikeThree.grid(row=10, column=0, columnspan=18)
                tryAgain=Button(Frame11, text="Κλείσιμο παραθύρου", bg="#000080", fg="white", padx=30, pady=11, command=lambda: root.destroy()) #κλείσιμο παραθύρου
                tryAgain.grid(row=60, column=8)
            else:               
                false=false+1
                miss=false
                verify.grid_forget()
                if false==2:
                    tries="Απομένει μία προσπάθεια."
                else:
                    tries="Απομένουν δύο προσπάθειες."
                strikeThree=Label(Frame11, pady=35, text="Λανθασμένοι κωδικοί χρήστη, η είσοδος στο πρόγραμμα δεν επιτράπηκε.\n\n"+tries, fg="#000080")
                strikeThree.grid(row=10, column=0, columnspan=18)
                tryAgain=Button(Frame11, text="Επανάληψη", padx=30, pady=11, command=logIn, bg="#000080", fg="white") 
                tryAgain.grid(row=60, column=8, padx=35)
                finish=Button(Frame11, text="Έξοδος", padx=30, pady=11, command=greetings, bg="#000080", fg="white",) 
                finish.grid(row=60, column=9, padx=35)
                root.bind('<Return>', lambda event: logIn())    

def show(): #Αναζήτηση των ραντεβού της ημέρας (τρέχουσα ημ/νία)
    wait(0)
    global counter
    if not counter==1:
        messagebox.showinfo('Ενημέρωση:', 'Σωστοί κωδικοί, η είσοδος πραγματοποιήθηκε με επιτυχία.')    
    global showFrame
    global today
    global before
    global x
    global z
    global bottomFrame
    copyPrevious=[]
    backupPrevious=[]
    copyCurrent=[]
    backupCurrent=[]
    with open("current.csv", "r", newline="", encoding="utf-8") as file:
        temp=[]
        today=[]
        after=[]
        before=[]
        ro=csv.reader(file, delimiter='$')
        for row in sorted(ro, key=lambda j:j[6]): #ταξινόμηση με βάση την ημερομηνία
            temp.append(row)
        x = str(datetime.date.today())  #current date
        x=x.split('-')
        x="".join(x)                    #current date as one string!
        for y in temp:
            if x == y[6]:
                today.append(y)
                after.append(y)           
            elif y[6]>x:
                after.append(y)
            else:
                before.append(y)
        z=datetime.datetime.now()
        showFrame=LabelFrame(root, padx=5, pady=10, bd=0)
        showFrame.grid(row=4, column=0, columnspan=10)
        bottomFrame=LabelFrame(showFrame, bd=0)
        bottomFrame.grid(row=102, column=0, columnspan=10)        
        root.unbind('<Return>')
        '''if x[-2:]in ['1', '15', '30']: #--> ενημέρωση αντιγράφων ασφαλείας ('current.csv', 'previous.csv') κάθε 1η, 15η, και 30η του μήνα αυτήν την στιγμή.
            global message
            with open("previous.csv", "r", encoding="utf-8", newline="") as file:
                ro=csv.reader(file, delimiter='$')
                for i in ro:
                    copyPrevious.append(i)
                with open("..\\..\\backup_previous.csv", "r", encoding="utf-8", newline="") as file:
                    ro=csv.reader(file, delimiter='$')
                    for i in ro:
                        backupPrevious.append(i)
                    if not backupPrevious==copyPrevious:
                        for i in copyPrevious:
                            if not i in backupPrevious:
                                backupPrevious.append(i)
                        with open("..\\..\\backup_previous.csv", "w", encoding="utf-8", newline="") as file:
                            wo=csv.writer(file, delimiter='$')
                            for i in backupPrevious:
                                wo.writerow(i)                    
            with open("current.csv", "r", encoding="utf-8", newline="") as file:
                ro=csv.reader(file, delimiter='$')
                for i in ro:
                    copyCurrent.append(i)                  
                with open("..\\..\\backup_current.csv", "r", encoding="utf-8", newline="") as file:
                    ro=csv.reader(file, delimiter='$')
                    for i in ro:
                        backupCurrent.append(i)
                    if not backupCurrent==copyCurrent:
                        backupCurrent.clear()
                        for i in copyCurrent:
                            backupCurrent.append(i)
                    with open("..\\..\\backup_current.csv", "w", encoding="utf-8", newline="") as file:
                        wo=csv.writer(file, delimiter='$')
                        for i in backupCurrent:
                            wo.writerow(i)
            message="Αυτόματη ενημέρωση αντιγράφων ασφαλείας: επιτυχής."
            messagebox.showinfo('Ενημέρωση:', message)
        else:
            message="Δεν έγινε αυτόματη ενημέρωση των αντιγράφων ασφαλείας."
            messagebox.showwarning('Σημαντικό:', message)'''      
        if len(today)==0:
            message="Δεν υπάρχουν προγραμματισμένα ιατρικά ραντεβού εξυπηρετούμενων για σήμερα."
            messagebox.showwarning('Σημαντικό:', message) 
        else:           
            if len(today)==1:
                resultToday=Label(showFrame, fg="#000080", text="\nΒρέθηκε "+ str(len(today))+" ιατρικό ραντεβού εξυπηρετούμενου για σήμερα ("+ z.strftime("%d - %m - %Y")+").")
                resultToday.grid(row=90, column=5, padx=65)#, columnspan=10)
            else:
                resultToday=Label(showFrame, fg="#000080", text="\nΒρέθηκαν συνολικά "+ str(len(today))+" ιατρικά ραντεβού εξυπηρετούμενων για σήμερα ("+ z.strftime("%d - %m - %Y")+").")
                resultToday.grid(row=90, column=5, padx=65)#, columnspan=10)
            showToday=Button(showFrame, text="Εμφάνιση", padx=60, pady=11, bg="#000080", fg="#ffffff", command=lambda: ektyposi(showFrame, today))
            showToday.grid(row=90, column=9)
        if len(before)>0:
            question=Label(showFrame, fg="#000080", pady=20, text="Υπάρχουν επίσης "+str(len(before))+" εγγραφές από προηγούμενα ιατρικά ραντεβού που δεν έχετε παρακολουθήσει.")
            question.grid(row=101, column=0, columnspan=10)            
            previous=Button(bottomFrame, padx=20, pady=11, bg="#000080", fg="#ffffff", text="<< Προηγούμενα ραντεβού", command=lambda: ektyposi(showFrame, before))
            previous.grid(row=102, column=4, pady=100, padx=65)
            enterMenu=Button(bottomFrame, text="Κεντρικό Μενού >>", padx=43, pady=11, bg="#000080", fg="#ffffff", command=lambda: transition(2))
            enterMenu.grid(row=102, column=5, pady=100, padx=65)
        else:
            enterMenu=Button(bottomFrame, text="Κεντρικό Μενού", padx=43, pady=11, bg="#000080", fg="#ffffff", command=lambda: transition(2))
            enterMenu.grid(row=102, column=0, columnspan=10, pady=100)            
    with open("current.csv", "w", newline="", encoding="utf-8") as file:
        wo=csv.writer(file, delimiter='$')
        for i in after:
            wo.writerow(i)
    with open("previous.csv", "a", newline="", encoding="utf-8") as file:
        wo=csv.writer(file, delimiter='$')
        for i in before:
            wo.writerow(i)

def transition(x): #συνάρτηση πολλαπλών εφαρμογών (τη χρησιμοποιώ για μεταβάσεις από μία οθόνη σε άλλη και για εκτέλεση lambda function()
    global beforeFrame
    global previousFrame
    global returnMenu
    
    global text1
    if x==1: #Αναζήτηση προηγούμενων ραντεβού που δεν τα έχουμε παρακολουθήσει (από την show())
        showFrame.grid_forget()       
        previousFrame=LabelFrame(root, pady=10, fg="#000080", bd=0)
        previousFrame.grid(row=100, column=0, columnspan=10)        
        ektyposi(previousFrame, before)        
        if len(before)==1:
            text1="Βρέθηκε "+ str(len(before))+" προγραμματισμένο ιατρικό ραντεβού εξυπηρετούμενου πριν από: "+ z.strftime("%d - %m - %Y")+", το οποίο μεταφέρθηκε ήδη στο αρχείο."          
        else:
            text1="\nΒρέθηκαν συνολικά "+ str(len(before))+" προγραμματισμένα ιατρικά ραντεβού εξυπηρετούμενων πριν από: "+ z.strftime("%d - %m - %Y")+", τα οποία μεταφέρθηκαν ήδη στο αρχείο."
        messagebox.showinfo('Ενημέρωση:', text1)
        '''enterMenu=Button(previousFrame, text="Κεντρικό Μενού", padx=35, pady=11, bg="#000080", fg="#ffffff", command=lambda: transition(3))
        enterMenu.grid(row=102, column=3, pady=15)
        exitSystem=Button(previousFrame, text="Έξοδος", padx=59, pady=11, bg="#000080", fg="white", command=lambda: transition(4))
        exitSystem.grid(row=102, column=6, pady=15)'''    
    elif x==2: #επιστροφή στο κεντρικό μενού (από την show())
        showFrame.grid_forget()
        menu()
    elif x==3: #επιστροφή στο κεντρικό μενού (από την show(), αλλά ΑΠΟ ΑΛΛΟ της ΣΗΜΕΙΟ)
        FrameForScroll.grid_forget()
        #global k
        #k.grid_forget()
        menu()
    elif x==4: #έξοδος προγ/τος (μέσω της show())
        k.grid_forget() 
        greetings()
        '''elif x==5: #εκτύπωση μηνύματος επιτυχίας (από checkMiss()) και αναμονή για είσοδο του χρήστη στο κεντρικό μενού
        global gotoMenu
        verify.grid_forget()
        gotoMenu=LabelFrame(root, fg="#000080", bd=0)
        gotoMenu.grid(row=4, column=0, columnspan=10)
        success=Label(gotoMenu, text="Σωστός κωδικός, είσοδος στο σύστημα...", fg="#000080", pady=15, padx=5, bd=0)
        success.grid(row=4, column=0)
        toMenu=Button(gotoMenu, text="Είσοδος", padx=35, pady=11, bg="#000080", fg="#ffffff", command=lambda: transition(6))
        toMenu.grid(row=5, column=0, pady=15)
        elif x==6: #είσοδος στο κεντρικό μενού (ανακατεύθυνση από την προηγούμενη συνθήκη για το x (--> if x==5...)
        gotoMenu.grid_forget()
        show()'''
    elif x==7: #τερματισμός του προγ/τος από το κεντρικό μενού
        mainMenu.grid_forget()
        greetings()
    elif x==8: #Νέα προσθήκη (ΕΠΑΝΑΛΗΨΗ ΜΕΤΑ ΑΠΟ ΑΠΟΤΥΧΗΜΕΝΗ ΕΓΓΡΑΦΗ, ΔΙΑΦΟΡΕΤΙΚΗ FUNCTION ΑΠΟ ΤΗΝ ΝΕΑ ΠΡΟΣΘΗΚΗ ΜΕΤΑ ΑΠΟ ΕΠΙΤΥΧΗΜΕΝΗ ΕΓΓΡΑΦΗ (--> if x==14)
        global verifyNew
        global changes2
        changes2.grid_forget()
        newUsername2.delete(0, END)
        newPassword2.delete(0, END)
        changePass(1)
    elif x==9: #επιστροφή στο κύριο μενού μετά από επιτυχημένη προσθήκη λογ/μού χρήστη 
        changes2.grid_forget()
        menu()
    elif x==10: #Οριστική διαγραφή χρήστη
        global failDelete2
        global erase
        global changes5
        delName=delUsername2.get()
        delPwd=delPassword2.get()
        delName=delName.strip()
        delPwd=delPwd.strip()
        erase=[delName.upper(),delPwd.upper()]
        verifyDel.grid_forget()
        changes.grid_forget()
        if erase not in eraseList:
            message="Δεν υπάρχει Λογαριασμός χρήστη με τα συγκεκριμένα στοιχεία, η ενέργεια απέτυχε."                   
        else:         
            i=0
            while i<len(eraseList):
                if erase==eraseList[i]:
                    eraseList.remove(eraseList[i])
                    i=0
                else:
                    i=i+1
            with open("password.csv", "w", newline="", encoding="utf-8") as file:
                global successDel
                wo=csv.writer(file, delimiter='$')
                for x in eraseList:
                    wo.writerow(x)
                message="Ο Λογαριασμός χρήστη διαγράφηκε με επιτυχία."
        changes5=LabelFrame(root, bd=0)
        changes5.grid(row=4, column=0, columnspan=10)
        successDel=Label(changes5, text=message, fg="#000080", pady=15)
        successDel.grid(row=101, column=0, columnspan=10)
        newDelete=Button(changes5, fg="#ffffff", bg="#000080", text="Νέα διαγραφή", padx=30, pady=11, command=lambda: transition(11))
        newDelete.grid(row=102, column=4, pady=15, padx=20)                    
        returnMenu=Button(changes5, fg="#ffffff", bg="#000080", text="Κεντρικό Μενού", padx=30, pady=11, command=lambda: transition(20))
        returnMenu.grid(row=102, column=5, pady=15, padx=20)
    elif x==11: #Νέα διαγραφή χρήστη (ΑΝΕΞΑΡΤΗΤΑ αν η προηγούμενη διαγραφή ήταν επιτυχημένη, καλύπτει ΚΑΙ ΤΙΣ ΔΥΟ περιπτώσεις)
        changes5.grid_forget()
        erase.clear()
        changePass(2)
    elif x==12: #Αλλαγή λογ/μού χρήστη (username/password) -->ΜΟΝΟ για την πρώτη φορά, για τις επόμενες x==13
        global newEntry2
        global newEntry3
        global newChange
        global failChange
        global oldEntry
        global newName2
        global newPwd2
        global newUsername4
        global newPassword4
        global newUsername6
        global newPassword6
        global newUsername3
        global newPassword3
        global newUsername5
        global newPassword5
        global validChange
        global changes4
        verifyOld.grid_forget()
        newEntry2=[]
        newEntry3=[]        
        oldName=oldUsername2.get()
        oldPwd=oldPassword2.get()
        oldName=oldName.strip()
        oldPwd=oldPwd.strip()
        oldEntry=[oldName.upper(),oldPwd.upper()]
        changes3.grid_forget()
        changes4=LabelFrame(root, bd=0)
        changes4.grid(row=4, column=0, columnspan=10)
        if oldEntry not in changeList:
            failChange=Label(changes4, text="Δε βρέθηκε Λογαριασμός χρήστη με τα συγκεκριμένα στοιχεία (Username/Password), η ενέργεια ακυρώθηκε.", fg="#000080", pady=15)
            failChange.grid(row=20, column=0, columnspan=10)
            newChange=Button(changes4, bg="#000080", fg="#ffffff", text="Νέα αλλαγή", padx=30, pady=11, command=lambda: transition(18))
            newChange.grid(row=100, column=4, pady=15, padx=20)                    
            returnMenu=Button(changes4, bg="#000080", fg="#ffffff", text="Κεντρικό Μενού", padx=30, pady=11, command=lambda: transition(19))
            returnMenu.grid(row=100, column=5, pady=15, padx=20)           
        else:
            #changes3.grid_forget()
            newUsername3=Label(changes4, text="Εισάγετε νέο Username:", fg="#000080", pady=10)
            newUsername3.grid(row=7, column=3, columnspan=2)
            newUsername4=Entry(changes4, width=50, bg= "#d9d9d9", fg="#000080")
            newUsername4.grid(row=7, column=5, columnspan=10, pady=10)   
            newPassword3=Label(changes4, text="Εισάγετε νέο Password:", fg="#000080", pady=10)
            newPassword3.grid(row=8, column=3, columnspan=2)
            newPassword4=Entry(changes4, width=50, bg= "#d9d9d9", fg="#000080")
            newPassword4.grid(row=8, column=5, columnspan=10, pady=10)
            validChange=Label(changes4, text="Επαλήθευση νέων στοιχείων:", fg="#000080", pady=10)
            validChange.grid(row=9, column=0, columnspan=10)
            newUsername5=Label(changes4, text="Εισάγετε ξανά το νέο Username:", fg="#000080", pady=10)
            newUsername5.grid(row=10, column=3, columnspan=2)
            newUsername6=Entry(changes4, width=50, bg= "#d9d9d9", fg="#000080")
            newUsername6.grid(row=10, column=5, columnspan=10, pady=10)   
            newPassword5=Label(changes4, text="Εισάγετε ξανά το νέο Password:", fg="#000080", pady=10)
            newPassword5.grid(row=11, column=3, columnspan=2)
            newPassword6=Entry(changes4, width=50, bg= "#d9d9d9", fg="#000080")
            newPassword6.grid(row=11, column=5, columnspan=10, pady=10)            
            verifyNew=Button(changes4, bg="#000080", fg="#ffffff", text="Υποβολή", padx=30, pady=11, command=lambda: transition(16))
            verifyNew.grid(row=100, column=0, pady=15, padx=20, columnspan=10)            
    elif x==13: #ΝΕΑ αλλαγή λογ/μού (ΔΙΑΦΟΡΕΤΙΚΗ από την αμέσως προηγούμενη λειτουργία (--> if x==12...), αυτή καθαρίζει τα πεδία αλλαγής λογ/μού από πριν
        global failChange2
        oldUsername2.delete(0, END)
        oldPassword2.delete(0, END)
        failChange.grid_forget()
        changePass(3)
    elif x==14: #Νέα προσθήκη λογ/μού χρήστη
        global done
        global newEntry
        done.grid_forget()
        newUserEntry.grid_forget()
        returnMenu.grid_forget()
        newEntry.clear()
        changePass(1)
    elif x==15: #έλεγχος υποβολής στοιχείων για εισαγωγή νέου χρήστη για ΠΡΩΤΗ ΦΟΡΑ ΜΟΝΟ
        newName=newUsername2.get()
        newPwd=newPassword2.get()
        newName=newName.strip()
        newPwd=newPwd.strip()  
        newEntry=[newName.upper(),newPwd.upper()]
        changes.grid_forget()
        changes2=LabelFrame(root, bd=0)
        changes2.grid(row=4, column=0, columnspan=10)         
        if len(newName)!=0 and len(newPwd)!=0:           
            with open("password.csv", "r", newline="", encoding="utf-8") as file:
                wo=csv.reader(file, delimiter='$')
                for row in wo:
                    passList.append(row)
                if newEntry in passList:
                    message2="Ο συγκεκριμένος Λογαριασμός χρήστη υπάρχει ήδη, η ενέργεια προσθήκης απέτυχε."
                else:
                    passList.append(newEntry)
                    with open("password.csv", "w", newline="", encoding="utf-8") as file:
                        wo=csv.writer(file, delimiter='$')
                        for x in passList:
                            wo.writerow(x)
                        message2="Τα στοιχεία του νέου χρήστη (Username/Password) καταχωρήθηκαν και ο νέος Λογαριασμός δημιουργήθηκε με επιτυχία."                       
        else:
            message2="Δεν πρέπει να υπάρχει κενό πεδίο (Username/Password), η ενέργεια ακυρώθηκε."
        newUserEntry=Button(changes2, fg="#ffffff", bg="#000080", text="Νέα προσθήκη", padx=30, pady=11, command=lambda: transition(22))
        newUserEntry.grid(row=101, column=3, pady=15, padx=20)
        returnMenu=Button(changes2, fg="#ffffff", bg="#000080", text="Κεντρικό Μενού", padx=30, pady=11, command=lambda: transition(9))
        returnMenu.grid(row=101, column=5, pady=15, padx=20)            
        done=Label(changes2, text=message2, fg="#000080", pady=15)
        done.grid(row=8, column=0, columnspan=10)
    elif x==16: #εκτέλεση ελέγχου (από lambda function()) αν η αλλαγή στοιχείων χρήστη είναι επιτυχής ή όχι
        global successChange
        newName2=newUsername4.get()
        newPwd2=newPassword4.get()
        newName2=newName2.strip()
        newPwd2=newPwd2.strip()
        newName3=newUsername6.get()
        newPwd3=newPassword6.get()
        newName3=newName3.strip()
        newPwd3=newPwd3.strip()                       
        newEntry2=[newName2.upper(),newPwd2.upper()]
        newEntry3=[newName3.upper(),newPwd3.upper()]
        verifyNew.grid_forget()
        if newEntry2[0] == newEntry3[0] and newEntry2[1]==newEntry3[1]:
            for k in changeList:
                if oldEntry==k:
                    k[0]=newName2.upper()
                    k[1]=newPwd2.upper()
            with open("password.csv", "w", newline="", encoding="utf-8") as file:
                wo=csv.writer(file, delimiter='$')
                for row in changeList:
                    wo.writerow(row)
            message="Η αλλαγή στοιχείων στον Λογαριασμό χρήστη πραγματοποιήθηκε με επιτυχία."                           
        else:
            message="Δεν συμφωνούν τα νέα στοιχεία (Username/Password) με αυτά της επαλήθευσης, η ενέργεια ακυρώθηκε."
        successChange=Label(changes4, text=message, fg="#000080", pady=15)
        successChange.grid(row=50, column=0, columnspan=10)            
        newChange=Button(changes4, bg="#000080", fg="#ffffff", text="Νέα αλλαγή", padx=30, pady=11, command=lambda: transition(17)) 
        newChange.grid(row=100, column=4, pady=15, padx=20)                    
        returnMenu=Button(changes4, bg="#000080", fg="#ffffff", text="Κεντρικό Μενού", padx=30, pady=11, command=lambda: transition(9)) 
        returnMenu.grid(row=100, column=5, pady=15, padx=20)
    elif x==17: #ΝΕΑ αλλαγή λογ/μού 
        changes4.grid_forget()
        changePass(3)
    elif x==18: #ΝΕΑ αλλαγή λογ/μού 
        changes4.grid_forget()
        changePass(3)
    elif x==19: #επιστροφή στο κεντρικό μενού μετά από αλλαγή λογ/μού  
        changes4.grid_forget()
        changes3.grid_forget()
        menu()  
    elif x==20: #επιστροφή στο κύριο μενού μετά από οριστική διαγραφή λογ/μού χρήστη (ΜΟΝΟ την ΠΡΩΤΗ φορά)
        changes5.grid_forget()
        erase.clear()
        menu()
    elif x==21: #νέα αλλαγή λογ/μού μετά από επιτυχημένη αλλαγή λογ/μού
        changes4.grid_forget()
        newUsername2.delete(0, END)
        newPassword2.delete(0, END)
        changePass(3)        
    elif x==22: #νέα προσθήκη λογ/μού μετά από επιτυχημένη προσθήκη λογ/μού
        changes2.grid_forget()
        changePass(1)
    elif x==23: #επιστροφή στο κεντρικό μενού μετά από αλλαγή λογ/μού (από ΑΛΛΗ ενέργεια)
        changes4.grid_forget()
        changes3.grid_forget()
        menu()
    elif x==24: #επιστροφή στην αρχική οθόνη μετά από την εκτύπωση των ραντεβού της τρέχουσας ημέρας.
        FrameForScroll.grid_forget()
        global counter
        counter=1
        show()
                
def ektyposi(x, y): #εκτυπώσεις (παίρνει 2 παραμέτρους: x-->το Frame μέσα στο οποίο θα γίνουν οι εκτυπώσεις και y-->η λίστα που θα εκτυπωθεί)
    global status
    global k
    global FrameForScroll
    FrameForScroll=LabelFrame(root, bd=0) #scrollbar attempt!!!
    FrameForScroll.grid(row=5, column=0, columnspan=18)
    Frame100=LabelFrame(FrameForScroll, bd=0)
    Frame100.grid(row=500, column=0, columnspan=18)
    if x==showFrame:
        returnMenu=Button(Frame100, text="<<Επιστροφή", padx=40, pady=11, bg="#000080", fg="#ffffff", command=lambda: transition(24))    
    k=x
    k.grid_forget()    
    #ΝΑ ΕΛΕΓΞΩ ΤΙΣ ΔΙΑΣΤΑΣΕΙΣ ΤΟΥ MONITOR ΓΙΑ ΝΑ ΓΙΟΥΝ ADJUSTMENTS ΣΤΗΝ ΕΠΟΜΕΝΗ ΓΡΑΜΜΗ(HEIGHT, WIDTH)!!!
    canvas=Canvas(FrameForScroll, bd=0, height=480, width=1220) 
    canvas.grid(row=0, column=0, columnspan=18, sticky=N+S+E+W)
    x=LabelFrame(canvas, bd=0)
    scrollbar = Scrollbar(FrameForScroll, orient="vertical", command=canvas.yview)
    scrollbar.grid(row=0, column=18, sticky=N+S)
    x.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=x, anchor="nw", width=2000)
    canvas.configure(yscrollcommand=scrollbar.set)
 
    if y==before:
        previousLabel=Label(x, pady=15, bg="#d9d9d9", fg="#000080", text="ΠΡΟΓΡΑΜΜΑΤΙΣΜΕΝΑ ΗΜΕΡΗΣΙΑ ΙΑΤΡΙΚΑ ΡΑΝΤΕΒΟΥ ΕΞΥΠΗΡΕΤΟΥΜΕΝΩΝ - ΗΜΕΡΟΜΗΝΙΑ: Πριν από: "+z.strftime("%d - %m - %Y"))              
        previousLabel.grid(row=4, column=0, columnspan=10, sticky=W+E)
    elif y==today:
        #showFrame.grid_forget()
        title=Label(x, pady=15, bg= "#d9d9d9", fg="#000080", text="ΠΡΟΓΡΑΜΜΑΤΙΣΜΕΝΑ ΗΜΕΡΗΣΙΑ ΙΑΤΡΙΚΑ ΡΑΝΤΕΒΟΥ ΕΞΥΠΗΡΕΤΟΥΜΕΝΩΝ - ΗΜΕΡΟΜΗΝΙΑ:  "+str(z.strftime("%d - %m - %Y")))
        title.grid(row=4, column=0, columnspan=10, pady=10, sticky=W+E)         
    aaPrint=Label(x, fg="#000080", text="Α/Α", padx=5, pady=5)
    aaPrint.grid(row=5, column=0, sticky=W)
    amkaPrint=Label(x, fg="#000080", text="ΑΜΚΑ", padx=5, pady=5)
    amkaPrint.grid(row=5, column=1, sticky=W)
    surnamePrint=Label(x, fg="#000080", text="ΕΠΩΝΥΜΟ", padx=5, pady=5)
    surnamePrint.grid(row=5, column=2, sticky=W)
    namePrint=Label(x, fg="#000080", text="ΟΝΟΜΑ", padx=5, pady=5)
    namePrint.grid(row=5, column=3, sticky=W)
    akhaPrint=Label(x, fg="#000080", text="ΚΩΔ. ΑΚΗΑ", padx=5, pady=5)
    akhaPrint.grid(row=5, column=4, sticky=W)    
    iatreioPrint=Label(x, fg="#000080", text="ΙΑΤΡΕΙΟ", padx=5, pady=5)
    iatreioPrint.grid(row=5, column=5, sticky=W)
    priorityPrint=Label(x, fg="#000080", text="ΠΡΟΤΕΡΑΙΟΤΗΤΑ", padx=5, pady=5)
    priorityPrint.grid(row=5, column=6, sticky=W)
    datePrint=Label(x, fg="#000080", text="ΗΜ/ΝΙΑ ΡΑΝΤΕΒΟΥ", padx=5, pady=5)
    datePrint.grid(row=5, column=7, sticky=W)
    timePrint=Label(x, fg="#000080", text="ΩΡΑ ΡΑΝΤΕΒΟΥ", padx=5, pady=5)
    timePrint.grid(row=5, column=8, sticky=W)
    notesPrint=Label(x, fg="#000080", text="ΠΑΡΑΤΗΡΗΣΕΙΣ", padx=5, pady=5)
    notesPrint.grid(row=5, column=9, sticky=W)

    returnMenu.grid(row=102, column=4, pady=40, padx=65)
    enterMenu=Button(Frame100, text="Κεντρικό Μενού", padx=35, pady=11, bg="#000080", fg="#ffffff", command=lambda: transition(3))
    enterMenu.grid(row=102, column=5, pady=40, padx=65)    
    exitSystem=Button(Frame100, text="Έξοδος", padx=59, pady=11, bg="#000080", fg="white", command=lambda: transition(4))
    exitSystem.grid(row=102, column=6, pady=40, padx=65)     
    i=0
    while i<len(y):
        aaTotal=Label(x, fg="#000080", padx=5, pady=5, text=str(i+1))
        aaTotal.grid(row=7+2*i, column=0, sticky=W)
        amkaTotal=Label(x, fg="#000080", padx=5, pady=5, text=str(y[i][0]))
        amkaTotal.grid(row=7+2*i, column=1, sticky=W)  
        surnameTotal=Label(x, fg="#000080", padx=5, pady=5, text=str(y[i][1]))
        surnameTotal.grid(row=7+2*i, column=2, sticky=W)
        nameTotal=Label(x, fg="#000080", padx=5, pady=5, text=str(y[i][2]))
        nameTotal.grid(row=7+2*i, column=3, sticky=W)
        akhaTotal=Label(x, fg="#000080", padx=5, pady=5, text=str(y[i][3]))
        akhaTotal.grid(row=7+2*i, column=4, sticky=W)        
        iatreioTotal=Label(x, fg="#000080", padx=5, pady=5, text=str(y[i][4]))
        iatreioTotal.grid(row=7+2*i, column=5, sticky=W)                
        priorityTotal=Label(x, fg="#000080", padx=5, pady=5, text=str(y[i][5]))
        priorityTotal.grid(row=7+2*i, column=6, sticky=W)                
        dateTotal=Label(x, fg="#000080", padx=5, pady=5, text=y[i][6][6:]+"-"+str(y[i][6][4:6])+"-"+str(y[i][6][:4]))
        dateTotal.grid(row=7+2*i, column=7, sticky=W)                
        timeTotal=Label(x, fg="#000080", padx=5, pady=5, text=str(y[i][7]))
        timeTotal.grid(row=7+2*i, column=8, sticky=W)                
        notesTotal=Label(x, fg="#000080", padx=5, pady=5, text=str(y[i][8]))
        notesTotal.grid(row=7+2*i, column=9, sticky=W)
        #blank=Label(x, text="", pady=5, bg= "#d9d9d9")
        #blank.grid(row=8+2*i, column=0, columnspan=10, sticky=W+E)
        i=i+1    

def insert(y, x): #παίρνει δύο μεταβλητές, y--> frame που καταργείται και x--> ενέργεια που έχει επιλεχθεί από τον χρήστη.
    global add
    global errorFlag
    global addAmka2
    global amka
    global appointment
    global addSurname2
    global addName2
    global surname
    global addName2
    global name
    global addHospital2
    global addPriority2
    global addDate2
    global addTime2
    global addNotes2
    global addFrame1
    global addFrame2
    global submit2
    global check
    global alter
    global fixFrame1
    global fixAmka2
    global fixFrame
    global newList
    global deleteList
    global delete
    appointment=[]
    contents=[]
    newEntry=[]    
    check=[]
    alter=[]
    newList=[]
    delete=[]
    deleteList=[]
    checkLogin=[]
    if x==1: #ΔΕΝ έχει κληθεί ακόμα η checkAmka(), είναι πρώτη εισαγωγή στοιχείων
        errorFlag=1
        y.grid_forget()     
        add=LabelFrame(root, bd=0)
        add.grid(row=4, column=0, columnspan=10)
        addFrame1=LabelFrame(add, bd=0) #το frame που περιλαμβάνει το πεδίο ΑΜΚΑ μόνο
        addFrame1.grid(row=4, column=0, columnspan=10)
        kataxorisi=Label(addFrame1, text="Καταχώρηση ραντεβού", fg="#000080", pady=25)
        kataxorisi.grid(row=4, column=0, columnspan=10)
        addAmka1=Label(addFrame1, text="ΑΜΚΑ εξυπηρετούμενου:", fg="#000080")
        addAmka1.grid(row=5, column=4, pady=15)
        addAmka2=Entry(addFrame1, width=50, fg="#000080", bg="#d9d9d9", borderwidth=5)
        addAmka2.grid(row=5, column=5, pady=15)
        addAmka3=Button(addFrame1, text="Έλεγχος ΑΜΚΑ", pady=11, fg="#ffffff", bg="#000080", command=lambda: checkAmka(1))
        addAmka3.grid(row=5, column=6, padx=15, pady=15)    
    elif x==2: #Διόρθωση ραντεβού, ΔΕΝ έχει κληθεί ακόμα η checkAmka(), είναι πρώτη εισαγωγή στοιχείων
        y.grid_forget()
        global fixFrame1
        global surnameSearch2
        global cardSearch2
        global amkaSearch2
        global afmSearch2
        global akhaSearch2
        global update1Search2
        global update2Search2
        global activeSearch2        
        fixFrame1=LabelFrame(root, bd=0)  #το frame που περιλαμβάνει το πεδίο ΑΜΚΑ μόνο
        fixFrame1.grid(row=4, column=0, columnspan=10)
        '''diorthosi=Label(fixFrame1, text="Διόρθωση ραντεβού", fg="#000080", pady=15)
        diorthosi.grid(row=0, column=0, columnspan=10)      
        fixAmka1=Label(fixFrame1, text="ΑΜΚΑ εξυπηρετούμενου:", fg="#000080")
        fixAmka1.grid(row=5, column=4, pady=15)
        fixAmka2=Entry(fixFrame1, width=50, fg="#000080", bg="#d9d9d9", borderwidth=5)
        fixAmka2.grid(row=5, column=5, pady=15)
        fixAmka3=Button(fixFrame1, text="Έλεγχος ΑΜΚΑ", pady=11, fg="#ffffff", bg="#000080", padx=30, command=lambda: checkAmka(2))  
        fixAmka3.grid(row=5, column=6, padx=15, pady=15)'''
        surnameSearch1=Label(fixFrame1, fg="#000080", text="ΕΠΩΝΥΜΟ:", padx=15, pady=20)
        surnameSearch1.grid(row=8, column=4, sticky=E)
        surnameSearch2=Entry(fixFrame1, width=50, relief=SUNKEN, borderwidth=5)
        surnameSearch2.grid(row=8, column=5)      
        amkaSearch1=Label(fixFrame1, fg="#000080", text="ΑΜΚΑ:", padx=15, pady=20)
        amkaSearch1.grid(row=10, column=4, sticky=E)
        amkaSearch2=Entry(fixFrame1, width=50, relief=SUNKEN, borderwidth=5)
        amkaSearch2.grid(row=10, column=5)
        akhaSearch1=Label(fixFrame1, fg="#000080", text="ΚΩΔΙΚΟΣ ΑΚΗΑ:", padx=15, pady=20)
        akhaSearch1.grid(row=12, column=4, sticky=E)
        akhaSearch2=Entry(fixFrame1, width=50, relief=SUNKEN, borderwidth=5)
        akhaSearch2.grid(row=12, column=5)
        update1Search1=Label(fixFrame1, fg="#000080", text="ΠΡΟΤΕΡΑΙΟΤΗΤΑ:", padx=15, pady=20)
        update1Search1.grid(row=14, column=4, sticky=E)
        update1Search2=Entry(fixFrame1, width=50, relief=SUNKEN, borderwidth=5)
        update1Search2.grid(row=14, column=5) 
        update2Search1=Label(fixFrame1, fg="#000080", text="ΗΜ/ΝΙΑ ΡΑΝΤΕΒΟΥ:", padx=15, pady=20)
        update2Search1.grid(row=16, column=4, sticky=E)
        update2Search2=Entry(fixFrame1, width=50, relief=SUNKEN, borderwidth=5)
        update2Search2.grid(row=16, column=5)       
        for i in range(5):
            choiceSearch=Button(fixFrame1, text="Επιλογή", padx=40, pady=11, command=lambda i=i: search(fixFrame1, i, 3))
            choiceSearch.grid(row=8+2*i, column=8, padx=15)
        returnSearch=Button(fixFrame1, text="<<Επιστροφή", padx=35, pady=11, command=lambda: goto(55))#εκκρρεμεί η goto().
        returnSearch.grid(row=1000, column=0, columnspan=10, pady=25)



        
    elif x==3: #Ακύρωση ραντεβού, αναζήτηση με βάση τον ΑΜΚΑ
        global delSearch2
        global delFrame
        global delNextStep1
        global delSearch1
        global delSearch0
        y.grid_forget()
        delFrame=LabelFrame(root, bd=0)
        delFrame.grid(row=4, column=0, columnspan=10)
        delSearch0=Label(delFrame, text="Ακύρωση ραντεβού", fg="#000080")
        delSearch0.grid(row=5, column=0, columnspan=10, pady=15)
        delSearch1=Label(delFrame, text="ΑΜΚΑ:", fg="#000080")
        delSearch1.grid(row=6, column=4)
        delSearch2=Entry(delFrame, width=50, borderwidth=5, relief=SUNKEN, fg="#000080", bg="#d9d9d9")
        delSearch2.grid(row=6, column=5, padx=30)
        delNextStep1=Button(delFrame, text="Υποβολή", fg="#ffffff", bg="#000080", padx=30, pady=11, command=lambda: goto(16)) 
        delNextStep1.grid(row=7, column=0, columnspan=10, pady=15)        
    elif x==4: #ο ΑΜΚΑ ελέγχθηκε από την checkAmka() και είναι σωστός
        amka2=addAmka2.get()
        amka2=amka2.split()
        amka=""
        for i in amka2:
            amka=amka+i
        amka=amka.strip()
        addFrame2=LabelFrame(add, bd=0) #το frame που περιλαμβάνει όλα τα υπόλοιπα πεδία της φόρμας εκτός του ΑΜΚΑ
        addFrame2.grid(row=16, column=0, columnspan=10)        
        with open("data.csv", "r", newline="", encoding="utf-8") as file:
            ro=csv.reader(file, delimiter='$')
            for row in ro:
                contents.append(row)
            if len(contents)>0: #υπάρχουν στη Βάση Δεδομένων εγγραφές που θα ελεγχθούν και ανάλογα με το αποτέλεσμα προχωράει η διαδικασία       
                for i in contents:
                    if amka == i[0]: #ο ΑΜΚΑ υπάρχει ήδη στη Βάση Δεδομένων από προηγούμενα ραντεβού, εμφανίζονται αυτόματα το όνομα/επώνυμο
                        surname=i[1]
                        name=i[2]
                        addLabel=Label(addFrame2, text="Καταχώρηση στοιχείων ραντεβού", fg="#000080", pady=15)
                        addLabel.grid(row=0, column=0, columnspan=10)
                        addAmka1=Label(addFrame2, text="ΑΜΚΑ εξυπηρετούμενου:", fg="#000080")
                        addAmka1.grid(row=5, column=4)
                        addAmka2.grid_forget()
                        addAmka2=Label(addFrame2, text=amka+str(78*" "), fg="#000080", bg="#d9d9d9", borderwidth=5, relief=SUNKEN)  #πατέντα, για να "καθίσει" ο ΑΜΚΑ στα αριστερά
                        addAmka2.grid(row=5, column=5, sticky=W)
                        addSurname1=Label(addFrame2, text="Επώνυμο:", fg="#000080")
                        addSurname1.grid(row=6, column=4)
                        addSurname2=Entry(addFrame2,  width=50, fg="#000080", bg="#d9d9d9", borderwidth=5)
                        addSurname2.grid(row=6, column=5)
                        addSurname2.insert(0, surname)
                        addName1=Label(addFrame2, text="Όνομα:", fg="#000080")
                        addName1.grid(row=7, column=4)
                        addName2=Entry(addFrame2,  width=50, fg="#000080", bg="#d9d9d9", borderwidth=5)
                        addName2.grid(row=7, column=5)
                        addName2.insert(0, name)
                        addName2.grid(row=7, column=5)
                        addFrame2.grid(row=4, column=0, columnspan=10)
                        errorFlag=3 #στην checkData() οι μεταβλητές surname, name παίρνουν τιμές από τη Βάση Δεδομένων, επομένως στην checkData() ΔΕΝ θα βάλω surname.get(), name.get()
                        break
                    elif i==contents[-1] or len(contents)==0: #ο ΑΜΚΑ δεν υπάρχει ήδη στη Βάση Δεδομένων από προηγούμενα ραντεβού ή η Βάση Δεδεομένων είναι εντελώς άδεια
                        addLabel=Label(addFrame2, text="Καταχώρηση στοιχείων ραντεβού", fg="#000080", pady=15)
                        addLabel.grid(row=0, column=0, columnspan=10)
                        addAmka1=Label(addFrame2, text="ΑΜΚΑ εξυπηρετούμενου:", fg="#000080")
                        addAmka1.grid(row=5, column=4)
                        addAmka2.grid_forget()
                        addAmka2=Label(addFrame2, text=amka+str(78*" "), fg="#000080", bg="#d9d9d9", borderwidth=5, relief=SUNKEN)  #padx=118,
                        addAmka2.grid(row=5, column=5, sticky=W)
                        addSurname1=Label(addFrame2, text="Επώνυμο:", fg="#000080")
                        addSurname1.grid(row=6, column=4)
                        addSurname2=Entry(addFrame2,  width=50, fg="#000080", bg="#d9d9d9", borderwidth=5)
                        addSurname2.grid(row=6, column=5)
                        addName1=Label(addFrame2, text="Όνομα:", fg="#000080")
                        addName1.grid(row=7, column=4)
                        addName2=Entry(addFrame2,  width=50, fg="#000080", bg="#d9d9d9", borderwidth=5)
                        addName2.grid(row=7, column=5)
                        surname=""
                        name=""
                addHospital1=Label(addFrame2, text="Ιατρείο:", fg="#000080")
                addHospital1.grid(row=8, column=4)
                addHospital2=Entry(addFrame2, width=50, fg="#000080", bg="#d9d9d9", borderwidth=5)
                addHospital2.grid(row=8, column=5)
                addPriority1=Label(addFrame2, text="Προτεραιότητα:", fg="#000080")
                addPriority1.grid(row=9, column=4)
                addPriority2=Entry(addFrame2, width=50, fg="#000080", bg="#d9d9d9", borderwidth=5)
                addPriority2.grid(row=9, column=5)
                addDate1=Label(addFrame2, text="Ημ/νία ραντεβού (ηη-μμ-εεεε, ηη/μμ/εεεε):", fg="#000080")
                addDate1.grid(row=10, column=4)
                addDate2=Entry(addFrame2, width=50, fg="#000080", bg="#d9d9d9", borderwidth=5)
                addDate2.grid(row=10, column=5)
                addTime1=Label(addFrame2, text="Ώρα ραντεβού (ωω:λλ):", fg="#000080")
                addTime1.grid(row=11, column=4)
                addTime2=Entry(addFrame2, width=50, fg="#000080", bg="#d9d9d9", borderwidth=5)
                addTime2.grid(row=11, column=5)            
                addNotes1=Label(addFrame2, text="Παρατηρήσεις:", fg="#000080")
                addNotes1.grid(row=12, column=4)
                addNotes2=Entry(addFrame2, width=50, fg="#000080", bg="#d9d9d9", borderwidth=5)
                addNotes2.grid(row=12, column=5)
                submit2=Button(addFrame2, bg="#000080", fg="#ffffff", text="Υποβολή", padx=35, pady=11, command= lambda: checkData(1))
                submit2.grid(row=13, column=4, columnspan=10, pady=15)        
                contents.clear()      
    elif x==5: #Καταχώρηση ραντεβού, errorFlag==0
        contents.clear()
        with open("data.csv", "r", newline="", encoding="utf-8") as file:
            ro=csv.reader(file, delimiter='$')
            for row in ro:
                contents.append(row)
            if len(contents)>0: #υπάρχουν στη Βάση Δεδομένων εγγραφές που θα ελεγχθούν και ανάλογα με το αποτέλεσμα προχωράει η διαδικασία       
                for i in contents:
                    if amka == i[0]: #ο ΑΜΚΑ υπάρχει ήδη στη Βάση Δεδομένων από προηγούμενα ραντεβού, εμφανίζονται αυτόματα το όνομα/επώνυμο
                        surname=i[1]
                        name=i[2]
                        addLabel=Label(addFrame2, text="Καταχώρηση στοιχείων ραντεβού", fg="#000080", pady=15)
                        addLabel.grid(row=0, column=0, columnspan=10)
                        addAmka1=Label(addFrame2, text="ΑΜΚΑ εξυπηρετούμενου:", fg="#000080")
                        addAmka1.grid(row=5, column=4)
                        addAmka2.grid_forget()
                        addAmka2=Label(addFrame2, text=amka+str(78*" "), fg="#000080", bg="#d9d9d9", borderwidth=5, relief=SUNKEN)  #πατέντα, για να "καθίσει" ο ΑΜΚΑ στα αριστερά
                        addAmka2.grid(row=5, column=5, sticky=W)
                        addSurname1=Label(addFrame2, text="Επώνυμο:", fg="#000080")
                        addSurname1.grid(row=6, column=4)
                        addSurname2=Entry(addFrame2,  width=50, fg="#000080", bg="#d9d9d9", borderwidth=5)
                        addSurname2.grid(row=6, column=5)
                        addSurname2.insert(0, surname)
                        addName1=Label(addFrame2, text="Όνομα:", fg="#000080")
                        addName1.grid(row=7, column=4)
                        addName2=Entry(addFrame2,  width=50, fg="#000080", bg="#d9d9d9", borderwidth=5)
                        addName2.grid(row=7, column=5)
                        addName2.insert(0, name)
                        addName2.grid(row=7, column=5)
                        addFrame2.grid(row=4, column=0, columnspan=10)
                        errorFlag=3 #στην checkData() οι μεταβλητές surname, name παίρνουν τιμές από τη Βάση Δεδομένων, επομένως στην checkData() ΔΕΝ θα βάλω surname.get(), name.get()
                        break
                    elif i==contents[-1]: #ο ΑΜΚΑ δεν υπάρχει ήδη στη Βάση Δεδομένων από προηγούμενα ραντεβού, το όνομα/επώνυμο εισάγονται από τον χρήστη
                        addLabel=Label(addFrame2, text="Καταχώρηση στοιχείων ραντεβού", fg="#000080", pady=15)
                        addLabel.grid(row=0, column=0, columnspan=10)
                        addAmka1=Label(addFrame2, text="ΑΜΚΑ εξυπηρετούμενου:", fg="#000080")
                        addAmka1.grid(row=5, column=4)
                        addAmka2.grid_forget()
                        addAmka2=Label(addFrame2, text=amka+str(78*" "), fg="#000080", bg="#d9d9d9", borderwidth=5, relief=SUNKEN)  #padx=118,
                        addAmka2.grid(row=5, column=5, sticky=W)
                        addSurname1=Label(addFrame2, text="Επώνυμο:", fg="#000080")
                        addSurname1.grid(row=6, column=4)
                        addSurname2=Entry(addFrame2, width=50, fg="#000080", bg="#d9d9d9", borderwidth=5)
                        addSurname2.grid(row=6, column=5)
                        addName1=Label(addFrame2, text="Όνομα:", fg="#000080")
                        addName1.grid(row=7, column=4)
                        addName2=Entry(addFrame2, width=50, fg="#000080", bg="#d9d9d9", borderwidth=5)
                        addName2.grid(row=7, column=5)
                        addFrame2.grid(row=4, column=0, columnspan=10)
                        errorFlag=4 #στην checkData() οι μεταβλητές surname, name θα πάρουν τιμές από τον χρήστη (Entry), επομένως στην checkData() θα βάλω name.get(), surname.get()
                        break
            else: #Η Βάση Δεδομένων είναι άδεια, όλα τα πεδία - εκτός από τον ΑΜΚΑ που δόθηκε νωρίτερα - θα συμπληρωθούν από τον χρήστη
                addSurname1=Label(addFrame2, text="Επώνυμο:", fg="#000080")
                addSurname1.grid(row=6, column=4)
                addSurname2=Entry(addFrame2, width=50, fg="#000080", bg="#d9d9d9", borderwidth=5)
                addSurname2.grid(row=6, column=5)
                addName1=Label(addFrame2, text="Όνομα:", fg="#000080")
                addName1.grid(row=7, column=4)
                addName2=Entry(addFrame2, width=50, fg="#000080", bg="#d9d9d9", borderwidth=5)
                addName2.grid(row=7, column=5)
    elif x==6: #Διόρθωση ραντεβού, errorFlag==0
        alter.clear()
        amka2=fixAmka2.get() 
        amka2=amka2.split() #κόψιμο κενών ανάμεσα στα ψηφία του ΑΜΚΑ
        amka=""
        for i in amka2:
            amka=amka+i
        amka=amka.strip()        
        with open("current.csv", "r", newline="", encoding="utf-8") as file:
            ro=csv.reader(file, delimiter='$')
            for row in sorted(ro, key=lambda j:j[5]):
                alter.append(row)
            for x in alter:
                if amka==x[0]:
                    newList.append(x)
            if len(newList)==0:  #δεν υπάρχει καταχωρημένο ραντεβού με τον συγκεκριμένο ΑΜΚΑ
                global fixFrame4l
                fixFrame4=LabelFrame(root, bd=0)
                fixFrame4.grid(row=4, column=0, columnspan=10)
                fixFalse=Label(fixFrame4, text="Δεν υπάρχει καταχωρημένο ραντεβού προσεχώς με αυτόν τον ΑΜΚΑ, η ενέργεια ακυρώθηκε.", fg="#000080", pady=15)
                fixFalse.grid(row=119, column=0, columnspan=10)
                fixNew=Button(fixFrame4, text="Νέα διόρθωση", padx=25, pady=11, fg="#ffffff", bg="#000080", command=lambda: goto(7))
                fixNew.grid(row=120, column=4, columnspan=10, pady=15) 
                fixCancel=Button(fixFrame4, text="Κεντρικό μενού", padx=30, pady=11, fg="#ffffff", bg="#000080", command=lambda: goto(8))
                fixCancel.grid(row=120, column=5, columnspan=10, pady=15)                                
            else:   #υπάρχουν στη Βάση Δεδομένων εγγραφές με βάση τον ΑΜΚΑ που θα ελεγχθούν και ανάλογα με το αποτέλεσμα προχωράει η διαδικασία                     
                goto(9) 
    elif x==7: #Αναζήτηση ραντεβού
        global dateList
        global checkList
        global viewFrame2
        global status
        y.grid_forget()
        viewFrame2=LabelFrame(root, bd=0)
        viewFrame2.grid(row=4, column=0, columnspan=10)
        viewShowLabel=Label(viewFrame2, text="Αναζήτηση ραντεβού με βάση:", fg="#000080", pady=15)
        viewShowLabel.grid(row=4, column=0, columnspan=10)
        dateList=[]
        checkList=[]
        #global surnameSearch2
        global cardSearch2
        #global amkaSearch2
        global afmSearch2
        #global akhaSearch2
        #global update1Search2
        #global update2Search2
        global activeSearch2
        surnameSearch1=Label(viewFrame2, fg="#000080", text="ΕΠΩΝΥΜΟ:", padx=15, pady=20)
        surnameSearch1.grid(row=8, column=4, sticky=E)
        surnameSearch2=Entry(viewFrame2, width=50, relief=SUNKEN, borderwidth=5)
        surnameSearch2.grid(row=8, column=5)      
        amkaSearch1=Label(viewFrame2, fg="#000080", text="ΑΜΚΑ:", padx=15, pady=20)
        amkaSearch1.grid(row=10, column=4, sticky=E)
        amkaSearch2=Entry(viewFrame2, width=50, relief=SUNKEN, borderwidth=5)
        amkaSearch2.grid(row=10, column=5)
        akhaSearch1=Label(viewFrame2, fg="#000080", text="ΚΩΔΙΚΟΣ ΑΚΗΑ:", padx=15, pady=20)
        akhaSearch1.grid(row=12, column=4, sticky=E)
        akhaSearch2=Entry(viewFrame2, width=50, relief=SUNKEN, borderwidth=5)
        akhaSearch2.grid(row=12, column=5)
        update1Search1=Label(viewFrame2, fg="#000080", text="ΠΡΟΤΕΡΑΙΟΤΗΤΑ:", padx=15, pady=20)
        update1Search1.grid(row=14, column=4, sticky=E)
        update1Search2=Entry(viewFrame2, width=50, relief=SUNKEN, borderwidth=5)
        update1Search2.grid(row=14, column=5) 
        update2Search1=Label(viewFrame2, fg="#000080", text="ΗΜ/ΝΙΑ ΡΑΝΤΕΒΟΥ:", padx=15, pady=20)
        update2Search1.grid(row=16, column=4, sticky=E)
        update2Search2=Entry(viewFrame2, width=50, relief=SUNKEN, borderwidth=5)
        update2Search2.grid(row=16, column=5)       
        for i in range(5):
            choiceSearch=Button(viewFrame2, text="Επιλογή", padx=40, pady=11, command=lambda i=i: search(viewFrame2, i, 1))
            choiceSearch.grid(row=8+2*i, column=8, padx=15)
        returnSearch=Button(viewFrame2, text="<<Επιστροφή", padx=35, pady=11, command=lambda: goto(53))
        returnSearch.grid(row=1000, column=0, columnspan=10, pady=25)




        
        '''viewShowOpt1=Button(viewFrame2, text="ΑΜΚΑ (ιστορικό)", bg="#000080", pady=11, padx=40, fg="#ffffff", command=lambda: goto(28)) 
        viewShowOpt1.grid(row=5, column=4, padx=20)
        viewShowOpt2=Button(viewFrame2, text="Ημερομηνία", bg="#000080", pady=11, padx=35, fg="#ffffff", command=lambda: goto(29)) 
        viewShowOpt2.grid(row=5, column=5, padx=20)
        viewShowOpt3=Button(viewFrame2, text="Προτεραιότητα", bg="#000080", pady=11, padx=35, fg="#ffffff", command=lambda: goto(30)) 
        viewShowOpt3.grid(row=5, column=6, padx=20)
        viewShowOpt4=Button(viewFrame2, text="<<Επιστροφή", bg="#000080", pady=11, padx=35, fg="#ffffff", command=lambda: goto(53)) 
        viewShowOpt4.grid(row=5, column=7, padx=20)'''


def search(x, k, n): #Ανακατεύθυνση από το μενού αναζήτησης προς όπου χρειάζεται να συνεχίσει το πρόγραμμα, παίρνει 3 ορίσματα-->x (Frame που θα καταργηθεί), -->k (επιλογή 
    x.grid_forget() #από την goto(7) που δείχνει το κριτίριο αναζήτησης, n-->ενέργεια που θα ακολουθήσει(πχ διαγραφή), αναζήτηση, n==1 -->διαγραφή, n==2, n==3 -->διόρθωση.
    global Frame17
    Frame17=LabelFrame(root, bd=0)
    Frame17.grid(row=5, column=0, columnspan=18)
    global option
    option=n
    if option==1:
        labelText="ΑΝΑΖΗΤΗΣΗ ΡΑΝΤΕΒΟΥ"
    elif option==2:
        labelText="ΔΙΑΓΡΑΦΗ ΡΑΝΤΕΒΟΥ"
    else:
        labelText="ΔΙΟΡΘΩΣΗ ΡΑΝΤΕΒΟΥ"
    label=Label(Frame17, text=labelText, fg="#000080", bg="#d9d9d9",  pady=15)
    label.grid(row=5, column=0, columnspan=18, sticky=W+E)
    errorFlag=0
    message=""
    surname=surnameSearch2.get()
    #card2=cardSearch2.get()
    amka2=amkaSearch2.get()
    #afm2=afmSearch2.get()
    akha2=akhaSearch2.get()
    surname=surname.strip()
    surname=surname.upper()
    if k==0 and len(surname)==0:
        errorFlag=1
        message=message+"\nΔεν είναι σωστή η καταχώρηση."
    #card2=card2.strip()
    #card2=card2.split() #κόψιμο κενών ανάμεσα στα ψηφία του κωδικού της κάρτας ΔΥΠΑ.
    #card=""
    #for i in card2:
        #card=card+i
    #card=card.strip()
    #if k==1 and not card.isdigit(): # εσφαλμένος κωδικός δελτίου ανεργίας.
        #errorFlag=1
        #message=message+"\nΔεν είναι σωστή η καταχώρηση, ο κωδικός του δελτίου ανεργίας πρέπει να περιέχει (16) ψηφία."
    amka2=amka2.strip()
    amka2=amka2.split() #κόψιμο κενών ανάμεσα στα ψηφία του ΑΜΚΑ
    amka=""
    for i in amka2:
        amka=amka+i    
    if k==1 and (not (amka.isdigit() and len(amka)==11)): #σωστός ΑΜΚΑ
        errorFlag=1
        message=message+"\nΔεν είναι σωστή η καταχώρηση, ο ΑΜΚΑ πρέπει να περιέχει (11) ψηφία."
    #afm2=afm2.strip()
    #afm2=afm2.split() #κόψιμο κενών ανάμεσα στα ψηφία του ΑΜΚΑ
    #afm=""
    #for i in afm2:
        #afm=afm+i
    #if k==3 and (not (afm.isdigit() and len(afm)==9)): #σωστός ΑΜΚΑ
        #errorFlag=1
        #message=message+"\nΔεν είναι σωστή η καταχώρηση, ο ΑΦΜ πρέπει να περιέχει (9) ψηφία."
    akha2=akha2.strip()
    akha2=akha2.split() #κόψιμο κενών ανάμεσα στα ψηφία του ΑΚΗΑ
    akha=""
    for i in akha2:
        akha=akha+i    
    if k==2 and (not akha.isdigit()): #εσφαλμένος κωδικός ΑΚΗΑ
        errorFlag=1
        message=message+"\nΔεν είναι σωστή η καταχώρηση, ο κωδικός ΑΚΗΑ περιλαμβάνει μόνο ψηφία."
    if n==1: #διαδικασία αναζήτησης δελτίων.        
        date1=update2Search2.get()
        #date2=update2Search2.get()
        #date1.strip()
        #date2.strip()        
        day1=checkDate(date1)
        #day2=checkDate(date2)    
        if k==4 and day1==0:
            errorFlag=1
            message=message+"\nΜη έγκυρη ημερομηνία."
        #if k==6 and day2==0:
            #errorFlag=1
            #message=message+"\nΜη έγκυρη ημερομηνία."
        #active=activeSearch2.get()
        #active=active.strip()
        #active=active.upper()
        #if k==7 and active not in ['ΝΑΙ', 'ΟΧΙ']:
            #errorFlag=1
            #message=message+"\nΥπάρχουν μόνο δύο επιλογές για την ενεργή/ ανενεργή κάρτα (ΝΑΙ/ΟΧΙ)."
    if errorFlag==1: #Ύπαρξη σφάλματος, εκτύπωση μηνύματος και επιλογές επιστροφής / νέας ενέργειας.
        backSearch=Button(Frame17, text="<<Επιστροφή", padx=32, pady=11, command=lambda: insert(Frame17, 7))#goto(134))#
        backSearch.grid(row=1000, column=8, padx=65, pady=45)          
        returnSearch=Button(Frame17, text="Κεντρικό μενού", padx=28, pady=11, command=lambda: goto(54))
        returnSearch.grid(row=1000,  column=9, padx=65, pady=45)
        message=message[:-1]+", η ενέργεια ακυρώθηκε."
        messagebox.showerror('Σφάλμα:', message)        
    else:
        global tempList1
        global tempList2
        tempList1=[]
        tempList2=[]
        global criterion
        with open("current.csv", "r", encoding="utf-8", newline="") as file: #ενεργά και ανενεργά δελτία ανεργίας, αλλά ΟΧΙ διεγραμμένα (τα διεγραμμένα βρίσκονται από default στο 
            ro=csv.reader(file, delimiter='$')                               #αρχείο 'previous.csv').
            for row in ro:
                tempList2.append(row)
        if n==1: #αναζήτηση.
            searchList=[surname, amka, akha, day1]
            criterion=["ΕΠΩΝΥΜΟ", "ΑΜΚΑ", "ΚΩΔΙΚΟΣ ΑΚΗΑ", "ΗΜ/ΝΙΑ ΡΑΝΤΕΒΟΥ "]
            with open("previous.csv", "r", encoding="utf-8", newline="") as file: #στο 'previous.csv' καταχωρούνται τα διεγραμμένα δελτία, ώστε αν χρειαστεί κάποτε να τα επαναφέρουμε.
                ro=csv.reader(file, delimiter='$')
                for row in ro:
                    tempList1.append(row)               
                for record in tempList1: #κόψιμο διπλοεγγραφή)
                    for temp in tempList2:
                        if (record[0] not in temp) and (record[3] not in temp) and (record[6] not in temp):
                            tempList2.append(record)                    
        elif n==2: #διαγραφή.
            searchList=[surname, amka, akha]
            criterion=["ΕΠΩΝΥΜΟ", "ΑΜΚΑ", "ΚΩΔΙΚΟΣ ΑΚΗΑ"]
        else: #διόρθωση
            searchList=[surname, amka, akha, priority, day1]
            criterion=["ΕΠΩΝΥΜΟ", "ΑΜΚΑ", "ΚΩΔΙΚΟΣ ΑΚΗΑ", "ΠΡΟΤΕΡΑΙΟΤΗΤΑ", "ΗΜ/ΝΙΑ ΡΑΝΤΕΒΟΥ"]           
        global dateList
        dateList=[]
        dateList.clear()     
        with open("previous.csv", "r", encoding="utf-8", newline="") as file: #στο 'previous.csv' καταχωρούνται τα διεγραμμένα δελτία, ώστε αν χρειαστεί κάποτε να τα επαναφέρουμε.
            ro=csv.reader(file, delimiter='$')
            for row in ro:
                tempList1.append(row) 
        for record in tempList2:
            if searchList[k] in record: #έλεγχος αν η τιμή του κριτιρίου αναζήτησης (πχ τιμή ΑΜΚΑ) αντιστοιχεί σε εγγραφή στο σύστημα (αν ΝΑΙ, εγγραφή στην λίστα για εκτύπωση).
                dateList.append(record)            
        if len(dateList)==0:
            returnSearch=Button(Frame17, text="Κεντρικό μενού", padx=32, pady=11, command=lambda: goto(54))
            returnSearch.grid(row=1000, column=9, padx=50, pady=45)
            if n==1: #αναζήτηση.
                backSearch=Button(Frame17, text="Νέα αναζήτηση", padx=25, pady=11, command=lambda: insert(Frame17, 7))
                backSearch.grid(row=1000, column=8, padx=50, pady=45)                
            elif n==2: #διαγραφή.
                backSearch=Button(Frame17, text="Νέα διαγραφή", padx=32, pady=11, command=lambda: insert(Frame17, 5))
                backSearch.grid(row=1000, column=8, padx=50, pady=45)            
            message="\nΔε βρέθηκαν εγγραφές στο σύστημα σύμφωνα με τα κριτίρια αναζήτησης (με βάση: "+criterion[k]+")."
            messagebox.showwarning('Σφάλμα:', message)
            for record in tempList1:
                if searchList[k] in record: #έλεγχος αν η τιμή του κριτιρίου αναζήτησης (πχ τιμή ΑΜΚΑ) αντιστοιχεί σε εγγραφή στο σύστημα που έχει ΗΔΗ διαγραφεί.
                    dateList.append(record)
                if len(dateList)>0:
                     message="\nΗ εγγραφή σύμφωνα με τα κριτίρια αναζήτησης (με βάση: "+criterion[k]+") έχει ήδη διαγραφεί."
                     messagebox.showwarning('Σφάλμα:', message)
        else:
            global newSearch
            if n==1: #στο επόμενο Frame ακολουθεί ενέργεια αναζήτησης (ΜΟΝΟ προβολή στοιχείων)
                lambda criterion=criterion[k]: goto(34)
                showSearch=Button(Frame17, text="Εμφάνιση", padx=40, pady=11, command=lambda criterion=criterion[k]: goto(34))
                showSearch.grid(row=1000, column=9,  padx=65, pady=45)
            elif n==2: #στο επόμενο Frame ακολουθεί ενέργεια αναζήτησης για διαγραφή.                
                showSearch=Button(Frame17, text="Εμφάνιση", padx=45, pady=11, command=lambda criterion=criterion[k]: goto(25)) 
                showSearch.grid(row=1000, column=9, padx=65, pady=45)
            newSearch=Button(Frame17, text="<<Επιστροφή", padx=34, pady=11, command=lambda: insert(Frame17, 7))
            newSearch.grid(row=1000, column=8,  padx=65, pady=45)            
            if len(dateList)==1:
                message="Βρέθηκε στο σύστημα ένα δελτίο για διαγραφή σύμφωνα με τα κριτίρια αναζήτησης (με βάση: "+criterion[k]+")."
            else:
                message="Βρέθηκαν στο σύστημα "+str(len(dateList))+" δελτία για διαγραφή σύμφωνα με τα κριτίρια αναζήτησης (με βάση: "+criterion[k]+")."
            messagebox.showinfo('', message)    





        
                    
def checkAmka(x):
    global errorAmka
    if x==1:
        addFrame1.grid_forget()
        amka2=addAmka2.get()
        amka2=amka2.split() #κόψιμο κενών ανάμεσα στα ψηφία του ΑΜΚΑ
        amka=""
        for i in amka2:
            amka=amka+i
        amka=amka.strip()
        if amka.isdigit() and len(amka)==11:
            errorFlag=0
            insert(4) #σημαίνει πως ο ΑΜΚΑ είναι σωστός και καλεί την insert() για να συνεχιστεί η εισαγωγή των στοιχείων
        else:
            message="Δεν είναι σωστή η καταχώρηση, ο ΑΜΚΑ πρέπει να περιέχει (11) ψηφία."
            errorAmka=Label(add, text=message, fg="#000080")
            errorAmka.grid(row=50, column=0, columnspan=10, pady=15)
            newAdd=Button(add, text="Νέα καταχώρηση", fg="#ffffff", bg="#000080", padx=30, pady=11, command=lambda: goto(2))
            newAdd.grid(row=100, column=4, pady=15, padx=25)
            returnAdd=Button(add, text="Κεντρικό μενού", fg="#ffffff", bg="#000080", padx=36, pady=11, command=lambda: goto(1))
            returnAdd.grid(row=100, column=5, pady=15, padx=25)        
    elif x==2: #έλεγχος ΑΜΚΑ (λειτουργία διόρθωσης ραντεβού)
        amka2=fixAmka2.get()
        amka2=amka2.split() #κόψιμο κενών ανάμεσα στα ψηφία του ΑΜΚΑ
        amka=""
        for i in amka2:
            amka=amka+i
        amka=amka.strip()        
        amka=amka.strip()
        fixFrame1.grid_forget() 
        if amka.isdigit() and len(amka)==11: #έλεγχος ορθότητας ΑΜΚΑ            
            errorFlag=0
            insert(6)
        else:
            global fixFrame5
            errorFlag=1
            fixFrame5=LabelFrame(root, bd=0)
            fixFrame5.grid(row=7, column=0, columnspan=10)
            message="Δεν είναι σωστή η καταχώρηση, ο ΑΜΚΑ πρέπει να περιέχει (11) ψηφία."
            fixErrorAmka=Label(fixFrame5, text=message, fg="#000080")
            fixErrorAmka.grid(row=90, column=0, columnspan=10, pady=15)
            fixNew=Button(fixFrame5, text="Νέα διόρθωση", padx=30, pady=11, fg="#ffffff", bg="#000080", command=lambda: goto(5))
            fixNew.grid(row=120, column=4, pady=15, padx=20) 
            fixCancel=Button(fixFrame5, text="Κεντρικό μενού", padx=30, pady=11, fg="#ffffff", bg="#000080", command=lambda: goto(6))
            fixCancel.grid(row=120, column=5, pady=15, padx=20)        

def checkData(m): #τρεις παράμετροι: m-->(1) για καταχώρηση, (2) για διόρθωση, (3) για διαγραφή ραντεβού, k-->επώνυμο, l-->όνομα
    global num
    global wra
    y = str(datetime.date.today())
    y=y.split('-')
    y="".join(y)                    #current date as one string!      
    if m==1:                        #καταχώρηση νέου ραντεβού
        surname=addSurname2.get()
        name=addName2.get()
        surname=surname.strip()
        name=name.strip()
        wra=addTime2.get()
        wra=wra.strip()   
        hospital=addHospital2.get()
        hospital=hospital.strip()
        priority=addPriority2.get()
        priority=priority.strip()
        day=addDate2.get()
        day=day.strip()
        valid=checkDate(day)        
        notes=addNotes2.get()
        notes=notes.strip()
        submit2.grid_forget()
        if valid==0: #μη έγκυρη ημερομηνία από τον χρήστη
            message="Μη έγκυρη ημερομηνία, η ενέργεια ακυρώθηκε."
        else:
            testing=[]
            appointment=[amka, surname.upper(), name.upper()]
            newEntry=[amka, surname.upper(), name.upper(), hospital.upper(), priority.upper(), valid.upper(), wra.upper(), notes.upper()]
            with open("data.csv", "r", newline="", encoding="utf-8") as file: 
                ro=csv.reader(file, delimiter='$')
                for row in ro:
                    testing.append(row)
                for i in testing:
                    if appointment == i: #έλεγχος δεδομένων (κόψιμο διπλοεγγραφής στο μητρώο)
                        file.close()
                        break
                    elif i==testing[-1]:
                        with open("data.csv", 'a', encoding="utf-8", newline="") as file: #εγγραφή στο μητρώο (ΑΜΚΑ, επώνυμο, όνομα)
                            wo=csv.writer(file, delimiter='$')
                            wo.writerow(appointment)
            y= str(datetime.date.today())  #current date
            y=y.split('-')
            y="".join(y)                    #current date as one string!                
            if valid>=y:            #ημερομηνίες από την τρέχουσα και μεταγενέστερα
                with open("current.csv", "r", newline="", encoding="utf-8") as file: #κόψιμο διπλοεγγραφής 
                    ro=csv.reader(file, delimiter='$')
                    for row in ro:
                        check.append(row)                
                    if newEntry in check:
                        message="Η συγκεκριμένη εγγραφή έχει ήδη καταχωρηθεί, η ενέργεια ακυρώθηκε."
                        check.clear()
                    else:
                        with open("current.csv", "a", newline="", encoding="utf-8") as file:  
                            wo=csv.writer(file, delimiter='$')                           
                            wo.writerow(newEntry)
                        message="Το ραντεβού καταχωρήθηκε με επιτυχία."                         
                        check.clear()                            
            else:                   #ημερομηνίες πριν από την τρέχουσα (ρολόι υπολογιστή)
                with open("previous.csv", "r", newline="", encoding="utf-8") as file:
                    ro=csv.reader(file, delimiter='$')
                    for row in ro:
                        check.append(row)
                    if newEntry in check:
                        message="Η συγκεκριμένη εγγραφή έχει ήδη καταχωρηθεί, η ενέργεια ακυρώθηκε."
                        check.clear()                       
                    else:                    
                        with open("previous.csv", "a", newline="", encoding="utf-8") as file:
                            wo=csv.writer(file, delimiter='$')                           
                            wo.writerow(newEntry)
                        message="Το ραντεβού καταχωρήθηκε με επιτυχία."
                        check.clear()                        
        addSuccess=Label(addFrame2, bd=0, text=message, fg="#000080")
        addSuccess.grid(row=95, column=0, columnspan=10, pady=15)
        newAdd=Button(addFrame2, text="Νέα καταχώρηση", fg="#ffffff", bg="#000080", padx=30, pady=11, command=lambda: goto(3))
        newAdd.grid(row=100, column=4, padx=25)         
        returnAdd=Button(addFrame2, text="Κεντρικό μενού", fg="#ffffff", bg="#000080", padx=30, pady=11, command=lambda: goto(4))
        returnAdd.grid(row=100, column=5, padx=25) 
    else:                       #διόρθωση/διαγραφή ραντεβού (αρχικοποίηση μεταβλητών)
        if m==2:                #διόρθωση ραντεβού          
            num=fixChoice2.get() #change--> o A/A του ραντεβού που ανιχνεύθηκε από το πρόγραμμα σύμφωνα με τα κριτήρια αναζήτησης
            num=num.strip()
            if not num.isdigit():
                global fixFrame3
                fixChoice2.delete(0, END)
                fixFalse2=Label(fixFrame3, fg="#000080", text="Λανθασμένη επιλογή, παρακαλώ επιλέξτε ξανά (1-"+str(len(newList))+").")
                fixFalse2.grid(row=1000, column=0, columnspan=10, pady=15)
            else:
                global fixChange
                global fixChange1
                global fixNewHospital2
                global fixNewPriority2
                global fixNewDate2
                global fixNewTime2
                global fixNewNotes2
                surname=newList[int(num3)-1][1]
                name=newList[int(num3)-1][2]
                fixChange1=LabelFrame(root, bd=0)
                fixChange1.grid(row=4, column=0, columnspan=10)
                fixNewAmka1=Label(fixChange1, text="ΑΜΚΑ:", fg="#000080")
                fixNewAmka1.grid(row=5, column=4, columnspan=10, padx=30, sticky=W)
                fixNewAmka2=Label(fixChange1, text=amka, fg="#000080") 
                fixNewAmka2.grid(row=5, column=5, columnspan=1, padx=30, sticky=W)                
                fixNewSurname1=Label(fixChange1, text="Επώνυμο:", fg="#000080")
                fixNewSurname1.grid(row=6, column=4, columnspan=1, padx=30, sticky=W)
                fixNewSurname2=Label(fixChange1, text=surname, fg="#000080") 
                fixNewSurname2.grid(row=6, column=5, columnspan=10, padx=30, sticky=W)                
                fixNewName1=Label(fixChange1, text="Όνομα:", fg="#000080")
                fixNewName1.grid(row=7, column=4, columnspan=10, padx=30, sticky=W)
                fixNewName2=Label(fixChange1, text=name, fg="#000080") 
                fixNewName2.grid(row=7, column=5, columnspan=10, padx=30, sticky=W)
                fixNewHospital1=Label(fixChange1, text="Ιατρείο:", fg="#000080")
                fixNewHospital1.grid(row=8, column=4, columnspan=10, padx=30, sticky=W)
                fixNewHospital2=Entry(fixChange1, width=50, fg="#000080", bg="#d9d9d9", borderwidth=5, relief=SUNKEN) 
                fixNewHospital2.grid(row=8, column=5, columnspan=10, padx=30, sticky=W)
                fixNewPriority1=Label(fixChange1, text="Προτεραιότητα:", fg="#000080")
                fixNewPriority1.grid(row=9, column=4, columnspan=10, padx=30, sticky=W)
                fixNewPriority2=Entry(fixChange1, width=50, fg="#000080", bg="#d9d9d9", borderwidth=5, relief=SUNKEN) 
                fixNewPriority2.grid(row=9, column=5, columnspan=10, padx=30, sticky=W)
                fixNewDate1=Label(fixChange1, text="Ημ/νία ραντεβού:", fg="#000080")
                fixNewDate1.grid(row=10, column=4, columnspan=10, padx=30, sticky=W)
                fixNewDate2=Entry(fixChange1, width=50, fg="#000080", bg="#d9d9d9", borderwidth=5, relief=SUNKEN) 
                fixNewDate2.grid(row=10, column=5, columnspan=10, padx=30)
                fixNewTime1=Label(fixChange1, text="Ώρα ραντεβού:", fg="#000080")
                fixNewTime1.grid(row=11, column=4, columnspan=10, padx=30, sticky=W)
                fixNewTime2=Entry(fixChange1, width=50, fg="#000080", bg="#d9d9d9", borderwidth=5, relief=SUNKEN) 
                fixNewTime2.grid(row=11, column=5, columnspan=10, padx=30, sticky=W)
                fixNewNotes1=Label(fixChange1, text="Παρατηρήσεις:", fg="#000080")
                fixNewNotes1.grid(row=12, column=4, columnspan=10, padx=30, sticky=W)
                fixNewNotes2=Entry(fixChange1, width=50, fg="#000080", bg="#d9d9d9", borderwidth=5, relief=SUNKEN) 
                fixNewNotes2.grid(row=12, column=5, columnspan=10, padx=30, sticky=W)
                fixNewSubmit=Button(fixChange1, text="Υποβολή", padx=35, pady=11, fg="#ffffff", bg="#000080", command=lambda: goto(12)) 
                fixNewSubmit.grid(row=50, column=0, columnspan=10, pady=15)            
        else:                   #ακύρωση ραντεβού (τη διοχέτευσα αλλού)
            pass

def goto(x): #βοηθητική function στην οποία εκτελούνται οι μεταβάσεις (μέσω των lambda functions)
    if x==0: #Καταχώρηση ραντεβού μετά από έλεγχο (function insert())
        errorFlag=0
        insert(5)
    elif x==1: #επιστροφή στο κεντρικό μενού από την ενέργεια 'καταχώρηση ραντεβού' μετά από αποτυχία καταώρηρησης
        add.grid_forget()
        menu()
    elif x==2: #απανάληψη καταχώρησης ραντεβού (ΔΕΝ έχει κληθεί ακόμα η checkAmka(), είναι πρώτη εισαγωγή στοιχείων)
        add.grid_forget()
        insert(1)
    elif x==3: #επανάληψη καταχώρησης μετά από εσφαλμένη ημ/νία
        addFrame2.grid_forget()
        add.grid_forget()
        insert(1)
    elif x==4: #επιστροφή στο κεντρικό μενού από την καταχώρηση ραντεβού (ΑΝΕΞΑΡΤΗΤΑ αν ήταν επιτυχημένη ή όχι)
        addFrame2.grid_forget()
        add.grid_forget()
        menu()
    elif x==5: #νέα διόρθωση μετά από αποτυχία διόρθωσης ραντεβού (λάθος ΑΜΚΑ)
        fixFrame5.grid_forget()
        insert(2)
    elif x==6: #επιστροφή στο κεντρικό μενού μετά από σφάλμα στη διόρθωση ραντεβού (λάθος ΑΜΚΑ)
        fixFrame5.grid_forget()
        menu()
    elif x==7: #νέα διόρθωση μετά από σφάλμα στη διόρθωση ραντεβού (δε βρέθηκαν ο ΑΜΚΑ και το ραντεβού στη Βάση Δεδομένων)
        fixFrame4.grid_forget()                
        insert(2)
    elif x==8: #επιστροφή στο κεντρικό μενού μετά από σφάλμα στη διόρθωση ραντεβού (δε βρέθηκαν ο ΑΜΚΑ και το ραντεβού στη Βάση Δεδομένων)
        fixFrame4.grid_forget()
        menu()
    elif x==9: #Αναζήτηση της λίστας που περιλαμβάνει όλες τις πιθανές εγγραφές ραντεβού για διόρθωση
        global submit3
        global fixFrame2
        global fixLabel0
        fixFrame2=LabelFrame(root, bd=0) #το frame με όλα τα στοιχεία των εγγραφών με βάση τον ΑΜΚΑ που δόθηκε από τον χρήστη
        fixFrame2.grid(row=4, column=0, columnspan=10)
        fixLabel0=LabelFrame(fixFrame2, bd=0)
        fixLabel0.grid(row=4, column=0, columnspan=10, sticky=W+E)
        fixLabel0.config(background="#d9d9d9")
        fixLabel1=Label(fixFrame2, text="Διόρθωση στοιχείων ραντεβού", fg="#000080", pady=10)
        fixLabel1.grid(row=3, padx=30, column=0, columnspan=10)
        fixAa1=Label(fixLabel0, text="Α/Α", fg="#000080", bg="#d9d9d9", padx=30)
        fixAa1.grid(row=5, column=0, sticky=W+E)
        fixAmka1=Label(fixLabel0, text="ΑΜΚΑ", padx=30, fg="#000080", bg="#d9d9d9")
        fixAmka1.grid(row=5, column=1, sticky=W+E)
        fixSurname1=Label(fixLabel0, padx=30, text="Επώνυμο", fg="#000080", bg="#d9d9d9")
        fixSurname1.grid(row=5, column=2, sticky=W+E)
        fixName1=Label(fixLabel0, padx=30, text="Όνομα", fg="#000080", bg="#d9d9d9")
        fixName1.grid(row=5, column=3, sticky=W+E)
        fixHospital1=Label(fixLabel0, padx=30, text="Ιατρείο", fg="#000080", bg="#d9d9d9")
        fixHospital1.grid(row=5, column=4, sticky=W+E)
        fixPriority1=Label(fixLabel0, padx=30, text="Προτεραιότητα", fg="#000080", bg="#d9d9d9")
        fixPriority1.grid(row=5, column=5, sticky=W+E)
        fixDate1=Label(fixLabel0, padx=30, text="Ημ/νία ραντεβού", fg="#000080", bg="#d9d9d9")
        fixDate1.grid(row=5, column=6, sticky=W+E)
        fixTime1=Label(fixLabel0, padx=30, text="Ώρα ραντεβού", fg="#000080", bg="#d9d9d9")
        fixTime1.grid(row=5, column=7, sticky=W+E)
        fixNotes1=Label(fixLabel0, padx=30, text="Παρατηρήσεις", fg="#000080", bg="#d9d9d9")
        fixNotes1.grid(row=5, column=8, sticky=W+E)
        amka2=fixAmka2.get()
        amka2=amka2.split() #κόψιμο κενών ανάμεσα στα ψηφία του ΑΜΚΑ
        amka=""
        for x in amka2:
            amka=amka+x
        amka=amka.strip()        
        for i in range(len(newList)):
            global fixChoice2            
            surname=newList[i][1]
            name=newList[i][2]
            hospital=newList[i][3]
            priority=newList[i][4]
            valid=newList[i][5]
            wra=newList[i][6]
            notes=newList[i][7]           
            fixAa2=Label(fixFrame2, padx=30, text=i+1, fg="#000080")
            fixAa2.grid(row=6+i, column=0, sticky=W)            
            fixAmka4=Label(fixFrame2, padx=30, text=amka, fg="#000080")  
            fixAmka4.grid(row=6+i, column=1, sticky=W)
            fixAmka2.grid_forget()
            fixSurname2=Label(fixFrame2, padx=30,  fg="#000080", text=surname.upper())
            fixSurname2.grid(row=6+i, column=2, sticky=W)
            fixName2=Label(fixFrame2, padx=30,  fg="#000080", text=name.upper())                       
            fixName2.grid(row=6+i, column=3, sticky=W)       
            fixHospital2=Label(fixFrame2, padx=30, fg="#000080", text=hospital.upper()) 
            fixHospital2.grid(row=6+i, column=4, sticky=W)
            fixPriority2=Label(fixFrame2, padx=30, fg="#000080", text=priority.upper())
            fixPriority2.grid(row=6+i, column=5, sticky=W)
            fixDate2=Label(fixFrame2, padx=30, fg="#000080", text=valid[-2:]+"-"+valid[-4:-2]+"-"+valid[:-4])
            fixDate2.grid(row=6+i, column=6, sticky=W)
            fixTime2=Label(fixFrame2, padx=30, fg="#000080", text=wra.upper())
            fixTime2.grid(row=6+i, column=7, sticky=W)            
            fixNotes2=Label(fixFrame2, padx=30, fg="#000080", text=notes.upper())
            fixNotes2.grid(row=6+i, column=8, sticky=W)
            fixChoice1=Label(fixFrame2, padx=30, text="Επιλογή Α/Α ραντεβού για διόρθωση:", fg="#000080")
            fixChoice1.grid(row=999, column=4, padx=20)
            fixChoice2=Entry(fixFrame2, width=50, borderwidth=5, relief=SUNKEN, fg="#000080", bg="#d9d9d9")
            fixChoice2.grid(row=999, column=5, pady=10, padx=20)                                
            submit3=Button(fixFrame2, bg="#000080", fg="#ffffff", text="Υποβολή", padx=35, pady=11, command=lambda: goto(10)) 
            submit3.grid(row=999, column=6, pady=10)                                               
            fixCancel=Button(fixFrame2, text="Κεντρικό μενού", padx=30, pady=11, fg="#ffffff", bg="#000080", command=lambda: goto(11)) 
            fixCancel.grid(row=1001, column=0, columnspan=10, pady=10)
    elif x==10: #υποβολή της επιλεγμένης εγγραφής ραντεβού για διόρθωση στοιχείων
        global num3
        num3=fixChoice2.get()
        num3=num3.strip()
        if num3.isdigit():
            num3=int(num3) 
            if (num3>0 and num3<=len(newList)):
                #surname=newList[int(num3)-1][1]
                #name=newList[int(num3)-1][2]
                fixFrame2.grid_forget()
                checkData(2)
        else:
            fixChoice2.delete(0, END)
            enterNumAgain=Label(fixFrame2, text="Μη έγκυρη επιλογή, παρακαλώ επιλέξτε έναν Α/Α από 1 έως "+str(len(newList)), fg="#000080", pady=10)
            enterNumAgain.grid(row=1000, column=0, columnspan=10)
    elif x==11: #επιστροφή στο κεντρικό μενού πριν από την υποβολή της φόρμας για διόρθωση στοιχείων (ακύρωση και επιστροφή)
        fixFrame2.grid_forget()
        menu()
    elif x==12: #ολοκλήρωση διόρθωσης ραντεβού
        valid=checkDate(fixNewDate2.get())
        fixChange1.grid_forget()
        global fixChange2
        fixChange2=LabelFrame(root, bd=0)
        fixChange2.grid(row=4, column=0,  columnspan=10)
        if valid==0:
            y = str(datetime.date.today())  #current date
            y=y.split('-')
            y="".join(y)
            fixCancelMessage=Label(fixChange2, fg="#000080", pady=25, text="Δεν μπορεί να γίνει διόρθωση, διότι η ημερομηνία για το συγκεκριμένο ραντεβού είναι προγενέστερη της σημερινής ("+x[-2:]+"-"+x[-4:-2]+"-"+x[:4] + "), η ενέργεια ακυρώθηκε.")
            fixCancelMessage=Label(row=4, column=0, columnspan=10, pady=15)
            fixNew2=Button(fixChange2, text="Νέα διόρθωση", fg="#ffffff", bg="#000080", padx=30, pady=11, command=lambda: goto(13)) 
            fixNew2.grid(row=5, column=4, padx=40)            
            fixReturn=Button(fixChange2, text="Κεντρικό μενού", padx=30, pady=11, fg="#ffffff", bg="#000080", command=lambda: goto(14)) 
            fixReturn.grid(row=5, column=5, padx=40)
        else:
            for x in alter:
                num=fixChoice2.get()
                if x==newList[int(num)-1]:
                    hospital=fixNewHospital2.get()
                    priority=fixNewPriority2.get()
                    day=checkDate(fixNewDate2.get())
                    time=fixNewTime2.get()
                    notes=fixNewNotes2.get()
                    x[3]=hospital.upper()
                    x[4]=priority.upper()
                    x[5]=day.upper()
                    x[6]=time.upper()
                    x[7]=notes.upper()
            with open("current.csv", "w", newline="", encoding="utf-8") as file:
                wo=csv.writer(file, delimiter='$')
                for x in alter:
                    wo.writerow(x)
                fixSuccessMessage=Label(fixChange2, text="Η διόρθωση του ραντεβού έγινε με επιτυχία.", fg="#000080")
                fixSuccessMessage.grid(row=10, column=0, columnspan=10, pady=15)                                                     
                fixReturn2=Button(fixChange2, text="Κεντρικό μενού", padx=30, pady=11, fg="#ffffff", bg="#000080", command=lambda: goto(15)) 
                fixReturn2.grid(row=20, column=5, columnspan=10) 
    elif x==13: #νέα διορθωση ραντεβού μετά από σφάλμα στην ημ/νία καταχώρησης
        fixChange1.grid_forget()
        insert(2)
    elif x==14: #επιστροφή στο κεντρικό μενού μετά από σφάλμα στην ημ/νία καταχώρησης
        #fixChange1.grid_forget()
        fixChange2.grid_forget()
        menu()
    elif x==15: #επιστροφή στο κεντρικό μενού μετά από επιτυχημένη διόρθωση ραντεβού
        fixChange2.grid_forget()
        menu()        
    elif x==16: #ακύρωση ραντεβού (έλεγχος ύπαρξης ή όχι του ΑΜΚΑ)
        amka2=delSearch2.get()
        amka2=amka2.split() #κόψιμο κενών ανάμεσα στα ψηφία του ΑΜΚΑ
        amka=""
        for i in amka2:
            amka=amka+i
        amka=amka.strip()        
        amka=amka.strip()
        delFrame1=LabelFrame(root, bd=0)
        delFrame1.grid(row=4, column=0, columnspan=10)
        if amka.isdigit() and len(amka)==11: #έλεγχος ορθότητας ΑΜΚΑ       
            with open("current.csv", "r", newline="", encoding="utf-8") as file:
                ro=csv.reader(file, delimiter='$')
                for row in sorted(ro, key=lambda j:j[5]):
                    delete.append(row)
                for x in delete:
                    if amka == x[0]:
                        deleteList.append(x)
                if len(deleteList)==0:
                    global message1
                    message1="Δεν υπάρχει καταχωρημένο ραντεβού προσεχώς με αυτόν τον ΑΜΚΑ, η ενέργεια ακυρώθηκε."
                    delError=Label(delFrame, text=message1, fg="#000080", pady=15)
                    delError.grid(row=90, column=0, columnspan=10)
                    delNew=Button(delFrame, text="Νέα ακύρωση", padx=30, pady=11, fg="#ffffff", bg="#000080", command=lambda: goto(17)) 
                    delNew.grid(row=100, column=4, pady=15, padx=25)            
                    delReturn=Button(delFrame, text="Κεντρικό μενού", padx=30, pady=11, fg="#ffffff", bg="#000080", command=lambda: goto(18))
                    delReturn.grid(row=100, column=5, pady=15, padx=25)                                              
                else:
                    goto(19)                     
        else:
            delNextStep1.grid_forget()
            message1="Δεν είναι σωστή η καταχώρηση, ο ΑΜΚΑ πρέπει να περιέχει (11) ψηφία."
            delError=Label(delFrame, text=message1, fg="#000080", pady=15)
            delError.grid(row=90, column=0, columnspan=10)
            delNew=Button(delFrame, text="Νέα ακύρωση", padx=30, pady=11, fg="#ffffff", bg="#000080", command=lambda: goto(17)) 
            delNew.grid(row=100, column=4, pady=15, padx=25)            
            delReturn=Button(delFrame, text="Κεντρικό μενού", padx=30, pady=11, fg="#ffffff", bg="#000080", command=lambda: goto(18))
            delReturn.grid(row=100, column=5, pady=15, padx=25)
    elif x==17: #νέα ακύρωση ραντεβού
        delFrame.grid_forget()
        insert(3)
    elif x==18: #επιστροφή στο κύριο μενού από την ακύρωση ραντεβού
        delFrame.grid_forget()
        menu()
    elif x==19: #Αναζήτηση της λίστας που περιλαμβάνει όλες τις πιθανές εγγραφές ραντεβού για ακύρωση
        global delChoice2
        global delFrame2
        global delFrame3
        global delSurname1
        global delSurname2
        global delName1
        global delName2
        global delAmka6                            
        global delHospital1
        global delHospital2
        global delPriority1
        global delPriority2
        global delDate1
        global delDate2
        global delTime1 
        global delTime2
        global delNotes1 
        global delNotes2
        delSearch0.grid_forget() 
        delSearch1.grid_forget()
        delSearch2.grid_forget()
        delNextStep1.grid_forget()        
        delFrame2=LabelFrame(delFrame, bd=0) #το frame που όλα τα στοιχεία των εγγραφών με βάση τον ΑΜΚΑ που δόθηκε από τον χρήστη
        delFrame2.grid(row=4, column=0, columnspan=10)
        delLabel=Label(delFrame2, text="Ακύρωση ραντεβού", fg="#000080", pady=10)
        delLabel.grid(row=4, column=0, sticky=W+E, columnspan=10)
        delAa1=Label(delFrame2, text="Α/Α", fg="#000080")
        delAa1.grid(row=5, column=0, sticky=W, padx=20)
        delAmka1=Label(delFrame2, text="ΑΜΚΑ", fg="#000080")
        delAmka1.grid(row=5, column=1, sticky=W, padx=20)
        delSurname1=Label(delFrame2, text="Επώνυμο", fg="#000080")
        delSurname1.grid(row=5, column=2, sticky=W, padx=20)
        delName1=Label(delFrame2, text="Όνομα", fg="#000080")
        delName1.grid(row=5, column=3, sticky=W, padx=20)
        delHospital1=Label(delFrame2, text="Ιατρείο", fg="#000080")
        delHospital1.grid(row=5, column=4, sticky=W, padx=20)
        delPriority1=Label(delFrame2, text="Προτεραιότητα", fg="#000080")
        delPriority1.grid(row=5, column=5, sticky=W, padx=20)
        delDate1=Label(delFrame2, text="Ημ/νία ραντεβού", fg="#000080")
        delDate1.grid(row=5, column=6, sticky=W, padx=20)
        delTime1=Label(delFrame2, text="Ώρα ραντεβού", fg="#000080")
        delTime1.grid(row=5, column=7, sticky=W, padx=20)
        delNotes1=Label(delFrame2, text="Παρατηρήσεις", fg="#000080")
        delNotes1.grid(row=5, column=8, sticky=W, padx=20)
        amka2=delSearch2.get()
        amka2=amka2.split() #κόψιμο κενών ανάμεσα στα ψηφία του ΑΜΚΑ
        amka=""
        for i in amka2:
            amka=amka+i
        amka=amka.strip()        
        amka=amka.strip()
        for i in range(len(deleteList)):
            surname=deleteList[i][1]
            name=deleteList[i][2]
            hospital=deleteList[i][3]
            priority=deleteList[i][4]
            valid=deleteList[i][5]
            wra=deleteList[i][6]
            notes=deleteList[i][7]          
            delAa2=Label(delFrame2, text=i+1, fg="#000080")
            delAa2.grid(row=6+i, column=0, sticky=W, padx=20)
            delAmka2=Label(delFrame2, text=amka, fg="#000080")
            delAmka2.grid(row=6+i, column=1, sticky=W, padx=20)             
            delSurname2=Label(delFrame2,  fg="#000080", text=surname.upper())
            delSurname2.grid(row=6+i, column=2, sticky=W, padx=20)
            delName2=Label(delFrame2,  fg="#000080", text=name.upper())                       
            delName2.grid(row=6+i, column=3, sticky=W, padx=20)       
            delHospital2=Label(delFrame2, fg="#000080", text=hospital.upper())
            delHospital2.grid(row=6+i, column=4, sticky=W, padx=20)
            delPriority2=Label(delFrame2, fg="#000080", text=priority.upper())
            delPriority2.grid(row=6+i, column=5, sticky=W, padx=20)
            delDate2=Label(delFrame2, fg="#000080", text=valid[-2:]+"-"+valid[-4:-2]+"-"+valid[:-4])
            delDate2.grid(row=6+i, column=6, sticky=W, padx=20)
            delTime2=Label(delFrame2, fg="#000080", text=wra.upper())
            delTime2.grid(row=6+i, column=7, sticky=W, padx=20)            
            delNotes2=Label(delFrame2, fg="#000080", text=notes.upper())
            delNotes2.grid(row=6+i, column=8, sticky=W, padx=20)
            delFrame3=LabelFrame(delFrame, bd=0) #frame μόνο για τα κουμπιά στο τέλος, ώστε στο από πάνω frame (delFrame2) να γίνεται η εναλλαγή των δεδομένων
            delFrame3.grid(row=1000, column=0, columnspan=10)            
            delChoice1=Label(delFrame3, text="Επιλογή Α/Α ραντεβού για ακύρωση:", fg="#000080", pady=15)
            delChoice1.grid(row=999, column=4, padx=20)
            delChoice2=Entry(delFrame3, width=50, borderwidth=5, relief=SUNKEN, fg="#000080", bg="#d9d9d9")
            delChoice2.grid(row=999, column=5, padx=20)                                
            submit3=Button(delFrame3, bg="#000080", fg="#ffffff", text="Υποβολή", padx=35, pady=11, command=lambda: goto(20)) 
            submit3.grid(row=1001, column=4, pady=15, padx=20)                                               
            delCancel=Button(delFrame3, text="Κεντρικό μενού", padx=30, pady=11, fg="#ffffff", bg="#000080", command=lambda: goto(21)) 
            delCancel.grid(row=1001, column=5, pady=15, padx=20)
    elif x==20: #υποβολή της επιλεγμένης εγγραφής ραντεβού για ακύρωση
        global delFrame4
        global delValid2
        global delValid4
        global delFalse2
        global change2        
        change2=delChoice2.get() #change2--> o A/A του ραντεβού που ανιχνεύθηκε από το πρόγραμμα σύμφωνα με τα κριτήρια αναζήτησης
        change2=change2.strip()        
        if (not change2.isdigit()) or int(change2)<1 or int(change2)>len(deleteList):         
            delFalse2=Label(delFrame2, fg="#000080", text="Λανθασμένη επιλογή, αποδεκτές τιμές: (1-"+str(len(deleteList))+"), η ενέργεια ακυρώθηκε.")
            delFalse2.grid(row=1000, column=0, columnspan=10, pady=15)
            delReturn2=Button(delFrame3, text="Νέα ακύρωση", bg="#000080", fg="#ffffff", padx=35, pady=11, command=lambda: goto(22)) 
            delReturn2.grid(row=1001, column=4, pady=15)
            delCancel=Button(delFrame3, text="Κεντρικό μενού", padx=30, pady=11, fg="#ffffff", bg="#000080", command=lambda: goto(21)) 
            delCancel.grid(row=1001, column=5, pady=15)
        else:
            global delSummary
            global delAmka5
            global delSubmit
            global delCancel2
            global elSubmit
            global delCancel2
            global delFrame5            
            amka2=delSearch2.get()
            amka2=amka2.split() #κόψιμο κενών ανάμεσα στα ψηφία του ΑΜΚΑ
            amka=""
            for i in amka2:
                amka=amka+i
            amka=amka.strip()            
            amka=amka.strip()
            num2=delChoice2.get() #A/A
            surname=deleteList[int(num2)-1][1]
            name=deleteList[int(num2)-1][2]
            hospital=deleteList[int(num2)-1][3]
            priority=deleteList[int(num2)-1][4]
            valid=deleteList[int(num2)-1][5]
            wra=deleteList[int(num2)-1][6]
            notes=deleteList[int(num2)-1][7]
            delFrame.grid_forget()
            delFrame5=LabelFrame(root, bd=0)
            delFrame5.grid(row=4, column=0, columnspan=10)            
            delSummary=Label(delFrame5, text="Στοιχεία ραντεβού για ακύρωση:", fg="#000080", pady=15)
            delSummary.grid(row=4, column=0, columnspan=10)
            delAmka5=Label(delFrame5, text="ΑΜΚΑ:", fg="#000080")
            delAmka5.grid(row=5, column=4)
            delAmka6=Label(delFrame5, text=amka, fg="#000080") 
            delAmka6.grid(row=5, column=5)                
            delSurname1=Label(delFrame5, text="Επώνυμο:", fg="#000080")
            delSurname1.grid(row=6, column=4)
            delSurname2=Label(delFrame5, text=surname.upper(), fg="#000080") 
            delSurname2.grid(row=6, column=5)                
            delName1=Label(delFrame5, text="Όνομα:", fg="#000080")
            delName1.grid(row=7, column=4)
            delName2=Label(delFrame5, text=name.upper(), fg="#000080") 
            delName2.grid(row=7, column=5)
            delHospital1=Label(delFrame5, text="Ιατρείο:", fg="#000080")
            delHospital1.grid(row=8, column=4)
            delHospital2=Label(delFrame5, text=hospital.upper(), fg="#000080") 
            delHospital2.grid(row=8, column=5)
            delPriority1=Label(delFrame5, text="Προτεραιότητα:", fg="#000080")
            delPriority1.grid(row=9, column=4)
            delPriority2=Label(delFrame5, text=priority.upper(), fg="#000080") 
            delPriority2.grid(row=9, column=5)
            delDate1=Label(delFrame5, text="Ημ/νία ραντεβού:", fg="#000080")
            delDate1.grid(row=10, column=4)
            delDate2=Label(delFrame5, text=valid[-2:]+"-"+valid[-4:-2]+"-"+valid[:-4], fg="#000080") 
            delDate2.grid(row=10, column=5)
            delTime1=Label(delFrame5, text="Ώρα ραντεβού:", fg="#000080")
            delTime1.grid(row=11, column=4)
            delTime2=Label(delFrame5, text=wra.upper(), fg="#000080") 
            delTime2.grid(row=11, column=5)
            delNotes1=Label(delFrame5, text="Παρατηρήσεις:", fg="#000080")
            delNotes1.grid(row=12, column=4)
            delNotes2=Label(delFrame5, text=notes.upper(), fg="#000080") 
            delNotes2.grid(row=12, column=5)
            delSubmit=Button(delFrame5, text="Οριστική διαγραφή", padx=35, pady=11, fg="#ffffff", bg="#000080", command=lambda: goto(23)) 
            delSubmit.grid(row=50, column=5, pady=15, padx=20)
            delCancel2=Button(delFrame5, text="Κεντρικό μενού", padx=40, pady=11, fg="#ffffff", bg="#000080", command=lambda: goto(24)) 
            delCancel2.grid(row=50, column=4, pady=15, padx=20)
    elif x==21: #επιστροφή στο κύριο μενού από την ακύρωση ραντεβού (από ΔΥΟ διαφορετικά σημεία)
        delFrame.grid_forget()
        menu()      
    elif x==22: #επανάληψη εισόδου Α/Α για ακύρωση ραντεβού
        delFrame.grid_forget()
        insert(3)      
    elif x==23: #τελική φάση ακύρωσης ραντεβού
        delFrame2.grid_forget() #απενεργοποίηση του κουμπιού εισαγωγής για την ενέργεια της διόρθωσης στοιχείων
        delFrame5.grid_forget()
        delFrame4=LabelFrame(root, bd=0)
        delFrame4.grid(row=4, column=0, columnspan=10)
        delValid0=Label(delFrame4, text="Για να πραγματοποιηθεί διαγραφή ραντεβού από το σύστημα πρέπει να διαθέτετε \nδικαίωμα πρόσβασης στη βάση δεδομένων. Παρακαλώ εισάγετε στοιχεία χρήστη:", fg="#000080")
        delValid0.grid(row=5, column=0, columnspan=10, pady=10)
        delValid1=Label(delFrame4, text="Username:", fg="#000080")
        delValid1.grid(row=6, column=4, padx=20, pady=15)                
        delValid2=Entry(delFrame4, bg="#d9d9d9", fg="#000080", relief=SUNKEN, borderwidth=5, width=50)
        delValid2.grid(row=6, column=5, padx=20, pady=15)
        delValid3=Label(delFrame4, text="Password:", fg="#000080")
        delValid3.grid(row=7, column=4, padx=20)                
        delValid4=Entry(delFrame4, bg="#d9d9d9", fg="#000080", relief=SUNKEN, borderwidth=5, width=50)
        delValid4.grid(row=7, column=5, padx=20)
        delValidSubmit=Button(delFrame4, text="Υποβολή", padx=35, pady=11, fg="#ffffff", bg="#000080", command=lambda: goto(25)) 
        delValidSubmit.grid(row=8, column=0, columnspan=10, pady=15)        
    elif x==24: #ακύρωση ενέργειας διαγραφής ραντεβού και επιστροφή στο κεντρικό μενού
        delFrame5.grid_forget()
        menu()
    elif x==25: #ολοκλήρωση ακύρωσης διαγραφής μετά από επαλήθευση των δικαιωμάτων πρόσβασης (Username/Password)
        with open("password.csv", "r", newline="", encoding="utf-8") as file:
            ro=csv.reader(file, delimiter='$')
            for row in ro:
                checkLogin.append(row)
            if len(checkLogin)==0:
                message="Παρακαλώ πολύ επικοινωνήστε με την προγραμματίστρια, κωδικός σφάλματος: EMPTY_PASSWORD_0." #το αρχείο με τους κωδικούς είναι άδειο (ΟΧΙ το backup του...)
            else:
                username=delValid2.get()
                password=delValid4.get()
                username=username.strip()
                password=password.strip()
                checkIn=[username.upper(), password.upper()]                         
                for x in checkLogin:
                    if checkIn==x:
                        for i in range(len(delete)):
                            if delete[i]==deleteList[int(change2)-1]:
                                delete.pop(i)
                                break
                        with open("current.csv", "w", newline="", encoding="utf-8") as file:
                            wo=csv.writer(file, delimiter='$')
                            for x in delete:
                                wo.writerow(x)
                                #wait(3)
                                message="Η ακύρωση πραγματοποιήθηκε με επιτυχία, το ραντεβού διαγράφηκε οριστικά από το σύστημα."
                            break
                    elif x==checkLogin[-1]:
                        message="Αποτυχία επιβεβαίωσης στοιχείων πρόσβασης, το αίτημα διαγραφής απορρίφθηκε."
                        break       
        delMessage=Label(delFrame4, text=message, fg="#000080")
        delMessage.grid(row=70, column=0, columnspan=10, pady=20)
        delAgain=Button(delFrame4, text="Νέα ακύρωση", fg="#ffffff", bg="#000080", padx=30, pady=11, command=lambda: goto(26))
        delAgain.grid(row=100, column=4, padx=20)
        delReturnMenu=Button(delFrame4, text="Κεντρικό μενού", fg="#ffffff", bg="#000080", padx=30, pady=11, command=lambda: goto(27)) 
        delReturnMenu.grid(row=100, column=5, padx=20)
    elif x==26: #νέα ακύρωση ραντεβού
        delFrame4.grid_forget()
        insert(3)
    elif x==27: #επιστροφή στο κεντρικό μενού μετά από ενέργεια ακύρωσης ραντεβού
        delFrame4.grid_forget()
        menu()        
    elif x==28: #Αναζήτηση ραντεβού με βάση τον ΑΜΚΑ (ατομικό ιστορικό)
        global viewShowAmka2
        global viewShowAmka4
        global viewFrame5
        global viewShowAmkaSubmit
        global viewShowAmkaSearch2
        global viewShowDaySubmit
        global flag #δείκτης, 1-->με βάση τον ΑΜΚΑ, 2-->με βάση την ημ/νία, 3, 4, 5, 6--> με βάση την προτεραιότητα
        flag=1
        viewFrame2.grid_forget()
        viewFrame5=LabelFrame(root, bd=0)
        viewFrame5.grid(row=4, column=0, columnspan=10)
        viewShowAmkaLabel=Label(viewFrame5, text="Αναζήτηση ραντεβού με βάση τον ΑΜΚΑ (ατομικό ιστορικό)", fg="#000080", pady=15)
        viewShowAmkaLabel.grid(row=5, column=0, columnspan=10)        
        viewShowAmkaSearch1=Label(viewFrame5, text="ΑΜΚΑ:", pady=15, fg="#000080")
        viewShowAmkaSearch1.grid(row=6, column=4, padx=5)
        viewShowAmkaSearch2=Entry(viewFrame5, width=50, borderwidth=5, relief=SUNKEN, bg="#d9d9d9", fg="#000080")
        viewShowAmkaSearch2.grid(row=6, column=5, padx=5)
        viewShowDaySubmit=Button(viewFrame5, text=" Υποβολή", bg="#000080", fg="#ffffff", padx=30, pady=11, command=lambda: goto(31)) 
        viewShowDaySubmit.grid(row=100, column=4, padx=65, pady=15)
        viewShowDayReturn=Button(viewFrame5, text="<<Επιστροφή", bg="#000080", fg="#ffffff", padx=30, pady=11, command=lambda: goto(45)) 
        viewShowDayReturn.grid(row=100, column=5, padx=65, pady=15)               
    elif x==29: #Αναζήτηση ραντεβού με βάση την ημερομηνία
        global viewShowDay2
        global viewShowDay4
        global viewFrame3        
        flag=2
        viewFrame2.grid_forget()
        viewFrame3=LabelFrame(root, bd=0)
        viewFrame3.grid(row=4, column=0, columnspan=10)
        viewShowDayLabel=Label(viewFrame3, text="Αναζήτηση ραντεβού με βάση την ημερομηνία", fg="#000080", pady=15)
        viewShowDayLabel.grid(row=5, column=0, columnspan=10)
        viewShowDay1=Label(viewFrame3, text="Αρχική ημερομηνία:", fg="#000080")
        viewShowDay1.grid(row=6, column=4, padx=5, pady=10)
        viewShowDay2=Entry(viewFrame3, width=50, fg="#000080", bg="#d9d9d9", borderwidth=5, relief=SUNKEN)
        viewShowDay2.grid(row=6, column=5, padx=5, pady=10)        
        viewShowDay3=Label(viewFrame3, text="Τελική ημερομηνία:", fg="#000080")
        viewShowDay3.grid(row=7, column=4, padx=5, pady=10)
        viewShowDay4=Entry(viewFrame3, width=50, fg="#000080", bg="#d9d9d9", borderwidth=5, relief=SUNKEN)
        viewShowDay4.grid(row=7, column=5, padx=5, pady=10)
        viewShowDaySubmit=Button(viewFrame3, text=" Υποβολή", bg="#000080", fg="#ffffff", padx=30, pady=11, command=lambda: goto(32)) 
        viewShowDaySubmit.grid(row=100, column=0, columnspan=10, pady=15)        
    elif x==30: #Αναζήτηση ραντεβού με βάση την προτεραιότητα
        global viewShowPriority2
        global viewShowPriority4
        global viewShowPrioritySubmit
        global viewShowPrioritySearch2
        global viewShowPriorityLabel
        flag=3
        viewFrame2.grid_forget()
        viewFrame5=LabelFrame(root, bd=0)
        viewFrame5.grid(row=4, column=0, columnspan=10)
        viewShowPriorityLabel=Label(viewFrame5, text="Αναζήτηση ραντεβού με βάση την προτεραιότητα", fg="#000080", pady=15)
        viewShowPriorityLabel.grid(row=5, column=0, columnspan=10)
        viewLow=Button(viewFrame5, text="Χαμηλή", padx=44, pady=11, fg="#ffffff", bg="#000080", command=lambda: checkPriority(1,0)) 
        viewLow.grid(row=10, column=4, padx=65, pady=45)
        viewMedium=Button(viewFrame5, text="Μέτρια", padx=45, pady=11, fg="#ffffff", bg="#000080", command=lambda: checkPriority(2,0)) 
        viewMedium.grid(row=10, column=5, padx=65, pady=45)
        viewHigh=Button(viewFrame5, text="Υψηλή", padx=47, pady=11, fg="#ffffff", bg="#000080", command=lambda: checkPriority(3,0)) 
        viewHigh.grid(row=10, column=6, padx=65, pady=45)
    elif x==31: #έλεγχος ΑΜΚΑ και ανακατεύθυνση για εκτύπωση αποτελεσμάτων (flag=1)  -->goto()
        amka2=viewShowAmkaSearch2.get()
        amka2=amka2.split() #κόψιμο κενών ανάμεσα στα ψηφία του ΑΜΚΑ
        amka=""
        for i in amka2:
            amka=amka+i
        amka=amka.strip()        
        amka=amka.strip()
        if amka.isdigit() and len(amka)==11:
            with open("previous.csv", "r", newline="", encoding="utf-8") as file:
                ro=csv.reader(file, delimiter='$')
                for row in ro:
                    checkList.append(row)
            with open("current.csv", "r", newline="", encoding="utf-8") as file:
                ro=csv.reader(file, delimiter='$')
                for row in ro:
                    checkList.append(row)
                for x in checkList:
                    if x[0]==amka and x not in dateList:
                        dateList.append(x)
                checkList.clear()
            goto(34)
        else:
            global viewErrorAmka
            global viewErrorAmkaNew
            global viewErrorAmkaCancel
            global viewFrame7
            viewFrame7=LabelFrame(root, bd=0)
            viewFrame7.grid(row=6, column=0, columnspan=10)
            viewShowDaySubmit.grid_forget()
            messagebox.showerror('Λανθασμένος ΑΜΚΑ:', 'Δεν είναι σωστή η καταχώρηση, ο ΑΜΚΑ πρέπει να περιέχει (11) ψηφία.')
            #viewErrorAmka=Label(viewFrame7, text="Δεν είναι σωστή η καταχώρηση, ο ΑΜΚΑ πρέπει να περιέχει (11) ψηφία.", fg="#000080")
            #viewErrorAmka.grid(row=50, column=0, columnspan=10, pady=15)
            viewErrorAmkaNew=Button(viewFrame7, text="Νέα αναζήτηση", padx=30, pady=11, fg="#ffffff", bg="#000080", command=lambda: goto(35))
            viewErrorAmkaNew.grid(row=120, column=4, padx=20, pady=15) 
            viewErrorAmkaCancel=Button(viewFrame7, text="Κεντρικό μενού", padx=30, pady=11, fg="#ffffff", bg="#000080", command=lambda: goto(36)) 
            viewErrorAmkaCancel.grid(row=120, column=5, padx=20, pady=15)
    elif x==32: #Έλεγχος ημερομηνιών και ανακατεύθυνση για εκτύπωση αποτελεσμάτων (flag=2)
        global day1
        global day2
        global viewShowDayError
        global viewShowDayAgain1
        global viewShowDayReturn1
        viewShowDaySubmit.grid_forget()
        day1=viewShowDay2.get()
        day1=day1.strip()
        day1=checkDate(day1)                                         
        day2=viewShowDay4.get()
        day2=day2.strip()
        day2=checkDate(day2)
        if day1==0 or day2==0:
            viewShowDayError=Label(viewFrame3, text="Μη έγκυρη ημερομηνία.", fg="#000080")
            viewShowDayError.grid(row=20, column=0, columnspan=10, pady=15)
            viewShowDayAgain1=Button(viewFrame3, text="Νέα αναζήτηση", fg="#ffffff", bg="#000080", padx=35, pady=11, command=lambda: goto(37))                              
            viewShowDayAgain1.grid(row=30, column=4, padx=20, pady=10)                                
            viewShowDayReturn1=Button(viewFrame3, text="Κεντρικό μενου", fg="#ffffff", bg="#000080", padx=35, pady=11, command=lambda: goto(38))                            
            viewShowDayReturn1.grid(row=30, column=5, padx=20, pady=10)
        else:
            global flag2 #δείκτης ανακατεύθυνσης για την goto(31) (δύο περιπτώσεις)
            flag2=3
            y=str(datetime.date.today())  #current date
            y=y.split('-')
            y="".join(y)                    #current date as one string!            
            if day1>=y and day2>=y:
                with open("current.csv", "r", newline="", encoding="utf-8") as file:
                    ro=csv.reader(file, delimiter='$')
                    for row in ro:
                        checkList.append(row)
                    for x in checkList:
                        if x[6]>=day1 and x[6]<=day2:
                            dateList.append(x)
                    goto(39) #goto(37)
            elif day1<y and day2<y:
                with open("previous.csv", "r", newline="", encoding="utf-8") as file:
                    ro=csv.reader(file, delimiter='$')
                    for row in ro:
                        checkList.append(row)
                    for x in checkList:
                        if x[6]>=day1 and x[6]<=day2:
                            dateList.append(x)
                    goto(39) #goto(37))
            else:
                with open("previous.csv", "r", newline="", encoding="utf-8") as file:
                    ro=csv.reader(file, delimiter='$')
                    for row in ro:
                        checkList.append(row)
                    for x in checkList:
                        if x[6]>=day1 and x not in dateList:
                            dateList.append(x)
                    checkList.clear()
                with open("current.csv", "r", newline="", encoding="utf-8") as file:
                    ro=csv.reader(file, delimiter='$')
                    for row in ro:
                        checkList.append(row)
                    for x in checkList:
                        if x[6]<=day2 and x not in dateList:
                            dateList.append(x)                               
                    goto(39) 
    elif x==33: #επιλογή κριτιρίων Αναζήτησης με βάση την προτεραιότητα
        pass
        '''global viewShowPriority1
        global viewShowPriority2
        global viewShowPriority3
        global viewShowPriority4
        global priority2
        priority2=viewShowPrioritySearch2.get()
        priority2=priority2.strip()
        priority2=priority2.upper()
        if priority2 not in ['ΧΑΜΗΛΗ', 'ΜΕΤΡΙΑ', 'ΥΨΗΛΗ']:
            errorMessage=Label(viewFrame5, text="Μη έγκυρη τιμή, η ενέργεια ακυρώθηκε.", fg="#000080", pady=15)
            errorMessage.grid(row=200, column=0, columnspan=10)
            viewShowDayNew1=Button(viewFrame5, text="Νέα Αναζήτηση", fg="#ffffff", bg="#000080", padx=35, pady=11, command=lambda: goto(44))                           
            viewShowDayNew1.grid(row=500, column=4, padx=20, pady=10)
            viewShowDayReturn1=Button(viewFrame5, text="Κεντρικό μενού", fg="#ffffff", bg="#000080", padx=35, pady=11, command=lambda: goto(45))                         
            viewShowDayReturn1.grid(row=500, column=5, padx=20, pady=10)
        else:
        global viewFrame6
        viewFrame5.grid_forget()
        viewFrame6=LabelFrame(root, bd=0)
        viewFrame6.grid(row=4, column=0, columnspan=10)
        viewShowPriorityLabel=Label(viewFrame6, text="Επιλογή Αναζήτησης ραντεβού με βάση την προτεραιότητα:", fg="#000080", pady=15)
        viewShowPriorityLabel.grid(row=5, column=0, columnspan=10, pady=15)
        viewShowPriority1=Button(viewFrame6, text="Προσεχή", fg="#ffffff", bg="#000080", padx=35, pady=11, command=lambda: checkPriority(1)) 
        viewShowPriority1.grid(row=6, column=1, padx=30, pady=15)        
        viewShowPriority2=Button(viewFrame6, text="Παρελθόντα", fg="#ffffff", bg="#000080", padx=35, pady=11, command=lambda: checkPriority(2))
        viewShowPriority2.grid(row=6, column=3, padx=30, pady=15)
        viewShowPriority3=Button(viewFrame6, text="Συνολικά", fg="#ffffff", bg="#000080", padx=35, pady=11, command=lambda: checkPriority(3))
        viewShowPriority3.grid(row=6, column=5, padx=30, pady=15)
        viewShowPriority4=Button(viewFrame6, text="Με εύρος (από - μέχρι)", fg="#ffffff", bg="#000080", padx=35, pady=11, command=lambda: goto(41)) 
        viewShowPriority4.grid(row=6, column=7, padx=30, pady=15)'''
    elif x==34: #εκτύπωση αποτελεσμάτων στην οθόνη (ανακατεύθυνση από άλλο σημείο)
        global viewFrame4
        global viewShowResultsLabel
        global FrameForScroll2        
        #viewFrame4=LabelFrame(root, bd=0)
        #viewFrame4.grid(row=4, column=0, columnspan=10)
        Frame17.grid_forget()
        FrameForScroll2=LabelFrame(root, bd=0) #scrollbar attempt!!!
        FrameForScroll2.grid(row=5, column=0, columnspan=18)
        #ΝΑ ΕΛΕΓΞΩ ΤΙΣ ΔΙΑΣΤΑΣΕΙΣ ΤΟΥ MONITOR ΓΙΑ ΝΑ ΓΙΟΥΝ ADJUSTMENTS ΣΤΗΝ ΕΠΟΜΕΝΗ ΓΡΑΜΜΗ(HEIGHT, WIDTH)!!!
        canvas=Canvas(FrameForScroll2, bd=0, height=460, width=1220) 
        canvas.grid(row=0, column=0, columnspan=18, sticky=N+S+E+W)
        viewFrame4=LabelFrame(canvas, bd=0)
        scrollbar = Scrollbar(FrameForScroll2, orient="vertical", command=canvas.yview)
        scrollbar.grid(row=0, column=18, sticky=N+S)
        viewFrame4.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=viewFrame4, anchor="nw", width=2000)
        canvas.configure(yscrollcommand=scrollbar.set)    
        Frame100=LabelFrame(FrameForScroll2, bd=0)
        Frame100.grid(row=500, column=0, columnspan=18)
        viewShowDayResult2=Label(viewFrame4, text="ΠΡΟΒΟΛΗ ΙΑΤΡΙΚΩΝ ΡΑΝΤΕΒΟΥ ΕΞΥΠΗΡΕΤΟΥΜΕΝΩΝ", fg="#000080", bg= "#d9d9d9", pady=10)
        viewShowDayResult2.grid(row=5, column=0, columnspan=10, sticky=W+E)
        viewShowResultsAa2=Label(viewFrame4, text="A/A", fg="#000080")
        viewShowResultsAa2.grid(row=7, column=0, sticky=W, padx=20)
        viewShowResultsAmka2=Label(viewFrame4, text="AΜΚA", fg="#000080")
        viewShowResultsAmka2.grid(row=7, column=1, sticky=W, padx=20)
        viewShowResultsSurname2=Label(viewFrame4, text="ΕΠΩΝΥΜΟ", fg="#000080")
        viewShowResultsSurname2.grid(row=7, column=2, sticky=W, padx=20)
        viewShowResultsName2=Label(viewFrame4, text="ΟΝΟΜΑ", fg="#000080")
        viewShowResultsName2.grid(row=7, column=3, sticky=W, padx=20)
        viewShowResultsAkha2=Label(viewFrame4, text="ΑΚΗΑ", fg="#000080")
        viewShowResultsAkha2.grid(row=7, column=4, sticky=W, padx=20)        
        viewShowResultsHospital2=Label(viewFrame4, text="ΙΑΤΡΕΙΟ", fg="#000080")
        viewShowResultsHospital2.grid(row=7, column=5, sticky=W, padx=20)
        viewShowResultsPriority2=Label(viewFrame4, text="ΠΡΟΤΕΡΑΙΟΤΗΤΑ", fg="#000080")
        viewShowResultsPriority2.grid(row=7, column=6, sticky=W, padx=20)
        viewShowResultsDate2=Label(viewFrame4, text="ΗΜ/ΝΙΑ ΡΑΝΤΕΒΟΥ", fg="#000080")
        viewShowResultsDate2.grid(row=7, column=7, sticky=W, padx=20)
        viewShowResultsTime2=Label(viewFrame4, text="ΩΡΑ ΡΑΝΤΕΒΟΥ", fg="#000080")
        viewShowResultsTime2.grid(row=7, column=8, sticky=W, padx=20)                        
        viewShowResultsNotes2=Label(viewFrame4, text="ΠΑΡΑΤΗΡΗΣΕΙΣ", fg="#000080")
        viewShowResultsNotes2.grid(row=7, column=9, sticky=W, padx=20)                                                                    
        for i in range(len(dateList)):
            viewShowResultsAa4=Label(viewFrame4, text=i+1, fg="#000080")
            viewShowResultsAa4.grid(row=8+i, column=0, sticky=W, padx=20)
            viewShowResultsAmka4=Label(viewFrame4, text=dateList[i][0], fg="#000080")
            viewShowResultsAmka4.grid(row=8+i, column=1, sticky=W, padx=20)
            viewShowResultsSurname4=Label(viewFrame4, text=dateList[i][1], fg="#000080")
            viewShowResultsSurname4.grid(row=8+i, column=2, sticky=W, padx=20)
            viewShowResultsName4=Label(viewFrame4, text=dateList[i][2], fg="#000080")
            viewShowResultsName4.grid(row=8+i, column=3, sticky=W, padx=20)            
            viewShowResultsAkha4=Label(viewFrame4, text=dateList[i][3], fg="#000080")
            viewShowResultsAkha4.grid(row=8+i, column=4, sticky=W, padx=20)           
            viewShowResultsHospital4=Label(viewFrame4, text=dateList[i][4], fg="#000080")
            viewShowResultsHospital4.grid(row=8+i, column=5, sticky=W, padx=20)
            viewShowResultsPriority4=Label(viewFrame4, text=dateList[i][5], fg="#000080")
            viewShowResultsPriority4.grid(row=8+i, column=6, sticky=W, padx=20)
            viewShowResultsDate4=Label(viewFrame4, text=str(dateList[i][6][-2:]+"-"+dateList[i][6][-4:-2]+"-"+dateList[i][6][:-4]), fg="#000080")
            viewShowResultsDate4.grid(row=8+i, column=7, sticky=W, padx=20)
            viewShowResultsTime4=Label(viewFrame4, text=dateList[i][7], fg="#000080")
            viewShowResultsTime4.grid(row=8+i, column=8, sticky=W, padx=20)                        
            viewShowResultsNotes4=Label(viewFrame4, text=dateList[i][8], fg="#000080")
            viewShowResultsNotes4.grid(row=8+i, column=9, sticky=W, padx=20)
        if len(dateList)==0:
            message="Δε βρέθηκαν προγραμματισμένα ραντεβού με βάση τα κριτίρια αναζήτησης."          
            messagebox.showwarning('Ένημέρωση:', message)
            viewShowDayNew1=Button(viewFrame4, text="Νέα Αναζήτηση", fg="#ffffff", bg="#000080", padx=35, pady=11, command=lambda: goto(51))                              
            viewShowDayNew1.grid(row=500, column=4, padx=65, pady=10)
            viewShowDayReturn1=Button(viewFrame4, text="Κεντρικό μενού", fg="#ffffff", bg="#000080", padx=35, pady=11, command=lambda: goto(52))                             
            viewShowDayReturn1.grid(row=500, column=5, padx=65, pady=10)            
        else:
            pass
            '''if flag==1:
                message1="\n\n(ΑΜΚΑ: "+dateList[0][0]+"\nΕπώνυμο: "+dateList[0][1]+"\nΌνομα: "+dateList[0][2]+".)"
            elif flag==2:
                message1="\n\n(Ημερομηνίες από:"+day1[-2:]+"-"+day1[-4:-2]+"-"+day1[:-4]+" μέχρι "+day2[-2:]+"-"+day2[-4:-2]+"-"+day2[:-4]+".)"
            elif flag==3:
                    message1="\n\n(Προτεραιότητα: "+dateList[0][5]+" για τα προσεχή ραντεβού"+".)"
            elif flag==4:
                    message1="\n\n(Προτεραιότητα: "+dateList[0][5]+" για τα παρελθόντα ραντεβού"+".)"
            elif flag==5:
                    message1="\n\n(Προτεραιότητα: "+dateList[0][5]+" για όλα τα καταχωρημένα ραντεβού"+".)"
            elif flag==6:
                    message1="\n\n(Προτεραιότητα: "+dateList[0][5]+" για τα ραντεβού από "+day1[-2:]+"-"+day1[-4:-2]+"-"+day1[:-4]+" μέχρι "+day2[-2:]+"-"+day2[-4:-2]+"-"+day2[:-4]+".)"            
            #viewShowDayNew1=Button(Frame100, text="Νέα Αναζήτηση", fg="#ffffff", bg="#000080", padx=35, pady=11, command=lambda: goto(42))                              
            #viewShowDayNew1.grid(row=500, column=4, padx=65, pady=10)
            #viewShowDayReturn1=Button(Frame100, text="Κεντρικό μενού", fg="#ffffff", bg="#000080", padx=35, pady=11, command=lambda: goto(43))                             
            #viewShowDayReturn1.grid(row=500, column=5, padx=65, pady=10)            
            if len(dateList)==1:
                message="Βρέθηκε ένα ραντεβού με βάση τα κριτίρια αναζήτησης."
            else:
                message="Βρέθηκαν συνολικά "+str(len(dateList))+" ραντεβού με βάση τα κριτίρια αναζήτησης."

            messagebox.showinfo('Αποτελέσματα αναζήτησης:', message)#+message1)'''
        viewShowDayNew1=Button(Frame100, text="Νέα Αναζήτηση", fg="#ffffff", bg="#000080", padx=35, pady=11, command=lambda: goto(42))                              
        viewShowDayNew1.grid(row=500, column=4, padx=65, pady=10)
        viewShowDayReturn1=Button(Frame100, text="Κεντρικό μενού", fg="#ffffff", bg="#000080", padx=35, pady=11, command=lambda: goto(43))                             
        viewShowDayReturn1.grid(row=500, column=5, padx=65, pady=10)            
        checkList.clear()
        dateList.clear()        
    elif x==35: #καθαρισμός οθόνης μετά από αποτυχημένη είσοδο ΑΜΚΑ και νέα αναζήτηση ραντεβού
        viewFrame7.grid_forget()
        viewFrame5.grid_forget()
        viewFrame2.grid_forget()
        insert(7) 
    elif x==36: #καθαρισμός οθόνης μετά από αποτυχημένη είσοδο ΑΜΚΑ και επιστροφή στο κεντρικό μενού
        viewFrame7.grid_forget()
        viewFrame5.grid_forget()
        viewFrame2.grid_forget()
        menu()
    elif x==37: #καθαρισμός πεδίων και επανάληψη εισαγωγής ημερομηνιών για Αναζήτηση ραντεβού
        viewShowDayError.grid_forget()
        viewShowDay2.delete(0, END)
        viewShowDay4.delete(0, END)
        viewShowDayAgain1.grid_forget()
        viewShowDayReturn1.grid_forget()
        viewShowDaySubmit=Button(viewFrame3, text=" Υποβολή", bg="#000080", fg="#ffffff", padx=30, pady=11, command=lambda: goto(32))
        viewShowDaySubmit.grid(row=100, column=0, columnspan=10, pady=15)
    elif x==38: #επιστροφή στο κεντρικό μενού (από την ενέργεια Αναζήτηση ραντεβού με βάση την ημ/νία ή την προτεραιότητα)
        viewFrame3.grid_forget()
        menu()        
    elif x==39: #εκτύπωση αποτελεσμάτων στην οθόνη
        global viewShowResultsLabel
        viewShowDaySubmit.grid_forget()
        viewFrame3.grid_forget()               
        FrameForScroll2=LabelFrame(root, bd=0) #scrollbar attempt!!!
        FrameForScroll2.grid(row=5, column=0, columnspan=18)
        #viewFrame4=LabelFrame(FrameForScroll2, bd=0)
        #viewFrame4.grid(row=4, column=0, columnspan=10)         
        #ΝΑ ΕΛΕΓΞΩ ΤΙΣ ΔΙΑΣΤΑΣΕΙΣ ΤΟΥ MONITOR ΓΙΑ ΝΑ ΓΙΟΥΝ ADJUSTMENTS ΣΤΗΝ ΕΠΟΜΕΝΗ ΓΡΑΜΜΗ(HEIGHT, WIDTH)!!!
        canvas=Canvas(FrameForScroll2, bd=0, height=460, width=1220) 
        canvas.grid(row=0, column=0, columnspan=18, sticky=N+S+E+W)
        viewFrame4=LabelFrame(canvas, bd=0)
        scrollbar = Scrollbar(FrameForScroll2, orient="vertical", command=canvas.yview)
        scrollbar.grid(row=0, column=18, sticky=N+S)
        viewFrame4.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=viewFrame4, anchor="nw", width=2000)
        canvas.configure(yscrollcommand=scrollbar.set)        
        Frame100=LabelFrame(FrameForScroll2, bd=0)
        Frame100.grid(row=1000, column=0, columnspan=18)
        viewShowDayResult2=Label(viewFrame4, text="ΠΡΟΒΟΛΗ ΙΑΤΡΙΚΩΝ ΡΑΝΤΕΒΟΥ ΕΞΥΠΗΡΕΤΟΥΜΕΝΩΝ", fg="#000080", bg= "#d9d9d9", pady=15)
        viewShowDayResult2.grid(row=5, column=0, columnspan=10, sticky=W+E)
        viewShowResultsAa2=Label(viewFrame4, text="A/A", fg="#000080")
        viewShowResultsAa2.grid(row=7, column=0, sticky=W, padx=5)
        viewShowResultsAmka2=Label(viewFrame4, text="AΜΚA", fg="#000080")
        viewShowResultsAmka2.grid(row=7, column=1, sticky=W, padx=5)
        viewShowResultsSurname2=Label(viewFrame4, text="ΕΠΩΝΥΜΟ", fg="#000080")
        viewShowResultsSurname2.grid(row=7, column=2, sticky=W, padx=5)
        viewShowResultsName2=Label(viewFrame4, text="ΟΝΟΜΑ", fg="#000080")
        viewShowResultsName2.grid(row=7, column=3, sticky=W, padx=5)
        viewShowResultsAkha2=Label(viewFrame4, text="ΑΚΗΑ", fg="#000080")
        viewShowResultsAkha2.grid(row=7, column=4, sticky=W, padx=5)        
        viewShowResultsHospital2=Label(viewFrame4, text="ΙΑΤΡΕΙΟ", fg="#000080")
        viewShowResultsHospital2.grid(row=7, column=5, sticky=W, padx=5)
        viewShowResultsPriority2=Label(viewFrame4, text="ΠΡΟΤΕΡΑΙΟΤΗΤΑ", fg="#000080")
        viewShowResultsPriority2.grid(row=7, column=6, sticky=W, padx=5)
        viewShowResultsDate2=Label(viewFrame4, text="ΗΜ/ΝΙΑ ΡΑΝΤΕΒΟΥ", fg="#000080")
        viewShowResultsDate2.grid(row=7, column=7, sticky=W, padx=5)
        viewShowResultsTime2=Label(viewFrame4, text="ΩΡΑ ΡΑΝΤΕΒΟΥ", fg="#000080")
        viewShowResultsTime2.grid(row=7, column=8, sticky=W, padx=5)                       
        viewShowResultsNotes2=Label(viewFrame4, text="ΠΑΡΑΤΗΡΗΣΕΙΣ", fg="#000080")
        viewShowResultsNotes2.grid(row=7, column=9, sticky=W, padx=5)
        viewShowDayNew1=Button(Frame100, text="Νέα Αναζήτηση", fg="#ffffff", bg="#000080", padx=35, pady=11, command=lambda: goto(49))                          
        viewShowDayNew1.grid(row=10+len(dateList), column=4, padx=65, pady=10)
        viewShowDayReturn1=Button(Frame100, text="Κεντρικό μενού", fg="#ffffff", bg="#000080", padx=35, pady=11, command=lambda: goto(50))                         
        viewShowDayReturn1.grid(row=10+len(dateList), column=5, padx=65, pady=10)        
        for i in range(len(dateList)):
            viewShowResultsAa4=Label(viewFrame4, text=i+1, fg="#000080")
            viewShowResultsAa4.grid(row=8+i, column=0, sticky=W, padx=5)
            viewShowResultsAmka4=Label(viewFrame4, text=dateList[i][0], fg="#000080")
            viewShowResultsAmka4.grid(row=8+i, column=1, sticky=W, padx=5)
            viewShowResultsSurname4=Label(viewFrame4, text=dateList[i][1], fg="#000080")
            viewShowResultsSurname4.grid(row=8+i, column=2, sticky=W, padx=5)
            viewShowResultsName4=Label(viewFrame4, text=dateList[i][2], fg="#000080")
            viewShowResultsName4.grid(row=8+i, column=3, sticky=W, padx=5)
            viewShowResultsAkha4=Label(viewFrame4, text=dateList[i][3], fg="#000080")
            viewShowResultsAkha4.grid(row=8+i, column=4, sticky=W, padx=5)           
            viewShowResultsHospital4=Label(viewFrame4, text=dateList[i][4], fg="#000080")
            viewShowResultsHospital4.grid(row=8+i, column=5, sticky=W, padx=5)
            viewShowResultsPriority4=Label(viewFrame4, text=dateList[i][5], fg="#000080")
            viewShowResultsPriority4.grid(row=8+i, column=6, sticky=W, padx=5)            
            viewShowResultsDate4=Label(viewFrame4, text=str(dateList[i][6][-2:]+"-"+dateList[i][6][-4:-2]+"-"+dateList[i][6][:-4]), fg="#000080")
            viewShowResultsDate4.grid(row=8+i, column=7, sticky=W, padx=5)
            viewShowResultsTime4=Label(viewFrame4, text=dateList[i][7], fg="#000080")
            viewShowResultsTime4.grid(row=8+i, column=8, sticky=W, padx=5)                       
            viewShowResultsNotes4=Label(viewFrame4, text=dateList[i][8], fg="#000080")
            viewShowResultsNotes4.grid(row=8+i, column=9, sticky=W, padx=5)
            
        if len(dateList)==0:
            message="Δε βρέθηκαν προγραμματισμένα ραντεβού από "+day1[-2:]+"-"+day1[-4:-2]+"-"+day1[:-4]+" μέχρι "+day2[-2:]+"-"+day2[-4:-2]+"-"+day2[:-4]        
        elif len(dateList)==1:
            message="Βρέθηκε ένα ραντεβού με βάση τα κριτίρια αναζήτησης."
        else:
            message="Βρέθηκαν συνολικά "+str(len(dateList))+" ραντεβού με βάση τα κριτίρια αναζήτησης."
        
        if flag==1:
            message+="\n\n(ΑΜΚΑ: "+dateList[0][0]+"    Επώνυμο: "+dateList[0][1]+"    Όνομα: "+dateList[0][2]+".)"
        elif flag==2:
            message+="\n\n(Ημερομηνίες από: "+day1[-2:]+"-"+day1[-4:-2]+"-"+day1[:-4]+" μέχρι "+day2[-2:]+"-"+day2[-4:-2]+"-"+day2[:-4]+".)"
        elif flag==3:
             message+="\n\n(Προτεραιότητα: "+dateList[0][4]+" για τα προσεχή ραντεβού"+".)"
        elif flag==4:
             message+="\n\n(Προτεραιότητα: "+dateList[0][4]+" για τα παρελθόντα ραντεβού"+".)"
        elif flag==5:
             message+="\n\n(Προτεραιότητα: "+dateList[0][4]+" για όλα τα καταχωρημένα ραντεβού"+".)"
        elif flag==6:
             message+="\n\n(Προτεραιότητα: "+dateList[0][4]+" για τα ραντεβού από "+day1[-2:]+"-"+day1[-4:-2]+"-"+day1[:-4]+" μέχρι "+day2[-2:]+"-"+day2[-4:-2]+"-"+day2[:-4]+".)"
        if len(dateList)==0:
            messagebox.showwarning('Ενημέρωση:', message)
        else:
            messagebox.showinfo('Ενημέρωση:', message)
        checkList.clear()
        dateList.clear()        
    elif x==40: #επιστροφή στο κεντρικό μενού σε περίπτωση που δε βρέθηκαν αποτελέσματα αναζήτησης με βάση την προτεραιότητα.
        viewFrame6.grid_forget()
        menu()
    elif x==41: #έλεγχος ημ/νιών αναζήτησης ραντεβού με βάση την προτεραιότητα (από...μέχρι) και ανακατεύθυνση για συνέχιση ενεργειών.
        global checkDate2
        global checkDate4
        day1=checkDate(checkDate2.get())
        day2=checkDate(checkDate4.get())
        if day1==0 or day2==0:
            errorMessage=Label(viewFrame6, text="Μη έγκυρες τιμές ημερομηνίας, η ενέργεια ακυρώθηκε.", fg="#000080")
            errorMessage.grid(row=60, column=0, columnspan=10, pady=15)
            viewShowDayNew1=Button(viewFrame6, text="Νέα Αναζήτηση", fg="#ffffff", bg="#000080", padx=35, pady=11, command=lambda: goto(46))                         
            viewShowDayNew1.grid(row=500, column=5, padx=20, pady=10)
            viewShowDayReturn1=Button(viewFrame6, text="Κεντρικό μενού", fg="#ffffff", bg="#000080", padx=35, pady=11, command=lambda: goto(47))                       
            viewShowDayReturn1.grid(row=500, column=5, padx=20, pady=10)
        else:
            global epilogi2
            epilogi1=LabeL(viewFrame6, text="Προτεραιότητα (ΧΑΜΗΛΗ, ΜΕΤΡΙΑ, ΥΨΗΛΗ):", fg="#000080")
            epilogi1.grid(row=63, column=4, pady=15)
            epilogi2=Entry(viewFrame6, width=50, bg="#d9d9d9", fg="#000080")                        
            epilogi2.grid(row=63, column=5, pady=15)
            prioritySubmit=Button(viewFrame6, text="Υποβολή", fg="#ffffff", bg="#000080", padx=35, pady=11, command=lambda: goto(48)) 
            prioritySubmit.grid(row=65, column=2, pady=15)
    elif x==42: #νέα ενέργεια Αναζήτησης μετά από επιτυχημένη αναζήτηση ραντεβού με βάση τον ΑΜΚΑ
        FrameForScroll2.grid_forget()
        insert(viewFrame4, 7)
    elif x==43: #επιστροφή στο κεντρικό μενού μετά από επιτυχημένη αναζήτηση ραντεβού με βάση τον ΑΜΚΑ
        FrameForScroll2.grid_forget()
        menu()        
    elif x==44: #νέα αναζήτηση μετά από επιτυχημένη αναζήτηση ραντεβού με βάση την προτεραιότητα
        viewFrame5.grid_forget()
        insert(7)
    elif x==45: #επιστροφή στο κεντρικό μενού μετά από επιτυχημένη αναζήτηση ραντεβού με βάση την προτεραιότητα
        viewFrame5.grid_forget()
        menu()            
    elif x==46: #νέα αναζήτηση μετά από αποτυχημένη αναζήτηση με βάση την προτεραιότητα
        viewFrame6.grid_forget()
        viewFrame5.grid_forget()
        insert(7)
    elif x==47: #επιστροφή στο κεντρικό μενού μετά από αποτυχημένη αναζήτηση με βάση την προτεραιότητα
        viewFrame6.grid_forget()
        viewFrame5.grid_forget()
        menu()
    elif x==48: #ολοκλήρωση διαδικασίας αναζήτησης ραντεβού με βάση την προτεραιότητα (από...μέχρι)
        priority2=epilogi2.get()
        priority2=priority2.strip()
        priority2=priority2.upper()
        if priority2 not in ['ΧΑΜΗΛΗ', 'ΜΕΤΡΙΑ', 'ΥΨΗΛΗ']:
            errorMessage=Label(viewFrame6, text="Μη έγκυρη τιμή, η ενέργεια ακυρώθηκε.", fg="#000080", pady=15)
            errorMessage.grid(row=200, column=0, columnspan=10)
            viewShowDayNew1=Button(viewFrame6, text="Νέα Αναζήτηση", fg="#ffffff", bg="#000080", padx=35, pady=11, command=lambda: goto(46))                        
            viewShowDayNew1.grid(row=500, column=5, padx=20, pady=10)
            viewShowDayReturn1=Button(viewFrame6, text="Κεντρικό μενού", fg="#ffffff", bg="#000080", padx=35, pady=11, command=lambda: goto(47))                     
            viewShowDayReturn1.grid(row=500, column=5, padx=20, pady=10)
        else:           
            y=str(datetime.date.today())  #current date
            y=x.split('-')
            y="".join(y)                    #current date as one string!            
            if day1>=y and day2>=y:
                with open("current.csv", "r", newline="", encoding="utf-8") as file:
                    ro=csv.reader(file, delimiter='$')
                    for row in ro:
                        checkList.append(row)
                    for x in checkList:
                        if x[4]==priority2:
                            dateList.append(x)
                    goto(39) 
            elif day1<y and day2<y:
                with open("previous.csv", "r", newline="", encoding="utf-8") as file:
                    ro=csv.reader(file, delimiter='$')
                    for row in ro:
                        checkList.append(row)
                    for x in checkList:
                        if x[4]==priority2:
                            dateList.append(x)
                    goto(39) 
            else:
                with open("previous.csv", "r", newline="", encoding="utf-8") as file:
                    ro=csv.reader(file, delimiter='$')
                    for row in ro:
                        checkList.append(row)
                    for x in checkList:
                        if x[4]==priority2 and x not in dateList:
                            dateList.append(x)
                    checkList.clear()
                with open("current.csv", "r", newline="", encoding="utf-8") as file:
                    ro=csv.reader(file, delimiter='$')
                    for row in ro:
                        checkList.append(row)
                    for x in checkList:
                        if x[4]==priority2 and x not in dateList:
                            dateList.append(x)                               
                    goto(39)
    elif x==49: #νέα αναζήτηση μετά από επιτυχημένη αναζήτηση ραντεβού με βάση την προτεραιότητα
        FrameForScroll2.grid_forget()
        mainFrame=LabelFrame(root, bd=0)
        mainFrame.grid(row=5, column=0, columnspan=10)
        insert(7)
    elif x==50: #επιστροφή στο κεντρικό μενού μετά από επιτυχημένη αναζήτηση ραντεβού με βάση την προτεραιότητα
        FrameForScroll2.grid_forget()
        menu()
    elif x==51: #νέα ενέργεια Αναζήτησης μετά από αποτυχημένη αναζήτηση ραντεβού.
        viewFrame4.grid_forget()
        insert(7)
    elif x==52: #επιστροφή στο κεντρικό μενού μετά από αποτυχημένη αναζήτηση ραντεβού.
        viewFrame4.grid_forget()
        menu()
    elif x==53: #επιστροφή στο κεντρικό μενού από το μενού αναζήτησης ραντεβού.
        viewFrame2.grid_forget()
        menu()
    elif x==54: #επιστροφή στο κεντρικό μενού από το μενού αναζήτησης ραντεβού (από ΑΛΛΟ σημείο).
        Frame17.grid_forget()
        menu()
    elif x==55: #επιστροφή στο κεντρικό μενού από το μενού διόρθωσης ραντεβού.
        fixFrame1.grid_forget()
        menu()

def checkPriority(x, y): #παίρνει 2 ορίσματα --> x: βαθμός προτεραιότητας ('ΧΑΜΗΛΗ', 'ΜΕΤΡΙΑ', 'ΥΨΗΛΗ') --> y: χρονικό εύρος αναζήτησης (0, 'ΠΡΟΣΕΧΗ'(1), 'ΠΑΡΕΛΘΟΝΤΑ'(2), 'ΣΥΝΟΛΙΚΑ'(3)
    global p
    p=x
    if y==0:             #ΜΕ ΕΥΡΟΣ (ΑΠΟ... - ΜΕΧΡΙ...)(4)
        global viewFrame6
        print("p=", p)
        viewFrame5.grid_forget()
        viewFrame6=LabelFrame(root, bd=0)
        viewFrame6.grid(row=4, column=0, columnspan=10)
        viewShowPriorityLabel=Label(viewFrame6, text="Επιλογή Αναζήτησης ραντεβού με βάση την προτεραιότητα:", fg="#000080", pady=15)
        viewShowPriorityLabel.grid(row=5, column=0, columnspan=10, pady=15)
        viewShowPriority1=Button(viewFrame6, text="Προσεχή", fg="#ffffff", bg="#000080", padx=45, pady=11, command=lambda: checkPriority(p, 1)) 
        viewShowPriority1.grid(row=6, column=3, padx=45, pady=45)        
        viewShowPriority2=Button(viewFrame6, text="Παρελθόντα", fg="#ffffff", bg="#000080", padx=35, pady=11, command=lambda: checkPriority(p, 2))
        viewShowPriority2.grid(row=6, column=4, padx=45, pady=45)
        viewShowPriority3=Button(viewFrame6, text="Συνολικά", fg="#ffffff", bg="#000080", padx=45, pady=11, command=lambda: checkPriority(p, 3))
        viewShowPriority3.grid(row=6, column=5, padx=45, pady=45)
        viewShowPriority4=Button(viewFrame6, text="Με εύρος (από - μέχρι)", fg="#ffffff", bg="#000080", padx=7, pady=11, command=lambda: checkPriority(p, 4))
        viewShowPriority4.grid(row=6, column=6, padx=45, pady=45)
    else:
        if x==4: #έλεγχος προτεραιότητας και ανακατεύθυνση για εκτύπωση αποτελεσμάτων Αναζήτησης με βάση την προτεραιότητα (flag=3, Με εύρος (από - έως)), -->x==4
            checkDate1=Label(viewFrame6, text="Από:", fg="#000080", pady=15)
            checkDate1.grid(row=50, column=4)
            checkDate2=Entry(viewFrame6, width=50, fg="#000080", bg= "#d9d9d9", pady=15)
            checkDate2.grid(row=50,column=5)
            checkDate3=Label(viewFrame6, text="Μέχρι:", fg="#000080", pady=15)
            checkDate3.grid(row=51, column=4)
            checkDate4=Entry(viewFrame6, width=50, fg="#000080", bg= "#d9d9d9", pady=15)
            checkDate4.grid(row=51,column=5)
            checkDateSubmit=Button(viewFrame6, text="Υποβολή", bg="#000080", fg= "#ffffff", padx=35, pady=11, command=lambda: goto(41))
            checkDateSubmit.grid(row=51,column=0, columnspan=10, pady=15)
        else:
            global priority
            if p==1: #'ΧΑΜΗΛΗ'
                priority='ΧΑΜΗΛΗ'
            elif p==2: #'ΜΕΤΡΙΑ'
                priority='ΜΕΤΡΙΑ'
            else: #'ΥΨΗΛΗ'
                priority='ΥΨΗΛΗ'         
            if y==1: #έλεγχος προτεραιότητας και ανακατεύθυνση για εκτύπωση αποτελεσμάτων Αναζήτησης με βάση την προτεραιότητα (flag=3, Προσεχή)
                checkList.clear()
                dateList.clear()            
                with open("current.csv", "r", newline="", encoding="utf-8") as file:
                    ro=csv.reader(file, delimiter='$')
                    for row in sorted(ro, key=lambda j:j[6], reverse=True):
                        checkList.append(row)
                    for x in checkList:                       
                        if x[5]==priority and x not in dateList:
                            dateList.append(x)
                    checkList.clear()        
                    flag=3               
            elif y==2: #έλεγχος προτεραιότητας και ανακατεύθυνση για εκτύπωση αποτελεσμάτων Αναζήτησης με βάση την προτεραιότητα (flag=4, Παρελθόντα)
                with open("previous.csv", "r", newline="", encoding="utf-8") as file:
                    ro=csv.reader(file, delimiter='$')
                    for row in sorted(ro, key=lambda j:j[6], reverse=True):
                        checkList.append(row)
                    for x in checkList:
                         if x[5]==priority and x not in dateList:
                            dateList.append(x)
                    checkList.clear()
                    flag=4        
            elif y==3: #έλεγχος προτεραιότητας και ανακατεύθυνση για εκτύπωση αποτελεσμάτων Αναζήτησης με βάση την προτεραιότητα (flag=5, Συνολικά)r
                with open("current.csv", "r", newline="", encoding="utf-8") as file:
                    ro=csv.reader(file, delimiter='$')
                    for row in sorted(ro, key=lambda j:j[6], reverse=True):
                        checkList.append(row)
                    for x in checkList:
                        if x[5]==priority and x not in dateList:
                            dateList.append(x)
                    checkList.clear()
                with open("previous.csv", "r", newline="", encoding="utf-8") as file:
                    ro=csv.reader(file, delimiter='$')
                    for row in sorted(ro, key=lambda j:j[6], reverse=True):
                        checkList.append(row)
                    for x in checkList:
                        if x[5]==priority and x not in dateList:
                            dateList.append(x)
                    checkList.clear()
                    flag=5         
            #if len(dateList)==0:
                #messagebox.showwarning('Ένημέρωση:', "Δε βρέθηκαν αποτελέσματα σύμφωνα με τα κριτίρια αναζήτησης.")
                #noResults=Label(viewFrame6, text=", "+priorityChoice+" ραντεβού με βάση την προτεραιότητα).")
                #noResults.grid(row=55, column=0, columnspan=10)
                #returnPriority=Button(viewFrame6, text="Κεντρικό μενού", fg= "#ffffff", bg="#000080", padx=35, pady=11, command=lambda: goto(40))
                #returnPriority.grid(row=56, column=0, columnspan=10, pady=15)
            #else:
            viewFrame6.grid_forget()
            goto(34) #εκτύπωση αποτελεσμάτων (από την dateList) με βάση την προτεραιότητα.
                    
def checkDate(date): #έλεγχος αν η ημερομηνία είναι σωστή
    if '/' not in date and '-' not in date or len(date)<=5 or len(date)>10:
        return 0
    else:         
        if date[-3] in ['/', '-']:
            year='20'+date[-2:]
        elif date[-5] in ['/', '-']:
            year=date[-4:]
        else:
            return 0
        if len(date)>8 and date[-8] in ['/', '-']:
            month=date[-7:-5]
            day=date[-len(date):-8]
        elif len(date)>6 and date[-6] in ['/', '-']:
            month=date[-5:-3]
            day=date[-len(date):-6]
            if '/' in month or '-' in month:
                return 0
        elif len(date)>7 and date[-7] in ['/', '-']:
            month='0'+date[-6]
            day=date[-len(date):-7]
        elif len(date)>5 and date[-5] in ['/', '-']:
            if date[-4] not in year:
                month='0'+date[-4]
                day=date[-len(date):-5]
            else:
                return 0                    
        if '/' in day or '-' in day or len(day)>2 or len(day)==0:
            return 0                
        elif len(day)==1:
            day='0'+day
    finalDate=year+month+day
    return finalDate

def changePass(x): #Προσθήκη/Κατάργηση/Αλλαγή λογ/μού χρήστη, η changePass(x) παίρνει μία παράμετρο x--> (1=προσθήκη, 2=κατάργηση, 3=αλλαγή)
    global passist
    global newEntry
    global passList
    global newUsername2
    global newPassword2
    global changes
    mainMenu.grid_forget()
    changes=LabelFrame(root, bd=0, fg="#000080")
    changes.grid(row=4, column=0, columnspan=10)
    if x==1:  #Προσθήκη Λογαριασμού
        passList=[]
        newList=[]
        newEntry=[]
        newUser=Label(changes, text="Προσθήκη Λογαριασμού χρήστη", bg= "#d9d9d9", fg="#000080", pady=15)
        newUser.grid(row=4, column=0, columnspan=10)
        newUsername1=Label(changes, text="Εισάγετε Username:", fg="#000080", pady=10)
        newUsername1.grid(row=5, column=4)
        newUsername2=Entry(changes, width=50, bg= "#d9d9d9", fg="#000080")
        newUsername2.grid(row=5, column=5,pady=10)   
        newPassword1=Label(changes, text="Εισάγετε Password:", fg="#000080", pady=10)
        newPassword1.grid(row=6, column=4)
        newPassword2=Entry(changes, width=50, bg= "#d9d9d9", fg="#000080")
        newPassword2.grid(row=6, column=5, pady=10)
        verifyNew=Button(changes, bg="#000080", fg="#ffffff", text="Υποβολή", padx=30, pady=11, command=lambda: transition(15))
        verifyNew.grid(row=100, column=0, pady=15, padx=20, columnspan=10) 
    elif x==2: #Κατάργηση Λογαριασμού
        global newDelete
        global verifyDel
        global eraseList
        global delUsername2
        global delPassword2       
        global verifyDel
        erase=[]
        eraseList=[]
        finalList=[]
        delUser=Label(changes, text="Κατάργηση Λογαριασμού χρήστη", bg= "#d9d9d9", fg="#000080", pady=15)
        delUser.grid(row=4, column=0, columnspan=10)
        with open("password.csv", "r", newline="", encoding="utf-8") as file:
            ro=csv.reader(file, delimiter='$')
            for row in ro:
                eraseList.append(row)
            if len(eraseList)==1:
                failDelete=Label(changes, text="Δε γίνεται να καταργηθεί ο Λογαριασμός χρήστη γιατί είναι μοναδικός, η ενέργεια απέτυχε.", fg="#000080", pady=25)
                failDelete.grid(row=8, column=0, columnspan=10)
                returnMenu=Button(changes, bg="#000080", fg="#ffffff", text="Κεντρικό Μενού", padx=30, pady=11, command=lambda: transition(9))
                returnMenu.grid(row=100, column=5, pady=15, padx=20)
            else:
                delUsername1=Label(changes, text="Εισάγετε Username:", fg="#000080", pady=10)
                delUsername1.grid(row=5, column=4, sticky=W)
                delUsername2=Entry(changes, width=50, bg= "#d9d9d9", fg="#000080")
                delUsername2.grid(row=5, column=5, pady=10)   
                delPassword1=Label(changes, text="Εισάγετε Password:", fg="#000080", pady=10)
                delPassword1.grid(row=6, column=4, sticky=W)
                delPassword2=Entry(changes, width=50, bg= "#d9d9d9", fg="#000080")
                delPassword2.grid(row=6, column=5, pady=10)                
                verifyDel=Button(root, bg="#000080", fg="#ffffff", text="Οριστική διαγραφή χρήστη", padx=30, pady=11, command=lambda: transition(10))
                verifyDel.grid(row=100, column=0, pady=15, padx=20, columnspan=10)                
    elif x==3: #Αλλαγή Λογαριασμού
        global oldEntry
        global changeList
        global verifyOld
        global oldPassword2
        global oldUsername2
        global changes3
        change=[]
        changeList=[]
        oldEntry=[]
        newEntry=[]
        changes3=LabelFrame(root, bd=0)
        changes3.grid(row=4, column=0, columnspan=10)
        changeUser=Label(changes3, text="Αλλαγή Λογαριασμού χρήστη", bg= "#d9d9d9", fg="#000080", pady=15)
        changeUser.grid(row=4, column=0, columnspan=10)
        with open("password.csv", "r", newline="", encoding="utf-8") as file:
            ro=csv.reader(file, delimiter='$')
            for row in ro:
                changeList.append(row)
            oldUsername1=Label(changes3, text="Εισάγετε Username:", fg="#000080", pady=10)
            oldUsername1.grid(row=5, column=4)
            oldUsername2=Entry(changes3, width=50, bg= "#d9d9d9", fg="#000080")
            oldUsername2.grid(row=5, column=5, pady=10)   
            oldPassword1=Label(changes3, text="Εισάγετε Password:", fg="#000080", pady=10)
            oldPassword1.grid(row=6, column=4)
            oldPassword2=Entry(changes3, width=50, bg= "#d9d9d9", fg="#000080")
            oldPassword2.grid(row=6, column=5, pady=10)
            verifyOld=Button(changes3, bg="#000080", fg="#ffffff", text="Υποβολή", padx=30, pady=11, command=lambda: transition(12))
            verifyOld.grid(row=100, column=0, pady=15, padx=20, columnspan=10)

main()

#Να ελέγξω την σειρά των πεδίων που εκτυπώνονται.
#Να βάλω scrollbar και να βρω τρόπο να εκτυπώνει τα αποτελέσματα στον εκτυπωτή.
#Να φτιάξω κουμπί που να επιτρέπει - χειροκίνητα και όχι αυτόματα - τη δημιουργία αντιγράφων ασφαλείας.
#ΔΟΥΛΕΥΩ ΣΤΗΝ search().
 
