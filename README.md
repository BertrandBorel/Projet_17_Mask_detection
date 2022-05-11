# Projet_17_Mask_detection

## Objectifs du projet :
Reprendre notre modèle de détection des masques et l'utiliser dans une application streamlit. 
Streamlit est une librairie open source en Python créée en 2018.
En outre c'est un framework offrant la possibilité de déployer très rapidement une application.

## Caractéristiques :
L'application qui a été développée devait répondre aux caractéristiques suivantes :
- Importer et visualiser une image
- Lancer la webcam (facultatif).
- Détecter le port du masque (ou son absence)
- Comptage (personne avec masque et personne sans masque).
- Un historique sous forme un tableau (personne, date/heure de détection et statut).


## Utilisation :
L'application permet de détecter sur une photo si une ou plusieurs personnes portent un masque ou non.
Après avoir lancé la détection, l'utilisateur peut récupérer les données dans un csv. 

## Conclusion du projet :
L'application rencontre des difficultés à reconnaître les masques lorsqu'il y a un trop grand nombre de personnes sur la photo.
Il serait intéressant d'entraîner un nouveau modèle car celui-ci présente des lacunes. 


## Captures d'écran :

<img width="294" alt="Capturex" src="https://user-images.githubusercontent.com/95342688/167912060-685cf1e3-b9fc-49de-b5e4-9d454b636e82.PNG"> 
L'utilisateur peut charger une image de son choix et lancer la détection à partir de celle-ci en appuyant sur un bouton. 



<img width="280" alt="Capturex" src="https://user-images.githubusercontent.com/95342688/167912306-b10a506b-898f-49a5-80ab-d8be26f2ab0b.PNG">
Une fois la détection réalisée, un tableau de données est affiché, contenant chaque personne identifiée avec la date et l'heure. 

L'image montre les personnes portant un masque et celles qui n'en n'ont pas. Les visages non encadrés sont ceux que le modèle n'a pas identifié.

Un message s'affiche avec un fond vert. Il indique le nombre de personnes qui ont un masque et le nombre de celles qui n'en portent pas. 

L'utilisateur peut télécharger le tableau de données dans un fichier csv en appuyant sur un bouton. 
