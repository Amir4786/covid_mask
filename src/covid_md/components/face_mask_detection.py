from covid_md import logger
from covid_md.entity import MaskDetectionConfig
from covid_md.config import ConfigurationManager

import numpy as np
from keras.models import load_model
import os, cv2

class MaskDetection:
    def __init__(self, config: MaskDetectionConfig):
        self.config= config
    def load_model(self):
        path= self.config.root_dir
        os.chdir(path)
        print(os.listdir())
        logger.info("give one model name from any of trained models...")
        logger.info("select any of the above models...")
        logger.info("for better accuracy select the latest one...")
        model= str(input("Type Model Name:"))
        model= load_model(model)
        os.chdir("../../")
        logger.info("here is your model...")
        return model
    def other_params(self):
        logger.info("this function is to call hyper parameters...")
        classifier= self.config.face_classifier
        face_classifier= cv2.CascadeClassifier(classifier)
        source= cv2.VideoCapture(0)
        labels_dict= {1: 'Mask', 0: 'No Mask'}
        color_dict= {1: (0,255,0), 0:(0,0,255)}
        logger.info("here are your hyper parameters...")
        return face_classifier, source, labels_dict, color_dict
    def face_mask_detection(seld, model, face_classifier, source, labels_dict, color_dict):
        while(True):
            logger.info("live face mask detection shall start here...")
            ret, img= source.read()
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces= face_classifier.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                face_img= gray[y:y+w, x:x+w]
                resize_img= cv2.resize(face_img, (100,100))
                normalized= resize_img/255.0
                reshaped= np.reshape(normalized, (1,100,100,1))
                result= model.predict(reshaped)
                label= np.argmax(result, axis=1)[0]
                cv2.rectangle(img, (x,y), (x+w, y+h), color_dict[label],2)
                cv2.rectangle(img, (x,y-40), (x+w,y), color_dict[label], -1)
                cv2.putText(img, labels_dict[label], (x,y-10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)
            cv2.imshow('LIVE', img)
            key= cv2.waitKey(1)

            if(key=='q'):
                break
        cv2.destroyAllWindows()
        source.release()
        logger.info("share your experience...")
        logger.info("Thank you!!!")