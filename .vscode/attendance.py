from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        #first img
        img = Image.open(r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\face recognition system\m.png")
        img = img.resize((700, 200), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=700, height=200)
        
        #second img
        img1 = Image.open(r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\face recognition system\c.jpg")
        img1 = img1.resize((700, 200), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=700, y=0, width=700, height=200)

        img3 = Image.open( r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\face recognition system\bg.jpg")
        img3 = img3.resize((1500, 580), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1500, height=580)

        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 25, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1490, height=30)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=15, y=35, width=1330, height=552)

        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,text="Student Attendance Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=-4, width=700, height=550)

        img_left = Image.open(r"C:\Users\dell\OneDrive - Indian Institute of Technology (BHU), Varanasi\Desktop\face recognition system\att.jpg")
        img_left = img_left.resize((690, 120), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=-2, width=690, height=120)

        left_inside_frame = Frame(Left_frame, bd=2,relief=RIDGE ,bg="white")
        left_inside_frame.place(x=0, y=130, width=685, height=350)

        #level and entry
        #  attendanceid
        # attendanceid_label = Label(left_inside_frame , text="AttendanceId:", font=("times new roman", 13, "bold"), bg="white")
        # attendanceid_label.grid(row=0, column=0, padx=10,pady=5, sticky=W)

        # attendanceid_entry = ttk.Entry(left_inside_frame , font=("times new roman", 13, "bold"),textvariable=self.var_atten_id,width=20)
        # attendanceid_entry.grid(row=0, column=1, padx=10,pady=5, sticky=W)

        #  Name
        Name_label = Label(left_inside_frame , text=" Name:", font=( "comicsansns", 11, "bold"), bg="white")
        Name_label.grid(row=1, column=0)

        atten_name= ttk.Entry(left_inside_frame ,font=( "comicsansns", 11, "bold"),textvariable=self.var_atten_name,width=22)
        atten_name.grid(row=1, column=1,pady=8)
        
        #  Name
        roll_label = Label(left_inside_frame , text=" Roll:", font=( "comicsansns", 11, "bold"), bg="white")
        roll_label.grid(row=0, column=2,padx=8,pady=4)

        atten_roll= ttk.Entry(left_inside_frame ,font=( "comicsansns", 11, "bold"),textvariable=self.var_atten_roll, width=22)
        atten_roll.grid(row=0, column=3,pady=8)

        # #  Name
        # dep_label = Label(left_inside_frame , text=" Department:", font=( "comicsansns", 11, "bold"), bg="white")
        # dep_label.grid(row=1, column=2)

        # atten_dep= ttk.Entry(left_inside_frame ,font=( "comicsansns", 11, "bold"),textvariable=self.var_atten_dep, width=22)
        # atten_dep.grid(row=1, column=3,pady=8)

        #  Name
        time_label = Label(left_inside_frame , text=" Time:", font=( "comicsansns", 11, "bold"), bg="white")
        time_label.grid(row=2, column=0)

        atten_time= ttk.Entry(left_inside_frame ,font=( "comicsansns", 11, "bold"),textvariable=self.var_atten_time,width=22)
        atten_time.grid(row=2, column=1,pady=8)

        #  Name
        date_label = Label(left_inside_frame , text=" Date:", font=( "comicsansns", 11, "bold"), bg="white")
        date_label.grid(row=2, column=2)

        atten_date= ttk.Entry(left_inside_frame ,font=( "comicsansns", 11, "bold"),textvariable=self.var_atten_date, width=22)
        atten_date.grid(row=2, column=3,pady=8)

        #  Name
        attendance_label = Label(left_inside_frame , text="Attendance status", font=( "comicsansns", 11, "bold"), bg="white")
        attendance_label.grid(row=3, column=0)

        attendance_combo = ttk.Combobox(left_inside_frame, font=( "comicsansns", 11, "bold"),textvariable=self.var_atten_attendance, state="readonly", width=22)
        attendance_combo["values"] = ("Status", "Present","Absent")
        attendance_combo.current(0)
        attendance_combo.grid(row=3, column=1,pady=8)

        # buttonsframe
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=240, width=685, height=35)

        save_btn = Button(btn_frame, text="Import csv", width=16,command=self.importCsv, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Export csv",width=16,command=self.exportCsv, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Update",width=16, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        Reset_btn = Button(btn_frame, text="Reset",width=16,command=self.reset_data , font=("times new roman", 13, "bold"), bg="blue", fg="white")
        Reset_btn.grid(row=0, column=3)

        

        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,text="Attendance Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=720, y=-4, width=600, height=550)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=580, height=425)

       # ==================================================scroll bar and table================================
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,column=("roll","name","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        # self.AttendanceReportTable.heading("id",text="Attendance Id")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        # self.AttendanceReportTable.heading("dep",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        # self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=200)
        self.AttendanceReportTable.column("name",width=200)
        # self.AttendanceReportTable.column("dep",width=100)
        self.AttendanceReportTable.column("time",width=200)
        self.AttendanceReportTable.column("date",width=200)
        self.AttendanceReportTable.column("attendance",width=200)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    def fetchData(self,rows):
      self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
      for i in rows:
        self.AttendanceReportTable.insert("",END,values=i)

    def importCsv(self):
      global mydata
      mydata.clear()
      fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")) ,parent=self.root)
      with open(fln) as myfile:
        csvread=csv.reader(myfile,delimiter=",")
        for i in csvread:
          mydata.append(i)
        self.fetchData(mydata)


    def exportCsv(self):
      try:
        if len(mydata)<1:
          messagebox.showerror("No Data","No data found to export",parent=self.root)
          return False
        fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")) ,parent=self.root)
        with open(fln,mode='w',newline="") as myfile:
          exp_write=csv.writer(myfile,delimiter=",")
          for i in mydata:
            exp_write.writerow(i)
          messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+"successfully")
      except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    

    def get_cursor(self,event=""):
      cursor_row = self.AttendanceReportTable.focus()
      content = self.AttendanceReportTable.item(cursor_row)
      rows=content['values']
      # self.var_atten_id.set(rows[0])
      self.var_atten_roll.set(rows[0])
      self.var_atten_name.set(rows[1])
      # self.var_atten_dep.set(rows[3])
      self.var_atten_time.set(rows[2])
      self.var_atten_date.set(rows[3])
      self.var_atten_attendance.set(rows[4])

    def reset_data(self):
      # self.var_atten_id.set("")
      self.var_atten_roll.set("")
      self.var_atten_name.set("")
      # self.var_atten_dep.set("")
      self.var_atten_time.set("")
      self.var_atten_date.set("")
      self.var_atten_attendance.set("")



























if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
