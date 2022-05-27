from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from cv2 import CamShift
import cv2
import mysql.connector
import numpy as np


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")


        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 25, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1490, height=30)


        img_top = Image.open( r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\face recognition system\d.jpg")
        img_top = img_top.resize((1380, 650), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=30, width=1380, height=650)

        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=950, y=0, width=400, height=500)
           

        # img_top1 = Image.open( r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\face recognition system\h.jpg")
        # img_top1 = img_top1.resize((150, 140), Image.Resampling.LANCZOS)
        # self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        # f_lbl = Label(main_frame, image=self.photoimg_top1)
        # f_lbl.place(x=280, y=0, width=150, height=140)


        dev_label = Label(main_frame, text="hello my name,Chelsi", font=("times new roman", 13, "bold"),fg="blue", bg="white")
        dev_label.place(x=0,y=5)
        dev_label = Label(main_frame, text="I am full stack developer", font=("times new roman", 13, "bold"),fg="blue", bg="white")
        dev_label.place(x=0,y=40)

        img2 = Image.open(r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\face recognition system\standford.jpg")
        img2 = img2.resize((480, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(main_frame, image=self.photoimg2)
        f_lbl.place(x=960, y=0, width=480, height=100)

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()