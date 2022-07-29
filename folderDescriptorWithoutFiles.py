import glob
import numpy as np
from natsort import natsorted

path = '/home/prf-05/Documentos/folderDecriptor/TestPath/'

splitSep = '/'
f = open("mavicIdd.csv", "w")
spc = '  '
matrix = []

for file in glob.glob(path+'**',recursive=True):
    files = file.split(splitSep)

    del files[0:files.index('TestPath')+1]

    files_arr = np.array(files)
    matrix.append(files_arr)


matrix = natsorted(matrix)
mmm=matrix
aux = ' '
height = 0
width = 0
count = 0
print(matrix)
var = True
while var:
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

matrix_badPart = []
matrix_converted = []
for mat in matrix:

    matrix_converted.append(mat.tolist())
    for m in mat:
        test = (m.split('.'))[-1]
        if test == 'txt' or test == 'pptx' or test == 'png' or test == 'mp4' or test == 'avi' or test == 'mat' or test == 'jpeg' or test == 'mkv':

            matrix_badPart.append(mat.tolist())
            break

print(matrix)

for i in matrix_badPart:
    del matrix_converted[matrix_converted.index(i)]

for mat in matrix_converted:
    print(*mat, sep='    ', file=f)
f.close()

print('DONE!!!')