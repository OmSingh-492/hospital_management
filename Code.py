"""
    TOPIC FOR COMPUTER PRACTICALS: HOSPITAL MANAGEMENT SYSTEM
    STUDENT NAME: OM SINGH
    CLASS: 12-"A"
    SCHOOL: AMITY INTERNATIONAL SCHOOL,SAKET    
"""
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Import statements which are to be used at some point in the program>>>>>>>>>>>>>>>>>>>>>>>>>>>>

from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import csv
import uuid

#===========================<><><><><><><><><><><><><><>Start of the Program<><><><><>><><><><><><><><>==========================

def main():
    root=Tk()
    app=Window1(root)

#====================================================Creating Master Window=====================================================

class Window1():
    def __init__(self,master):
        self.master=master
        self.master.title("Introduction")
        self.master.geometry('580x450+200+0')
        self.master.config(bg="white")
        self.frame=Frame(self.master)
        self.frame.pack()
        
        #Creating Required Frames
        self.Frame1=LabelFrame(self.frame,bd=0)
        self.Frame1.grid(row=0,column=0)
        self.Frame2=LabelFrame(self.frame,bd=0)
        self.Frame2.grid(row=1,column=0)
        self.Frame3=LabelFrame(self.frame,relief="ridge",bd=10)
        self.Frame3.grid(row=2,column=0)
        self.Frame4=LabelFrame(self.frame,bd=0)
        self.Frame4.grid(row=3,column=0)
        
        #Placing Required Widgets
        self.label=Label(self.Frame1,text='XYZ HOSPITAL, NEW DELHI',font=("Bell MT",30,"bold","underline"),fg="AntiqueWhite4")
        self.label.grid(row=0,column=0,columnspan=2,pady=40)        
        self.label=Label(self.Frame2,text='Hi!! Welcome to XYZ Hospital, New Delhi.',font=("Cambria",15),fg="black")
        self.label.grid(row=2,column=0,columnspan=2)
        self.label=Label(self.Frame2,text='Before moving ahead, please select which',font=("Cambria",15),fg="black")
        self.label.grid(row=3,column=0,columnspan=2)
        self.label=Label(self.Frame2,text='of the following applies to you.',font=("Cambria",15),fg="black")
        self.label.grid(row=4,column=0,columnspan=2)        
        self.label=Label(self.Frame2,text='')
        self.label.grid(row=5,column=0,columnspan=2)        
        self.label=Label(self.Frame2,text="I am :-",font=("Cambria",15),fg="black")
        self.label.grid(row=7,column=0,columnspan=2,pady=5)               
        
        #Creating Required Buttons
        self.btnDoc=Button(self.Frame3,text="A Doctor",width=20,font=("Bell MT",15,"bold"),command=self.Doctor_Login)
        self.btnDoc.grid(row=8,column=0)        
        self.btnDoc=Button(self.Frame3,text="A Patient",width=20,font=("Bell MT",15,"bold"),command=self.Patient_Login)
        self.btnDoc.grid(row=9,column=0)        
        self.btnAbout=Button(self.Frame4,text="About Us",font=("Cambria",12,"bold","underline"),fg="blue",command=self.About_Us)
        self.btnAbout.grid(row=9,column=0,pady=20)       
        self.label=Label(self.Frame4,text=8*"\t")
        self.label.grid(row=9,column=1,pady=20)       
        self.btnContact=Button(self.Frame4,text="Contact Us",font=("Cambria",12,"bold","underline"),fg="blue",command=self.Contact_Us)
        self.btnContact.grid(row=9,column=2,pady=20)                  
        
        #Running the mainloop
        self.master.mainloop()
        
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Functions for Buttons of Master Window>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>    
    
    def Doctor_Login(self):        
        self.newwindow=Toplevel(self.master)        
        self.app=Doc_Window(self.newwindow) 
        
    def Patient_Login(self):
        self.newwindow=Toplevel(self.master)        
        self.app=Patient_Window(self.newwindow)
        
    def About_Us(self):
        str_objectives="OUR OBJECTIVES:-\n\nWe at XYZ Hospital, New Delhi always try to provide our patients with the best medical infrastructure, and our 24X7 dedicated medical fraternity are always ready to serve you.\nFOR US OUR JOURNEY ITSELF IS OUR DESTINATION. BE A PART OF THIS MEDICAL REVOLUTION..\n\n"
        str_awards="AWARDS AND RECOGNITIONS:-\n\n(i) Best Multispeciality Hospital across India as per the survey by XXX.\n(ii) Best Cancer Care and Research Institute as per the survey by XXX.\n(iii) The first hospital in the country having the experience of more than X0,000 Open Heart Surgeries..\n\n"
        str_mission="FUTURE PLANS:-\n\nLET'S MAKE A HEALTHY, PROGRESSED AND HIGHLY ACHIEVING INDIA."
        tkinter.messagebox.askokcancel("About Us",str_objectives+str_awards+str_mission)
    
    def Contact_Us(self):
        str_address="ADDRESS:-\nXYZ Multispeciality Hospital,\n#17, Block II, Saket Road,\nSaket\nNew Delhi-122 002\n\n"
        str_mapview="LINK FOR NAVIGATION THROUGH GOOGLE MAPS:-\nmaps.google.com/sjhhVGY12/jhba\n\n"
        str_emailid="E-MAIL ADDRESSES:-\n(i) For queries regarding patient/doctor registration:\n  xyzregistration@gmail.com\n(ii) For obtaining past health records/medical scans of the patient:\n  xyzpatientsscan@gmail.com\n(iii) For feedbacks:\n  xyzfeedbacks@gmail.com\n(iv) For medical fraternity except our doctors and patients(like nurses,etc.):\n  xyzgeneralinfo@gmail.com\n\n"
        str_contact="PHONE NUMBER DIRECTORY:-\n(i) Toll free number:-XXXXXXXXXX\n(ii) General Ward Administrator Contact Number:-XXXXXXXXXX\n(iii) For enquiries of a patient through his/her Patient ID:-XXXXXXXXXX\n\n"
        tkinter.messagebox.askokcancel("Contact Us",str_address+str_mapview+str_emailid+str_contact)

#===================================================Creating Master Doctor Window===============================================        

