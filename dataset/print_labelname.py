import os

prefix = '/home/zengyj/YoloFP/datasets/2021-RMUC-0417-0916/'
labels_path = './labels_new/'
files = os.listdir(labels_path)
labelnames = []
for i, file in enumerate(files):
    txtFile = open(labels_path + file)
    txtList = txtFile.readlines()
    for j in txtList:
        oneline = j.strip('\n').split(" ")
        labelnames.append(int(oneline[0]))

count_dist = dict()
for i in labelnames:
    if i in count_dist:
        count_dist[i] += 1
    else:
        count_dist[i] = 1
print(count_dist)



