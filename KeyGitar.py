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
    import re
    print("re est installé et importé correctement.")
except ImportError:
    print("re n'est pas installé ou n'a pas été importé correctement.")
try:
    import sys
    print("sys est installé et importé correctement.")
except ImportError:
    print("sys n'est pas installé ou n'a pas été importé correctement.")
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
        print("[xx] Pour quitée la première entrée est igniorée")
        print("DE a - z")
        print("")


        touche_profile_choisi = input(": ")
        touche_profile_choisi = str(touche_profile_choisi)
        if touche_profile_choisi == "xx":
            touche_profile_choisi = ''
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
# Définition du tableau globale profile pour les touches
profile_globale = {
    'q': "Vide",
    'w': "Vide",
    'e': "Vide",
    'r': "Vide",
    't': "Vide",
    'z': "Vide",
    'u': "Vide",
    'i': "Vide",
    'o': "Vide",
    'p': "Vide",
    'a': "Vide",
    's': "Vide",
    'd': "Vide",
    'f': "Vide",
    'g': "Vide",
    'h': "Vide",
    'j': "Vide",
    'k': "Vide",
    'l': "Vide",
    'y': "Vide",
    'x': "Vide",
    'c': "Vide",
    'v': "Vide",
    'b': "Vide",
    'n': "Vide",
    'm': "Vide",
}


def get_value(key): # Permet de récupérer le contenu de profile
    if key in profile_globale:
        return profile_globale[key]
    else:
        return None




def touche_entrer_a():
    os.system('clear')
    global actf_a
    if 'actf_a' not in locals():
        actf_a = 0
    print("Tu as entré a")
    print(get_value('a'))
    if get_value('a') != "Vide":
        if actf_a != 1:
            pygame.init() # ci variable pas vide !
            pygame.mixer.init()

            sona = pygame.mixer.Sound(get_value('a'))
            sona.play(-1)
            actf_a = 1
        else:   # Stope le sont ci actiffe
            sona.stop()
            actf_a = 0

def touche_entrer_b():
    os.system('clear')
    global actf_b
    if 'actf_b' not in locals():
        actf_b = 0
    print("Tu as entré b")
    print(get_value('b'))
    if get_value('b') != "Vide":
        if actf_b != 1:
            pygame.init() # ci variable pas vide !
            pygame.mixer.init()

            sonb = pygame.mixer.Sound(get_value('b'))
            sonb.play(-1)
            actf_b = 1
        else:   # Stope le sont ci actiffe
            sonb.stop()
            actf_b = 0

def touche_entrer_c():
    os.system('clear')
    global actf_c
    if 'actf_c' not in locals():
        actf_c = 0
    print("Tu as entré c")
    print(get_value('c'))
    if get_value('c') != "Vide":
        if actf_c != 1:
            pygame.init() # ci variable pas vide !
            pygame.mixer.init()

            sonc = pygame.mixer.Sound(get_value('c'))
            sonc.play(-1)
            actf_c = 1
        else:   # Stope le sont ci actiffe
            sonc.stop()
            actf_c = 0

def touche_entrer_d():
    os.system('clear')
    global actf_d
    if 'actf_d' not in locals():
        actf_d = 0
    print("Tu as entré d")
    print(get_value('d'))
    if get_value('d') != "Vide":
        if actf_d != 1:
            pygame.init() # ci variable pas vide !
            pygame.mixer.init()

            sond = pygame.mixer.Sound(get_value('d'))
            sond.play(-1)
            actf_d = 1
        else:   # Stope le sont ci actiffe
            sond.stop()
            actf_d = 0

def touche_entrer_e():
    os.system('clear')
    global actf_e
    if 'actf_e' not in locals():
        actf_e = 0
    print("Tu as entré e")
    print(get_value('e'))
    if get_value('e') != "Vide":
        if actf_e != 1:
            pygame.init() # ci variable pas vide !
            pygame.mixer.init()

            sone = pygame.mixer.Sound(get_value('e'))
            sone.play(-1)
            actf_e = 1
        else:   # Stope le sont ci actiffe
            sone.stop()
            actf_e = 0

