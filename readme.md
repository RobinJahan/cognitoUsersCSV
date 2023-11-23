# **Création de utilisateur Cognito à partir d'une liste**

Ce script python permet de créer des utilisateurs dans un userpool Cognito à partir d'une liste d'utilisateur en format .csv

Une fois éxecuter, il va parcourir le fichier.csv ligne par ligne pour créer des comptes sur le userpool cognito grace à l'API cognito. En cas d'erreur le script affiche dans les logs en fin d'execution : les emails des comptes qui ont retourné une erreur.

## Prérequis

Installer Pandas :  `pip install pandas `

Installer Boto3 : `pip install boto3`

Boto3 demande d'avoir AWS CLI d'installé et configuré (aws configure)

Avoir un fichier.csv contenant les users ainsi que leurs attributs à saisir dans Cognito.

PS : Ce script ne fait que la création de compte ainsi que l'ajout d'attribut dans cognito. **Il n'ajoute pas les Users dans des groupes**, il faudra le faire manuellement ou bien faire évoluer ce script.

## Etapes à suivre

- Si il y a des attribut custom, penser à ajouter les attributs custom dans le userpool cognito avant de créer les users.
- Vérifier la région utilisée par le service Amazon Cognito dans **region_name** (ligne 5 de main.py)
- Renseigner le nom du fichier.csv que le script va lire (ligne 7 de main.py)
- Renseigner l'id du Userpool Cognito auquel on effectue la création de compte (ligne 8 de main.py)
- Renseigner le mot de passe temporaire des comptes créés (ligne 9 de main.py) L'utilisateur changera ce mot de passe dés la première connexion.
- Saisir les attributs du user parmis les champs du fichier csv (ligne 20 de main.py) puis les renseigner dans l'array UserAttributes de la fonction admin_create_user (ligne 32 de main.py) (**minimum requis : email, email_verified**)
- Executer main.py