class Doc_Window:
    def __init__(self,master):
        self.master=master
        self.master.title("Doctor's Portal, XYZ Hospital, New Delhi")
        self.master.geometry('650x450+175+0')
        self.master.config(bg="white")
        self.frame=Frame(self.master)        
        self.frame.grid(row=0,column=0)
        
        #Creating variabes
        self.Username=StringVar()
        self.Password=StringVar()
        
        #Creating the required frames        
        self.windowLayout=LabelFrame(self.frame,width=650,height=150,bd=0)
        self.windowLayout.grid(row=1,column=0,padx=20)
        self.Doc_Login_Frame=LabelFrame(self.frame,width=650,height=150,relief="groove",bd=10)
        self.Doc_Login_Frame.grid(row=2,column=0,padx=30)
        self.Submit_Reset=LabelFrame(self.frame,width=650,height=150,bd=0)
        self.Submit_Reset.grid(row=3,column=0,padx=30)
        self.Instructions=LabelFrame(self.frame,width=650,height=150,bd=0)
        self.Instructions.grid(row=4,column=0,padx=30)
        self.buttons=LabelFrame(self.frame,width=650,height=150,bd=0)
        self.buttons.grid(row=5,column=0,padx=10)
        
        #Placing the required widgets
        self.label=Label(self.windowLayout,text="Welcome to Doctor's Portal of XYZ Hospital, New Delhi.",font=("Cambria",18,"bold","underline"),fg="AntiqueWhite4")
        self.label.grid(row=1,column=0)        
        self.label=Label(self.windowLayout,text="If you are already registered with us,\nkindly enter your Username and Password in the Login Frame.",font=("Cambria",12),fg="black")
        self.label.grid(row=2,column=0,pady=10)       
        self.lbl=Label(self.Doc_Login_Frame,text=2*"\t")
        self.lbl.grid(row=4,column=0)
        self.lbl=Label(self.Doc_Login_Frame,text="LOGIN FRAME",font=("Cambria",12,"underline"),fg="AntiqueWhite4")
        self.lbl.grid(row=4,column=1)
        self.lblUsername=Label(self.Doc_Login_Frame,text="Enter Username",font=("Cambria",13,"bold"),fg="blue")
        self.lblUsername.grid(row=5,column=0)
        self.lbl=Label(self.Doc_Login_Frame,text="\t")
        self.lbl.grid(row=5,column=1)
        self.txtUsername=Entry(self.Doc_Login_Frame,font=("Cambria",12),bg="gainsboro",textvariable=self.Username)
        self.txtUsername.grid(row=5,column=2,pady=10)
        self.lbl=Label(self.Doc_Login_Frame,text=7*" ")
        self.lbl.grid(row=6,column=3)
        self.lblPassword=Label(self.Doc_Login_Frame,text="Enter Password",width=20,font=("Cambria",13,"bold"),fg="blue")
        self.lblPassword.grid(row=6,column=0)
        self.lbl=Label(self.Doc_Login_Frame,text="\t")
        self.lbl.grid(row=6,column=1)
        self.txtPassword=Entry(self.Doc_Login_Frame,font=("Cambria",12),bg="gainsboro",show="*",width=20,textvariable=self.Password)
        self.txtPassword.grid(row=6,column=2,pady=10)
        self.lbl=Label(self.Doc_Login_Frame,text=7*" ")
        self.lbl.grid(row=6,column=3)  
       
        #Creating required Buttons        
        self.btnSubmit=Button(self.Submit_Reset,text="Submit",font=("Cambria",12,"bold"),fg="blue",command=self.submit)
        self.btnSubmit.grid(row=7,column=0)         
        self.btnReset=Button(self.Submit_Reset,text="Reset",font=("Cambria",12,"bold"),fg="blue",command=self.reset)
        self.btnReset.grid(row=7,column=1)        
        self.lbl=Label(self.Instructions,text="In case you are registered with us, and want to retrieve\nyour Username or Password,click on FORGOT Button.\nFor new Applications, click on NEW APPLICATIONS button.",font=("Cambria",12))
        self.lbl.grid(row=8,column=0,pady=15)
        self.btnForgot=Button(self.buttons,text="Forgot Username/Password?",font=("Cambria",10,"bold","underline"),fg="blue",command=self.forgot)
        self.btnForgot.grid(row=9,column=0,pady=20)
        self.lbl=Label(self.buttons,text=65*" ")
        self.lbl.grid(row=9,column=1)
        self.btnNewApp=Button(self.buttons,text="New Doctor's Application",font=("Cambria",10,"bold","underline"),fg="blue",command=self.New)
        self.btnNewApp.grid(row=9,column=2)        
        self.btnAbout=Button(self.buttons,text="About us",font=("Cambria",10,"bold","underline"),fg="blue",command=self.About_Us)
        self.btnAbout.grid(row=10,column=0)
        self.lbl=Label(self.buttons,text=75*" ")
        self.lbl.grid(row=10,column=1)
        self.btnContact=Button(self.buttons,text="Contact us",font=("Cambria",10,"bold","underline"),fg="blue",command=self.Contact_Us)
        self.btnContact.grid(row=10,column=2)  
        
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Functions for the Buttons of Master Doctor Window>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
       
    def Credentials(self):        
        d={}
        with open("Doctor's List.csv","r")as readFile:
            reader=csv.reader(readFile)
            lines=list(reader)
            count=0
            for row in lines:
                count+=1                
                if(count==1):
                    continue
                x=0
                for column in row:
                    x+=1
                    if(x==2):
                        d[column]=0
                        x=0
                        for c in row:
                            x+=1
                            if(x==3):
                                d[column]=c
                                break
                        break             
        return(d)
                    
    def submit(self):
        u=(self.Username.get())
        p=(self.Password.get())
        d=self.Credentials()
        check_for_prescence=0       
        for keys in d:
            if(keys==u):                                                                   
                check_for_prescence=1
                if(d[keys]==p):                                        
                    self.newwindow=Toplevel(self.master)        
                    self.app=Doc_Page(self.newwindow)                    
                else:
                    tkinter.messagebox.askokcancel("Invalid Password","Sorry! But you Password is incorrect.. Please enter a valid Password")
                    self.Password.set("")
                    self.txtPassword.focus()
        if(check_for_prescence==0):
            tkinter.messagebox.askokcancel("Invalid Username","Sorry! But your Username is incorrect.. Please enter a valid Username")
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()
                    
    def reset(self):
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()
        
    def forgot(self):
        self.newwindow=Toplevel(self.master)        
        self.app=Forgot(self.newwindow)
        
    def About_Us(self):
        str_objectives="OUR OBJECTIVES:-\n\nWe at XYZ Hospital, New Delhi always try to provide our patients with the best medical infrastructure, and our 24X7 dedicated medical fraternity are always ready to serve you.\nFOR US OUR JOURNEY ITSELF IS OUR DESTINATION. BE A PART OF THIS MEDICAL REVOLUTION..\n\n"
        str_awards="AWARDS AND RECOGNITIONS:-\n\n(i) Best Multispeciality Hospital across India as per the survey by XXX.\n(ii) Best Cancer Care and Research Institute as per the survey by XXX.\n(iii) The first hospital in the country having the experience of more than X0,000 Open Heart Surgeries..\n\n"
        str_mission="FUTURE PLANS:-\n\nLET'S MAKE A HEALTHY, PROGRESSED AND HIGHLY ACHIEVING INDIA."
        tkinter.messagebox.askokcancel("About Us",str_objectives+str_awards+str_mission)
    
    def Contact_Us(self):
        str_address="ADDRESS:-\nXYZ Multispeciality Hospital,\n#17, Block II, Saket Road,\nSaket\nNew Delhi-122 002\n\n"
        str_mapview="LINK FOR NAVIGATION THROUGH GOOGLE MAPS:-\nmaps.google.com/sjhhVGY12/jhba\n\n"
        str_emailid="E-MAIL ADDRESSES:-\n(i) For queries regarding patient/doctor registration:\n  xyzregistration@gmail.com\n(ii) For obtaining past health records/medical scans of the patient:\n  xyzpatientsscan@gmail.com\n(iii) For feedbacks:\n  xyzfeedbacks@gmail.com\n(iv) For medical fraternity except our doctors and patients(like nurses,etc.):\n  xyzgeneralinfo@gmail.com\n\n"
        str_contact="PHONE NUMBER DIRECTORY:-\n(i) Toll free number:-XXXXXXXXXX\n(ii) General Ward Administrator Contact Number:-XXXXXXXXXX\n(iii) For enquiries of a patient through his/her Patient ID:-XXXXXXXXXX\n\n"
        tkinter.messagebox.askokcancel("Contact Us",str_address+str_mapview+str_emailid+str_contact)
        
    def New(self):
        self.newwindow=Toplevel(self.master)
        self.app=New_Application(self.newwindow)
        
#============================================Creating a window for New Doctor's Application=====================================
        
