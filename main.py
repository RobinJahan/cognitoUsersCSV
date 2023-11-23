import boto3
import json
import pandas

client_cognito = boto3.client('cognito-idp', region_name='eu-west-3') # vérifier la région utilisée par AWS Cognito

csvName = "exemple.csv" #Saisir le nom du fichier CSV contenant les users
userPoolId = "eu-west-exemple" # Saisir l'id du userpool cognito
temporaryPassword = "mdp-exemple" # Saisir le mot de passe par défaut, l'utilisateur devra le changer à la première connexion

dataframe = pandas.read_csv(csvName)  

total = 0 # total de création de compte
success = 0 # total de compte créé
errors = [] # liste des adresses mail qui n'ont pas été créée

for index, row in dataframe.iterrows():
    total = total + 1
    try: 
        #Saisir les attributs du user parmis les champs du fichier csv
        username =  str(row['utl_mail'])
        email = str(row['utl_mail'])
        prenom = str(row['utl_prenom'])
        nom = str(row['utl_nom'])

        #puis les renseigner dans l'array UserAttributes de la fonction admin_create_user()
        print('================= adding email : ' + username)

        response = client_cognito.admin_create_user(
        UserPoolId=userPoolId,  
        Username=username,
        TemporaryPassword=temporaryPassword, 
        MessageAction='SUPPRESS', # Supprime l'envoie de mail à l'utilisateur lors de la création de comptes sur cognito
        UserAttributes=[ # les attribus à renseigner dans le compte, les champs requis sont email & email_verified
            {
                'Name': 'family_name', #nom de l'attribut dans cognito, on peut mettre des attribut custom
                'Value': nom #valeur du fichier csv
            },
            {
                'Name': 'given_name',
                'Value': prenom
            },
            {
                'Name': 'email',
                'Value': email
            },
            {
                'Name': 'email_verified',
                'Value': 'true'
            },
        ]
        )
        success = success + 1
        print(response)
    except Exception as e:
        print("Error for ", username)
        errors.append(username)
        print("error :", str(e))



print("================= WORK FINISHED =================")
print("total emails : " + str(total) + ", success : " + str(success) + ", failed : " + str(len(errors)))
if len(errors) > 0 :
    print("emails in error are : ")
    print(errors)