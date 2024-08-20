import matplotlib.pyplot as plt
from deepface import DeepFace
from retinaface import RetinaFace
from numpy.linalg import norm
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os
faces = RetinaFace.extract_faces("/Users/umang/Downloads/IMG_6731.JPG", align = True)
count = 0
people = []
path = "/Users/umang/Desktop/embeddings/new"
emb = []
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
person = ''
max_simi=0
for face in faces:
    count = count +1
    print(face)
    
    plt.imshow(face)
    plt.axis('off')
    plt.savefig(f"pune/face_{count}.png", bbox_inches='tight', pad_inches = 0)
    print(count)
    embedding = DeepFace.represent(img_path = f"pune/face_{count}.png", 
        model_name = models[2], enforce_detection=False)
    print(embedding)
    inp = (embedding[0].get('embedding'))
    emb.append(inp)
    files_emb = os.listdir(path)
    for embeddings in files_emb:
        
        embed = np.load(f'{path}/{embeddings}')
        cos =np.dot(np.squeeze(inp),np.squeeze(embed))/((norm(inp))*norm((embed)))
        if(cos>max_simi):
            ind = embeddings.find('_')
            max_simi=cos
            person = embeddings[:ind]
    print(max_simi)
    people.append(person)
    person = ''
    max_simi = 0 

print(people)
print(count)