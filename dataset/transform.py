import os
import cv2
import numpy as np

def plot_boxes_cv2(img, boundings):

    img = np.copy(img)

    width = img.shape[1]
    height = img.shape[0]


    for bounding in boundings:
        

        x1 = int((bounding[1] - bounding[3]/2) * width)
        y1 = int((bounding[2] - bounding[4]/2) * height)
        x2 = int((bounding[1] + bounding[3]/2) * width)
        y2 = int((bounding[2] + bounding[4]/2) * height)
        c = str(bounding[0])
        print((int(bounding[0])),x1,x2,y1,y2)
        
        rgb = [np.random.randint(0,255),np.random.randint(0,255),np.random.randint(0,255)]
        
        img = cv2.putText(img, str(int(bounding[0])), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1.2, rgb, 1)
        img = cv2.rectangle(img, (x1, y1), (x2, y2), rgb, 1)

    return img


file_path = './labels/'
img_path = './images/'
dst_path = './labels_new/'

if not os.path.exists(dst_path):
    os.mkdir(dst_path)

dir = os.listdir(file_path)

for file in dir:

    # img_name = img_path + file[:file.find('.')] + '.jpg'

    # img = cv2.imread(img_name)

    # height, width, c = img.shape
    

    with open(os.path.join(file_path,file),'r') as f:

        lines = f.readlines()
        boundingbox = []

        for line in lines:

            line = line.strip('\n')
            line = line.split(' ')
            
            ''' 
            # 读入图片测试数据

            x1,y1 = int(width * float(line[1])), int(height * float(line[2]))
            x2,y2 = int(width * float(line[3])), int(height * float(line[4]))
            x3,y3 = int(width * float(line[5])), int(height * float(line[6]))
            x4,y4 = int(width * float(line[7])), int(height * float(line[8]))

            img = cv2.circle(img,center=(x1,y1),radius=3,color=(255,255,255),thickness=3)
            img = cv2.circle(img,center=(x2,y2),radius=3,color=(255,255,255),thickness=3)
            img = cv2.circle(img,center=(x3,y3),radius=3,color=(255,255,255),thickness=3)
            img = cv2.circle(img,center=(x4,y4),radius=3,color=(255,255,255),thickness=3)
            '''

            x1,y1,x2,y2,x3,y3,x4,y4 = np.array(line[1:]).astype(np.float32)


            # 忽略错误数据
            if min(x1,x2,x3,x4,y1,y2,y3,y4) < 0 or max(x1,x2,x3,x4,y1,y2,y3,y4) > 1:
                continue
            
            # print(x1,y1,x2,y2,x3,y3,x4,y4)

            # 生成标注
            # c, xmin,ymin,w,h, x1y1 x2y2 x3y3 x4y4

            xmin = min(x1,x2,x3,x4)
            ymin = min(y1,y2,y3,y4)
            xmax = max(x1,x2,x3,x4)
            ymax = max(y1,y2,y3,y4)

            x = (xmin + xmax)/2
            y = (ymin + ymax)/2
            w = xmax - xmin
            h = ymax - ymin

            # 生成boundingbox
            # bbox = [int(line[0]),x,y,w,h]
            # boundingbox.append(bbox)

            # 转为格式化字符串
            string = []
            string.append('{:.6f}'.format(x))
            string.append('{:.6f}'.format(y))
            string.append('{:.6f}'.format(w))
            string.append('{:.6f}'.format(h))

            # 插入原数据行中
            line.insert(1,string[0])
            line.insert(2,string[1])
            line.insert(3,string[2])
            line.insert(4,string[3])
            line = ' '.join(line)

            with open(os.path.join(dst_path,file),'a') as f_new:
                # 写入文件
                f_new.write(''.join(line))
                f_new.write('\n')

    # print(boundingbox)
    # img = plot_boxes_cv2(img, boundingbox)
    # cv2.imshow('',img)
    # cv2.waitKey(0)
