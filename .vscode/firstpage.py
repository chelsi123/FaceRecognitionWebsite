from tkinter import*
from tkinter import ttk
from tokenize import String
from PIL import Image ,ImageTk
import tkinter
import os
from time import strftime
from datetime import datetime
from studentDetails import Student 
from train import Train
from faceDetector import Face_Recognition


class Face_recognition_System:
 def __init__(self,root):
    self.root = root
    self.root.geometry("1380x790+0+0")
    self.root.title("Face Recognition System")

    image1=Image.open (r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\attendance system\Images\faces.jpg")
    image1=image1.resize((1380,200),Image.Resampling.LANCZOS)
    self.photoimg1 = ImageTk.PhotoImage(image1)

    f_label=Label(self.root,image=self.photoimg1)
    f_label.place(x=0,y=0,width=1380,height=200)

    image2=Image.open (r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\attendance system\Images\background.jpg")
    image2=image2.resize((1380,710),Image.Resampling.LANCZOS)
    self.photoimg2 = ImageTk.PhotoImage(image2)

    backg_img=Label(self.root,image=self.photoimg2)
    backg_img.place(x=0,y=200,width=1380,height=710)

    ttl_label=Label(backg_img,text="FACE  RECOGNITION  ATTENDENCE  SYSTEM ",font=("comicsansns",25,"bold"),bg="white",fg="purple")
    ttl_label.place(x=0,y=0,width=1380,height=40)
     

    def time():
        string=strftime('%H:%M:%S %p')
        label.config(text=string)
        label.after(1000,time)

    label=Label(ttl_label, font=("times new roman",15,"bold"),bg="white",fg="dark blue")
    label.place(x=0,y=0,width=110,height=40)
    time()

    image3=Image.open (r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\attendance system\Images\student.jpg")
    image3=image3.resize((180,180),Image.Resampling.LANCZOS)
    self.photoimg3 = ImageTk.PhotoImage(image3)
    
    btn1=Button(backg_img,image=self.photoimg3,cursor="hand2",command=self.studentDetails)
    btn1.place(x=120,y=160,width=180,height=180)

    btn1_1=Button(backg_img,text="Student Details",cursor="hand2",command=self.studentDetails,font=("comicsansns",14,"bold"),bg="dark blue",fg="white")
    btn1_1.place(x=120,y=330,width=180,height=30)


    image4=Image.open (r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\attendance system\Images\Train.jpg")
    
    image4=image4.resize((180,180),Image.Resampling.LANCZOS)
    self.photoimg4 = ImageTk.PhotoImage(image4)
    
    btn1=Button(backg_img,image=self.photoimg4,cursor="hand2",command=self.train_Data)
    btn1.place(x=360,y=160,width=180,height=180)

    btn1_1=Button(backg_img,text="Train Data",cursor="hand2",command=self.train_Data,font=("comicsansns",15,"bold"),bg="dark blue",fg="white")
    btn1_1.place(x=360,y=330,width=180,height=30)

    

    image5=Image.open (r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\attendance system\Images\faceRecog.png")
    image5=image5.resize((180,180),Image.Resampling.LANCZOS)
    self.photoimg5 = ImageTk.PhotoImage(image5)
    
    btn1=Button(backg_img,image=self.photoimg5,cursor="hand2",command=self.face_Data)
    btn1.place(x=600,y=160,width=180,height=180)

    btn1_1=Button(backg_img,text="Face Detector",cursor="hand2",command=self.face_Data,font=("comicsansns",15,"bold"),bg="dark blue",fg="white")
    btn1_1.place(x=600,y=330,width=180,height=30)

    
    

    image6=Image.open (r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\attendance system\Images\photos.png")
    image6=image6.resize((180,180),Image.Resampling.LANCZOS)
    self.photoimg6 = ImageTk.PhotoImage(image6)
    
    btn1=Button(backg_img,image=self.photoimg6,cursor="hand2",command=self.open_img)
    btn1.place(x=840,y=160,width=180,height=180)

    btn1_1=Button(backg_img,text="Photos",cursor="hand2",command=self.open_img,font=("comicsansns",15,"bold"),bg="dark blue",fg="white")
    btn1_1.place(x=840,y=330,width=180,height=30)
    

    image7=Image.open (r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\attendance system\Images\exit.png")
    image7=image7.resize((180,180),Image.Resampling.LANCZOS)
    self.photoimg7 = ImageTk.PhotoImage(image7)
    
    btn1=Button(backg_img,image=self.photoimg7,cursor="hand2",command=self.Exit)
    btn1.place(x=1080,y=160,width=180,height=180)

    btn1_1=Button(backg_img,text="Exit",cursor="hand2",command=self.Exit,font=("comicsansns",15,"bold"),bg="dark blue",fg="white")
    btn1_1.place(x=1080,y=330,width=180,height=30)

 def open_img(self):
     os.startfile("data")

 def Exit(self):
     self.Exit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit",parent=self.root)
     if  self.Exit>0:
         self.root.destroy()
     else:
        return


 def studentDetails(self):
    self.new_window=Toplevel(self.root)
    self.app=Student(self.new_window)

 def train_Data(self):
    self.new_window=Toplevel(self.root)
    self.app=Train(self.new_window)

 def face_Data(self):
    self.new_window=Toplevel(self.root)
    self.app=Face_Recognition(self.new_window)

if __name__ == "__main__":
    root=Tk()
    obj=Face_recognition_System(root)
    root.mainloop()
