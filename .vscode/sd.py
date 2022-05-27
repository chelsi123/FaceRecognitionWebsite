from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from cv2 import CamShift
import cv2
import mysql.connector
import numpy as np


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        # variables
        
        self.var_year = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_class = StringVar()
        self.var_address = StringVar()
        self.var_photo = StringVar()

        

        img3 = Image.open(r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\attendance system\f.png")
        img3 = img3.resize((1500, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1380, height=710)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 25, "bold"), bg="white", fg="green")
        title_lbl.place(x=1, y=-5, width=1390, height=30)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=15, y=90, width=1330, height=552)

        # left label Frame

        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=-4, width=700, height=550)

        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,text="Class Student Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=10, width=690, height=510)

        # year
        year_label = Label(class_student_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=0, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(class_student_frame, textvariable=self.var_year, font=( "times new roman", 12, "bold"), state="readonly", width=20)
        year_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=0, column=1, padx=10, pady=15, sticky=W)
       

        

        
       

        

        

        #  studentId
        studentId_label = Label(class_student_frame, text="StudentId", font=(
            "times new roman", 13, "bold"), bg="white")
        studentId_label.grid(row=0, column=2, padx=10, sticky=W)

        studentId_entry = ttk.Entry(class_student_frame, textvariable=self.var_id, font=(
            "times new roman", 13, "bold"), width=20)
        studentId_entry.grid(row=0, column=3, padx=10, pady=15,sticky=W)

        #  studentName
        studentName_label = Label(class_student_frame, text="Student Name", font=(
            "times new roman", 13, "bold"), bg="white")
        studentName_label.grid(row=1, column=0, padx=10, pady=15, sticky=W)

        studentName_entry = ttk.Entry(class_student_frame, textvariable=self.var_name, font=(
            "times new roman", 13, "bold"), width=20)
        studentName_entry.grid(row=1, column=1, padx=10, pady=15, sticky=W)

        # classDivision
        class_div_label = Label(class_student_frame, text="Class Division", font=("times new roman", 13, "bold"), bg="white")
        class_div_label.grid(row=1, column=2, padx=10, pady=15, sticky=W)

        class_div_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div, font=("times new roman", 12, "bold"), state="readonly", width=20)
        class_div_combo["values"] = ("A", "B",
                                     "C")
        class_div_combo.current(0)
        class_div_combo.grid(row=1, column=3, padx=10, pady=15, sticky=W)

        # Roll_no

        Roll_no_label = Label(class_student_frame, text="Roll No", font=("times new roman", 13, "bold"), bg="white")
        Roll_no_label.grid(row=2, column=0, padx=10, pady=15, sticky=W)

        Roll_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, font=("times new roman", 13, "bold"), width=20)
        Roll_no_entry.grid(row=2, column=1, padx=10, pady=15, sticky=W)

        # Gender
        Gender_label = Label(class_student_frame, text="Gender", font=( "times new roman", 13, "bold"), bg="white")
        Gender_label.grid(row=2, column=2, padx=10, pady=15, sticky=W)

        Gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("times new roman", 12, "bold"), state="readonly", width=20)
        Gender_combo["values"] = ("Male", "Female","other")
        Gender_combo.current(0)
        Gender_combo.grid(row=2, column=3, padx=10, pady=15, sticky=W)

        # DOB
        DOB_label = Label(class_student_frame, text="DOB", font=("times new roman", 13, "bold"), bg="white")
        DOB_label.grid(row=3, column=0, padx=10, pady=15, sticky=W)
        DOB_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, font=("times new roman", 13, "bold"), width=20)
        DOB_entry.grid(row=3, column=1, padx=10, pady=15, sticky=W)

        # Email
        Email_label = Label(class_student_frame, text="Email", font=("times new roman", 13, "bold"), bg="white")
        Email_label.grid(row=3, column=2, padx=10, pady=15, sticky=W)
        Email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, font=("times new roman", 13, "bold"), width=20)
        Email_entry.grid(row=3, column=3, padx=10, pady=15, sticky=W)

        # Phone No
        PhoneNo_label = Label(class_student_frame, text="class", font=( "times new roman", 13, "bold"), bg="white")
        PhoneNo_label.grid(row=4, column=0, padx=10, pady=15, sticky=W)
        PhoneNo_entry = ttk.Entry(class_student_frame, textvariable=self.var_class, font=("times new roman", 13, "bold"), width=20)
        PhoneNo_entry.grid(row=4, column=1, padx=10, pady=15, sticky=W)

        # Address
        Address_label = Label(class_student_frame, text="Address", font=("times new roman", 13, "bold"), bg="white")
        Address_label.grid(row=4, column=2, padx=10, pady=15, sticky=W)
        Address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, font=("times new roman", 13, "bold"), width=20)
        Address_entry.grid(row=4, column=3, padx=10, pady=15, sticky=W)
        
        # radiobtn
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(
            class_student_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=6, column=0,padx=10,pady=15)

        radiobtn2 = ttk.Radiobutton(
            class_student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=6, column=1, padx=50,pady=15)

         # buttonsframe
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=330, width=685, height=73)

        save_btn = Button(btn_frame, text="Save", width=22, command=self.add_data, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data,width=22, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        Reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=22,  font=("times new roman", 13, "bold"), bg="blue", fg="white")
        Reset_btn.grid(row=0, column=3)

        # buttonsframe
        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=365, width=685, height=35)

        Take_btn = Button(btn_frame1,text="Take Photo Sample", command=self.generate_dataset,  width=70, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        Take_btn.grid(row=0, column=0)
       

        

        

        # Right  label Frame

        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                 text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=720, y=-4, width=600, height=550)

        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=720, y=-4, width=600, height=550)

        
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=5, width=590, height=520)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        

        
        

        self.student_table = ttk.Treeview(table_frame, column=( "year", "id", "name", "div",
                                                               "roll", "gender", "dob", "email", "class", "address",  "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        
        self.student_table.heading("year", text="Year")
        
        self.student_table.heading("id", text="Id")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Div")
        self.student_table.heading("roll", text="Roll ")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("class", text="Class")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("photo", text="Photo")
        self.student_table["show"] = "headings"

        
        self.student_table.column("year", width=100)
        
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("class", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)

        self.fetch_data()

    def add_data(self):
        if self.var_gender.get() == "Select Gender" or self.var_id.get() == "" or self.var_name.get() == "":
            messagebox.showerror(
                "Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="9783185113", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    
                    self.var_year.get(),
                   
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_class.get(),
                    self.var_address.get(),
                    self.var_radio1.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Student Details have been added successfully", parent=self.root)
            except Exception as es:

                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.root)


#         # fetch data

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="9783185113", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
            conn.close()

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        
        self.var_year.set(data[0]),
       
        self.var_id.set(data[1]),
        self.var_name.set(data[2]),
        self.var_div.set(data[3]),
        self.var_roll.set(data[4]),
        self.var_gender.set(data[5]),
        self.var_dob.set(data[6]),
        self.var_email.set(data[7]),
        self.var_class.set(data[8]),
        self.var_address.set(data[9]),
        
        self.var_radio1.set(data[10])

    

# delete function
    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror(
                "Error", "id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "Student Delete Page", "Do you want to delete this student", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="9783185113", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where id=%s"
                    val = (self.var_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Delete", "Successfully deleted student details", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f" Due To:{str(es)}", parent=self.root)
# reset

    def reset_data(self):
        
        self.var_year.set("Select Year"),
        
        self.var_id.set(""),
        self.var_name.set(""),
        self.var_div.set("Select Divison"),
        self.var_roll.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_class.set(""),
        self.var_address.set(""),
        
        self.var_radio1.set("")

    # ============generate data set and taking photo samples============

    def generate_dataset(self):
        if self.var_gender.get() == "Select gender" or self.var_id.get() == "" or self.var_name.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="9783185113", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0

                for x in myresult:
                    id += 1
                my_cursor.execute("update student set `Year`=%s,`Name`=%s,`Div`=%s,`Roll`=%s,`Gender`=%s,`DOB`=%s,`Email`=%s,`Class`=%s,`Address`=%s,`Photo`=%s where Id=%s", (
                    
                    self.var_year.get(),
                    
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_class.get(),
                    self.var_address.get(),
                    self.var_radio1.get(),
                    self.var_id.get() == id+1
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # load predefined data on face frontal opencv
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    
                    
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("cropped face",face)
                        
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


            


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
