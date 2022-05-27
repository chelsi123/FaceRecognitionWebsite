from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from cv2 import CamShift
import cv2
import mysql.connector
import numpy as np


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")


        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman", 25, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1490, height=30)


        img_top = Image.open( r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\face recognition system\he.jpg")
        img_top = img_top.resize((1380, 650), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=30, width=1380, height=650)

        dev_label = Label(f_lbl, text="Email:chelsi1362@gmail.com", font=("times new roman", 20, "bold"),fg="blue", bg="white")
        dev_label.place(x=550,y=220)









if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()