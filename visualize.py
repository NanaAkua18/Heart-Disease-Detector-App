from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import mysql.connector



class HeartAttackDataClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Analysis History")
        self.root.config(bg="white")
        self.root.state('zoomed')
        self.root.focus_force()


        self.icon_image = ImageTk.PhotoImage(file="Images/icon2.png")
        self.root.iconphoto(False, self.icon_image)




        self.logo=ImageTk.PhotoImage(file="Images/Analysis History.png")
        self.myimage=Label(self.root,image=self.logo,bg="#ffffff")
        self.myimage.pack()

        # ================ Employee Details ===========
        frame = Frame(self.root, bd=3, relief=RIDGE)
        frame.place(x=0, y=250, relwidth=1, height=350)

        scrolly = Scrollbar(frame, orient=VERTICAL)
        scrollx = Scrollbar(frame, orient=HORIZONTAL)

        self.HeartDataTable = ttk.Treeview(frame, columns=("Name", "Date", "DOB", "Age", "Sex", "Cp", "TrestBPS", "Chol", "FBS", "RestECG", "Thalach", "Exang", "OldPeak", "Slope", "CA", "Thal", "Result"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.HeartDataTable.xview)
        scrolly.config(command=self.HeartDataTable.yview)

        self.HeartDataTable.heading("Name", text="Name")
        self.HeartDataTable.heading("Date", text="Date")
        self.HeartDataTable.heading("DOB", text="DOB")
        self.HeartDataTable.heading("Age", text="Age")
        self.HeartDataTable.heading("Sex", text="Sex")
        self.HeartDataTable.heading("Cp", text="CP")
        self.HeartDataTable.heading("TrestBPS", text="TrestBPS")
        self.HeartDataTable.heading("Chol", text="Chol")
        self.HeartDataTable.heading("FBS", text="FBS")
        self.HeartDataTable.heading("RestECG", text="RestECG")
        self.HeartDataTable.heading("Thalach", text="Thalach")
        self.HeartDataTable.heading("Exang", text="Exang")
        self.HeartDataTable.heading("OldPeak", text="OldPeak")
        self.HeartDataTable.heading("Slope", text="Slope")
        self.HeartDataTable.heading("CA", text="CA")
        self.HeartDataTable.heading("Thal", text="Thal")
        self.HeartDataTable.heading("Result", text="Result")

        self.HeartDataTable["show"] = "headings"

        for column in self.HeartDataTable["columns"]:
            self.HeartDataTable.column(column, width=100)

        self.HeartDataTable.column("Name", width=150)
        self.HeartDataTable.column("Age", width=50)
        self.HeartDataTable.column("Sex", width=50)
        self.HeartDataTable.column("Cp", width=50)
        self.HeartDataTable.column("Result", width=50)
        self.HeartDataTable.column("Slope", width=50)
        self.HeartDataTable.column("CA", width=50)

        self.HeartDataTable.pack(fill=BOTH, expand=1)

        self.show()

    def show(self):
        mydb = mysql.connector.connect(host='localhost', user='root', password='992922', database="Heart_Data")
        cur = mydb.cursor()
        try:
            cur.execute("SELECT Name, Date, DOB, Age, Sex, Cp, TrestBPS, Chol, FBS, RestECG, Thalach, Exang, OldPeak, Slope, CA, Thal, Result FROM data")
            rows = cur.fetchall()
            self.HeartDataTable.delete(*self.HeartDataTable.get_children())
            for row in rows:
                self.HeartDataTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            mydb.close()

if __name__ == "__main__":
    root = Tk()
    obj = HeartAttackDataClass(root)
    root.mainloop()
