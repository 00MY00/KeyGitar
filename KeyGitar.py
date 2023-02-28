########################################
#     Script crée par Kuroakashiro     #
########################################
# V 1.0
# Importation des Libreries
print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
try:
    import pygame
    print("Pygame est installé et importé correctement.")
except ImportError:
    print("Pygame n'est pas installé ou n'a pas été importé correctement.")
try:
    import keyboard
    print("keyboard est installé et importé correctement.")
except ImportError:
    print("keyboard n'est pas installé ou n'a pas été importé correctement.")
try:
    import os
    print("os est installé et importé correctement.")
except ImportError:
    print("os n'est pas installé ou n'a pas été importé correctement.")
try:
    import csv
    print("csv est installé et importé correctement.")
except ImportError:
    print("csv n'est pas installé ou n'a pas été importé correctement.")
try:
    from pydub import AudioSegment
    import simpleaudio as sa
    print("pydub est installé et importé correctement.")
except ImportError:
    print("pydub n'est pas installé ou n'a pas été importé correctement.")
print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

###############################################
# Variable Racine

# Récupère le nom du repertoire courent Exemple : 'c:\User'
Racine = os.getcwd()

# Pour entrer dans le répertoire son
RepTemporaire = Racine + "/son/"

###############################################
# Convertion des fichier audio en 'WAV'
# Appel de fonction Example : 'convert_mp3_to_wav("/chemin/du/répertoire")'

def convert_mp3_to_wav(Repertoire):
    for filename in os.listdir(Repertoire):
        if filename.endswith(".mp3"):
            filepath = os.path.join(Repertoire, filename)
            sound = AudioSegment.from_mp3(filepath)
            new_filename = os.path.splitext(filename)[0] + ".wav"
            new_filepath = os.path.join(Repertoire, new_filename)
            sound.export(new_filepath, format="wav")
            os.remove(filepath)

#----------------------------------------------
###############################################
# Récupération des nom de répertoire
# Appel de fonction Exemple : 'All_rep = get_all_dirs("/chemin/du/répertoire")'
def get_all_dirs(Repertoire):
    print("Recuperation des repertoires")
    All_rep = []
    for item in os.listdir(Repertoire):
        item_path = os.path.join(Repertoire, item)
        if os.path.isdir(item_path):
            All_rep.append(item)
    return All_rep

# Recuperation des nom de Repertoire
All_rep = get_all_dirs(RepTemporaire)

# Boucle/loop pour convertire chaque répertoir
print("Convertion des repertoire")
for i in range(len(All_rep)):
    print(RepTemporaire + All_rep[i])
    convert_mp3_to_wav(RepTemporaire + All_rep[i])
print("--------")

#----------------------------------------------
###############################################
# Ajout des nom des fichier audios 
# la clé = nom du répertoire. les valeurs = les nom des fichier.
# la variable x contien tous les clé et chemin !
print("Creation du dictionaire de sond !")
for i in range(len(All_rep)):
    print(All_rep[i])

x = {}
y = []
for var in All_rep:
    directory = RepTemporaire + var + "/"
    y = os.listdir(directory)
    x[var] = y
    y = set()
print("Affichage du dictionaire !")
for cle, valeur in x.items():
    print(f"{cle}: {valeur}")
print("--------")
#----------------------------------------------
###############################################
# Fonctions du programe


