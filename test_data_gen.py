import numpy as np
import cv2 as cv2
import os

print("-- BEGIN --")

# nb images
nb_images = 3000
step = 20

# nb keypoints
nb_kps = 8

# array where the keypoints coordinates are loaded
kps_pos = np.zeros([nb_images,2*nb_kps]).astype(np.short)
#name of the images
name_images = []

# text file

file = open("..\\..\\Dataset_Generation\\Blender\\txt_files\\train_virtual_256_2.txt", 'r')

# path to the images
images_path = "..\\..\\Dataset_Generation\\Blender\\virtual_dataset_256\\"
print(os.listdir(images_path))
for i in range(nb_images):
    line = file.readline()
    l = line.split(' ')
    name_images.append(l[0])
    for k in range(1,2*nb_kps+1):
        kps_pos[i, k-1] = l[k]


for i in range(6):
    j = i * step
    print("-- " + name_images[j] + " --")
    img_name = images_path + name_images[j]
    img = cv2.imread(img_name)
    height, width, channels = img.shape
    print("size : [",height,";",width,"]")
    for k in range(0,2*nb_kps-1,2):
        x = kps_pos[j,k]
        y = kps_pos[j,k+1]
        print("keypoint",k,"[",x,";",y,"]")
        #cv2.circle(img, (x, y), 2, (153, 0, 0), 2)
        cv2.circle(img, (x, 256-y), 2, (153, 0, 0), 2)
    cv2.imshow('image', img)
    print('..\\..\\Presentations\\Presentation2' + name_images[j])
    cv2.imwrite('..\\..\\Presentations\\Presentation2\\' + name_images[j],img)
    cv2.waitKey(0)

print("-- END --")