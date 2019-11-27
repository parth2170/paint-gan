import os
import numpy as np
import cv2
from PIL import Image
import pickle

listFolders = os.listdir('down/')
train_images = []
train_labels = []

classes = ['content_dog', 'content_cat', 'emotion_gloomy', 'emotion_scary', 'media_3d_graphics', 'media_comic', 'media_graphite', 'media_watercolor', 'content_people', 'content_cars']

def read_data():
  for label in listFolders:
    if label == '.gitignore' or label == '.DS_Store':
      continue 
    for image in os.listdir('down/'+label):
      img = cv2.imread('down/'+label+'/'+image)
      try:
        img = cv2.resize(img, (28,28))
      except:
        continue
      train_images.append(img)
      train_labels.append(label)
  with open('train_images.pkl', 'wb') as file:
    pickle.dump(train_images, file)
  with open('train_labels.pkl', 'wb') as file:
    pickle.dump(train_labels, file)
  return (train_images,train_labels), (None, None)

def load_data():
  with open('train_images.pkl', 'rb') as file:
    train_images = pickle.load(file)
  with open('train_labels.pkl', 'rb') as file:
    train_labels = pickle.load(file)
  return (train_images,train_labels), (None, None)