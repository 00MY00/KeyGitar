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
try:
    from pydub import AudioSegment
    import re
    print("re est installé et importé correctement.")
except ImportError:
    print("re n'est pas installé ou n'a pas été importé correctement.")
print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

###############################################
# Variable Racine

# Récupère le nom du repertoire courent Exemple : 'c:\User'
Racine = os.getcwd()

# Pour entrer dans le répertoire son
RepTemporaire = Racine + "/son/"
RepTemporaireProfil = Racine + "/Profiles/"

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

############################################################ Fonction Profiles
# Profiles en entrent le chifre changera le profil
def profiles(lettre):
    while True:
        os.system('clear')
        print("Lettre celectionée : ", lettre)
        print("")
        print("Entrée le nom de la touche qui sera relier au profile !")
        print("Exemple : '1'")
        print("")

        Profile_Name = input(": ")

        if Profile_Name.isdigit() and int(Profile_Name) >= 0 and int(Profile_Name) <= 9:
            print("Touche du Profile : ", Profile_Name)
            return Profile_Name
            
        else:
            print("Erreur d'entée seul et suporter des chiffres de 0 à 9 !")
    
def profiles_sond(lettre):
    # Profile choix du répertoire de sond a utiliser
    while True:
        os.system('clear')
        print("Lettre celectionée : ", lettre)
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
                if str(Profile_curent_repertoir) == "-1":
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

        # Profile permet de voire le nom des sond et de les atribuer a une touche
        if Profile_chox_sond == 1:
            while True:
                os.system('clear')
                print("Lettre celectionée : ", lettre)
                print("")
                print("Affichage du contenu de répertoire !")
                print("contenu du répertoire.")
                print("Entez [-1] pour quiter.")
                print("---------------------")

                # Dois faire un affichage plus lisible Clé en hau et les valeur lignes par ligne avec le numero de choix
                # Affichage_sons_profile_choisi = x[All_rep[Profile_curent_repertoir]]
                
                Profile_repertoire_choix = RepTemporaire + All_rep[Profile_curent_repertoir]
                fichiers = os.listdir(Profile_repertoire_choix)
                # Affichage du contenu du répertoire choisi
                i = 0
                for fichier in fichiers:
                    print(f"[{i}] {fichier}")
                    i += 1
                print("_____________________")

                Profile_sond_atribution = input(": ")
                Profile_sond_atribution = int(Profile_sond_atribution)
                # Affichage Débegage
                #print("Resultat : ", x[All_rep[Profile_curent_repertoir]][Profile_sond_atribution])
                #print("Nom Profile", Profile_Name)
                #print("Repertoire Temporaire : ", RepTemporaire)
                #print("Dossier de Sond: ", All_rep[Profile_curent_repertoir])
                #print("Fichier Sond selectioner : ", x[All_rep[Profile_curent_repertoir]][Profile_sond_atribution])
                print("Chemin : ", RepTemporaire + All_rep[Profile_curent_repertoir] + "/" + x[All_rep[Profile_curent_repertoir]][Profile_sond_atribution])
                Profile_chemin_choi = RepTemporaire + All_rep[Profile_curent_repertoir] + "/" + x[All_rep[Profile_curent_repertoir]][Profile_sond_atribution]
                return Profile_chemin_choi
                break

