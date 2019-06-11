from FaceScan import*
from keras.models import load_model
from tkinter import filedialog
import numpy as np
import pickle
from PIL import Image

coords_num = 72
my_width = 240
my_height = 280

def cutPic(imageSrcPath,imageDstPath):
    img = Image.open(imageSrcPath)
    scan = FaceScan()
    scan.getAttrOfPic(imageSrcPath)
    location = scan.location
    width = location['width']
    height = location['height']
    left = location['left']
    top = location['top']
    right = left + width
    bottom = top + height
    center = [(left+right)/2,(top+bottom)/2-height*0.25]

    # cropped = img.crop((left, top, right, bottom))
    # cropped.save(imageDstPath)
    # cropped.show()#这一行可要可不要就是用来看效果的

    if (height/width) < (my_height/my_width):
        height = width*(my_height/my_width)
    else:
        width = height*(my_width*my_height)

    left = center[0] - width*1.5/2
    right = center[0] + width*1.5/2
    top = center[1] - height*1.5/2
    bottom = center[1] + height*1.5/2

    cropped = img.crop((left, top, right, bottom))
    cropped = cropped.resize((my_width,my_height))
    cropped.save(imageDstPath)
    # cropped.show()#这一行可要可不要就是用来看效果的


def get_input(img_path):
    rCutPath = 'cutted.bmp'
    cutPic(img_path,rCutPath)
    img_path = rCutPath

    scan = FaceScan()
    scan.getAttrOfPic(img_path)
    face_coords = scan.getLandMark()    
    coords_array = []
    for coord in face_coords:
        coords_array.append(list(coord.values()))
    coords_array = np.array(coords_array)

    input_norm = coords_array/np.array([my_width,my_height])
    data = {'gender':scan.gender,'coords':input_norm,'shape':scan.shape}
    with open('user.data', 'wb') as file_pi:
        pickle.dump(data, file_pi)
    return scan.gender,input_norm

# 输入人脸图片地址，返回（脸型，概率）
def predict_shape(img_path):
    shape_dict = {0:'oblong',1:'diamond',2:'square',3:'heart',4:'triangle',5:'oval',6:'round'}  

    gender,input_norm = get_input(img_path)
    with open('user.data', 'rb') as file_pi:
        data = pickle.load(file_pi)
    gender = data['gender']
    input_norm = data['coords']

    model_input = np.reshape(input_norm,(-1,coords_num*2))
    if gender['type']=='male':
        model = load_model('mmodel.h5')
    else:
        model = load_model('fmodel.h5')
    pred_prob = model.predict(model_input)
    shape_label = np.argmax(pred_prob)
    shape = shape_dict[shape_label]
    return shape, pred_prob[0][shape_label]


'''
if __name__ == "__main__":    
    filename = filedialog.askopenfilename(initialdir = 'C:',title = "请选择您的正脸照片",
                    filetypes = (("jpg文件","*.jpg"),("jpeg文件","*.jpeg"),("png文件","*.png"),
                                ("所有文件","*.*")))
    a,b=predict_shape(filename)
    print(a)
    print(b)
'''