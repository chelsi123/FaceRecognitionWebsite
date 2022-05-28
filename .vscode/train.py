from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_label = Label(self.root, text="TRAIN DATA SET", font=(
            "comicsansns", 25, "bold"), bg="white", fg="purple")
        title_label.place(x=0, y=0, width=1490, height=45)


        image_top = Image.open(r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\attendance system\Images\faces.png")
        image_top = image_top.resize((1380, 300), Image.Resampling.LANCZOS)
        self.photo_img_top = ImageTk.PhotoImage(image_top)

        f_label = Label(self.root, image=self.photo_img_top)
        f_label.place(x=0, y=45, width=1380, height=300)


        btn1_1=Button(self.root,text="TRAIN DATA ",command=self.train_classifier,cursor="hand2",font=("comicsansns",30,"bold"),bg="brown",fg="white")
        btn1_1.place(x=0,y=345,width=1380,height=50)

        image_bottom = Image.open(r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\attendance system\Images\bottom.jpg")
        image_bottom = image_bottom.resize((1380, 300), Image.Resampling.LANCZOS)
        self.photo_img_bottom = ImageTk.PhotoImage(image_bottom)

        f_label = Label(self.root, image=self.photo_img_bottom)
        f_label.place(x=0, y=395, width=1380, height=300)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]


        faces=[]
        ids=[]


        for image in path:
            img=Image.open(image).convert('L')  
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        
        clsf=cv2.face.LBPHFaceRecognizer_create()
        clsf.train(faces,ids)
        clsf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training of dataset completed!!")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