class New_Application:
    def __init__(self,master):
        self.master=master
        self.master.title("New Doctor's Application")
        self.master.geometry('870x520+70+0')
        self.master.config(bg="white")
        self.frame=Frame(self.master)
        self.frame.grid(row=0,column=0) 
        
        #Creating the required variables
        self.Name=StringVar()
        self.Qualifications=StringVar()
        self.Address=StringVar()
        self.Email=StringVar()
        self.Contact=StringVar()
        self.DOB=StringVar()
        self.Res=StringVar()
        self.Language=StringVar()
        self.chkValue=BooleanVar()  
        self.chkValue.set(False)
        
        #Creating the required frames
        self.label_frame=LabelFrame(self.frame,bd=0)
        self.label_frame.grid(row=0,column=0)
        self.combo_frame=LabelFrame(self.frame,relief="groove",bd=10)
        self.combo_frame.grid(row=1,column=0)
        self.declaration_frame=LabelFrame(self.frame,relief="groove",bd=10)
        self.declaration_frame.grid(row=2,column=0)
        self.submit_frame=LabelFrame(self.frame,bd=0)
        self.submit_frame.grid(row=3,column=0)
        self.contact_frame=LabelFrame(self.frame,bd=0)
        self.contact_frame.grid(row=4,column=0)
        
        
        #Placing the required widgets
        self.lbl=Label(self.label_frame,text="Hi and Welcome to XYZ Hospital, New Delhi!!\nWe are delighted that you have show interest in applying as a doctor in one of the best multispeciality hospitals across India..\nTo know more about our awards and recognitions, click on About Us.",font=("Cambria",12),fg="AntiqueWhite4")
        self.lbl.grid(row=0,column=0)        
        self.lbl=Label(self.label_frame,text="To be a part of us and contribute towards HEALTHY INDIA, kindly fill the following details:\n(Note that all the columns are to be filled. For multiple entries, use commas)",font=("Cambria",12))
        self.lbl.grid(row=1,column=0,pady=5)
        self.lbl=Label(self.combo_frame,text="Name*\tDr.",font=("Cambria",12),fg="blue")
        self.lbl.grid(row=2,column=0)
        self.txtName=Entry(self.combo_frame,font=("Cambria",12),width=17,bg="gainsboro",textvar=self.Name)
        self.txtName.grid(row=2,column=1)
        self.lbl=Label(self.combo_frame,text="Department*\t  ",font=("Cambria",12),fg="blue")
        self.lbl.grid(row=3,column=0)
        self.department=ttk.Combobox(self.combo_frame,values=["---Select---","Bariatric Surgery","Cardiac Surgery","Cardiology","Critical Care","Dental Surgery","Dermatology","Emergency Medicine","Endocrinology","ENT","Gastroentrology and GI Surgery","General and Laparoscopic Surgery","Gynecology and Obsterics","Haematology","Internal Medicine","Kidney Transpant","Lab Sciences","Nephrology","Neurology","Neurosurgery","Nuclear Medicine","Nutrition and Dietetics","Oncology","Opthalmology","Orthopaedics and Joints","Paediatrics","Physiotherapy","Psychiatry and Psychology","Plastic and Reconstructive Surgery","Pulmonology","Radiology","Spine Services","Urology"])
        self.department.current(0)
        self.department.grid(row=3,column=1)
        self.lbl=Label(self.combo_frame,text="Qualifications (comma-separated)*\t  ",font=("Cambria",12),fg="blue")
        self.lbl.grid(row=4,column=0)
        self.txtQualification=Entry(self.combo_frame,font=("Cambria",12),bg="gainsboro",textvar=self.Qualifications)
        self.txtQualification.grid(row=4,column=1)
        self.lbl=Label(self.combo_frame,text="Residential Address*\t  ",font=("Cambria",12),fg="blue")
        self.lbl.grid(row=5,column=0)
        self.txtAddress=Entry(self.combo_frame,font=("Cambria",12),width=17,bg="gainsboro",textvar=self.Address)
        self.txtAddress.grid(row=5,column=1)
        self.lbl=Label(self.combo_frame,text="E-Mail Address*\t  ",font=("Cambria",12),fg="blue")
        self.lbl.grid(row=6,column=0)
        self.txtEmail=Entry(self.combo_frame,font=("Cambria",12),width=17,bg="gainsboro",textvar=self.Email)
        self.txtEmail.grid(row=6,column=1)
        self.lbl=Label(self.combo_frame,text="Contact Number*\t+91",font=("Cambria",12),fg="blue")
        self.lbl.grid(row=7,column=0)
        self.txtContact=Entry(self.combo_frame,font=("Cambria",12),width=17,bg="gainsboro",textvar=self.Contact)
        self.txtContact.grid(row=7,column=1)
        self.lbl=Label(self.combo_frame,text="Work Experience(in years)*\t  ",font=("Cambria",12),fg="blue")
        self.lbl.grid(row=8,column=0)        
        self.experience=ttk.Combobox(self.combo_frame,values=["---Select--"]+list(range(60)))
        self.experience.current(0)
        self.experience.grid(row=8,column=1)  
        self.lbl=Label(self.combo_frame,text="Date of Birth (in DDMMYYYY)*\t  ",font=("Cambria",12),fg="blue")
        self.lbl.grid(row=9,column=0)
        self.txtDOB=Entry(self.combo_frame,font=("Cambria",12),width=17,bg="gainsboro",textvar=self.DOB)
        self.txtDOB.grid(row=9,column=1)
        self.lbl=Label(self.combo_frame,text="Research and Publications*\t  ",font=("Cambria",12),fg="blue")
        self.lbl.grid(row=10,column=0)
        self.txtResearch=Entry(self.combo_frame,font=("Cambria",12),width=17,bg="gainsboro",textvar=self.Res)
        self.txtResearch.grid(row=10,column=1)
        self.lbl=Label(self.combo_frame,text="Languages Spoken*\t  ",font=("Cambria",12),fg="blue")
        self.lbl.grid(row=11,column=0)
        self.txtLanguage=Entry(self.combo_frame,font=("Cambria",12),width=17,bg="gainsboro",textvar=self.Language)
        self.txtLanguage.grid(row=11,column=1)        
        self.chk=Checkbutton(self.declaration_frame,text="By clicking the submit button, I accept that the entered details are to the best of my knowledge\nand I shall be solely responsible for any errors in this appliaction.",var=self.chkValue)
        self.chk.grid(row=12,column=0)
        
        #Creating the required Buttons
        self.btnSubmit=Button(self.submit_frame,text="Submit",font=("Cambria",12,"bold"),fg="blue",command=self.Submit)
        self.btnSubmit.grid(row=13,column=0)
        self.btnReset=Button(self.submit_frame,text="Reset",font=("Cambria",12,"bold"),fg="blue",command=self.Reset)
        self.btnReset.grid(row=13,column=2)
        self.btnAbout=Button(self.contact_frame,text="About Us",font=("Cambria",12,"bold","underline"),fg="blue",command=self.About_Us)
        self.btnAbout.grid(row=14,column=0)
        self.lbl=Label(self.contact_frame,text=9*"\t",font=("Cambria",12))
        self.lbl.grid(row=14,column=1)
        self.btnContact=Button(self.contact_frame,text="Contact Us",font=("Cambria",12,"bold","underline"),fg="blue",command=self.Contact_Us)
        self.btnContact.grid(row=14,column=2)
        
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Functions for Buttons of New Doctor's Application>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
    def Reset(self):
        self.Name.set("")
        self.Qualifications.set("")
        self.Address.set("")
        self.Email.set("")
        self.Contact.set("")
        self.DOB.set("")
        self.Res.set("")
        self.Language.set("")              
        self.chkValue.set(False)
        self.department.current(0)
        self.experience.current(0)
        self.txtName.focus()   
        
    def Submit(self):        
        if not((self.chkValue.get())):
            tkinter.messagebox.askokcancel("Error-Check Box not ticked","Please agree to the terms and conditions before proceeding.\nTick the check box at the end of the form, else this form won't be submitted.")
        else:
            if(len(self.Name.get())==0):
                tkinter.messagebox.askokcancel("Error in Name entry","Please enter a valid name in the space provided. You haven't entered anything in the space provided for entering the Name.")
            else:
                if(len(self.Address.get())==0):
                    tkinter.messagebox.askokcancel("Error in Address entry","Please enter a valid address in the space provided. You haven't entered anything in the space provided for entering the Address.")
                else:
                    if(len(self.Email.get())==0):
                        tkinter.messagebox.askokcancel("Error in Email entry","Please enter a valid E-Mail in the space provided. You haven't entered anything in the space provided for entering the E-Mail.")
                    else:
                        if(len(self.Contact.get())!=10):
                            tkinter.messagebox.askokcancel("Error in Contact Number entry","Please enter a valid contact number of 10 digits in the space provided.")
                        else:
                            if(len(self.DOB.get())<8 or len(self.DOB.get())<7):
                                tkinter.messagebox.askokcancel("Error in Date of Birth entry","Please enter a valid date of birth in the space provided.")
                            else:
                                if(len(self.Res.get())==0):
                                    tkinter.messagebox.askokcancel("Error in Research and Publications entry","Please enter something in the text box meant for Research and Publications.\nIn case you don't have any Publications, mwntion \"NONE\"")
                                else:
                                    if(len(self.Language.get())==0):
                                        tkinter.messagebox.askokcancel("Error in Language Entry","Please enter some Language in the space meant for Languages.\nIn case of multiple entries, separate them with commas.")
                                    else:
                                        if(str(self.department.get())=="---Select---"):
                                            tkinter.messagebox.askokcancel("Error in Deparatment Entry","Please select a valid department.\nIn case you can't find some department here, immediately inform our Hospital Mangemnt of the same, procedure of which is given in the Contact Us section")
                                        else:
                                            if(str(self.experience.get())=="---Select---"):
                                                tkinter.messagebox.askokcancel("Error in Experience Entry","Please select a valid number of years for work experience.")
                                            else:
                                                if(len(self.Qualifications.get())==0):
                                                    tkinter.messagebox.askokcancel("Error in Qualifications Entry","You haven't made any entry in the Qualifications section.\nIn case you don't have any qualifications, enter \"NONE\".")
                                                else:
                                                    with open("New Applications.csv","r")as readFile:
                                                        reader=csv.reader(readFile)
                                                        lines=list(reader)                                                    
                                                    id=uuid.uuid4()
                                                    l=[[id,self.Name.get(),str(self.department.get()),self.Qualifications.get(),self.Address.get(),self.Email.get(),self.Contact.get(),str(self.experience.get()),self.DOB.get(),self.Res.get(),self.Language.get()]]
                                                    list1=lines+l
                                                    with open("New Applications.csv","w",newline="")as csvfile:
                                                        csvwriter=csv.writer(csvfile)
                                                        csvwriter.writerows(list1)                                                                                                        
                                                    tkinter.messagebox.askokcancel("Application Success","Dear Dr. "+self.Name.get()+",\n\tWe have received your application bearing the Application Id:"+str(id)+"\n\n\tWe have also sent you an SMS on your registered mobile number quoting this Application ID for further reference. Note that all further queries related to the staus of the application can be made only after quoting this Application Id. Hence, you are expected to keep it preserved for further reference.\n\tYou will receive a call from us on your registered mobile number within 7 working days where you will be guided on the further process.\n\tNote that you need to being all the original certificates when your are called for an interview.\n\tWe thank you for your active participation.\n\nWith regards,\nXYZ Hospital, New Delhi" )

    def About_Us(self):
        str_objectives="OUR OBJECTIVES:-\n\nWe at XYZ Hospital, New Delhi always try to provide our patients with the best medical infrastructure, and our 24X7 dedicated medical fraternity are always ready to serve you.\nFOR US OUR JOURNEY ITSELF IS OUR DESTINATION. BE A PART OF THIS MEDICAL REVOLUTION..\n\n"
        str_awards="AWARDS AND RECOGNITIONS:-\n\n(i) Best Multispeciality Hospital across India as per the survey by XXX.\n(ii) Best Cancer Care and Research Institute as per the survey by XXX.\n(iii) The first hospital in the country having the experience of more than X0,000 Open Heart Surgeries..\n\n"
        str_mission="FUTURE PLANS:-\n\nLET'S MAKE A HEALTHY, PROGRESSED AND HIGHLY ACHIEVING INDIA."
        tkinter.messagebox.askokcancel("About Us",str_objectives+str_awards+str_mission)
    
    def Contact_Us(self):
        str_address="ADDRESS:-\nXYZ Multispeciality Hospital,\n#17, Block II, Saket Road,\nSaket\nNew Delhi-122 002\n\n"
        str_mapview="LINK FOR NAVIGATION THROUGH GOOGLE MAPS:-\nmaps.google.com/sjhhVGY12/jhba\n\n"
        str_emailid="E-MAIL ADDRESSES:-\n(i) For queries regarding patient/doctor registration:\n  xyzregistration@gmail.com\n(ii) For obtaining past health records/medical scans of the patient:\n  xyzpatientsscan@gmail.com\n(iii) For feedbacks:\n  xyzfeedbacks@gmail.com\n(iv) For medical fraternity except our doctors and patients(like nurses,etc.):\n  xyzgeneralinfo@gmail.com\n\n"
        str_contact="PHONE NUMBER DIRECTORY:-\n(i) Toll free number:-XXXXXXXXXX\n(ii) General Ward Administrator Contact Number:-XXXXXXXXXX\n(iii) For enquiries of a patient through his/her Patient ID:-XXXXXXXXXX\n\n"
        tkinter.messagebox.askokcancel("Contact Us",str_address+str_mapview+str_emailid+str_contact)

#=====================================Creating a new Window for Forgot Username/Password========================================

