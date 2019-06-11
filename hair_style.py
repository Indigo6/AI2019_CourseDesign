import tkinter as tk
from tkinter.filedialog import askopenfilename
from predict import*
import random
import cv2 as cv
path_=''
f=0

dis_height = 320
dis_width = 320

def selectPath():
    global path_
    path_ = filedialog.askopenfilename(initialdir = 'C:',title = "请选择您的正脸照片",
                    filetypes = (("jpg文件","*.jpg"),("jpeg文件","*.jpeg"),("png文件","*.png"),
                                ("所有文件","*.*")))
    path.set(path_)

def resize_image(path):
    image = cv.imread(path)
    height = image.shape[0]
    width = image.shape[1]
    if height>width:
        resized_img = cv.resize(image,(320,int(320*height/width)))
    else:
        resized_img = cv.resize(image,(int(320*width/height),320))
    cv.imwrite(path,resized_img)

def analyse():
    global imgLabel,path_
    a, b = predict_shape(path_)
    cc.set(b)
    if f==0:
        if a=='oblong':
            face="长方形"
            hair="西装头，飞机头，背头"
            k=random.randint(1, 3)
            road="data/male/oblong/" +str(k)+ ".png"
            resize_image(road)
            photo = tk.PhotoImage(file=road)
            imgLabel.config(image=photo)
            imgLabel.image = photo
            facetype.set(face)
            hairtype.set(hair)
        elif a=='diamond':
            face="菱形"
            hair="长发后梳，碎盖头，长边刘海"
            k=random.randint(1, 3)
            road="data/male/diomand/" +str(k)+ ".png"
            resize_image(road)
            photo = tk.PhotoImage(file=road)
            imgLabel.config(image=photo)
            imgLabel.image = photo
            facetype.set(face)
            hairtype.set(hair)
        elif a=='square':
            face="正方形"
            hair="寸头，上抓鸡冠发型，后前发"
            k=random.randint(1, 3)
            road="data/male/square/" +str(k)+ ".png"
            resize_image(road)
            photo = tk.PhotoImage(file=road)
            imgLabel.config(image=photo)
            imgLabel.image = photo
            facetype.set(face)
            hairtype.set(hair)
        elif a=='heart':
            face="心形"
            hair="寸头，上抓鸡冠发型，后前发"
            k=random.randint(1, 3)
            road="data/male/heart/" +str(k)+ ".png"
            resize_image(road)
            photo = tk.PhotoImage(file=road)
            imgLabel.config(image=photo)
            imgLabel.image = photo
            facetype.set(face)
            hairtype.set(hair)
        elif a=='triangle':
            face="三角形"
            hair="前刘海，后梳头，斜刘海短发"
            k=random.randint(1, 3)
            road="data/male/triangle/" +str(k)+ ".png"
            resize_image(road)
            photo = tk.PhotoImage(file=road)
            imgLabel.config(image=photo)
            imgLabel.image = photo
            facetype.set(face)
            hairtype.set(hair)
        elif a=='oval':
            face="椭圆形"
            hair="寸头，层次刘海，脏辫，锡纸烫"
            k=random.randint(1, 3)
            road="data/male/oval/" +str(k)+ ".png"
            resize_image(road)
            photo = tk.PhotoImage(file=road)
            imgLabel.config(image=photo)
            imgLabel.image = photo
            facetype.set(face)
            hairtype.set(hair)
        elif a=='round':
            face="圆形"
            hair="刘海，纹理烫"
            k=random.randint(1, 3)
            road="data/male/round/" +str(k)+ ".png"
            resize_image(road)
            photo = tk.PhotoImage(file=road)
            imgLabel.config(image=photo)
            imgLabel.image = photo
            facetype.set(face)
            hairtype.set(hair)
    elif f == 1:
        if a == 'oblong':
            face = "长方形"
            hair = "长直发，二八分烫"
            k = random.randint(1, 3)
            road = "data/female/oblong/" + str(k) + ".png"
            resize_image(road)
            photo = tk.PhotoImage(file=road)
            imgLabel.config(image=photo)
            imgLabel.image = photo
            facetype.set(face)
            hairtype.set(hair)
        elif a == 'diamond':
            face = "菱形"
            hair = "微卷中长发，空气刘海"
            k = random.randint(1, 3)
            road = "data/female/diomand/" + str(k) + ".png"
            resize_image(road)
            photo = tk.PhotoImage(file=road)
            imgLabel.config(image=photo)
            imgLabel.image = photo
            facetype.set(face)
            hairtype.set(hair)
        elif a == 'square':
            face = "正方形"
            hair = "偏分齐肩，纹理烫，短卷发"
            k = random.randint(1, 3)
            road = "data/female/square/" + str(k) + ".png"
            resize_image(road)
            photo = tk.PhotoImage(file=road)
            imgLabel.config(image=photo)
            imgLabel.image = photo
            facetype.set(face)
            hairtype.set(hair)
        elif a == 'heart':
            face = "心形"
            hair = "内卷偏分中长发，披肩长直发，（直接把头发扎起来也可以，你长得好看可以任性）"
            k = random.randint(1, 3)
            road = "data/female/heart/" + str(k) + ".png"
            resize_image(road)
            photo = tk.PhotoImage(file=road)
            imgLabel.config(image=photo)
            imgLabel.image = photo
            facetype.set(face)
            hairtype.set(hair)
        elif a == 'triangle':
            face = "三角形"
            hair = "刘海，梨花头，自然卷发"
            k = random.randint(1, 3)
            road = "data/female/triangle/" + str(k) + ".png"
            resize_image(road)
            photo = tk.PhotoImage(file=road)
            imgLabel.config(image=photo)
            imgLabel.image = photo
            facetype.set(face)
            hairtype.set(hair)
        elif a == 'oval':
            face = "椭圆形"
            hair = "中长直发，卷发，沙宣头"
            k = random.randint(1, 3)
            road = "data/female/oval/" + str(k) + ".png"
            resize_image(road)
            photo = tk.PhotoImage(file=road)
            imgLabel.config(image=photo)
            imgLabel.image = photo
            facetype.set(face)
            hairtype.set(hair)
        elif a == 'round':
            face = "圆形"
            hair = "分层内扣波波头，齐刘海短发，丸子头"
            k = random.randint(1, 3)
            road = "data/female/round/" + str(k) + ".png"
            resize_image(road)
            photo = tk.PhotoImage(file=road)
            imgLabel.config(image=photo)
            imgLabel.image = photo
            facetype.set(face)
            hairtype.set(hair)
