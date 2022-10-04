import os

BASE_DIR= r'/home/pujan/Desktop/random'  #  r means raw string

file_types={
    'photos':['jpg','jpeg','png'],
    'documents':['ppt','pdf'],
    'movie':['mkv','mp4'],
    'text_file':['txt'],
    'python':['py','pyc']
}

# for creating folder
for file_type in file_types:
    full_path=os.path.join(BASE_DIR,file_type)
    #print(full_path)
    #print('only key',file_type)
    if not os.path.exists(full_path):
        os.mkdir(full_path)
# logic for moving file to folder
for file in os.listdir(BASE_DIR):
    extension=file.split('.')[-1]
    #print(extension)
    for key in file_types:
        #print(file,key,file_types[key])
        if extension in file_types[key]:
            #print(extension,'is a ',key)
            path_src=os.path.join(BASE_DIR,file)
            path_dest=os.path.join(BASE_DIR,key,file)
            #print(path_src,path_dest)
            os.rename(path_src,path_dest)