def touche_entrer_f():
    os.system('clear')
    global actf_f
    if 'actf_f' not in locals():
        actf_f = 0
    print("Tu as entré f")
    print(get_value('f'))
    if get_value('f') != "Vide":
        if actf_f != 1:
            pygame.init() # ci variable pas vide !
            pygame.mixer.init()

            sonf = pygame.mixer.Sound(get_value('f'))
            sonf.play(-1)
            actf_f = 1
        else:   # Stope le sont ci actiffe
            sonf.stop()
            actf_f = 0

def touche_entrer_g():
    os.system('clear')
    global actf_g
    if 'actf_g' not in locals():
        actf_g = 0
    print("Tu as entré g")
    print(get_value('g'))
    if get_value('g') != "Vide":
        if actf_g != 1:
            pygame.init() # ci variable pas vide !
            pygame.mixer.init()

            song = pygame.mixer.Sound(get_value('g'))
            song.play(-1)
            actf_g = 1
        else:   # Stope le sont ci actiffe
            song.stop()
            actf_g = 0

def touche_entrer_h():
    os.system('clear')
    global actf_h
    if 'actf_h' not in locals():
        actf_h = 0
    print("Tu as entré h")
    print(get_value('h'))
    if get_value('h') != "Vide":
        if actf_h != 1:
            pygame.init() # ci variable pas vide !
            pygame.mixer.init()

            sonh = pygame.mixer.Sound(get_value('h'))
            sonh.play(-1)
            actf_h = 1
        else:   # Stope le sont ci actiffe
            sonh.stop()
            actf_h = 0

def touche_entrer_i():
    os.system('clear')
    global actf_i
    if 'actf_i' not in locals():
        actf_i = 0
    print("Tu as entré i")
    print(get_value('i'))
    if get_value('i') != "Vide":
        if actf_i != 1:
            pygame.init() # ci variable pas vide !
            pygame.mixer.init()

            soni = pygame.mixer.Sound(get_value('i'))
            soni.play(-1)
            actf_i = 1
        else:   # Stope le sont ci actiffe
            soni.stop()
            actf_i = 0

def touche_entrer_j():
    os.system('clear')
    global actf_j
    if 'actf_j' not in locals():
        actf_j = 0
    print("Tu as entré j")
    print(get_value('j'))
    if get_value('j') != "Vide":
        if actf_j != 1:
            pygame.init() # ci variable pas vide !
            pygame.mixer.init()

            sonj = pygame.mixer.Sound(get_value('j'))
            sonj.play(-1)
            actf_j = 1
        else:   # Stope le sont ci actiffe
            sonj.stop()
            actf_j = 0

def touche_entrer_k():
    os.system('clear')
    global actf_k
    if 'actf_k' not in locals():
        actf_k = 0
    print("Tu as entré k")
    print(get_value('k'))
    if get_value('k') != "Vide":
        if actf_k != 1:
            pygame.init() # ci variable pas vide !
            pygame.mixer.init()

            sonk = pygame.mixer.Sound(get_value('k'))
            sonk.play(-1)
            actf_k = 1
        else:   # Stope le sont ci actiffe
            sonk.stop()
            actf_k = 0

def touche_entrer_l():
    os.system('clear')
    global actf_l
    if 'actf_l' not in locals():
        actf_l = 0
    print("Tu as entré l")
    print(get_value('l'))
    if get_value('l') != "Vide":
        if actf_l != 1:
            pygame.init() # ci variable pas vide !
            pygame.mixer.init()

            sonl = pygame.mixer.Sound(get_value('l'))
            sonl.play(-1)
            actf_l = 1
        else:   # Stope le sont ci actiffe
            sonl.stop()
            actf_l = 0

def touche_entrer_m():
    os.system('clear')
    global actf_m
    if 'actf_m' not in locals():
        actf_m = 0
    print("Tu as entré m")
    print(get_value('m'))
    if get_value('m') != "Vide":
        if actf_m != 1:
            pygame.init() # ci variable pas vide !
            pygame.mixer.init()

            sonm = pygame.mixer.Sound(get_value('m'))
            sonm.play(-1)
            actf_m = 1
        else:   # Stope le sont ci actiffe
            sonm.stop()
            actf_m = 0

def touche_entrer_n():
    os.system('clear')
    global actf_n
    if 'actf_n' not in locals():
        actf_n = 0
    print("Tu as entré n")
    print(get_value('n'))
    if get_value('n') != "Vide":
        if actf_n != 1:
            pygame.init() # ci variable pas vide !
            pygame.mixer.init()

            sonn = pygame.mixer.Sound(get_value('n'))
            sonn.play(-1)
            actf_n = 1
        else:   # Stope le sont ci actiffe
            sonn.stop()
            actf_n = 0