def profiles_Creation_csv(nom, lettre, path):

    # Le nom du fichier CSV sera Profile_ + la valeur de la lettre suivie de ".csv"
    file_name = RepTemporaireProfil + "Profile_" + nom.lower() + ".csv"

    # Verification ci le fichier existe déja
    if os.path.isfile(file_name):
        print("Le fichier existe")
        # ci le fichier csv existe récuperation du contenu dans profile_Csv
        with open(file_name, newline='') as csvfile:
            reader = csv.reader(csvfile)
            profile_Csv = list(reader)
        
        # Ajoute le nouveau chemin a la clé
        for i in range(len(profile_Csv)):
            if profile_Csv[i][0] == lettre:
                profile_Csv[i][1] = path

        # Ouverture du fichier en mode écriture avec l'encodage UTF-8
        with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
            
            # Création de l'objet writer pour écrire dans le fichier
            writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            
            # Écriture des données dans le fichier
            for row in profile_Csv:
                writer.writerow(row)
        # Affichage de la donnée ajoutée
        os.system('clear')
        print("Ajout de : ", profile_Csv, "à", lettre)
        
    # Le fichier n'existe pas encore
    else:
        # Verifit ci la variable profile_Csv existe ci non la crée
        if 'profile_Csv' in locals():
            print("La variable existe !")
        else:
            # Creation de la variable profile_Csv
            profile_Csv = [
            ['Letter', 'Value'],
            ['q', "Vide"],
            ['w', "Vide"],
            ['e', "Vide"],
            ['r', "Vide"],
            ['t', "Vide"],
            ['z', "Vide"],
            ['u', "Vide"],
            ['i', "Vide"],
            ['o', "Vide"],
            ['p', "Vide"],
            ['a', "Vide"],
            ['s', "Vide"],
            ['d', "Vide"],
            ['f', "Vide"],
            ['g', "Vide"],
            ['h', "Vide"],
            ['j', "Vide"],
            ['k', "Vide"],
            ['l', "Vide"],
            ['y', "Vide"],
            ['x', "Vide"],
            ['c', "Vide"],
            ['v', "Vide"],
            ['b', "Vide"],
            ['n', "Vide"],
            ['m', "Vide"],   
            ]

        # Ajoute le nouveau chemin
        for i in range(len(profile_Csv)):
            if profile_Csv[i][0] == lettre:
                profile_Csv[i][1] = path

        # Ouverture du fichier en mode écriture avec l'encodage UTF-8
        with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
            
            # Création de l'objet writer pour écrire dans le fichier
            writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            
            # Écriture des données dans le fichier
            for row in profile_Csv:
                writer.writerow(row)
        # Affichage de la valeur ajoutée
        os.system('clear')
        print("Ajout de : ", profile_Csv, "à", lettre)

# Fonction à appeler pour Profile
def profiles_touche():
    while True:
        Profile_lettre = ''
        os.system('clear')
        if getattr(Profile_lettre, 'strip', lambda: '')():
            print("Nom du Profile précédemment utilisé : ", Profile_lettre)

        print("")
        print("Choisicer la touche sur la quelle ajouter un sond")
        print("[xx] Pour quitée")
        print("DE a - z")
        print("")


        touche_profile_choisi = input(": ")
        touche_profile_choisi = str(touche_profile_choisi)
        if touche_profile_choisi == "xx":
            break

        # Vérification si la chaîne est composée d'un seul caractère alphabétique
        pattern = r'^[a-zA-Z]+$'
        if len(touche_profile_choisi) == 1 and touche_profile_choisi.isalpha() and re.match(pattern, touche_profile_choisi):
            touche_profile_choisi = touche_profile_choisi.lower()
            # Debegage
            #print("La chaîne : ", touche_profile_choisi)
            #pause = input("PAUSE")
            Profile_lettre = profiles(touche_profile_choisi)
            profil_audio_chemin = profiles_sond(touche_profile_choisi)

            # Nom du profile, touche a utiliser, chemin du sond
            profiles_Creation_csv(Profile_lettre, touche_profile_choisi, profil_audio_chemin)
            

        else:
            print("La chaîne n'est pas valide.")
############################################################ FIN PROFIL



############################################################ FIN DETECTION DE TOUCHE




#----------------------------------------------
###############################################
# Boucle While True 




# Pour test
# profiles_touche() # Creation de Profil


def touche_entrer_a():
    os.system('clear')
    print("Tu as entré a")

def touche_entrer_b():
    os.system('clear')
    print("Tu as entré b")

def touche_entrer_c():
    os.system('clear')
    print("Tu as entré c")

def touche_entrer_d():
    os.system('clear')
    print("Tu as entré d")

def touche_entrer_e():
    os.system('clear')
    print("Tu as entré e")

def touche_entrer_f():
    os.system('clear')
    print("Tu as entré f")

def touche_entrer_g():
    os.system('clear')
    print("Tu as entré g")

def touche_entrer_h():
    os.system('clear')
    print("Tu as entré h")

def touche_entrer_i():
    os.system('clear')
    print("Tu as entré i")

def touche_entrer_j():
    os.system('clear')
    print("Tu as entré j")

def touche_entrer_k():
    os.system('clear')
    print("Tu as entré k")

def touche_entrer_l():
    os.system('clear')
    print("Tu as entré l")

def touche_entrer_m():
    os.system('clear')
    print("Tu as entré m")

def touche_entrer_n():
    os.system('clear')
    print("Tu as entré n")

def touche_entrer_o():
    os.system('clear')
    print("Tu as entré o")

def touche_entrer_p():
    os.system('clear')
    print("Tu as entré p")

