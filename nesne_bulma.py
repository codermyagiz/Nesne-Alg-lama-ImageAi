#Import Tkinter
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk,Image
import subprocess,io
#------------------------
from imageai.Detection import ObjectDetection #Import ImageAi
import os #Import Os

root = tk.Tk()
root.title('ImageAi ile Nesne Algılama') #Pencere Başlığı
root.geometry('400x220') #Pencere boyutu
root.maxsize(400,220) #Pencere'nin maksimum boyutu
root.minsize(400,220) #Pencere'nin minimum boyutu
root.configure(bg="DeepSkyBlue3")

resim_path = "nesneleri_bulunmus_resmin_kaydedilecegi_yer"

baslik_yazisi = tk.Label(root, text="ImageAi ile Nesne Algılama", fg="white", bg="DeepSkyBlue3", font=('Helvetica',13,'bold')) #Yazı
baslik_yazisi.place(x=100, y=10) #Yazıyı yerleştiriyoruz.

def open_image_path(): #Resmin yolunu bu fonksiyon ile tkinter'dan alıp global bir değişkene atıyoruz.
    image_path = tk.filedialog.askopenfilename(initialdir = "/", title = "Resmi Seçiniz",filetypes = (("jpeg files","*.jpg"),("all files","*.*"))) #Tkinter'dan resmin yolu alınıyor ve bir değişkene atanıyor.
    print(image_path) #Yol yazdırılıyor.
    global path
    path = image_path
    yazi_2.config(text=path)

def detect_object_on_picture(): #Fonksiyon
    global execution_path
    execution_path = os.getcwd() #https://docs.python.org/3/library/os.html#os.getcwd
    open_execution_path = resim_path+"\\"+"nesneleri_bulunmus.jpg"
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5")) #Kullanacağımız modelin yolunu ImageAi'ye söylüyoruz.
    detector.loadModel() #Ve modeli yüklüyoruz.

    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path, path), output_image_path=os.path.join(resim_path , "nesneleri_bulunmus.jpg"))

    for eachObject in detections:
        print(eachObject["name"] , " : " , eachObject["percentage_probability"] ) #Bulunan cisimlerin isimlerini ve yüzdesini yazdırıyor.

    yeni_resim = Toplevel(root) #Nesneleri Bulunmuş resmi göstermek için bir pencere oluşturulur.
    yeni_resim.title("Nesneleri Bulunmuş Hali") #Başlık
    yeni_resim.geometry("860x600") #Pencere Boyutu
    yeni_resim.maxsize(800, 600) #Pencere'nin maksimum boyutu
    yeni_resim.minsize(800, 600) #Pencere'nin minimum boyutu
    img = Image.open(open_execution_path) #Resim yükleniyor.
    img = img.resize((800, 600), Image.ANTIALIAS) #Yeniden boyutlandırılıyor.
    img = ImageTk.PhotoImage(img) #Resim gösteriliyor.
    panel = Label(yeni_resim, image = img)
    panel.image = img
    panel.grid(row = 2)
    yeni_resim.mainloop()

def go_to_detected_objects_image_path(): #Nesneleri Bulunan resmin yoluna gitmek için oluşturulan fonksiyon.
    path = os.path.realpath(resim_path)
    subprocess.Popen(f'explorer {os.path.realpath(path)}')

open_file_button = tk.Button(root, text="Resmi Seçiniz", width="22", fg="black", bg="LightSkyBlue2", command=open_image_path) #"Resmi Seçiniz" butonu
open_file_button.place(x=10, y=80) #Konumu

detect_object = tk.Button(root, text="Nesneleri Bul", width="22", bg="LightSkyBlue2", command=detect_object_on_picture) #"Objeleri Bul" butonu
detect_object.place(x=220, y=80) #Konumu

yazi_1 = tk.Label(root, text="Seçtiğiniz resmin dizini: ", fg="black", bg="DeepSkyBlue3", font=('Helvetica',10,'bold')) # "Seçtiğiniz resmin dizini: " yazısı
yazi_1.place(x=10, y=120) #Konumu

yazi_2 = tk.Label(root, text="", fg="black", bg="DeepSkyBlue3", font=('Helvetica',10,'bold')) # "Dizin" yazısı
yazi_2.place(x=175, y=120) #Konumu

indirilen_yer_1 = tk.Label(root, text="Nesneleri Bulunan Resmin Dizini:", fg="black", bg="DeepSkyBlue3", font=('Helvetica',10,'bold'))
indirilen_yer_1.place(x=10, y=160)


indirilen_yer_buton = tk.Button(root, text="Dizine Git", fg="black", bg="LightSkyBlue2", command=go_to_detected_objects_image_path)
indirilen_yer_buton.place(x=230, y=160)
root.mainloop()

#Kaynaklar:
#https://imageai.readthedocs.io/en/latest/detection/
#https://docs.python.org/3/library/os.html#os.getcwd
#https://docs.python.org/3/library/tkinter.html
#https://docs.python.org/3.9/library/dialog.html#tkinter.filedialog.askopenfilename
#https://github.com/OlafenwaMoses/ImageAI

#Test ettiğim resimler:
#https://www.freeimages.com/tr/photo/freeway-1449674
#https://www.freeimages.com/tr/photo/traffic-1450112
#https://www.freeimages.com/tr/photo/street-6-1199441
#https://www.freeimages.com/tr/photo/ships-1448875
