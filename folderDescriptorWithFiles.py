import glob
import numpy as np
from natsort import natsorted

path = '/home/prf-05/Documentos/folderDecriptor/TestPath/'

splitSep = '/'
f = open("mavicIdd.txt", "w")
spc = '  '
matrix = []

for file in glob.glob(path+'**',recursive=True):
    files = file.split(splitSep)

    del files[0:files.index('TestPath')+1]

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

print('fase 4')
aux = ' '
for mat in matrix:

    print(*mat, sep='    ', file=f)

    print('\n')

print(matrix)
f.close()
print('DONE!!!')