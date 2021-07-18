# Author: Manish Tiwaray
# you can edit or remove any folder by your choise 

from genericpath import isfile
import os,shutil
folders={
    'videos':['.mp4','.webm','.mkv'],
    'documents':['.doc','.txt','.pdf','.docx'],
    'images':['.png','.jpeg'],
    'music':['.mp3'],
    'excelFiles':['.xls','.xlsx','.csv'],
    'shapeFiles':['.shp','.dbf','.cpg','.prj','.sbn','.sbx','.shx','xml'],
    'kmlFiles':['.kml','.kmz'],
    'netcdfFiles':['.nc'],
    'zipFiles':['.zip','.rar','.tar.gz'],
    'rasterFiles':['.tfw','.tif','.tif.aux.xml','tif.ovr','.tiff','.img','.jp2','.jgwx','.jpg','.jpg.aux.xml'],
    'GeoJSON':['.json','.geojson'],
    'gisDocument':['.mxd','.qgs','.qgz']

}
# print(folders)
# for folder_name in folders:
#     print(folder_name)
#     for data in folders[folder_name]:
#         print(data)

def create_move_file(extention,file_name):
    search=False
    for folder_name in folders:
        if "."+extention in folders[folder_name]:
            search=True
            if folder_name not in os.listdir(formatdirectory):
                os.mkdir(os.path.join(formatdirectory,folder_name))
            shutil.move(os.path.join(formatdirectory,file_name),os.path.join(formatdirectory,folder_name))
            break
    if search!=True:
        if otherfolder_name not in os.listdir(formatdirectory):
           os.mkdir(os.path.join(formatdirectory,otherfolder_name)) 
        shutil.move(os.path.join(formatdirectory,file_name),os.path.join(formatdirectory,otherfolder_name))


formatdirectory=input('Enter format directory to format data into folders:')
otherfolder_name=input('Enter the folder name for others file:')
all_files_in_directory=os.listdir(formatdirectory)
length=len(all_files_in_directory)
count=1
#print(all_files_in_directory) 

#to select on files not touch folder b'coz we created folder for save data.
for files in all_files_in_directory:
    #print(files)
    #if os.path.isfile(formatdirectory+'\\'+files)==True:
    if os.path.isfile(os.path.join(formatdirectory,files))==True:
        #print('yes')
        print(f"Total Files: {length} --- Moved: {count} --- Left Files: {length-count}")
        create_move_file(files.split(".")[-1],files)
    count+=1
        #print(files.split(".")[-1])