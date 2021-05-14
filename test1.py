
import tkinter as tk;
from tkinter import filedialog
from PIL import Image , ImageTk
import numpy as np
import cv2


root = tk.Tk()
root.title("PhotoShop")
root.geometry("1300x700")

procImage = []

def brightnessFun(val=255):
    bright = int((int(val))*(255-(-255))/(250)+(-255))
    if bright > 0:
        shadow = bright
        maxs = 255
    else:
        shadow = 0
        maxs = 255+bright

    alpha = (maxs - shadow) / 255
    gama = shadow
    img_cv = cv2.imread(procImage[0])
    brightImage = cv2.addWeighted(img_cv, alpha, img_cv, 0, gama)
    procImage[1] = brightImage
    cal = cv2.resize(brightImage, (800, 500), brightImage)
    image = ImageTk.PhotoImage(Image.fromarray(cal))
    lbl.configure(image = image)
    lbl.image = image


def contrastFun(val):
    img_cv = cv2.imread(procImage[0])
    alpha = float(131*(int(val)+127))/(127*(180 - int(val)))
    gama = 127*(1 - alpha)
    contrastImage = cv2.addWeighted(img_cv, alpha,img_cv , 0, gama)
    cal = cv2.resize(contrastImage, (800, 500), contrastImage)
    procImage[1] = contrastImage
    image = ImageTk.PhotoImage(Image.fromarray(cal))
    lbl.configure(image=image)
    lbl.image = image

def threFun(val):
    img_cv = cv2.imread(procImage[0] ,0)
    ret,threshold = cv2.threshold(img_cv , int(val) , 255 , cv2.THRESH_BINARY)
    cal = cv2.resize(threshold, (800, 500), threshold)
    procImage[1] = threshold
    image = ImageTk.PhotoImage(Image.fromarray(cal))
    lbl.configure(image=image)
    lbl.image = image

def bitFun() :
    img_cv = cv2.imread(procImage[0] , 0
                        )
    r = img_cv.shape[0]
    c = img_cv.shape[1]
    x = np.zeros((r , c , 8) , dtype = np.uint8)
    for i in range(8) :
        x[: , : ,i] = 2 ** i # 2 power i
    r = np.zeros((r , c , 8) , dtype = np.uint8)

    for i in range(8) :
        r[:, :, i] = cv2.bitwise_and(img_cv , x[: , : , i])
        mask = r[: , : ,i] > 0
        r[mask] = 255
        cv2.imshow(str(i) , r[: , : , i])
def uploadImage():
    filePath = filedialog.askopenfilename(initialdir='/', title="Select Image")
    image = Image.open(filePath)
    image = image.resize((800, 500))
    image = ImageTk.PhotoImage(image)
    lbl.configure(image=image)
    lbl.image = image
    procImage.append(filePath)
    img_cv = cv2.imread(filePath)
    procImage.append(img_cv)

def saveImage ():
    filePath = filedialog.asksaveasfile(defaultextension='.jpg' , filetypes = [
        ("JPG image" , '.jpg')
    ])

    img = cv2.cvtColor(procImage[1] , cv2.COLOR_BGR2RGB)
    cv2.imwrite(str(filePath.name), img)
    filePath.close()
    print(filePath.name)
lable = tk.Label(root, text="PhotoShop")
lable.pack()

lbl = tk.Label(root)
lbl.place(x=50, y=100)


openImage = tk.Button(root, text="Upload image" , fg = "red" , command = uploadImage)
openImage.place(x=1000, y=100)

saveImage = tk.Button(root, text="Save image" , fg = "green" , command = saveImage)
saveImage.place(x=1150, y=100)

brightnessLabel = tk.Label(root , text = "Brightness" , fg = "green")
brightnessLabel.place(x = 1000 ,y = 230 )

slide1 = tk.Scale(root, from_=0, to=255, resolution=1, orient=tk.HORIZONTAL ,command = brightnessFun)
slide1.place(x=1000 , y = 250)


contrastLabel = tk.Label(root , text = "Contrast" , fg = "green")
contrastLabel.place(x = 1000 ,y = 300 )

slide2 = tk.Scale(root, from_=0, to=127, resolution=1, orient=tk.HORIZONTAL ,command = contrastFun)
slide2.place(x=1000 , y = 325)


threLable = tk.Label(root , text = "Threshold" , fg = "green")
threLable.place(x = 1000 ,y = 375 )

slide2 = tk.Scale(root, from_=0, to=255, resolution=1, orient=tk.HORIZONTAL ,command = threFun)
slide2.place(x=1000 , y = 400)

bitplane = tk.Button(root, text="Bit Plane", command = bitFun)
bitplane.place(x=1000, y=470)
root.mainloop()