class Forgot:
    def __init__(self,master):
        self.master=master
        self.master.title("Forgot Username/Password?")
        self.master.geometry('620x450+186+0')        
        self.master.config(bg="white")
        self.frame=Frame(self.master)        
        self.frame.grid(row=0,column=0)
        
        #Creating the required frames
        self.label_frame=LabelFrame(self.frame,bd=0)
        self.label_frame.grid(row=0,column=0)
        self.text_frame=LabelFrame(self.frame,relief="groove",bd=5)
        self.text_frame.grid(row=1,column=0,pady=20)
        self.btn_frame=LabelFrame(self.frame,relief="groove",bd=5)
        self.btn_frame.grid(row=2,column=0)
        self.about_frame=LabelFrame(self.frame,bd=0)
        self.about_frame.grid(row=3,column=0)
        
        #Creating the required variables
        self.Name=StringVar()
        self.Email=StringVar()
        self.DOB=StringVar()
        
        #Placing the required widgets
        self.lbl=Label(self.label_frame,text="RETRIEVE USERNAME AND PASSWORD PAGE",font=("Cambria",18,"bold","underline"),fg="AntiqueWhite4")
        self.lbl.grid(row=0,column=0)
        self.lbl=Label(self.label_frame,text="XYZ HOSPITAL,NEW DELHI\n",font=("Cambria",12,"underline"))
        self.lbl.grid(row=1,column=0)
        self.lbl=Label(self.label_frame,text="Don't worry, using this window, you can retrieve\nyour Username just by filling three entries\nand once you're done with that, you can straigtaway reset your password.\nIt's that easy!! Just confirm it's really you..",font=("Cambria",12))
        self.lbl.grid(row=2,column=0)       
        self.lbl=Label(self.label_frame,text="ENTRY FRAME",font=("Cambria",12,"underline"),fg="AntiqueWhite4")
        self.lbl.grid(row=3,column=0)
        self.lbl=Label(self.text_frame,text="Enter your full Name in CAPS",font=("Cambria",12),fg="blue")
        self.lbl.grid(row=4,column=0,pady=10)
        self.lbl=Label(self.text_frame,text="\tDr.",font=("Cambria",12))
        self.lbl.grid(row=4,column=1,pady=10)
        self.txtName=Entry(self.text_frame,font=("Cambria",12),textvar=self.Name,bg="gainsboro")
        self.txtName.grid(row=4,column=2,pady=10)
        self.lbl=Label(self.text_frame,text=2*" ",font=("Cambria",12))
        self.lbl.grid(row=4,column=3)
        self.lbl=Label(self.text_frame,text="Enter your E-Mail Address",font=("Cambria",12),fg="blue")
        self.lbl.grid(row=5,column=0,pady=10)
        self.lbl=Label(self.text_frame,text="\t  ",font=("Cambria",12))
        self.lbl.grid(row=5,column=1,pady=10)
        self.txtEmail=Entry(self.text_frame,font=("Cambria",12),textvar=self.Email,bg="gainsboro")
        self.txtEmail.grid(row=5,column=2,pady=10)
        self.lbl=Label(self.text_frame,text=2*" ",font=("Cambria",12))
        self.lbl.grid(row=4,column=3)        
        self.lbl=Label(self.text_frame,text="Enter the date of birth (in DDMMYYYY form)",font=("Cambria",12),fg="blue")
        self.lbl.grid(row=6,column=0,pady=10)
        self.lbl=Label(self.text_frame,text="\t  ",font=("Cambria",12))
        self.lbl.grid(row=6,column=1,pady=10)
        self.txtDOB=Entry(self.text_frame,font=("Cambria",12),textvar=self.DOB,bg="gainsboro")
        self.txtDOB.grid(row=6,column=2,pady=10)
        self.lbl=Label(self.text_frame,text=2*" ",font=("Cambria",12))
        self.lbl.grid(row=4,column=3)
        
        #Creating the Buttons       
        self.btnSubmit=Button(self.btn_frame,text="Submit",font=("Cambria",12,"bold","underline"),fg="blue",command=self.submit)
        self.btnSubmit.grid(row=7,column=0)
        self.btnReset=Button(self.btn_frame,text="Reset",font=("Cambria",12,"bold","underline"),fg="blue",command=self.reset)
        self.btnReset.grid(row=7,column=1)
        self.btnAbout=Button(self.about_frame,text="About us",font=("Cambria",10,"bold","underline"),fg="blue",command=self.About_Us)
        self.btnAbout.grid(row=8,column=0)
        self.lbl=Label(self.about_frame,text=125*" ")
        self.lbl.grid(row=8,column=1)
        self.btnContact=Button(self.about_frame,text="Contact us",font=("Cambria",10,"bold","underline"),fg="blue",command=self.Contact_Us)
        self.btnContact.grid(row=8,column=2) 

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Creating Functions for Buttons in the Forgot Username/Password Window>>>>>>>>>>>>>>>>>>>>>>>>>>
        
    def reset(self):
        self.Name.set("")
        self.Email.set("")
        self.DOB.set("")
        self.txtName.focus()
        
    def About_Us(self):
        str_objectives="OUR OBJECTIVES:-\n\nWe at XYZ Hospital, New Delhi always try to provide our patients with the best medical infrastructure, and our 24X7 dedicated medical fraternity are always ready to serve you.\nFOR US OUR JOURNEY ITSELF IS OUR DESTINATION. BE A PART OF THIS MEDICAL REVOLUTION..\n\n"
        str_awards="AWARDS AND RECOGNITIONS:-\n\n(i) Best Multispeciality Hospital across India as per the survey by XXX.\n(ii) Best Cancer Care and Research Institute as per the survey by XXX.\n(iii) The first hospital in the country having the experience of more than X0,000 Open Heart Surgeries..\n\n"
        str_mission="FUTURE PLANS:-\n\nLET'S MAKE A HEALTHY, PROGRESSED AND HIGHLY ACHIEVING INDIA."
        tkinter.messagebox.askokcancel("About Us",str_objectives+str_awards+str_mission)
    
    def Contact_Us(self):
        str_address="ADDRESS:-\nXYZ Multispeciality Hospital,\n#17, Block II, Saket Road,\nSaket\nNew Delhi-122 002\n\n"
        str_mapview="LINK FOR NAVIGATION THROUGH GOOGLE MAPS:-\nmaps.google.com/sjhhVGY12/jhba\n\n"
        str_emailid="E-MAIL ADDRESSES:-\n(i) For queries regarding patient/doctor registration:\n  xyzregistration@gmail.com\n(ii) For obtaining past health records/medical scans of the patient:\n  xyzpatientsscan@gmail.com\n(iii) For feedbacks:\n  xyzfeedbacks@gmail.com\n(iv) For medical fraternity except our doctors and patients(like nurses,etc.):\n  xyzgeneralinfo@gmail.com\n\n"
        str_contact="PHONE NUMBER DIRECTORY:-\n(i) Toll free number:-XXXXXXXXXX\n(ii) General Ward Administrator Contact Number:-XXXXXXXXXX\n(iii) For enquiries of a patient through his/her Patient ID:-XXXXXXXXXX\n\n"
        tkinter.messagebox.askokcancel("Contact Us",str_address+str_mapview+str_emailid+str_contact)
    
    def submit(self):     
        name=(self.Name.get())
        email=(self.Email.get())
        DOB=(self.DOB.get())
        list_of_lists=[]
        l=[]
        with open("Doctor's List.csv","r")as readFile:
            reader=csv.reader(readFile)
            lines=list(reader)
            skip=0
            count=0
            for x in lines:
                skip+=1
                if(skip==1):
                    continue
                else:
                    for y in x:
                        count+=1
                        if(count==1):
                            l.append(y)
                        if(count==2):
                            l.append(y)
                        if(count==7):
                            l.append(y)
                        if(count==10):
                            l.append(y)
                list_of_lists.append(l)
                count=0
        check=0
        for x in list_of_lists:
            if(x[0]==name and x[2]==email and x[3]==DOB):       
                str="You have entered correct credentials.\n\nYour Username is:\t"+x[1]+"\n\nPlease keep it secured for further usage. You can Reset your Password now from the next page."
                tkinter.messagebox.askokcancel("Username Retrieved Successfully!!",str)
                self.newwindow=Toplevel(self.master)        
                self.app=Reset(self.newwindow)
            else:
                tkinter.messagebox.askyesno("Error in the form filled","You details entered by you are incorrect. Kindly check again and enter the correct details for retrieving your username.\n\nIf the problem persists, feel free to contact the Hospital Mangement for further assistance, the contact numbers of which are accessible from Contact Us on the previous page.")
        
#=========================================Creating window for Resetting the Password============================================
        
class Reset:
    def __init__(self,master):
        self.master=master
        self.master.title("Reset Your Password-Doctor's Page")
        self.master.geometry('595x425+200+0')
        self.master.config(bg="white")
        self.frame=Frame(self.master)
        self.frame.grid(row=0,column=0)
        
        #Creating the required variables
        self.Username=StringVar()
        self.Password1=StringVar()
        self.Password2=StringVar()
        
        #Creating required frames
        self.label_frame=LabelFrame(self.frame,bd=0)
        self.label_frame.grid(row=0,column=0)
        self.entry_frame=LabelFrame(self.frame,relief="groove",bd=10)
        self.entry_frame.grid(row=1,column=0)
        self.button_frame=LabelFrame(self.frame,bd=0)
        self.button_frame.grid(row=2,column=0)
        self.contact_frame=LabelFrame(self.frame,bd=0)
        self.contact_frame.grid(row=3,column=0)
        
        #Placing the required widgets
        self.lbl=Label(self.label_frame,text="XYZ HOSPITAL, NEW DELHI",font=("Cambria",15,"bold","underline"),fg="AntiqueWhite4")
        self.lbl.grid(row=1,column=0,pady=10)
        self.lbl=Label(self.label_frame,text="We hope you have already recovered your Username.\n\nOn this page, you can Reset your Password by entering your Username.\nThese login credentials can be used for logging in in the future.\n\n",font=("cambria",12))
        self.lbl.grid(row=2,column=0)        
        self.lbl=Label(self.label_frame,text="ENTRY FRAME",font=("Cambria",12,"underline"),fg="AntiqueWhite4")
        self.lbl.grid(row=3,column=0,pady=5)
        self.lbl=Label(self.entry_frame,text="  Enter your Username\t\t\t",font=("Cambria",12))
        self.lbl.grid(row=4,column=0,pady=10)
        self.txtUsername=Entry(self.entry_frame,font=("Cambria",12),textvar=self.Username,bg="gainsboro")
        self.txtUsername.grid(row=4,column=1,pady=5)
        self.lbl=Label(self.entry_frame,text=5*" ",font=("Cambria",12))
        self.lbl.grid(row=4,column=2,pady=5)
        self.lbl=Label(self.entry_frame,text="  Enter your New Password\t\t\t",font=("Cambria",12))
        self.lbl.grid(row=5,column=0,pady=10)
        self.txtPassword1=Entry(self.entry_frame,font=("Cambra",12),show="*",textvar=self.Password1,bg="gainsboro")
        self.txtPassword1.grid(row=5,column=1,pady=5)
        self.lbl=Label(self.entry_frame,text=5*" ",font=("Cambria",12))
        self.lbl.grid(row=5,column=2,pady=5)
        self.lbl=Label(self.entry_frame,text="  Retype your new password\t\t\t",font=("Cambria",12))
        self.lbl.grid(row=6,column=0,pady=10)
        self.txtPassword2=Entry(self.entry_frame,font=("Cambria",12),show="*",textvar=self.Password2,bg="gainsboro")
        self.txtPassword2.grid(row=6,column=1,pady=5)
        self.lbl=Label(self.entry_frame,text=5*" ",font=("Cambria",12))
        self.lbl.grid(row=6,column=2,pady=5)
        
        #Creating required Buttons        
        self.btnSubmit=Button(self.button_frame,text="Submit",font=("Cambria",12,"bold"),fg="blue",command=self.Submit)
        self.btnSubmit.grid(row=7,column=0)
        self.btnReset=Button(self.button_frame,text="Reset",font=("Cambria",12,"bold"),fg="blue",command=self.Reset)
        self.btnReset.grid(row=7,column=1)
        self.btnAbout=Button(self.contact_frame,text="About us",font=("Cambria",10,"bold","underline"),fg="blue",command=self.About_Us)
        self.btnAbout.grid(row=8,column=0)
        self.lbl=Label(self.contact_frame,text=125*" ")
        self.lbl.grid(row=8,column=1)
        self.btnContact=Button(self.contact_frame,text="Contact us",font=("Cambria",10,"bold","underline"),fg="blue",command=self.Contact_Us)
        self.btnContact.grid(row=8,column=2) 
        
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Creating functions for Buttons on Reset Password Pag>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
    def Submit(self):
        with open("Doctor's List.csv","r")as readFile:
            reader=csv.reader(readFile)
            lines=list(reader)            
            lne1=-1
            if(self.Password1.get()==self.Password2.get() and len(self.Password1.get())!=0):                
                for x in lines:
                    count=0
                    lne1+=1
                    if(lne1==0):
                        continue
                    for y in x:                        
                        count+=1
                        if(count==2):
                            if(y==self.Username.get()):                                  
                                lines[lne1][2]=self.Password1.get()
                                with open("Doctor's List.csv","w",newline="")as csvfile:
                                    csvwriter=csv.writer(csvfile)
                                    csvwriter.writerows(lines)
                                str="Your Password change against the entered Username is successful.\nYour new login credentials are:\n\nUsername:"+self.Username.get()+"\nPassword:\t"+self.Password1.get()+"\n\nWith Regards,\nXYZ Hospital, New Delhi"
                                tkinter.messagebox.askokcancel("Password Changed Successfully",str)
            else:
                tkinter.messagebox.askyesno("Error in Password Entry","Either you haven't entered any password at all or the entered passwords don't match. Kindly rectify the same.\n\nIn case the problems persists, feel free to contact our Hospital Management, details of which are given under Contact Us on the previous page.\n\nWith regards,\nXYZ Hospital, New Delhi")
                self.Reset()            
    
    def Reset(self):
        self.Username.set("")
        self.Password1.set("")
        self.Password2.set("")
        self.txtUsername.focus()
        
    def About_Us(self):
        str_objectives="OUR OBJECTIVES:-\n\nWe at XYZ Hospital, New Delhi always try to provide our patients with the best medical infrastructure, and our 24X7 dedicated medical fraternity are always ready to serve you.\nFOR US OUR JOURNEY ITSELF IS OUR DESTINATION. BE A PART OF THIS MEDICAL REVOLUTION..\n\n"
        str_awards="AWARDS AND RECOGNITIONS:-\n\n(i) Best Multispeciality Hospital across India as per the survey by XXX.\n(ii) Best Cancer Care and Research Institute as per the survey by XXX.\n(iii) The first hospital in the country having the experience of more than X0,000 Open Heart Surgeries..\n\n"
        str_mission="FUTURE PLANS:-\n\nLET'S MAKE A HEALTHY, PROGRESSED AND HIGHLY ACHIEVING INDIA."
        tkinter.messagebox.askokcancel("About Us",str_objectives+str_awards+str_mission)
    
    def Contact_Us(self):
        str_address="ADDRESS:-\nXYZ Multispeciality Hospital,\n#17, Block II, Saket Road,\nSaket\nNew Delhi-122 002\n\n"
        str_mapview="LINK FOR NAVIGATION THROUGH GOOGLE MAPS:-\nmaps.google.com/sjhhVGY12/jhba\n\n"
        str_emailid="E-MAIL ADDRESSES:-\n(i) For queries regarding patient/doctor registration:\n  xyzregistration@gmail.com\n(ii) For obtaining past health records/medical scans of the patient:\n  xyzpatientsscan@gmail.com\n(iii) For feedbacks:\n  xyzfeedbacks@gmail.com\n(iv) For medical fraternity except our doctors and patients(like nurses,etc.):\n  xyzgeneralinfo@gmail.com\n\n"
        str_contact="PHONE NUMBER DIRECTORY:-\n(i) Toll free number:-XXXXXXXXXX\n(ii) General Ward Administrator Contact Number:-XXXXXXXXXX\n(iii) For enquiries of a patient through his/her Patient ID:-XXXXXXXXXX\n\n"
        tkinter.messagebox.askokcancel("Contact Us",str_address+str_mapview+str_emailid+str_contact)
        
