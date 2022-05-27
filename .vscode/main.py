from tkinter import*
from tkinter import ttk
from tokenize import String
from PIL import Image ,ImageTk
import tkinter
import os
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help

class Face_Recognition_System:
 def __init__(self,root):
    self.root = root
    self.root.geometry("1530x790+0+0")
    self.root.title("face Recognition System")

    img=Image.open (r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\face recognition system\standford.jpg")
    img=img.resize((480,200),Image.ANTIALIAS)
    self.photoimg = ImageTk.PhotoImage(img)

    f_lbl=Label(self.root,image=self.photoimg)
    f_lbl.place(x=0,y=0,width=480,height=200)

     
    img1=Image.open (r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\face recognition system\faces.png")
    img1=img1.resize((480,130),Image.ANTIALIAS)
    self.photoimg1 = ImageTk.PhotoImage(img1)

    f_lbl=Label(self.root,image=self.photoimg1)
    f_lbl.place(x=480,y=0,width=480,height=130)
    

    img2=Image.open (r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\face recognition system\standford.jpg")
    img2=img2.resize((480,130),Image.ANTIALIAS)
    self.photoimg2 = ImageTk.PhotoImage(img2)

    f_lbl=Label(self.root,image=self.photoimg2)
    f_lbl.place(x=960,y=0,width=480,height=130)


    img3=Image.open (r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\face recognition system\bg.jpg")
    img3=img3.resize((1500,710),Image.ANTIALIAS)
    self.photoimg3 = ImageTk.PhotoImage(img3)

    bg_img=Label(self.root,image=self.photoimg3)
    bg_img.place(x=0,y=130,width=1500,height=710)

    title_lbl=Label(bg_img,text="FACE  RECOGNITION  ATTENDENCE  SYSTEM  SOFTWARE",font=("times new roman",25,"bold"),bg="white",fg="red")
    title_lbl.place(x=0,y=0,width=1490,height=40)

    def time():
        string=strftime('%H:%M:%S %p')
        lbl.config(text=string)
        lbl.after(1000,time)

    lbl=Label(title_lbl, font=("times new roman",15,"bold"),bg="white",fg="dark blue")
    lbl.place(x=0,y=0,width=110,height=40)
    time()


    img4=Image.open (r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\face recognition system\student.jpg")
    img4=img4.resize((200,200),Image.ANTIALIAS)
    self.photoimg4 = ImageTk.PhotoImage(img4)
    
    b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
    b1.place(x=150,y=70,width=200,height=200)

    b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
    b1_1.place(x=150,y=270,width=200,height=30)


    img5=Image.open (r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\face recognition system\student.jpg")
    img5=img5.resize((200,200),Image.ANTIALIAS)
    self.photoimg5 = ImageTk.PhotoImage(img5)
    
    b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
    b1.place(x=420,y=70,width=200,height=200)

    b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
    b1_1.place(x=420,y=270,width=200,height=30)

    

    img6=Image.open (r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\face recognition system\student.jpg")
    img6=img6.resize((200,200),Image.ANTIALIAS)
    self.photoimg6 = ImageTk.PhotoImage(img6)
    
    b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
    b1.place(x=690,y=70,width=200,height=200)

    b1_1=Button(bg_img,text="Attendence",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
    b1_1.place(x=690,y=270,width=200,height=30)



    img7=Image.open (r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\face recognition system\student.jpg")
    img7=img7.resize((200,200),Image.ANTIALIAS)
    self.photoimg7 = ImageTk.PhotoImage(img7)
    
    b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
    b1.place(x=960,y=70,width=200,height=200)

    b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
    b1_1.place(x=960,y=270,width=200,height=30)



    img8=Image.open (r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\face recognition system\student.jpg")
    img8=img8.resize((200,200),Image.ANTIALIAS)
    self.photoimg8 = ImageTk.PhotoImage(img8)
    
    b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
    b1.place(x=150,y=300,width=200,height=200)

    b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
    b1_1.place(x=150,y=500,width=200,height=30)
    

    img9=Image.open (r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\face recognition system\student.jpg")
    img9=img9.resize((200,200),Image.ANTIALIAS)
    self.photoimg9 = ImageTk.PhotoImage(img9)
    
    b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
    b1.place(x=420,y=300,width=200,height=200)

    b1_1=Button(bg_img,text="Photos",command=self.open_img,cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
    b1_1.place(x=420,y=500,width=200,height=30)



    img10=Image.open (r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\face recognition system\student.jpg")
    img10=img10.resize((200,200),Image.ANTIALIAS)
    self.photoimg10 = ImageTk.PhotoImage(img10)
    
    b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
    b1.place(x=690,y=300,width=200,height=200)

    b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
    b1_1.place(x=690,y=500,width=200,height=30)



    img11=Image.open (r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\face recognition system\student.jpg")
    img11=img11.resize((200,200),Image.ANTIALIAS)
    self.photoimg11 = ImageTk.PhotoImage(img11)
    
    b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
    b1.place(x=960,y=300,width=200,height=200)

    b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit ,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
    b1_1.place(x=960,y=500,width=200,height=30)

 def open_img(self):
     os.startfile("data")

 def iExit(self):
     self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit",parent=self.root)
     if  self.iExit>0:
         self.root.destroy()
     else:
        return


 def student_details(self):
    self.new_window=Toplevel(self.root)
    self.app=Student(self.new_window)

 def train_data(self):
    self.new_window=Toplevel(self.root)
    self.app=Train(self.new_window)

 def face_data(self):
    self.new_window=Toplevel(self.root)
    self.app=Face_Recognition(self.new_window)

 def attendance_data(self):
    self.new_window=Toplevel(self.root)
    self.app=Attendance(self.new_window)

 def developer_data(self):
    self.new_window=Toplevel(self.root)
    self.app=Developer(self.new_window)

 def help_data(self):
    self.new_window=Toplevel(self.root)
    self.app=Help(self.new_window)
















    

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