# Profiles en entrent le chifre changera le profil
def profiles():
    while True:
        os.system('clear')
        print("")
        print("Entrée le nom de la touche qui sera relier au profile !")
        print("")

        Profile_Name = input(": ")

        if Profile_Name.isdigit() and int(Profile_Name) >= 0 and int(Profile_Name) <= 9:
            print("Touche du Profile : ", Profile_Name)
            break
        else:
            print("Erreur d'entée seul et suporter des chiffres de 0 à 9 !")

    # Profile choix du répertoire de sond a utiliser
    while True:
        os.system('clear')
        print("")
        print("Affichage des Repertoire de 'son'")
        print("Entez [-1] pour quiter.")
        print("")

        # Affichage des repertoires dans 'son'
        for i in range(len(All_rep)):
            print(f"[{i}]", All_rep[i])
        print("-------------------")
        # Entrée user suportent que des 'int'
        while True:
            try:
                Profile_curent_repertoir = int(input("Entrez votre choix : "))
                
                # Condition de sortye du mode profil
                if Profile_curent_repertoir == -1:
                    Profile_chox_sond = 0
                    break

                if Profile_curent_repertoir < len(All_rep):
                    print("Cette valeur n'existe pas !")
                    
                if Profile_curent_repertoir > len(All_rep):
                        print("Cette valeur n'existe pas !")
                else:
                    Profile_chox_sond = 1
                    break
            except ValueError:
                print("Veuillez entrer un nombre entier !")

        # Profile permet de voire le nom des sond et des les atribuer a une touche
        if Profile_chox_sond == 1:
            while True:
                os.system('clear')
                print("")
                print("Affichage du contenu de répertoire !")
                print("contenu du répertoire.")
                # Sonds = x[All_rep[Profile_curent_repertoir]]
                print(f"{x[All_rep[Profile_curent_repertoir]]}")

                Profile_sond_atribution = input(": ")

                Touche_q = ""
                Touche_w = ""
                Touche_e = ""
                Touche_r = ""
                Touche_t = ""
                Touche_z = ""
                Touche_u = ""
                Touche_i = ""
                Touche_o = ""
                Touche_p = ""
                Touche_a = ""
                Touche_s = ""
                Touche_d = ""
                Touche_f = ""
                Touche_g = ""
                Touche_h = ""
                Touche_j = ""
                Touche_k = ""
                Touche_l = ""
                Touche_y = ""
                Touche_x = ""
                Touche_c = ""
                Touche_v = ""
                Touche_b = ""
                Touche_n = ""
                Touche_m = ""


        # Entrées des sond pour les touche affiche les 
        # deferant clés puis en le selectionent dans 
        # l'ordre des lettre on indique le quelle de son et a utiliser avec un chiffre
        # Exemple 
        # [0] Basse
        # [1] Choral
        ###########
        # Basse
        # [0] Sond_basse_0
        # [1] Sond_basse_1
        ###################
        # Lettre actuel [Q]
        ###################

        


    # Définition des données pour le CSV
    profile_Csv = [
        ['Letter', 'Value'],
        ['q', "{Touche_q}"],
        ['w', "{Touche_w}"],
        ['e', "{Touche_e}"]
        ['r', "{Touche_r}"]
        ['t', "{Touche_t}"]
        ['z', "{Touche_z}"]
        ['u', "{Touche_u}"]
        ['i', "{Touche_i}"]
        ['o', "{Touche_o}"]
        ['p', "{Touche_p}"]
        ['a', "{Touche_a}"]
        ['s', "{Touche_s}"]
        ['d', "{Touche_d}"]
        ['f', "{Touche_f}"]
        ['g', "{Touche_g}"]
        ['h', "{Touche_h}"]
        ['j', "{Touche_j}"]
        ['k', "{Touche_k}"]
        ['l', "{Touche_l}"]
        ['y', "{Touche_y}"]
        ['x', "{Touche_x}"]
        ['c', "{Touche_c}"]
        ['v', "{Touche_v}"]
        ['b', "{Touche_b}"]
        ['n', "{Touche_n}"]
        ['m', "{Touche_m}"]    
    ]



    # Creation et ouverture du fichier en mode écriture
    with open(f'Profil_{Profile_Name}.csv', mode='w', newline='') as fichier_csv:
        # Création d'un objet writer
        writer = csv.writer(fichier_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # Écriture des données
        for ligne in profile_Csv:
            writer.writerow(ligne)






#----------------------------------------------
###############################################
# Boucle While True 









################################################################




