import numpy as np
import cv2 as cv2

print("-- BEGIN --")

# nb images
nb_images = 10

# nb keypoints
nb_kps = 8

# array where the keypoints coordinates are loaded
kps_pos = np.zeros([nb_images,2*nb_kps]).astype(np.short)

# text file
file = open("../Blender/txt_files/test1.txt", 'r')

# path to the images
images_path = "../Blender/Rendus/"

for i in range(nb_images):
    line = file.readline()
    l = line.split(' ')
    for k in range(2*nb_kps):
        kps_pos[i, k] = l[k]

for i in range(nb_images):
    print("-- image",i+1,"--")
    img_name = images_path + "image_num_" + str(i+1) + ".png"
    img = cv2.imread(img_name)
    height, width, channels = img.shape
    print("size : [",height,";",width,"]")
    for k in range(0,2*nb_kps-1,2):
        x = kps_pos[i,k]
        y = kps_pos[i,k+1]
        print("keypoint",k,"[",x,";",y,"]")
        #cv2.circle(img, (x, y), 2, (153, 0, 0), 2)
        cv2.circle(img, (x, height-y), 2, (153, 0, 0), 2)
    cv2.imshow('image', img)
    cv2.waitKey(0)

print("-- END --")