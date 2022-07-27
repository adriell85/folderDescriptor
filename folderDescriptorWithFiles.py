import glob
import numpy as np
from natsort import natsorted
# from termcolor import colored
# from cv2 import split

path = '/home/prf-05/Documentos/folderDecriptor/TestPath/'
# path_calib = '/home/prf-05/Documentos/folder test/'
splitSep = '/'
f = open("mavicIdd.txt", "w")
spc = '  '
matrix = []

for file in glob.glob(path+'**',recursive=True):
    files = file.split(splitSep)
    # files = del files
    del files[0:files.index('TestPath')+1]
    # print()
    # if ((files[-1]).split('.'))[-1] == 'txt' or 'pptx' or  'png' or 'mp4' or 'avi' or 'mat' or 'jpeg':
        # # print(files[-1])
        # del files[files.index(files[-1])]
    files_arr = np.array(files)
    matrix.append(files_arr)
print('fase 1')

matrix = natsorted(matrix)
mmm=matrix
aux = ' '
height = 0
width = 0
count = 0
print(matrix)
var = True
print('fase 2')
while var:
    print('f')
    for mat in matrix:
            for m in mat:
                if len(mat)>1+count:
                    if mat[count]==m:
                        matrix[height][width]=''
                        width = width + 1

                    else:
                        matrix[height][width]=m
                        width = width + 1

            height = height + 1
            width = 0
    count = count + 1
    height = 0
    if count >= len(matrix):
        var = False


print('fase 3')
# for mat in matrix:
#     for m in mat:
#         if (m.split('.'))[-1] == 'txt' or 'pptx' or  'png' or 'mp4' or 'avi' or 'mat' or 'jpeg':
#             del matrix[:] == mat
print('fase 4')
aux = ' '
for mat in matrix:
    # print(*mat, sep='-----', file=f)
    print(*mat, sep='    ', file=f)
    # for m in mat:
    #     if m == '':
    #         print(aux,file=f)
    #     else:
    #         print(m,file=f)
    print('\n')

        # aux = aux+aux
print(matrix)
f.close()
print('DONE!!!')