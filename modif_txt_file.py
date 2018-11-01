import os

print("-- BEGIN --")

# nb images
nb_images = 3000

# nb keypoints
nb_kps = 8

# text file
file_source = open("..\\..\\Dataset_Generation\\Blender\\txt_files\\train_virtual_256-Copy.txt", 'r')
file = open("..\\..\\Dataset_Generation\\Blender\\txt_files\\train_virtual_256_2.txt", 'w')


for i in range(nb_images):
    line = file_source.readline()
    l = line.split(' ')
    file.write('blender_' +l[0] + ' ')
    print('blender_' +l[0] + ' ')
    for j in range(1,len(l)-1,2):
        print(str(j) + ' : ' + str(int(l[j])) + ' ')
        print(str(j+1) + ' : ' + str(int(l[j+1])) + ' ')
        # l[j] : x

        if int(l[j])<0 or int(l[j])>256 or int(l[j+1])<0 or int(l[j+1])>256:
            l[j] = '-1'
            l[j+1] = '-1'
        file.write(l[j] + ' ' + l[j+1] + ' ')
    file.write('\n')


file_source.close()
file.close()
print("-- END --")