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
    root.option_add("*Button.cursor", "hand2")
    mainFrame=LabelFrame(root, bd=0)#, bg="#000080")
    mainFrame.grid(row=0, column=0, columnspan=10)
    my_img=ImageTk.PhotoImage(Image.open("unesco_logo_2.jpg"))
    my_label=Label(mainFrame, image=my_img)
    my_label.grid(row=0, padx=0, column=0, columnspan=2)
    my_img2=ImageTk.PhotoImage(Image.open("espaLogo_3.jpg"))
    my_label2=Label(mainFrame, image=my_img2) 
    my_label2.grid(row=0, padx=0, column=9, columnspan=2)
    root.title("Όμιλος για την Unesco Πειραιώς και Νήσων - Πρόγραμμα διαχείρισης και παρακολούθησης ιατρικών διαδικασιών και πράξεων - ΙΑΤΡΕΙΟ v.4.03 (Υφιστάμενη δομή)") #Υφιστάμενη δομή
    #root.title("Όμιλος για την Unesco Πειραιώς και Νήσων - Πρόγραμμα διαχείρισης και παρακολούθησης ιατρικών διαδικασιών και πράξεων - ΙΑΤΡΕΙΟ v.4.03  (Νέα δομή)")    #Νέα δομή
    label00= Label(mainFrame, bg="#000080", fg="#ffffff", padx=10, pady=0, text="Όμιλος για την Unesco Πειραιώς και Νήσων", font=('bold', 18), bd=40)
    label00.grid(row=0, column=2, columnspan=7, sticky=W+E, pady=0)
    my_img0=ImageTk.PhotoImage(Image.open("iatreio_logo2.jpg"))
    my_label=Label(mainFrame, image=my_img0)#, bg="#000080")
    my_label.grid(row=1, padx=0, column=3, sticky=E)
    label01= Label(mainFrame, fg="#000080", text="ΙΑΤΡΕΙΟ", font=('bold', 40))#bg="#000080", 
    label01.grid(row=1, column=4, columnspan=3, sticky=W)
    label02= Label(mainFrame, fg="#000080", text="Πρόγραμμα διαχείρισης και παρακολούθησης ιατρικών διαδικασιών και πράξεων", font=('bold', 14))#, bd=7)bg="#000080", 
    label02.grid(row=2, column=0, columnspan=10, sticky=N)    
    label= Label(mainFrame, fg="#000080", padx=511, pady=5, text="ΙΑΤΡΕΙΟ v.4.03  - powered by Python v.3.10.5")#bg="#000080", 
    label.grid(row=3, column=0, columnspan=10, sticky=N, pady=0)   
    firstFrame=LabelFrame(root, padx=5, pady=5, bd=0)
    firstFrame.grid(row=5, column=0, columnspan=10)
    enterSystem=Button(firstFrame, text="Είσοδος στο σύστημα", padx=20, pady=11, bg="#000080", fg="white", command=lambda: logIn())    
    enterSystem.grid(row=5, column=2, pady=100, padx=50)
    exitSystem=Button(firstFrame, text="Έξοδος", padx=59, pady=11, bg="#000080", fg="white", command=lambda: greetings())
    exitSystem.grid(row=5, column=3, pady=100, padx=50)
    service=Button(firstFrame, text="Contact Service", padx=37, pady=11, bg="#000080", fg="white", command=lambda: fire())
    service.grid(row=5, column=4, pady=100, padx=50)
    root.bind('<Escape>', lambda event: root.destroy())
    root.bind('<F11>', lambda event: goto(123))
    root.bind('<Return>', lambda event: logIn())
    root.mainloop()

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
        ro=csv.reader(file, delimiter=',')
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
            #show()
            menu()
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

def menu():#Κεντρικό μενού
    global mainMenu   
    mainMenu=LabelFrame(root, padx=5, pady=10, bd=0)
    mainMenu.grid(row=5, column=0, columnspan=10, padx=10, pady=15)
    title=Label(mainMenu, text="ΔΙΑΘΕΣΙΜΑ ΠΡΟΓΡΑΜΜΑΤΑ:", bg="#000080", fg="#ffffff", pady=15, font=('bold', 14))
    title.grid(row=7, column=0, columnspan=10, sticky=W+E)
    image4 = Image.open("rantevou.jpg")#ή "shery_pic_3.jpg"
    photo4 = ImageTk.PhotoImage(image4)
    label4 = Button(mainMenu, image = photo4, command=lambda: exec('ΡΑΝΤΕΒΟΥ_v.3.02.5.py'))
    label4.image = photo4
    label4.grid(row=9, column=4, pady=70)#, padx=100)
    blank=LabelFrame(mainMenu, bd=0)
    blank.grid(row=9, column=5, padx=150)
    image5 = Image.open("istoriko.jpg")#ή "shery_pic_3.jpg"
    photo5 = ImageTk.PhotoImage(image5)
    label5 = Button(mainMenu, image = photo5, command=lambda: exec('ΙΣΤΟΡΙΚΟ_v.1.02.py'))
    label5.image = photo5
    label5.grid(row=9, column=6, pady=70)#, padx=100)
    messagebox.showinfo('Ενημέρωση:', 'Επιτυχημένη είσοδος.\n\n\nΚαλωσήρθατε στο "ΙΑΤΡΕΙΟ"!')


def exec(x):
    root.destroy()
    os.system(x)

def greetings(): #μήνυμα τερματισμού του προγ/τος (το πρόγραμμα σε αυτό το σημείο είναι ανενεργό αλλά το παράθυρό του (root()) κλείνει ΜΟΝΟ με κλικ στο κουμπί "Κλείσιμο παράθυρου")
    global finish
    firstFrame.grid_forget()
    exitFrame=LabelFrame(root, bd=0)
    exitFrame.grid(row=4, column=0, columnspan=10)
    label4= Label(exitFrame, fg="#000080", text="Ευχαριστούμε πολύ που χρησιμοποιήσατε την εφαρμογή!\n\nProgrammed, designed and developed by Shery Panagiotaki, @copyright 2022\n\n\nContact info:\n\nTel.: (+30) 6976929404\n\nE-mail: sherypanagiotaki@yahoo.com,\n", bd=0)
    label4.grid(row=50, column=0, columnspan=10, pady=0)
    finish=Button(exitFrame, text="Κλείσιμο παράθυρου", padx=30, pady=11, fg="#ffffff", bg="#000080", command=lambda: root.destroy()) #κουμπί που κλείνει το παράθυρο του προγ/τος
    finish.grid(row=60, column=6, padx=45)
    info=Button(exitFrame, fg="#ffffff", bg="#000080", text="Contact Service", padx=37, pady=11, command=fire)    
    info.grid(row=60, column=7, padx=45)
    image6 = Image.open("iatreio_logo2.jpg")#ή "shery_pic_3.jpg"
    photo6 = ImageTk.PhotoImage(image6)
    label6 = Label(exitFrame, image = photo6, bd=0)
    label6.image = photo6
    label6.grid(row=45, column=0, columnspan=10, pady=25)#, padx=100)

def fire(): #μήνυμα στοιχείων επικοινωνίας για service.
    messagebox.showinfo('Service - Πληροφορίες επικοινωνίας:', 'Programmer / Developer: Shery Panagiotaki\n\nContact info:\n\nTel.: (+30) 6976929404\n\nE-mail: sherypanagiotaki@yahoo.com,\n             sherypamagiotaki@gmail.com')    
        
main()