def touche_entrer_o():
    os.system('clear')
    global actf_o
    if 'actf_o' not in locals():
        actf_o = 0
    print("Tu as entré o")
    print(get_value('o'))
    if get_value('o') != "Vide":
        if actf_o != 1:
            pygame.init() # ci variable pas vide !
            pygame.mixer.init()

            sono = pygame.mixer.Sound(get_value('o'))
            sono.play(-1)
            actf_o = 1
        else:   # Stope le sont ci actiffe
            sono.stop()
            actf_o = 0

def touche_entrer_p():
    os.system('clear')
    global actf_p
    if 'actf_p' not in locals():
        actf_p = 0
    print("Tu as entré p")
    print(get_value('p'))
    if get_value('p') != "Vide":
        if actf_p != 1:
            pygame.init() # ci variable pas vide !
            pygame.mixer.init()

            sonp = pygame.mixer.Sound(get_value('p'))
            sonp.play(-1)
            actf_p = 1
        else:   # Stope le sont ci actiffe
            sonp.stop()
            actf_p = 0

def touche_entrer_q():
    os.system('clear')
    global actf_q
    if 'actf_q' not in locals():
        actf_q = 0
    print("Tu as entré q")
    print(get_value('q'))
    if get_value('q') != "Vide":
        if actf_q != 1:
            pygame.init() # ci variable pas vide !
            pygame.mixer.init()

            sonq = pygame.mixer.Sound(get_value('q'))
            sonq.play(-1)
            actf_q = 1
        else:   # Stope le sont ci actiffe
            sonq.stop()
            actf_q = 0

def touche_entrer_r():
    os.system('clear')
    global actf_r
    if 'actf_r' not in locals():
        actf_r = 0
    print("Tu as entré r")
    print(get_value('r'))
    if get_value('r') != "Vide":
        if actf_r != 1:
            pygame.init() # ci variable pas vide !
            pygame.mixer.init()

            sonr = pygame.mixer.Sound(get_value('r'))
            sonr.play(-1)
            actf_r = 1
        else:   # Stope le sont ci actiffe
            sonr.stop()
            actf_r = 0

def touche_entrer_s():
    os.system('clear')
    global actf_s
    if 'actf_s' not in locals():
        actf_s = 0
    print("Tu as entré s")
    print(get_value('s'))
    if get_value('s') != "Vide":
        if actf_s != 1:
            pygame.init() # ci variable pas vide !
            pygame.mixer.init()

            sons = pygame.mixer.Sound(get_value('s'))
            sons.play(-1)
            actf_s = 1
        else:   # Stope le sont ci actiffe
            sons.stop()
            actf_s = 0

def touche_entrer_t():
    os.system('clear')
    global actf_t
    if 'actf_t' not in locals():
        actf_t = 0
    print("Tu as entré t")
    print(get_value('t'))
    if get_value('t') != "Vide":
        if actf_t != 1:
            pygame.init() # ci variable pas vide !
            pygame.mixer.init()

            sont = pygame.mixer.Sound(get_value('t'))
            sont.play(-1)
            actf_t = 1
        else:   # Stope le sont ci actiffe
            sont.stop()
            actf_t = 0

def touche_entrer_u():
    os.system('clear')
    global actf_u
    if 'actf_u' not in locals():
        actf_u = 0
    print("Tu as entré u")
    print(get_value('u'))
    if get_value('u') != "Vide":
        if actf_u != 1:
            pygame.init() # ci variable pas vide !
            pygame.mixer.init()

            sonu = pygame.mixer.Sound(get_value('u'))
            sonu.play(-1)
            actf_u = 1
        else:   # Stope le sont ci actiffe
            sonu.stop()
            actf_u = 0

def touche_entrer_v():
    os.system('clear')
    global actf_v
    if 'actf_v' not in locals():
        actf_v = 0
    print("Tu as entré v")
    print(get_value('v'))
    if get_value('v') != "Vide":
        if actf_v != 1:
            pygame.init() # ci variable pas vide !
            pygame.mixer.init()

            sonv = pygame.mixer.Sound(get_value('v'))
            sonv.play(-1)
            actf_v = 1
        else:   # Stope le sont ci actiffe
            sonv.stop()
            actf_v = 0

