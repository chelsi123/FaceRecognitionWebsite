from ast import Break
from pyexpat import features
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from cv2 import cvtColor
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_label = Label(self.root, text="FACE RECOGNITION",font=("comicsansns", 25, "bold"), bg="white", fg="green")
        title_label.place(x=0, y=0, width=1380, height=45)

        img = Image.open(r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\attendance system\Images\detector.webp")
        img = img.resize((1380,650), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_label = Label(self.root, image=self.photoimg)
        f_label.place(x=0, y=45, width=1380, height=650)


        

        btn1_1=Button(f_label,command=self.face_recog,text="Face Recognition",cursor="hand2",font=("comicsansns",18,"bold"),bg="darkgreen",fg="white")
        btn1_1.place(x=590,y=550,width=400,height=40)
    
    def attendance(self,i,r,n,c):
          
        with open(r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\attendance system\.vscode\attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (c not in name_list)):
              now=datetime.now()
              d1=now.strftime("%d/%m/%Y")
              dtString=now.strftime("%H:%M:%S")
              f.writelines(f"\n{i},{r},{n},{c},{dtString},{d1},present")

    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clsf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            
            cordinates=[]
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clsf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                
                conn=mysql.connector.connect(host="localhost",username="root",password="9783185113",database="face_recognizer")
                my_cursor=conn.cursor()

                
                my_cursor.execute("select id from student where Id="+str(id))
                i=my_cursor.fetchone()
                i=str(i)
                
                my_cursor.execute("select Roll from student where Id="+str(id))
                r=my_cursor.fetchone()
                r=str(r)
                
                my_cursor.execute("select Name from student where Id="+str(id))
                n=my_cursor.fetchone()
                n=str(n)            
                
                my_cursor.execute("select Class from student where Id="+str(id))
                c=my_cursor.fetchone()
                c=str(c)
                
                if confidence>75:
                    cv2.putText(img,f"Id:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)                    
                    cv2.putText(img,f"Class:{c}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)
                    self.attendance(i,r,n,c)
                    
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                cordinates=[x,y,w,h]
            return cordinates
        def recog(img,clsf,faceCascade):
            cordinates=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clsf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clsf=cv2.face.LBPHFaceRecognizer_create()
        clsf.read("classifier.xml")
        
        video_cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
        
        while True:
            ret,img=video_cam.read()
            img=recog(img,clsf,faceCascade)
            cv2.imshow("Welcome to face Recognition",img)
            k=cv2.waitKey(1)
            if (k==13) :
                break
        
        video_cam.release()
        cv2.destroyAllWindows()


    

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()