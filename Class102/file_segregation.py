import os
import shutil

from_dir="C:/Users/ADMIN/Desktop/Dummydocuments"
to_dir="C:/Users/ADMIN/Downloads/Class102"

list_of_files = os.listdir(from_dir)
print(list_of_files)



for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
    print(name)
    print(extension)

    if extension == "" :
        continue
        
    if extension in ['.png','.jpg'] :
        path1 = from_dir+'/'+file_name
        path2 = to_dir
        path3 = to_dir+'/'+file_name

    if  os.path.exists(path2):
            print("moving..."+file_name+"......")
            shutil.move(path1,path3)
    else:
        shutil.move(path2)
        print("moving..."+file_name+"......")
        shutil.move(path1,path3)