def touche_entrer_q():
    os.system('clear')
    print("Tu as entré q")

def touche_entrer_r():
    os.system('clear')
    print("Tu as entré r")

def touche_entrer_s():
    os.system('clear')
    print("Tu as entré s")

def touche_entrer_t():
    os.system('clear')
    print("Tu as entré t")

def touche_entrer_u():
    os.system('clear')
    print("Tu as entré u")

def touche_entrer_v():
    os.system('clear')
    print("Tu as entré v")

def touche_entrer_w():
    os.system('clear')
    print("Tu as entré w")

def touche_entrer_x():
    os.system('clear')
    print("Tu as entré x")

def touche_entrer_y():
    os.system('clear')
    print("Tu as entré y")

def touche_entrer_z():
    os.system('clear')
    print("Tu as entré z")

def touche_entrer_0():
    os.system('clear')
    print("Tu as entré 0")
    filename = 'Profile_0.csv'

    if os.path.isfile(filename):
        profile = {}
        with open(filename, 'r') as f:
            # Lire le contenu du fichier et le stocker dans le dictionnaire 'profile'
            for line in f:
                key, value = line.strip().split(',')
                profile[key] = value
            print("_________ CONTENU CSV")
            print(profile)
            print("_________")
    else:
        print(f"Le fichier {filename} n'existe pas.")

def touche_entrer_1():
    os.system('clear')
    print("Tu as entré 1")

def touche_entrer_2():
    os.system('clear')
    print("Tu as entré 2")

def touche_entrer_3():
    os.system('clear')
    print("Tu as entré 3")

def touche_entrer_4():
    os.system('clear')
    print("Tu as entré 4")

def touche_entrer_5():
    os.system('clear')
    print("Tu as entré 5")

def touche_entrer_6():
    os.system('clear')
    print("Tu as entré 6")

def touche_entrer_7():
    os.system('clear')
    print("Tu as entré 7")

def touche_entrer_8():
    os.system('clear')
    print("Tu as entré 8")

def touche_entrer_9():
    os.system('clear')
    print("Tu as entré 9")

keyboard.add_hotkey("a", touche_entrer_a)
keyboard.add_hotkey("b", touche_entrer_b)
keyboard.add_hotkey("c", touche_entrer_c)
keyboard.add_hotkey("d", touche_entrer_d)
keyboard.add_hotkey("e", touche_entrer_e)
keyboard.add_hotkey("f", touche_entrer_f)
keyboard.add_hotkey("g", touche_entrer_g)
keyboard.add_hotkey("h", touche_entrer_h)
keyboard.add_hotkey("i", touche_entrer_i)
keyboard.add_hotkey("j", touche_entrer_j)
keyboard.add_hotkey("k", touche_entrer_k)
keyboard.add_hotkey("l", touche_entrer_l)
keyboard.add_hotkey("m", touche_entrer_m)
keyboard.add_hotkey("n", touche_entrer_n)
keyboard.add_hotkey("o", touche_entrer_o)
keyboard.add_hotkey("p", touche_entrer_p)
keyboard.add_hotkey("q", touche_entrer_q)
keyboard.add_hotkey("r", touche_entrer_r)
keyboard.add_hotkey("s", touche_entrer_s)
keyboard.add_hotkey("t", touche_entrer_t)
keyboard.add_hotkey("u", touche_entrer_u)
keyboard.add_hotkey("v", touche_entrer_v)
keyboard.add_hotkey("w", touche_entrer_w)
keyboard.add_hotkey("x", touche_entrer_x)
keyboard.add_hotkey("y", touche_entrer_y)
keyboard.add_hotkey("z", touche_entrer_z)
keyboard.add_hotkey("0", touche_entrer_0)
keyboard.add_hotkey("1", touche_entrer_1)
keyboard.add_hotkey("2", touche_entrer_2)
keyboard.add_hotkey("3", touche_entrer_3)
keyboard.add_hotkey("4", touche_entrer_4)
keyboard.add_hotkey("5", touche_entrer_5)
keyboard.add_hotkey("6", touche_entrer_6)
keyboard.add_hotkey("7", touche_entrer_7)
keyboard.add_hotkey("8", touche_entrer_8)
keyboard.add_hotkey("9", touche_entrer_9)
keyboard.add_hotkey(",", profiles_touche) # Creation de profile



keyboard.add_hotkey("-", lambda: exit())

# On écoute en permanence les touches du clavier
while True:
    #os.system('clear')
    keyboard.wait()

################################################################




