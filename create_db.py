import os
from glob import glob
from glob import glob
import matplotlib.pyplot as plt
from deepface import DeepFace
from retinaface import RetinaFace
import numpy as np
path_ = "/Users/umang/Desktop"
subfolders = [ f.path for f in os.scandir(path_) if f.is_dir() ]
models = [
  "VGG-Face", 
  "Facenet", 
  "Facenet512", 
  "OpenFace", 
  "DeepFace", 
  "DeepID", 
  "ArcFace", 
  "Dlib", 
  "SFace",
]
subfolders.remove('/Users/umang/Desktop/$RECYCLE.BIN')
subfolders.remove('/Users/umang/Desktop/.vscode')
count = 0
file_num = 0
for folders in subfolders:
    name = folders.replace(path_, '')
   
    
    path = folders
    dir_list = os.listdir(path)
    file_num =0
    if(os.path.isdir(f'{folders}/new')!=True):
        os.mkdir(f'{folders}/new')
    for files in dir_list:
        
        
        
        print(files)
        if(files!='.DS_Store'):
            file_num = file_num+1
            faces = RetinaFace.extract_faces(f"{folders}/{files}", align = True)
            count=0
            for face in faces:
                count=count+1
                
                print(face)
                
                plt.imshow(face)
                plt.axis('off')
                plt.savefig(f"{folders}/new/{name}_face_{file_num}.png", bbox_inches='tight', pad_inches = 0)
                print(f"{files}_{count}")
                if(count>1):
                    os.remove(f"{folders}/{files}")
                    break    
                embedding = DeepFace.represent(img_path = f"{folders}/new/{name}_face_{file_num}.png",
                                                model_name = models[2], enforce_detection=False)
                np.save(f"{folders}/new/{name}_face_{file_num}.npy", embedding[0].get('embedding'))
                em = np.load(f"{folders}/new/{name}_face_{file_num}.npy", allow_pickle=True)
                print(em)
                # file =  open(f"{folders}/new/face_{file_num}.txt","w+")
                # file.write(embedding[0].get('embedding'))
                # file.close()

                
               
  
  
  
  
  

  

