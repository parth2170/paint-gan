import os
import numpy as np
import cv2
from PIL import Image

listFolders = os.listdir('down/')
train_images = []
train_labels = []

classes = ['content_dog', 'content_cat', 'emotion_gloomy', 'emotion_scary', 'media_3d_graphics', 'media_comic', 'media_graphite', 'media_watercolor', 'content_people', 'content_cars']

def load_data():
  for label in listFolders:
    if label == '.gitignore' or label == '.DS_Store':
      continue 
    for image in os.listdir('down/'+label):
      img = cv2.imread('down/'+label+'/'+image)
      img = cv2.resize(img, (28,28))
      train_images.append(img)
      train_labels.append(label)
  return (train_images,train_labels), (None, None)