def touche_entrer_w():
    os.system('clear')
    global actf_w
    if 'actf_w' not in locals():
        actf_w = 0
    print("Tu as entré w")
    print(get_value('w'))
    if get_value('w') != "Vide":
        if actf_w != 1:
            pygame.init() # ci variable pas vide !
            pygame.mixer.init()

            sonw = pygame.mixer.Sound(get_value('w'))
            sonw.play(-1)
            actf_w = 1
        else:   # Stope le sont ci actiffe
            sonw.stop()
            actf_w = 0

def touche_entrer_x():
    os.system('clear')
    global actf_x
    if 'actf_x' not in locals():
        actf_x = 0
    print("Tu as entré x")
    print(get_value('x'))
    if get_value('x') != "Vide":
        if actf_x != 1:
            pygame.init() # ci variable pas vide !
            pygame.mixer.init()

            sonx = pygame.mixer.Sound(get_value('x'))
            sonx.play(-1)
            actf_x = 1
        else:   # Stope le sont ci actiffe
            sonx.stop()
            actf_x = 0

def touche_entrer_y():
    os.system('clear')
    global actf_y
    if 'actf_y' not in locals():
        actf_y = 0
    print("Tu as entré y")
    print(get_value('y'))
    if get_value('y') != "Vide":
        if actf_y != 1:
            pygame.init() # ci variable pas vide !
            pygame.mixer.init()

            sony = pygame.mixer.Sound(get_value('y'))
            sony.play(-1)
            actf_y = 1
        else:   # Stope le sont ci actiffe
            sony.stop()
            actf_y = 0

def touche_entrer_z():
    os.system('clear')
    global actf_z
    if 'actf_z' not in locals():
        actf_z = 0
    print("Tu as entré z")
    print(get_value('z'))
    if get_value('z') != "Vide":
        if actf_z != 1:
            pygame.init() # ci variable pas vide !
            pygame.mixer.init()

            sonz = pygame.mixer.Sound(get_value('z'))
            sonz.play(-1)
            actf_z = 1
        else:   # Stope le sont ci actiffe
            sonz.stop()
            actf_z = 0



def touche_entrer_0():
    global profile_globale
    os.system('clear')
    print("Tu as entré 0")
    filename = 'Profile_0.csv'
    filepath = os.path.join('Profiles', filename)
    
    if os.path.isfile(filepath):
        profile_globale = {}
        with open(filepath, 'r') as f:
            # Lire le contenu du fichier et le stocker dans le dictionnaire 'profile'
            for line in f:
                key, value = line.strip().split(',')
                profile_globale[key] = value
            print("_________ CONTENU CSV")
            print(profile_globale)
            print("_________")
    else:
        print(f"Le fichier {filename} n'existe pas.")

def touche_entrer_1():
    global profile_globale
    os.system('clear')
    print("Tu as entré 1")
    filename = 'Profile_1.csv'
    filepath = os.path.join('Profiles', filename)
    
    if os.path.isfile(filepath):
        profile_globale = {}
        with open(filepath, 'r') as f:
            # Lire le contenu du fichier et le stocker dans le dictionnaire 'profile'
            for line in f:
                key, value = line.strip().split(',')
                profile_globale[key] = value
            print("_________ CONTENU CSV")
            print(profile_globale)
            print("_________")
    else:
        print(f"Le fichier {filename} n'existe pas.")

def touche_entrer_2():
    global profile_globale
    os.system('clear')
    print("Tu as entré 2")
    filename = 'Profile_2.csv'
    filepath = os.path.join('Profiles', filename)
    
    if os.path.isfile(filepath):
        profile_globale = {}
        with open(filepath, 'r') as f:
            # Lire le contenu du fichier et le stocker dans le dictionnaire 'profile'
            for line in f:
                key, value = line.strip().split(',')
                profile_globale[key] = value
            print("_________ CONTENU CSV")
            print(profile_globale)
            print("_________")
    else:
        print(f"Le fichier {filename} n'existe pas.")

