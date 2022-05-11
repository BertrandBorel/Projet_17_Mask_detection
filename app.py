from threading import activeCount
import cv2
import numpy as np 
from tensorflow import keras
import streamlit as st
from PIL import Image, ImageEnhance
import pandas as pd
from datetime import datetime


# fichier xml "cascade"
cascade_path = "./cascades/haarcascade_frontalface_default.xml"
cascade = cv2.CascadeClassifier(cascade_path)
color = (0, 0, 0) #La couleur du carré qui entoure le visage détecté

# model.h5 = notre modèle de reconnaissance 
model = keras.models.load_model('model.h5')

# listes servant à la construction du csv
personne = []
liste_date = []
heure = []

           

def detect_faces(our_image):

    # image
    new_img = np.array(our_image.convert('RGB'))
    faces = cascade.detectMultiScale(new_img[:,:,0])
    
    # incrémentation pour l'ordre des personnes
    somme = 0

    # labels (avec/sans)
    avec_masque = 0
    sans_masque = 0

    for x, y, w, h in faces:
        somme += 1

        # Récupération data (construction du futur csv)
        personne.append(somme)
        test = datetime.now().date()
        liste_date.append(test)
        now = datetime.now()
        instant = f"{now.hour}:{now.minute}:{now.second}"
        heure.append(instant)

        # Préparation de l'image
        face = new_img[x:x+w,y:y+h]
        face = cv2.resize(face,(224, 224), interpolation=cv2.INTER_AREA)/255
        face = np.expand_dims(face, 0) #axis=0
   
        # Prédiction sur l'image 
        pred = model.predict(face)    

        # on précise sur l'image avec/sans masque 
        if np.argmax(pred) == 0 :
            text = 'Avec masque'
            avec_masque += 1
            cv2.rectangle(new_img, (x, y), (x+w, y+h), color)
            cv2.rectangle(new_img, (x, y - 20), (x + w, y), color, -1)
            cv2.putText(new_img, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, .5, (255,255,255))
        else :
            text = 'Sans masque'
            sans_masque += 1
            cv2.rectangle(new_img, (x, y), (x+w, y+h), color)
            cv2.rectangle(new_img, (x, y - 20), (x + w, y), color, -1)
            cv2.putText(new_img, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, .5, (255,255,255))


    # concaténation des dfs en un seul 
    df1 = pd.DataFrame (personne, columns = ['Personne'])
    df2 = pd.DataFrame(liste_date, columns= ['Date'])
    df3 = pd.DataFrame(heure, columns= ['Heure'])    
    df = pd.concat([df1, df2, df3], axis=1)  
    
    # affichage de notre df
    st.dataframe(df)  


    return new_img, avec_masque, sans_masque, df



    
def main():

    # titre principal
    st.title("Détection de personnes")

    # choisir et ouvrir une image
    image_file = st.file_uploader("Choisissez une image :", type=['jpg', 'png', 'jpeg'])

    if image_file is not None:
            our_image = Image.open(image_file)
            # titre de l'image
            st.text("Votre Image")
            # visualisation de l'image
            st.image(our_image)

            # Détection (du visage)
            if st.button("Lancer la détection ! "):
                    result_img, avec_masque,sans_masque,_ = detect_faces(our_image) 
                    st.image(result_img)
                    st.success("{} personnes ont un masque. Nombre de personnes sans masque : {}".format(avec_masque, sans_masque))

            # Enregistrement dans un csv       
            if st.button('Enregistrer les données (csv)'):
                         
                        result_img, avec_masque, sans_masque, data = detect_faces(our_image)
                        data.to_csv(index=False)
                        data.to_csv (r'test_data.csv', index = False, header=True)
                        # phrase sur le téléchargement 
                        st.subheader('Téléchargement du csv réussi !') 
                              

if __name__ == '__main__':
    main()