#============================================Start of Window for Doctor's Personal Page==========================================

class Doc_Page:
    def __init__(self,master):
        self.master=master
        self.master.title("Doctor's Personal Page")
        self.master.geometry('882x472+74+0')
        self.master.config(bg="white")
        self.frame=Frame(self.master)
        self.frame.grid(row=0,column=0)
        
        #Craeting required frames
        self.label=LabelFrame(self.frame,bd=0)
        self.label.grid(row=0,column=0)
        self.text=LabelFrame(self.frame,relief="groove",bd=10)
        self.text.grid(row=1,column=0)        
        self.label_frame=LabelFrame(self.frame,bd=0)
        self.label_frame.grid(row=2,column=0)
        self.text_box=LabelFrame(self.frame,relief="groove",bd=10)
        self.text_box.grid(row=3,column=0)        
        self.Label_Frame=LabelFrame(self.frame,bd=0)
        self.Label_Frame.grid(row=4,column=0)
        self.Text_Box=LabelFrame(self.frame,relief="groove",bd=10)
        self.Text_Box.grid(row=5,column=0)
        self.lbl_frame=LabelFrame(self.frame,bd=0)
        self.lbl_frame.grid(row=6,column=0)
        
        #Creating the required variables
        self.Username=StringVar()
        self.Password=StringVar()
        self.Patname=StringVar()
        self.Patemail=StringVar()
        self.Medication=StringVar()
        
        #Placing the required widgets
        self.lbl=Label(self.label,text="DOCTOR'S PERSONAL PAGE",font=("Cambria",15,"bold","underline"),fg="AntiqueWhite4") 
        self.lbl.grid(row=0,column=0)
        self.lbl=Label(self.label,text="In the frame given below, first confirm your login details, before we authorize you to make any changes in Patient List contents.",font=("Cambria",12))
        self.lbl.grid(row=1,column=0)
        self.lbl=Label(self.label,text="LOGIN FRAME",font=("Cambria",12,"bold","underline"),fg="AntiqueWhite4")
        self.lbl.grid(row=2,column=0)
        self.lbl=Label(self.text,text="Enter your Username:\t",font=("Cambria",12),fg="blue")
        self.lbl.grid(row=3,column=0)
        self.txtUsername=Entry(self.text,font=("Cambria",12),bg="gainsboro",textvar=self.Username)
        self.txtUsername.grid(row=3,column=1)
        self.lbl=Label(self.text,text=15*" ",font=("Cambria",12))
        self.lbl.grid(row=3,column=2)
        self.lbl=Label(self.text,text="Enter your Password:\t",font=("Cambria",12),fg="blue")
        self.lbl.grid(row=4,column=0)
        self.txtPassword=Entry(self.text,font=("Cambria",12),show="*",bg="gainsboro",textvar=self.Password)
        self.txtPassword.grid(row=4,column=1)
        self.lbl=Label(self.text,text=15*" ",font=("Cambria",12))
        self.lbl.grid(row=4,column=2)
        self.btnSubmit=Button(self.text,text="Submit",font=("Cambria",12,"underline"),width=10,fg="blue",command=self.Submit)
        self.btnSubmit.grid(row=3,column=3)
        self.btnReset=Button(self.text,text="Reset",width=10,font=("Cambria",12,"underline"),fg="blue",command=self.Reset)
        self.btnReset.grid(row=4,column=3)
        self.btnAbout=Button(self.lbl_frame,text="About us",font=("Cambria",10,"bold","underline"),fg="blue",command=self.About_Us)
        self.btnAbout.grid(row=12,column=0)
        self.lbl=Label(self.lbl_frame,text=30*" "+"THANK YOU DOCTOR FOR MAKING US THE BEST AMONG THE REST ;)"+30*" ",font=("Cambria",12))
        self.lbl.grid(row=12,column=1)
        self.btnContact=Button(self.lbl_frame,text="Contact us",font=("Cambria",10,"bold","underline"),fg="blue",command=self.Contact_Us)
        self.btnContact.grid(row=12,column=2) 
     
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Creating Functions for Buttons on the Doctor's Page>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
    def About_Us(self):
        str_objectives="OUR OBJECTIVES:-\n\nWe at XYZ Hospital, New Delhi always try to provide our patients with the best medical infrastructure, and our 24X7 dedicated medical fraternity are always ready to serve you.\nFOR US OUR JOURNEY ITSELF IS OUR DESTINATION. BE A PART OF THIS MEDICAL REVOLUTION..\n\n"
        str_awards="AWARDS AND RECOGNITIONS:-\n\n(i) Best Multispeciality Hospital across India as per the survey by XXX.\n(ii) Best Cancer Care and Research Institute as per the survey by XXX.\n(iii) The first hospital in the country having the experience of more than X0,000 Open Heart Surgeries..\n\n"
        str_mission="FUTURE PLANS:-\n\nLET'S MAKE A HEALTHY, PROGRESSED AND HIGHLY ACHIEVING INDIA."
        tkinter.messagebox.askokcancel("About Us",str_objectives+str_awards+str_mission)
    
    def Contact_Us(self):
        str_address="ADDRESS:-\nXYZ Multispeciality Hospital,\n#17, Block II, Saket Road,\nSaket\nNew Delhi-122 002\n\n"
        str_mapview="LINK FOR NAVIGATION THROUGH GOOGLE MAPS:-\nmaps.google.com/sjhhVGY12/jhba\n\n"
        str_emailid="E-MAIL ADDRESSES:-\n(i) For queries regarding patient/doctor registration:\n  xyzregistration@gmail.com\n(ii) For obtaining past health records/medical scans of the patient:\n  xyzpatientsscan@gmail.com\n(iii) For feedbacks:\n  xyzfeedbacks@gmail.com\n(iv) For medical fraternity except our doctors and patients(like nurses,etc.):\n  xyzgeneralinfo@gmail.com\n\n"
        str_contact="PHONE NUMBER DIRECTORY:-\n(i) Toll free number:-XXXXXXXXXX\n(ii) General Ward Administrator Contact Number:-XXXXXXXXXX\n(iii) For enquiries of a patient through his/her Patient ID:-XXXXXXXXXX\n\n"
        tkinter.messagebox.askokcancel("Contact Us",str_address+str_mapview+str_emailid+str_contact)
    
    def Submit(self):
        u=(self.Username.get())
        p=(self.Password.get())
        d={}
        with open("Doctor's List.csv","r")as readFile:
            reader=csv.reader(readFile)
            lines=list(reader)
            count=0
            for row in lines:
                count+=1                
                if(count==1):
                    continue
                x=0
                for column in row:
                    x+=1
                    if(x==2):
                        d[column]=0
                        x=0
                        for c in row:
                            x+=1
                            if(x==3):
                                d[column]=c
                                break
                        break 
        check_for_prescence=0       
        for keys in d:
            if(keys==u):                                                                   
                check_for_prescence=1
                if(d[keys]==p):                                        
                    self.Create()                    
                else:
                    tkinter.messagebox.askokcancel("Invalid Password","Sorry! But you Password is incorrect.. Please enter a valid Password")
                    self.Password.set("")
                    self.txtPassword.focus()
        if(check_for_prescence==0):
            tkinter.messagebox.askokcancel("Invalid Username","Sorry! But your Username is incorrect.. Please enter a valid Username")
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()       
        
    def Reset(self):
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()
        
    def Create(self):
        self.lbl=Label(self.label_frame,text="After having logged in, in the following table, please enter the details\nof the patient whom you are attending by quoting Patient's Name and E-mail ID.",font=("Cambria",12))
        self.lbl.grid(row=5,column=0) 
        self.lbl=Label(self.label_frame,text="PATIENT DETAILS ENTRY FRAME",font=("Cambria",12),fg="AntiqueWhite4")
        self.lbl.grid(row=6,column=0)
        self.lbl=Label(self.text_box,text="Name of the Patient:\t",font=("Cambria",12),fg="blue")
        self.lbl.grid(row=7,column=0)
        self.txtPatient_Name=Entry(self.text_box,font=("Cambria",12),bg="gainsboro",textvar=self.Patname)
        self.txtPatient_Name.grid(row=7,column=1)
        self.lbl=Label(self.text_box,text=15*" ",font=("Cambria",12))
        self.lbl.grid(row=7,column=2)
        self.btnSubmit=Button(self.text_box,text="Submit",width=10,font=("Cambria",12,"underline"),fg="blue",command=self.Submit1)
        self.btnSubmit.grid(row=7,column=3)
        self.lbl=Label(self.text_box,text="E-Mail Address of the Patient:\t",font=("Cambria",12),fg="blue")
        self.lbl.grid(row=8,column=0)
        self.txtEMail=Entry(self.text_box,font=("Cambria",12),bg="gainsboro",textvar=self.Patemail)
        self.txtEMail.grid(row=8,column=1)
        self.lbl=Label(self.text_box,text=15*" ",font=("Cambria",12))
        self.lbl.grid(row=8,column=2)
        self.btnReset=Button(self.text_box,text="Reset",width=10,font=("Cambria",12,"underline"),fg="blue",command=self.Reset1)
        self.btnReset.grid(row=8,column=3)
        
    def Reset1(self):
        self.Patname.set("")
        self.Patemail.set("")
        self.txtPatient_Name.focus()
        
    def Submit1(self):
        with open("Patient List.csv","r")as readFile:
            reader=csv.reader(readFile)
            lines=list(reader)
        skip=0
        check_for_prescence=0
        for x in lines:
            skip+=1
            if(skip==1):
                continue            
            else:
                if(x[1]==self.Patname.get()):
                    check_for_prescence=1
                    if(x[6]==self.Patemail.get()):
                        doc=x[5]
                        with open("Doctor's List.csv","r")as readFile:
                            reader=csv.reader(readFile)
                            lines=list(reader)
                        for x in lines:
                            if(x[1]==self.Username.get()):
                                if(doc==x[0]):
                                    self.Last_Frame()
                                else:
                                    tkinter.messagebox.askyesno("Patient details don't match with you","As per our records, the patient had scheduled an appointment with some other doctor. Kindly convey the same to the patient. In case of discrepancies, kindly contact the Hospital Management on the contact numbers provided in the Contact Us on the previous page.")
                    else:
                        tkinter.messagebox.askokcancel("Invalid E-Mail Address entered","The E-Mail Address entered by you is incorrect as per our records. Kindly ask the patient to provide correct E-Mail Address to you.\n\nIf problem persists, kindly contact the Hospital Mangement on the contact numbers provided under Contact Us section on the previous page.")
                        self.Patemail.set("")
                        self.txtEMail.focus()
        if(check_for_prescence==0):
            tkinter.messagebox.askokcancel("Invalid Patient's Name entered","The patient's name entered by you is incorrect. Please enter the Name of the Patient correctly. Note that the Name is case-sensitive, and hence write the entire name in Uppercase Letters.\n\nIf the problem persists, kindly contact the Hospital Mangement on the contact numbers provided under Contact Us section on the previous page.")
            self.Reset1()
    
    def Last_Frame(self):
        self.lbl=Label(self.Label_Frame,text="PATIENT LIST MODIFICATIONS",fg="AntiqueWhite4",font=("Cambria",12,"underline"))
        self.lbl.grid(row=9)
        self.lbl=Label(self.Text_Box,text="Problem Resolved/Pending\t",font=("Cambria",12),fg="blue")
        self.lbl.grid(row=10,column=0)
        self.Resolved=ttk.Combobox(self.Text_Box,values=["---Select---","Pending","Resolved"])
        self.Resolved.current(0)
        self.Resolved.grid(row=10,column=1)
        self.lbl=Label(self.Text_Box,text=15*" ",font=("Cambria",12))
        self.lbl.grid(row=10,column=2)
        self.btnSubmit2=Button(self.Text_Box,text="Submit",width=10,font=("Cambria",12,"underline"),fg="blue",command=self.Submit2)
        self.btnSubmit2.grid(row=10,column=3)        
        self.lbl=Label(self.Text_Box,text="Prescribed Medicines/Scans/Surgeries\t",font=("Cambria",12),fg="blue")
        self.lbl.grid(row=11,column=0)
        self.Prescriptions=Entry(self.Text_Box,font=("Cambria",12),textvar=self.Medication)        
        self.Prescriptions.grid(row=11,column=1)
        self.lbl=Label(self.Text_Box,text=15*" ",font=("Cambria",12))
        self.lbl.grid(row=11,column=2)
        self.btnReset2=Button(self.Text_Box,text="Reset",width=10,font=("Cambria",12,"underline"),fg="blue",command=self.Reset2)
        self.btnReset2.grid(row=11,column=3)
        
    def Reset2(self):
        self.Medication.set("")
        self.Resolved.current(0)
        self.Prescriptions.focus()
    
    def Submit2(self):
        if(str(self.Resolved.get())=="---Select---"):
            tkinter.messagebox.askokcancel("Error in Present Status of Case","You haven't selected any option for the present status of the patient, i.e., whether his problem is resolved or is pending.\nKindly select a valid option for the same before proceeding further.")
            self.Reset2()
        else:
            if(len(self.Medication.get())==0):
                tkinter.messagebox.askokcancel("Error in Medications Prescribed","You haven't prescribed any Medicines/Scans/Surgeries to the patient. Please enter something in the respective text box.\nIf the patient is all good and requires no medical treatment, enter NONE in the text box.")
                self.Reset2()
            else:
                with open("Patient List.csv","r")as readFile:
                    reader=csv.reader(readFile)
                    lines=list(reader)
                l=[]
                for x in lines:
                    if(x[1]==self.Patname.get() and x[6]==self.Patemail.get()):
                        if(len(x)==11):                            
                            x[9]=str(self.Resolved.get())                            
                            x[10]=self.Medication.get()                            
                        else:
                            x.append(str(self.Prescriptions.get()))
                            x.append(self.Medication.get())
                    l.append(x)
                with open("Patient List.csv","w",newline="")as csvfile:
                    csvwriter=csv.writer(csvfile)
                    csvwriter.writerows(l)
                tkinter.messagebox.askokcancel("Succesfully edited","These details have been successfully updated in Patient List.csv. Please give a written prescription to the patient as well and communicate the health status to the patient as well.\n\nTHANKS A LOT FOR HEPING A PATIENT AND KEEPING OUR COUNTRY HEALTHY!!")
                self.newwindow=Toplevel(self.master)        
                self.app=Doc_Page(self.newwindow)
    
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Start of Patient's Master Window>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
class Patient_Window:
    def __init__(self,master):
        self.master=master
        self.master.title("Patient's Portal")
        self.master.geometry('878x486+80+0')
        self.master.config(bg="white")
        self.frame=Frame(self.master)
        self.frame.grid(row=0,column=0)
        
        #Creating required frames
        self.label_frame=LabelFrame(self.frame,bd=0)
        self.label_frame.grid(row=0,column=0)
        self.login_frame=LabelFrame(self.frame,relief="groove",bd=10)
        self.login_frame.grid(row=1,column=0)
        self.Label_frame=LabelFrame(self.frame,bd=0)
        self.Label_frame.grid(row=2,column=0)
        self.button_frame=LabelFrame(self.frame,bd=0)
        self.button_frame.grid(row=3,column=0)
        
        #Creating the required variables
        self.PatientID=StringVar()
        self.Password=StringVar()
        
        #Placing the required widgets
        self.lbl=Label(self.label_frame,text="XYZ HOSPITAL, NEW DELHI",font=("Cambria",20,"bold","underline"),fg="AntiqueWhite4")
        self.lbl.grid(row=0,column=0)
        self.lbl=Label(self.label_frame,text="Hi!! Welocome to the best Multispeciality Hospital of New Delhi!! At XYZ Hospital, we always keep Patients as our first priority.\nOur 24x7 dedicated medical experts are always there to help you. Give us the oppurtunity to attend to your ailments,\nand experience why we are the best and what distinguishes us from the rest..",font=("Cambria",12))
        self.lbl.grid(row=1,column=0)
        self.lbl=Label(self.label_frame,text="If you are already a registered patient, you may login by entering your details in the login frame. In case you have forgot\nyour Patient ID/Password, kindly contact Hospital Management\nas we can't allow the patients to reset their passwords without physical verification abiding by the\nprivacy guidelines. If you are a new patient, you may register yourself under New Patient Registration.\n\nIf you want to know more about us and/or want to provide feedback,\nuse Contact Us and/or About Us buttons.",font=("Cambria",12))
        self.lbl.grid(row=2,column=0,pady=5)
        self.lbl=Label(self.label_frame,text="PATIENT LOGIN FRAME",font=("Cambria",12,"bold","underline"),fg="blue")
        self.lbl.grid(row=3,column=0,pady=5)
        self.lbl=Label(self.login_frame,text="Enter Patient ID in the space provided\t\t",font=("Cambria",12),fg="blue")
        self.lbl.grid(row=4,column=0,pady=10)
        self.txtName=Entry(self.login_frame,font=("Cambria",12),bg="gainsboro",textvar=self.PatientID)
        self.txtName.grid(row=4,column=1)
        self.lbl=Label(self.login_frame,text=3*" ",font=("Cambria",12))
        self.lbl.grid(row=4,column=2)
        self.lbl=Label(self.login_frame,text="Enter your E-Mail Address in the space provided\t\t",font=("Cambria",12),fg="blue")
        self.lbl.grid(row=5,column=0,pady=10)
        self.txtPassword=Entry(self.login_frame,font=("Cambria",12),bg="gainsboro",textvar=self.Password)
        self.txtPassword.grid(row=5,column=1)
        self.lbl=Label(self.login_frame,text=3*" ",font=("Cambria",12))
        self.lbl.grid(row=5,column=2)
                
        #Placing the required Buttons
        self.btnSubmit=Button(self.Label_frame,text="Submit",font=("Cambria",12,"underline"),fg="blue",command=self.Submit)
        self.btnSubmit.grid(row=8,column=0)
        self.btnReset=Button(self.Label_frame,text="Reset",font=("Cambria",12,"underline"),fg="blue",command=self.Reset)
        self.btnReset.grid(row=8,column=1)
        self.lbl=Label(self.button_frame,text="",font=("Cambria",12))
        self.lbl.grid(row=9,column=0)
        self.btnContact_us=Button(self.button_frame,text="Contact Us",font=("Cambria",10,"underline"),fg="blue",command=self.Contact_Us)
        self.btnContact_us.grid(row=10,column=0)
        self.lbl=Label(self.button_frame,text=55*" ",font=("Cambria",12))
        self.lbl.grid(row=10,column=1)
        self.btnRegistration=Button(self.button_frame,text="New Patient Registartion",font=("Cambria",10,"underline"),fg="blue",command=self.Registration)
        self.btnRegistration.grid(row=10,column=2)
        self.lbl=Label(self.button_frame,text=55*" ",font=("Cambria",12))
        self.lbl.grid(row=10,column=3)         
        self.btnAbout_us=Button(self.button_frame,text="About Us",font=("Cambria",10,"underline"),fg="blue",command=self.About_Us)
        self.btnAbout_us.grid(row=10,column=4)
        
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Creating buttons for functions on the Patient Master Window>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
    def Credentials(self):
        d={}
        with open("Patient List.csv","r")as readFile:
            reader=csv.reader(readFile)
            lines=list(reader)
        count=0
        for row in lines:
            count+=1
            if(count==1):
                continue
            x=0
            for column in row:
                x+=1
                if(x==1):
                    d[column]=0
                    x=0
                    for c in row:
                        x+=1
                        if(x==7):
                            d[column]=c
                            break
                    break
        return(d)
    
    def Submit(self):
        u=(self.PatientID.get().strip())
        p=(self.Password.get())
        d=self.Credentials()        
        check_for_prescence=0
        for keys in d:
            if(keys==u):
                check_for_prescence=1
                if(d[keys]==p):
                    with open("Patient List.csv","r")as readFile:
                        reader=csv.reader(readFile)
                        lines=list(reader)
                    l=[]
                    skip=0
                    for x in lines:
                        skip+=1
                        if(skip==1):
                            continue
                        if(x[0]==u):
                            l=x
                    string="Dear Mr./Mrs. "+l[1]+",\n\n\tWelcome to the XYZ Hospital, New Delhi. We hope this finds you in high spirits and you are all good!!\n\tIn this page, we are going to give you all your details which have been registered with us, alongwith the prescribed dosages/medicines/scans/surgeries.\n\nPROBLEM RESOLVED OR NOT:\t"+l[9]+"\nPRESCRIBED MEDICATIONS/SCANS TO BE DONE/SURGERIES TO BE PERFORMED:\t"+l[10]+"\n\nGeneral Details:\nPatient ID:\t"+str(l[0])+"\nAge of the Patient:\t"+l[2]+"\nYour Doctor:\t"+l[5]+"\nYour E-Mail Address:\t"+l[6]+"\nYour Registered Mobile Number:\t"+l[7]+"\n\n\tHope that's all what you desired to get..\n\tWant to know something more? Feel free to contact our Hospital Mangement.. That's all from us at the moment..\n\nWith Regards,\nXYZ Hospital, New Delhi"
                    tkinter.messagebox.askyesno("Login Successful",string)
                else:
                    tkinter.messagebox.askyesno("Invalid E-Mail Address","Your entered E-Mail Address is incorrect. Kindly rectify it to proceed.\n\nIf problem persists, kindly contact the Hospital Management on the contact numbers provided under the Contact Us section.")
                    self.Password.set("")
                    self.txtPassword.focus()
        if(check_for_prescence==0):
            tkinter.messagebox.askyesno("Invalid PatientID entered","The Patient ID entered by you is incorrect as per our record. Kindly enter the correct Patient ID to continue.\n\nIn case the probelm persists, contact the Hospital Mangement who will guide you to recover your Patient ID, and the contact numbers of which have been provided in the Contact Us section..")
            self.PatientID.set("")
            self.Password.set("")
            self.txtName.focus()
    
    def Reset(self):
        self.PatientID.set("")
        self.Password.set("")
        self.txtName.focus()
        
    def Registration(self):
        self.newwindow=Toplevel(self.master)
        self.app=Patient_Registration(self.newwindow)    
        
    def About_Us(self):
        str_objectives="OUR OBJECTIVES:-\n\nWe at XYZ Hospital, New Delhi always try to provide our patients with the best medical infrastructure, and our 24X7 dedicated medical fraternity are always ready to serve you.\nFOR US OUR JOURNEY ITSELF IS OUR DESTINATION. BE A PART OF THIS MEDICAL REVOLUTION..\n\n"
        str_awards="AWARDS AND RECOGNITIONS:-\n\n(i) Best Multispeciality Hospital across India as per the survey by XXX.\n(ii) Best Cancer Care and Research Institute as per the survey by XXX.\n(iii) The first hospital in the country having the experience of more than X0,000 Open Heart Surgeries..\n\n"
        str_mission="FUTURE PLANS:-\n\nLET'S MAKE A HEALTHY, PROGRESSED AND HIGHLY ACHIEVING INDIA."
        tkinter.messagebox.askokcancel("About Us",str_objectives+str_awards+str_mission)
    
    def Contact_Us(self):
        str_address="ADDRESS:-\nXYZ Multispeciality Hospital,\n#17, Block II, Saket Road,\nSaket\nNew Delhi-122 002\n\n"
        str_mapview="LINK FOR NAVIGATION THROUGH GOOGLE MAPS:-\nmaps.google.com/sjhhVGY12/jhba\n\n"
        str_emailid="E-MAIL ADDRESSES:-\n(i) For queries regarding patient/doctor registration:\n  xyzregistration@gmail.com\n(ii) For obtaining past health records/medical scans of the patient:\n  xyzpatientsscan@gmail.com\n(iii) For feedbacks:\n  xyzfeedbacks@gmail.com\n(iv) For medical fraternity except our doctors and patients(like nurses,etc.):\n  xyzgeneralinfo@gmail.com\n\n"
        str_contact="PHONE NUMBER DIRECTORY:-\n(i) Toll free number:-XXXXXXXXXX\n(ii) General Ward Administrator Contact Number:-XXXXXXXXXX\n(iii) For enquiries of a patient through his/her Patient ID:-XXXXXXXXXX\n\n"
        tkinter.messagebox.askokcancel("Contact Us",str_address+str_mapview+str_emailid+str_contact)
        
