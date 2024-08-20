import os
import shutil
path = "/Users/umang/Desktop"
files = os.walk(path)
if(os.path.isdir("/Users/umang/Desktop/embeddings")!=True):
    os.mkdir("/Users/umang/Desktop/embeddings")
dst = "/Users/umang/Desktop/embeddings"
subfolders = [ f.path for f in os.scandir(path) if f.is_dir() ]
subfolders.remove('/Users/umang/Desktop/$RECYCLE.BIN')
subfolders.remove('/Users/umang/Desktop/.vscode')
subfolders.remove('/Users/umang/Desktop/embeddings')
f = []
for folders in subfolders:
   
        
    files = [ f.path for f in os.scandir(f'{folders}') if f.is_dir() ]
    print(folders)
    for f in files:
        com = [ f.path for f in os.scandir(f'{f}') ]
        
        for a in com:
            sub = a.replace(folders, '')
            if(a[-4:])==".npy":
                print(a)
                print(f'{dst}{sub}')
                shutil.copyfile(a, f'{dst}{sub}')
                
            
               
    

        
        # if(files=="new"):
        #     for f in files:
            
        #         if(f[-4:])==".npy":
        #             shutil.copyfile(f'{path}/{folders}/new/{f}', dst)
