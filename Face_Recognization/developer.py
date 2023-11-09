from tkinter import *  # for GUI purpose
from tkinter import ttk  # stylish toolkit
from PIL import Image, ImageTk  # for image editing
from tkinter import messagebox
from pymongo.mongo_client import MongoClient
import cv2                                # ML algorithum


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # window size geometry(width,height,x-axis,y-axis)
        self.root.title("Face Recognition System")

        # Title
        title_lb1 = Label(self.root, text="Developer", font=("times new roman", 35, "bold"), bg="white",fg="blue")  # Title
        title_lb1.place(x=0, y=0, width=1530, height=55)

        img_top = Image.open("Images/dev.jpg")  # Set Image Path
        img_top = img_top.resize((1530, 750))  # width , height  and ANTIALIAS used to convert high to low level image
        self.photoimg_top = ImageTk.PhotoImage(img_top)  # set image

        lb_img = Label(self.root, image=self.photoimg_top)
        lb_img.place(x=0, y=55, width=1530, height=750)  # image show on window place(x_axis,y_axis)

        # frame
        main_frame = Frame(lb_img, bd=2, bg="white")
        main_frame.place(x=950, y=10, width=550, height=120)

        # 1st
        lbl1 = Label(main_frame, text="Name :  Full name", font=("verdana", 15, "bold"), bg="white")
        lbl1.place(x=10, y=0)

        lbl1 = Label(main_frame, text="Phone No. : 1234567890", font=("verdana", 15, "bold"), bg="white")
        lbl1.place(x=10, y=30)

        lbl1 = Label(main_frame, text="Gmail : Devwizards.in@gmail.com", font=("verdana", 15, "bold"), bg="white")
        lbl1.place(x=10, y=60)
        


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()