#=============================================Creating the window for Patient Registration======================================
        
class Patient_Registration:
    def __init__(self,master):
        self.master=master
        self.master.title("New Patient Registration")
        self.master.geometry("652x500+180+0")
        self.master.config(bg="white")
        self.frame=Frame(self.master)
        self.frame.grid(row=0,column=0)
        
        #Creating the required variables
        self.name=StringVar()
        self.illness=StringVar()
        self.contact=StringVar()
        self.email=StringVar()
        self.address=StringVar()
        
        #Creating the required frames
        self.label_frame=LabelFrame(self.frame,bd=0)
        self.label_frame.grid(row=0,column=0)
        self.text_box=LabelFrame(self.frame,relief="groove",bd=10)
        self.text_box.grid(row=1,column=0)
        self.btnFrame=LabelFrame(self.frame,bd=0)
        self.btnFrame.grid(row=2,column=0)
        self.btn_frame=LabelFrame(self.frame,bd=0)
        self.btn_frame.grid(row=3,column=0)
        
        #Placing the required widgets
        self.lbl=Label(self.label_frame,text="PATIENT REGISTRATION PORTAL",font=("Cambria",20,"bold","underline"),fg="AntiqueWhite4")
        self.lbl.grid(row=0,column=0)
        self.lbl=Label(self.label_frame,text="Welcome to XYZ Hospital, New Delhi!! Don't worry.. We have medical experts who have\nvast experience of the most complicated of medical procedures.\nYou will soon be freed of all your diseases. All you need to do is to\nfill the registration form below, and we will soon get in touch with you!!",font=("Cambria",12))
        self.lbl.grid(row=1,column=0)
        self.lbl=Label(self.label_frame,text="Not sure of the Department which you want to refer?\nContact our Hospital Management at once..",font=("Cambria",12))
        self.lbl.grid(row=2,column=0)   
        self.lbl=Label(self.label_frame,text="APPLICATION'S FRAME",font=("Cambria",12,"underline"),fg="AntiqueWhite4")
        self.lbl.grid(row=3,column=0)
        self.lbl=Label(self.text_box,text="Enter your name\t\t",font=("Cambria",12),fg="blue")
        self.lbl.grid(row=4,column=0)
        self.txtName=Entry(self.text_box,font=("Cambria",12),bg="gainsboro",textvar=self.name)
        self.txtName.grid(row=4,column=1)
        self.lbl=Label(self.text_box,text=3*" ",font=("Cambria",12))
        self.lbl.grid(row=4,column=2)
        self.lbl=Label(self.text_box,text="Select your age(in years)\t\t",font=("Cambria",12),fg="blue")
        self.lbl.grid(row=5,column=0)
        self.Age=ttk.Combobox(self.text_box,values=["---Select---"]+list(range(100)))
        self.Age.current(0)
        self.Age.grid(row=5,column=1)
        self.lbl=Label(self.text_box,text="Enter your problem in brief\t\t",font=("Cambria",12),fg="blue")
        self.lbl.grid(row=6,column=0)
        self.txtIllness=Entry(self.text_box,font=("Cambria",12),bg="gainsboro",textvar=self.illness)
        self.txtIllness.grid(row=6,column=1)
        self.lbl=Label(self.text_box,text=3*" ",font=("Cambria",12))
        self.lbl.grid(row=6,column=2)
        self.lbl=Label(self.text_box,text="Select the Department\t\t",font=("Cambria",12),fg="blue")
        self.lbl.grid(row=7,column=0)
        self.Department=ttk.Combobox(self.text_box,values=["---Select---","Bariatric Surgery","Cardiac Surgery","Cardiology","Critical Care","Dental Surgery","Dermatology","Emergency Medicine","Endocrinology","ENT","Gastroentrology and GI Surgery","General and Laparoscopic Surgery","Gynecology and Obsterics","Haematology","Internal Medicine","Kidney Transpant","Lab Sciences","Nephrology","Neurology","Neurosurgery","Nuclear Medicine","Nutrition and Dietetics","Oncology","Opthalmology","Orthopaedics and Joints","Paediatrics","Physiotherapy","Psychiatry and Psychology","Plastic and Reconstructive Surgery","Pulmonology","Radiology","Spine Services","Urology"])
        self.Department.current(0)
        self.Department.grid(row=7,column=1)
        self.btnAssure=Button(self.text_box,text="Click me if you have entered the department",fg="blue",font=("Cambria",10),command=self.Assure)
        self.btnAssure.grid(row=8,column=1)
        self.lbl=Label(self.text_box,text="",font=("Cambria",12))
        self.lbl.grid(row=9,column=0)
        self.lbl=Label(self.text_box,text="Enter your E-Mail Address\t\t",font=("Cambria",12),fg="blue")
        self.lbl.grid(row=10,column=0)
        self.txtEmail=Entry(self.text_box,font=("Cambria",12),bg="gainsboro",textvar=self.email)
        self.txtEmail.grid(row=10,column=1)
        self.lbl=Label(self.text_box,text=3*" ",font=("Cambria",12))
        self.lbl.grid(row=10,column=2)
        self.lbl=Label(self.text_box,text="Enter your Contact Number(+91)\t\t",font=("Cambria",12),fg="blue")
        self.lbl.grid(row=11,column=0)
        self.txtContact=Entry(self.text_box,font=("Cambria",12),bg="gainsboro",textvar=self.contact)
        self.txtContact.grid(row=11,column=1)
        self.lbl=Label(self.text_box,text=3*" ",font=("Cambria",12))
        self.lbl.grid(row=11,column=2)
        self.lbl=Label(self.text_box,text="Enter your Contact Address\t\t",font=("Cambria",12),fg="blue")
        self.lbl.grid(row=12,column=0)
        self.txtAddress=Entry(self.text_box,font=("Cambria",12),bg="gainsboro",textvar=self.address)
        self.txtAddress.grid(row=12,column=1)
        self.lbl=Label(self.text_box,text=3*" ",font=("Cambria",12))
        self.lbl.grid(row=12,column=2)
        
        #Creating the required Buttons
        self.btnSubmit=Button(self.btnFrame,text="Submit",font=("Cambria",12,"underline"),fg="blue",command=self.Submit)
        self.btnSubmit.grid(row=16,column=0)
        self.btnReset=Button(self.btnFrame,text="Reset",command=self.Reset,font=("Cambria",12,"underline"),fg="blue")
        self.btnReset.grid(row=16,column=1)        
        self.btnAbout=Button(self.btn_frame,text="About Us",font=("Cambria",10,"underline"),fg="blue",command=self.About_Us)
        self.btnAbout.grid(row=17,column=0)        
        self.btnDoc=Label(self.btn_frame,text=135*" ",font=("Cambria",10),fg="blue")
        self.btnDoc.grid(row=17,column=1)        
        self.btnContact=Button(self.btn_frame,text="Contact Us",font=("Cambria",10,"underline"),fg="blue",command=self.Contact_Us)
        self.btnContact.grid(row=17,column=2)                  
        
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Creating required functions for Buttons>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
    def About_Us(self):
        str_objectives="OUR OBJECTIVES:-\n\nWe at XYZ Hospital, New Delhi always try to provide our patients with the best medical infrastructure, and our 24X7 dedicated medical fraternity are always ready to serve you.\nFOR US OUR JOURNEY ITSELF IS OUR DESTINATION. BE A PART OF THIS MEDICAL REVOLUTION..\n\n"
        str_awards="AWARDS AND RECOGNITIONS:-\n\n(i) Best Multispeciality Hospital across India as per the survey by XXX.\n(ii) Best Cancer Care and Research Institute as per the survey by XXX.\n(iii) The first hospital in the country having the experience of more than X0,000 Open Heart Surgeries..\n\n"
        str_mission="FUTURE PLANS:-\n\nLET'S MAKE A HEALTHY, PROGRESSED AND HIGHLY ACHIEVING INDIA."
        tkinter.messagebox.askokcancel("About Us",str_objectives+str_awards+str_mission)
    
    def Contact_Us(self):
        str_address="ADDRESS:-\nXYZ Multispeciality Hospital,\n#17, Block II, Saket Road,\nSaket\nNew Delhi-122 002\n\n"
        str_mapview="LINK FOR NAVIGATION THROUGH GOOGLE MAPS:-\nmaps.google.com/sjhhVGY12/jhba\n\n"
        str_emailid="E-MAIL ADDRESSES:-\n(i) For queries regarding patient/doctor registration:\n  xyzregistration@gmail.com\n(ii) For obtaining past health records/medical scans of the patient:\n  xyzpatientsscan@gmail.com\n(iii) For feedbacks:\n  xyzfeedbacks@gmail.com\n(iv) For medical fraternity except our doctors and patients(like nurses,etc.):\n  xyzgeneralinfo@gmail.com\n\n"
        str_contact="PHONE NUMBER DIRECTORY:-\n(i) Toll free number:-XXXXXXXXXX\n(ii) General Ward Administrator Contact Number:-XXXXXXXXXX\n(iii) For enquiries of a patient through his/her Patient ID:-XXXXXXXXXX\n\n"
        tkinter.messagebox.askokcancel("Contact Us",str_address+str_mapview+str_emailid+str_contact)
    
    def Assure(self):
        if(str(self.Department.get())=="---Select---"):
            tkinter.messagebox.askokcancel("Button falsely Pressed","\n\nSorry!! But you need to press the button only if you have selected a valid department from the drop-down menu.\nKindly take into account the same and fill the form again.\n\nWith regards,\nXYZ Hospital, New Delhi")
            self.Reset()
        else:
            dep=str(self.Department.get())
            with open("Doctor's List.csv","r")as readFile:
                reader=csv.reader(readFile)
                lines=list(reader)
            l=["---Select---"]
            for x in lines:
                if(x[3]==dep):
                    l.append(x[0])
            self.lbl=Label(self.text_box,text="Choose a doctor from the list\t\t",font=("Cambria",12),fg="blue")
            self.lbl.grid(row=9,column=0)
            self.Doctor=ttk.Combobox(self.text_box,values=l)
            self.Doctor.current(0)
            self.Doctor.grid(row=9,column=1)
            self.lbl=Label(self.text_box,text=3*" ",font=("Cambria",12))
            self.lbl.grid(row=9,column=2)
            
    def Reset(self):
        self.contact.set("")    
        self.email.set("")
        self.name.set("")
        self.illness.set("")
        self.address.set("")
        self.Department.current(0)
        self.Age.current(0)
    
    def Submit(self):
        if(len(self.name.get())==0):
            tkinter.messagebox.askokcancel("Error in Name entry","You haven't enterd your Name in the respective text box. Kindly enter a valid name before proceeding further.")
        else:
            if(len(self.illness.get())==0):
                tkinter.messagebox.askokcancel("Error in Medical Problem entry","You haven't entered anything in the text-box supposed for entry of medical problem. Kindly rectify the same before proceeding further.")
            else:
                if(len(self.contact.get())!=10):
                    tkinter.messagebox.askokcancel("Error in Conntact Number entry","You have entered an invalid contact number. Please rectify the same before proceeding further.")
                else:
                    if(len(self.email.get())==0):
                        tkinter.messagebox.askokcancel("Error In E-Mail Address entry","You haven't entered anything in the text-box for entering E-Mail address. Please rectify the same before proceeding futher.")
                    else:
                        if(len(self.address.get())==0):
                            tkinter.messagebox.askokcancel("Error in Residential Address entered","You haven't entered anything in the text-box for entering your Residential address. Please rectify the same before proceeding further.")
                        else:
                            if(str(self.Department.get())=="---Select--"):
                                tkinter.messagebox.askokcancel("Error in Department Entry","You haven't selected any department. In case you don't know about the department, kindly feel free to contact the Hospital Mangement on the contact numbers provided in the Contact Us section. After selecting the department, click on the button to get a list if available doctors in that department.")
                            else:
                                if(str(self.Age.get())=="---Select---"):
                                    tkinter.messagebox.askokcancel("Error in Age Entry","You haven't selected any value for your Age in years. Kindly select an age of the patient entry before proceeding ahead.")
                                else:
                                    id=uuid.uuid4()
                                    entry=[[str(id),self.name.get(),self.Age.get(),self.illness.get(),self.Department.get(),self.Doctor.get(),self.email.get(),self.contact.get(),self.address.get()]]
                                    with open("Patient List.csv","r")as readFile:
                                        reader=csv.reader(readFile)
                                        lines=list(reader)
                                    l=lines+entry
                                    with open("Patient List.csv","w",newline="")as csvfile:
                                        csvwriter=csv.writer(csvfile)
                                        csvwriter.writerows(l)
                                    stri="Dear Mr./Mrs. "+self.name.get()+",\n\n\tYour registration is successful, and you are very close to get all your ailments resolved. Our Hospital Management will call you within 1 working day to provide you with your appointment date and time.\n\tTill then, you can contact our Hospital Mangement for any queries. While contacting, you need to quote your Patient ID to be\t"+str(id)+".\n\tKeep your Patient ID secured for further usage.\n\nWith Regards,\nXYZ Hospital, New Delhi."
                                    tkinter.messagebox.askyesno("Successful Registration of the Patient",stri)
    

#==================<><><><><><><><><><><>Ending the Program for Hospital Management System<><><><><><><><><><><>=================

#Last Statement
if __name__=='__main__':
    main()
    
#Hope you liked it ;)