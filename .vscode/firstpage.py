from tkinter import*
from tkinter import ttk
from tokenize import String
from PIL import Image ,ImageTk
import tkinter
import os
from time import strftime
from datetime import datetime
from sd import Student 
from train import Train
from faceDetector import Face_Recognition
# from attendance import Attendance
# from developer import Developer
# from help import Help

class Face_Recognition_System:
 def __init__(self,root):
    self.root = root
    self.root.geometry("1530x790+0+0")
    self.root.title("face Recognition System")

    img=Image.open (r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\attendance system\a.jpg")
    img=img.resize((1380,200),Image.Resampling.LANCZOS)
    self.photoimg = ImageTk.PhotoImage(img)

    f_lbl=Label(self.root,image=self.photoimg)
    f_lbl.place(x=0,y=0,width=1380,height=200)

    img3=Image.open (r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\attendance system\bg.jpg")
    img3=img3.resize((1380,710),Image.ANTIALIAS)
    self.photoimg3 = ImageTk.PhotoImage(img3)

    bg_img=Label(self.root,image=self.photoimg3)
    bg_img.place(x=0,y=200,width=1380,height=710)

    title_lbl=Label(bg_img,text="FACE  RECOGNITION  ATTENDENCE  SYSTEM  SOFTWARE",font=("comicsansns",25,"bold"),bg="white",fg="purple")
    title_lbl.place(x=0,y=0,width=1380,height=40)
     

    def time():
        string=strftime('%H:%M:%S %p')
        lbl.config(text=string)
        lbl.after(1000,time)

    lbl=Label(title_lbl, font=("times new roman",15,"bold"),bg="white",fg="dark blue")
    lbl.place(x=0,y=0,width=110,height=40)
    time()

    img4=Image.open (r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\attendance system\student.jpg")
    img4=img4.resize((150,150),Image.ANTIALIAS)
    self.photoimg4 = ImageTk.PhotoImage(img4)
    
    b1=Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.student_details)
    b1.place(x=100,y=180,width=150,height=150)

    b1_1=Button(bg_img,text="Student Details",cursor="hand2",command=self.student_details,font=("times new roman",14,"bold"),bg="dark blue",fg="white")
    b1_1.place(x=100,y=315,width=150,height=30)


    img5=Image.open (r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\attendance system\d.jpg")
    
    img5=img5.resize((150,150),Image.ANTIALIAS)
    self.photoimg5 = ImageTk.PhotoImage(img5)
    
    b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.train_data)
    b1.place(x=300,y=180,width=150,height=150)

    b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
    b1_1.place(x=300,y=315,width=150,height=30)

    

    img6=Image.open (r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\attendance system\b.png")
    img6=img6.resize((150,150),Image.ANTIALIAS)
    self.photoimg6 = ImageTk.PhotoImage(img6)
    
    b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_data)
    b1.place(x=500,y=180,width=150,height=150)

    b1_1=Button(bg_img,text="Face Detectors",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
    b1_1.place(x=500,y=315,width=150,height=30)

    img8=Image.open (r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\attendance system\c.jpg")
    
    img8=img8.resize((150,150),Image.ANTIALIAS)
    self.photoimg8 = ImageTk.PhotoImage(img8)
    
    b1=Button(bg_img,image=self.photoimg8,cursor="hand2")
    b1.place(x=700,y=180,width=150,height=150)

    b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
    b1_1.place(x=700,y=315,width=150,height=30)
    

    img9=Image.open (r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\attendance system\e.png")
    img9=img9.resize((150,150),Image.ANTIALIAS)
    self.photoimg9 = ImageTk.PhotoImage(img9)
    
    b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
    b1.place(x=900,y=180,width=150,height=150)

    b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
    b1_1.place(x=900,y=315,width=150,height=30)
    

    img11=Image.open (r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\attendance system\g.png")
    img11=img11.resize((150,150),Image.ANTIALIAS)
    self.photoimg11 = ImageTk.PhotoImage(img11)
    
    b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
    b1.place(x=1100,y=180,width=150,height=150)

    b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
    b1_1.place(x=1100,y=315,width=150,height=30)

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

#  def attendance_data(self):
#     self.new_window=Toplevel(self.root)
#     self.app=Attendance(self.new_window)

#  def developer_data(self):
#     self.new_window=Toplevel(self.root)
#     self.app=Developer(self.new_window)

#  def help_data(self):
#     self.new_window=Toplevel(self.root)
#     self.app=Help(self.new_window)


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
