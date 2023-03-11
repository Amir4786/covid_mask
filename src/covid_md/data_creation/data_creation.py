import os
import cv2
import numpy as np
import time
import uuid
from covid_md import logger

img_folder= 'collected_data'
labels= ['NO Mask','MASK']
no_of_images= 40

for label in labels:
    directory= os.path.join(img_folder,label)
    os.makedirs(directory, exist_ok=True)
    video= cv2.VideoCapture(0)
    logger.info(f"Create data for: {label}")
    time.sleep(5)
    for image in range(no_of_images):
        ret,frame= video.read()
        imagename= os.path.join(img_folder,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename,frame)
        cv2.imshow('frame',frame)
        time.sleep(2)
        logger.info(f"Data for {label} is completed")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            logger.info(f"Data for {label} is done")
            break
    video.release()
