import glob
import numpy as np
from natsort import natsorted
# from termcolor import colored
# from cv2 import split

# path = '/home/prf-05/Documentos/oneDriver/'
path_calib = '/home/prf-05/Documentos/folder test/'
splitSep = '/'
f = open("mavicIdd.txt", "w")
spc = '  '
matrix = []

for file in glob.glob(path_calib+'**',recursive=True):
    files = file.split(splitSep)
    # files = del files
    del files[0:files.index('folder test')+1]
    # print()
    # if ((files[-1]).split('.'))[-1] == 'txt' or ((files[-1]).split('.'))[-1] == 'pptx' or ((files[-1]).split('.'))[-1] == 'png' or ((files[-1]).split('.'))[-1] == 'mp4' or ((files[-1]).split('.'))[-1] == 'avi':
    #     # print(files[-1])
    #     del files[files.index(files[-1])]
    files_arr = np.array(files)
    matrix.append(files_arr)
    # print(len(files))
    # print(files)
    # aux=''
    # # files = 
    # next=''
    # previous=''
    # count=0
    # for fil in files:
    #     # if files+
    #     print(aux+fil)
    #     aux = aux+spc
    #     count=+1
    # print(file)
#     folder = (file.split(splitSep))[-1]
#     # print(folder)
#     f.write(folder+'\n')
#     for folders in glob.glob(file+splitSep+'*'):
#         subfolder = (folders.split(splitSep))[-1]
#         # print("     ",subfolder)
#         f.write("     " + subfolder+'\n')
#         for ffolders in glob.glob(file+splitSep+'*'+splitSep+'*'):
#             subffolder = (ffolders.split(splitSep))[-1]
#             # print("         ",subffolder)
#             f.write("         " + subffolder+'\n')
# f.close()
# matrix = np.unique(matrix)
count = 0
# print(matrix[0])
aux=' '
z = 0
repetitive_folders=[]
rows = np.shape(matrix[:])
# cols = np.shape(matrix[:])
matrix = natsorted(matrix)
for mat in matrix:
    # 0
    # if count != 0:
    if count>0 :
        if mat[0] == matrix[count-1][0]:
            print(aux + mat[0], file=f)
            np.where(mat[0] == matrix,'',matrix)
            # matrix = np.delete(matrix,1,1)
            # repetitive_folders.append(mat[0])
    #         if(len(matrix)>0):
    #             for row in range(rows[0]):
    #                 if matrix[row][0] == mat[0]:
    #         aux = aux + aux
    #
    #
    #                     # line = matrix[row]
    #                     # if len(line) == 1:
    #                     #     del line
    #                     #     # line.remove(mat[0])
    #                     #     matrix[row] = []
    #                     # else:
    #                     #     # del line[0]
    #                     #     line[0]=''
    #                     #     # line.remove(mat[0])
    #                     #     matrix[row]=line
    #
    #
    #
    #             # for m in range(len(matrix)):
    #             #     if matrix[m][0] == repetitive_folders[-1]:
    #             #      del matrix[m][0]
    #         # aux = aux+aux
    # else:
    #     print(aux + mat[0], file=f)
    #     aux=aux+aux


        # for m in mat:
        #     print(mat,file=f)
    # if len(matrix[count]) != len(m): 
    #     print('    |',*m,'\"(txt,mp4,png,avi,pptx)files\";',sep='-----',file=f)
    # else:
    #     print(*m,sep='-----',file=f)
        
    count=count+1
# print(matrix)
f.close()
print('DONE!!!')