def touche_entrer_3():
    global profile_globale
    os.system('clear')
    print("Tu as entré 3")
    filename = 'Profile_3.csv'
    filepath = os.path.join('Profiles', filename)
    
    if os.path.isfile(filepath):
        profile_globale = {}
        with open(filepath, 'r') as f:
            # Lire le contenu du fichier et le stocker dans le dictionnaire 'profile'
            for line in f:
                key, value = line.strip().split(',')
                profile_globale[key] = value
            print("_________ CONTENU CSV")
            print(profile_globale)
            print("_________")
    else:
        print(f"Le fichier {filename} n'existe pas.")

def touche_entrer_4():
    global profile_globale
    os.system('clear')
    print("Tu as entré 4")
    filename = 'Profile_4.csv'
    filepath = os.path.join('Profiles', filename)
    
    if os.path.isfile(filepath):
        profile_globale = {}
        with open(filepath, 'r') as f:
            # Lire le contenu du fichier et le stocker dans le dictionnaire 'profile'
            for line in f:
                key, value = line.strip().split(',')
                profile_globale[key] = value
            print("_________ CONTENU CSV")
            print(profile_globale)
            print("_________")
    else:
        print(f"Le fichier {filename} n'existe pas.")

def touche_entrer_5():
    global profile_globale
    os.system('clear')
    print("Tu as entré 5")
    filename = 'Profile_5.csv'
    filepath = os.path.join('Profiles', filename)
    
    if os.path.isfile(filepath):
        profile_globale = {}
        with open(filepath, 'r') as f:
            # Lire le contenu du fichier et le stocker dans le dictionnaire 'profile'
            for line in f:
                key, value = line.strip().split(',')
                profile_globale[key] = value
            print("_________ CONTENU CSV")
            print(profile_globale)
            print("_________")
    else:
        print(f"Le fichier {filename} n'existe pas.")

def touche_entrer_6():
    global profile_globale
    os.system('clear')
    print("Tu as entré 6")
    filename = 'Profile_6.csv'
    filepath = os.path.join('Profiles', filename)
    
    if os.path.isfile(filepath):
        profile_globale = {}
        with open(filepath, 'r') as f:
            # Lire le contenu du fichier et le stocker dans le dictionnaire 'profile'
            for line in f:
                key, value = line.strip().split(',')
                profile_globale[key] = value
            print("_________ CONTENU CSV")
            print(profile_globale)
            print("_________")
    else:
        print(f"Le fichier {filename} n'existe pas.")

def touche_entrer_7():
    global profile_globale
    os.system('clear')
    print("Tu as entré 7")
    filename = 'Profile_7.csv'
    filepath = os.path.join('Profiles', filename)
    
    if os.path.isfile(filepath):
        profile_globale = {}
        with open(filepath, 'r') as f:
            # Lire le contenu du fichier et le stocker dans le dictionnaire 'profile'
            for line in f:
                key, value = line.strip().split(',')
                profile_globale[key] = value
            print("_________ CONTENU CSV")
            print(profile_globale)
            print("_________")
    else:
        print(f"Le fichier {filename} n'existe pas.")

def touche_entrer_8():
    global profile_globale
    os.system('clear')
    print("Tu as entré 8")
    filename = 'Profile_8.csv'
    filepath = os.path.join('Profiles', filename)
    
    if os.path.isfile(filepath):
        profile_globale = {}
        with open(filepath, 'r') as f:
            # Lire le contenu du fichier et le stocker dans le dictionnaire 'profile'
            for line in f:
                key, value = line.strip().split(',')
                profile_globale[key] = value
            print("_________ CONTENU CSV")
            print(profile_globale)
            print("_________")
    else:
        print(f"Le fichier {filename} n'existe pas.")

def touche_entrer_9():
    global profile_globale
    os.system('clear')
    print("Tu as entré 9")
    filename = 'Profile_9.csv'
    filepath = os.path.join('Profiles', filename)
    
    if os.path.isfile(filepath):
        profile_globale = {}
        with open(filepath, 'r') as f:
            # Lire le contenu du fichier et le stocker dans le dictionnaire 'profile'
            for line in f:
                key, value = line.strip().split(',')
                profile_globale[key] = value
            print("_________ CONTENU CSV")
            print(profile_globale)
            print("_________")
    else:
        print(f"Le fichier {filename} n'existe pas.")

def exitt(key):
    if key.name == '-':
        sys.exit()

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



keyboard.add_hotkey('-', exitt)

# On écoute en permanence les touches du clavier
while True:
    #os.system('clear')
    keyboard.wait()

################################################################