def sex():
    global f
    f=int(var.get())



window = tk.Tk()
window.title('发型推荐')
window.geometry('900x550')

tk.Label(window,text = "请选择正脸照片",font=("Arial", 12)).place(x=150,y=40,width=150,height=40)


path = tk.StringVar()
var= tk.StringVar()
var.set(0)
facetype=tk.StringVar()
hairtype=tk.StringVar()
cc=tk.StringVar()

tk.Label(window,text = "目标路径:").place(x=100,y=100,width=50,height=30)
tk.Entry(window, textvariable = path).place(x=160,y=100,width=150,height=30)
tk.Button(window, text = "路径选择",command = selectPath).place(x=330,y=100,width=60,height=30)

tk.Button(window, text = "开始分析",command = analyse).place(x=180,y=200,width=80,height=50)

tk.Radiobutton(window,text='男',variable=var,value='0',command=sex).place(x=180,y=150,width=30,height=30)
tk.Radiobutton(window,text='女',variable=var,value='1',command=sex).place(x=250,y=150,width=30,height=30)


tk.Label(window,text = "脸型分析:").place(x=100,y=350,width=50,height=30)
tk.Entry(window, textvariable = facetype).place(x=160,y=350,width=150,height=30)

tk.Label(window,text = "发型推荐:").place(x=100,y=400,width=50,height=30)
tk.Entry(window, textvariable = hairtype).place(x=160,y=400,width=150,height=30)

tk.Label(window,text = "预测概率:").place(x=100,y=450,width=50,height=30)
tk.Entry(window, textvariable = cc).place(x=160,y=450,width=150,height=30)

photopath="data/a.png"
photo = tk.PhotoImage(file=photopath)
imgLabel = tk.Label(window,image=photo)
imgLabel.place(x=460,y=110,width=320,height=320)
window.mainloop()

