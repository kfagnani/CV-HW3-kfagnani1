import cv2
import numpy as np
from PIL import Image
import os
path = './images/'
grant = cv2.face.LBPHFaceRecognizer_create()

detect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml');

def getImagesAndLabels(path):
    pathof_img = [os.path.join(path,f) for f in os.listdir(path)]
    face_idea=[]
    ids = []
    for imagePath in pathof_img:

        PIL_img = Image.open(imagePath).convert('L')
        img_numpy = np.array(PIL_img,'uint8')
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detect.detectMultiScale(img_numpy)
        for (x,y,w,h) in faces:
            face_idea.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)
    return face_idea,ids
print ("\n[INFO] Training faces...")
faces,ids = getImagesAndLabels(path)
grant.train(faces, np.array(ids))

grant.write('trainer.yml')
print("\n[INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))
