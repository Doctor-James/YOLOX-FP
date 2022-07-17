from xml.dom.minidom import Document
import os
import cv2


# def makexml(txtPath, xmlPath, picPath):  # txt所在文件夹路径，xml文件保存路径，图片所在文件夹路径

def makexml(picPath, txtPath, xmlPath):  # txt所在文件夹路径，xml文件保存路径，图片所在文件夹路径
    """此函数用于将yolo格式txt标注文件转换为voc格式xml标注文件
    在自己的标注图片文件夹下建三个子文件夹，分别命名为picture、txt、xml
    """
    dic = {}


    names = ['B_G','B_1','B_2','B_3','B_4','B_5','B_O','B_Bs','B_Bb','R_G','R_1','R_2','R_3','R_4','R_5','R_O','R_Bs','R_Bb',
'N_G','N_1','N_2','N_3','N_4','N_5','N_O','N_Bs','N_Bb','P_G','P_1','P_2','P_3','P_4','P_5','P_O','P_Bs','P_Bb',
    ]

    for index, name in enumerate(names):
        dic.update({str(index):name})

    files = os.listdir(txtPath)
    is_label = True
    count = 0
    length = len(files)

    for i, name in enumerate(files):
        count += 1
        #print(count/length)

        txtFile = open(txtPath + name)
        txtList = txtFile.readlines()

        xmlBuilder = Document()
        annotation = xmlBuilder.createElement("annotation")  # 创建annotation标签
        xmlBuilder.appendChild(annotation)
        img = cv2.imread(picPath + name[0:-4] + ".jpg")
        Pheight, Pwidth, Pdepth = img.shape

        folder = xmlBuilder.createElement("folder")  # folder标签
        foldercontent = xmlBuilder.createTextNode("driving_annotation_dataset")
        folder.appendChild(foldercontent)
        annotation.appendChild(folder)  # folder标签结束

        filename = xmlBuilder.createElement("filename")  # filename标签
        filenamecontent = xmlBuilder.createTextNode(name[0:-4] + ".jpg")
        filename.appendChild(filenamecontent)
        annotation.appendChild(filename)  # filename标签结束

        size = xmlBuilder.createElement("size")  # size标签
        width = xmlBuilder.createElement("width")  # size子标签width
        widthcontent = xmlBuilder.createTextNode(str(Pwidth))
        width.appendChild(widthcontent)
        size.appendChild(width)  # size子标签width结束

        height = xmlBuilder.createElement("height")  # size子标签height
        heightcontent = xmlBuilder.createTextNode(str(Pheight))
        height.appendChild(heightcontent)
        size.appendChild(height)  # size子标签height结束

        depth = xmlBuilder.createElement("depth")  # size子标签depth
        depthcontent = xmlBuilder.createTextNode(str(Pdepth))
        depth.appendChild(depthcontent)
        size.appendChild(depth)  # size子标签depth结束

        annotation.appendChild(size)  # size标签结束


        for j in txtList:

            oneline = j.strip('\n').split(" ")

            if(int(oneline[0]) != 13 and int(oneline[0]) != 21 and int(oneline[0]) != 17 and int(oneline[0]) != 4 and int(oneline[0]) != 9 and int(oneline[0]) != 12):
                is_label = False
                continue
            # print(oneline)

            object = xmlBuilder.createElement("object")  # object 标签
            picname = xmlBuilder.createElement("name")  # name标签
            namecontent = xmlBuilder.createTextNode(dic[oneline[0]])
            
            picname.appendChild(namecontent)
            object.appendChild(picname)  # name标签结束

            pose = xmlBuilder.createElement("pose")  # pose标签
            posecontent = xmlBuilder.createTextNode("Unspecified")
            pose.appendChild(posecontent)
            object.appendChild(pose)  # pose标签结束

            truncated = xmlBuilder.createElement("truncated")  # truncated标签
            truncatedContent = xmlBuilder.createTextNode("0")
            truncated.appendChild(truncatedContent)
            object.appendChild(truncated)  # truncated标签结束

            difficult = xmlBuilder.createElement("difficult")  # difficult标签
            difficultcontent = xmlBuilder.createTextNode("0")
            difficult.appendChild(difficultcontent)
            object.appendChild(difficult)  # difficult标签结束

            # bndbox = xmlBuilder.createElement("bndbox")  # bndbox标签
            # xmin = xmlBuilder.createElement("xmin")  # xmin标签
            # mathData = int(((float(oneline[1])) * Pwidth + 1) - (float(oneline[3])) * 0.5 * Pwidth)
            # xminContent = xmlBuilder.createTextNode(str(mathData))
            # xmin.appendChild(xminContent)
            # bndbox.appendChild(xmin)  # xmin标签结束

            # ymin = xmlBuilder.createElement("ymin")  # ymin标签
            # mathData = int(((float(oneline[2])) * Pheight + 1) - (float(oneline[4])) * 0.5 * Pheight)
            # yminContent = xmlBuilder.createTextNode(str(mathData))
            # ymin.appendChild(yminContent)
            # bndbox.appendChild(ymin)  # ymin标签结束

            # xmax = xmlBuilder.createElement("xmax")  # xmax标签
            # mathData = int(((float(oneline[1])) * Pwidth + 1) + (float(oneline[3])) * 0.5 * Pwidth)
            # xmaxContent = xmlBuilder.createTextNode(str(mathData))
            # xmax.appendChild(xmaxContent)
            # bndbox.appendChild(xmax)  # xmax标签结束

            # ymax = xmlBuilder.createElement("ymax")  # ymax标签
            # mathData = int(((float(oneline[2])) * Pheight + 1) + (float(oneline[4])) * 0.5 * Pheight)
            # ymaxContent = xmlBuilder.createTextNode(str(mathData))
            # ymax.appendChild(ymaxContent)
            # bndbox.appendChild(ymax)  # ymax标签结束

            # object.appendChild(bndbox)  # bndbox标签结束






            bndbox = xmlBuilder.createElement("bndbox")  # bndbox标签

            xmin = xmlBuilder.createElement("xmin")  # xmin标签
            mathData = int(((float(oneline[1])) * Pwidth + 1) - (float(oneline[3])) * 0.5 * Pwidth)
            xminContent = xmlBuilder.createTextNode(str(mathData))
            xmin.appendChild(xminContent)
            bndbox.appendChild(xmin)  # xmin标签结束

            ymin = xmlBuilder.createElement("ymin")  # ymin标签
            mathData = int(((float(oneline[2])) * Pheight + 1) - (float(oneline[4])) * 0.5 * Pheight)
            yminContent = xmlBuilder.createTextNode(str(mathData))
            ymin.appendChild(yminContent)
            bndbox.appendChild(ymin)  # ymin标签结束

            xmax = xmlBuilder.createElement("xmax")  # xmax标签
            mathData = int(((float(oneline[1])) * Pwidth + 1) + (float(oneline[3])) * 0.5 * Pwidth)
            xmaxContent = xmlBuilder.createTextNode(str(mathData))
            xmax.appendChild(xmaxContent)
            bndbox.appendChild(xmax)  # xmax标签结束

            ymax = xmlBuilder.createElement("ymax")  # ymax标签
            mathData = int(((float(oneline[2])) * Pheight + 1) + (float(oneline[4])) * 0.5 * Pheight)
            ymaxContent = xmlBuilder.createTextNode(str(mathData))
            ymax.appendChild(ymaxContent)
            bndbox.appendChild(ymax)  # ymax标签结束

            object.appendChild(bndbox)  # bndbox标签结束


            points = xmlBuilder.createElement("points")  # bndbox标签
            
            x1 = xmlBuilder.createElement("x1")  # x1标签
            mathData = int(((float(oneline[5])) * Pwidth + 1))
            x1Content = xmlBuilder.createTextNode(str(mathData))
            x1.appendChild(x1Content)
            points.appendChild(x1)  # x1标签结束

            y1 = xmlBuilder.createElement("y1")  # ymin标签
            mathData = int(((float(oneline[6])) * Pheight + 1))
            y1Content = xmlBuilder.createTextNode(str(mathData))
            y1.appendChild(y1Content)
            points.appendChild(y1)  # ymin标签结束

            x2 = xmlBuilder.createElement("x2")  # xmax标签
            mathData = int(((float(oneline[7])) * Pwidth + 1))
            x2Content = xmlBuilder.createTextNode(str(mathData))
            x2.appendChild(x2Content)
            points.appendChild(x2)  # xmax标签结束

            y2 = xmlBuilder.createElement("y2")  # ymax标签
            mathData = int(((float(oneline[8])) * Pheight + 1))
            y2Content = xmlBuilder.createTextNode(str(mathData))
            y2.appendChild(y2Content)
            points.appendChild(y2)  # ymax标签结束

            x3 = xmlBuilder.createElement("x3")  # xmin标签
            mathData = int(((float(oneline[9])) * Pwidth + 1))
            x3Content = xmlBuilder.createTextNode(str(mathData))
            x3.appendChild(x3Content)
            points.appendChild(x3)  # xmin标签结束

            y3 = xmlBuilder.createElement("y3")  # ymin标签
            mathData = int(((float(oneline[10])) * Pheight + 1))
            y3Content = xmlBuilder.createTextNode(str(mathData))
            y3.appendChild(y3Content)
            points.appendChild(y3)  # ymin标签结束

            x4 = xmlBuilder.createElement("x4")  # xmax标签
            mathData = int(((float(oneline[11])) * Pwidth + 1))
            x4Content = xmlBuilder.createTextNode(str(mathData))
            x4.appendChild(x4Content)
            points.appendChild(x4)  # xmax标签结束

            y4 = xmlBuilder.createElement("y4")  # ymax标签
            mathData = int(((float(oneline[12])) * Pheight + 1))
            y4Content = xmlBuilder.createTextNode(str(mathData))
            y4.appendChild(y4Content)
            points.appendChild(y4)  # ymax标签结束

            object.appendChild(points)  # bndbox标签结束























            annotation.appendChild(object)  # object标签结束

        if(is_label == False):
            is_label = True
            continue
        f = open(xmlPath + name[0:-4] + ".xml", 'w')
        xmlBuilder.writexml(f, indent='\t', newl='\n', addindent='\t', encoding='utf-8')
        f.close()


if __name__ == "__main__":
    picPath = "./images/"  # 图片所在文件夹路径，后面的/一定要带上
    txtPath = "./labels_new/"  # txt所在文件夹路径，后面的/一定要带上
    xmlPath = "./Annotations/"  # xml文件保存路径，后面的/一定要带上

    if not os.path.exists(xmlPath):
        os.mkdir(xmlPath)

    makexml(picPath, txtPath, xmlPath)