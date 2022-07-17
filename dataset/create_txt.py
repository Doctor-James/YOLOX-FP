import os
import random

images_path = './JPEGImages'
labels_path = './Annotations'

prefix = '/home/zengyj/YoloFP/YOLOXP/datasets/VOCdevkit/VOC2007/JPEGImages/'

image_dir = os.listdir(images_path)
label_dir = os.listdir(labels_path)
random.shuffle(label_dir)

file_train = open('./ImageSets/Main/train.txt','w')
file_test = open('./ImageSets/Main/test.txt','w')

length = len(label_dir)
count = 0

for label in label_dir:
    if count / length < 0.9:
        
        #label = prefix + label 
        label = label.split('.')[0] 
        file_train.write(label)
        file_train.write('\n')
        # print(name)

    else:
        label = label.split('.')[0]  
        file_test.write(label)
        file_test.write('\n')
    count += 1
    print(count/length)

file_train.close()
file_test.close()

