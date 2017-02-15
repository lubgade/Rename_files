import os
import random

def rename_files():
    # 1. Get files from the folder and attach random numbers
    file_list = os.listdir("/home/ubuntu/Downloads/Leena/alphascrambled")
    print(file_list)
    saved_path = os.getcwd()
    print("Current directory"+saved_path)
    os.chdir("/home/ubuntu/Downloads/Leena/alphascrambled")

    for file_name in file_list:
        prefix = str(random.randint(1,99))
        new_name = prefix + file_name
        os.rename(file_name,new_name)
        print new_name
        
    #2 Get the renamed files 
    file_list = os.listdir("/home/ubuntu/Downloads/Leena/alphascrambled") 
    print("current directory"+os.getcwd())
    os.chdir("/home/ubuntu/Downloads/Leena/alphascrambled")

    #3 Renaming  files
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))


    rename_files()    
