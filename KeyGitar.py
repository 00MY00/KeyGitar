########################################
#     Script crée par Kuroakashiro     #
########################################
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
    from pydub import AudioSegment
    import simpleaudio as sa
    print("pydub est installé et importé correctement.")
except ImportError:
    print("pydub n'est pas installé ou n'a pas été importé correctement.")
print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

###############################################
# Variable Racine

#récupère le nom du repertoire courent Exemple : 'c:\User'
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


# Récupération des nom de répertoire
# Appel de fonction Exemple : 'All_rep = get_all_dirs("/chemin/du/répertoire")'
def get_all_dirs(Repertoire):
    All_rep = []
    for item in os.listdir(Repertoire):
        item_path = os.path.join(Repertoire, item)
        if os.path.isdir(item_path):
            All_rep.append(item)
    return All_rep




# Recuperation des nom de Repertoire
All_rep = get_all_dirs(RepTemporaire)

# Boucle/loop pour convertire chaque répertoir
for i in range(len(All_rep)):
    print(RepTemporaire + All_rep[i])
    convert_mp3_to_wav(RepTemporaire + All_rep[i])


###
# Variable de fichier audio

for i in range(len(All_rep)):
    print(All_rep[i])


## Exemple

variable = ['Bass', 'Record']
y = ['chemin1', 'chemin2', 'chemin3']
# dans une boucle increment pour repertorier tous les répertoires
# dabore crée toute les clé dans x se qui corespon a Bass Record et ensuite ajouter les chemins
# x = {variable[0]: y}

# executer le script 
# ajoute les clés
# x = {var: [] for var in variable}

# crée une boucle qui récupère les chemin dans y

# for item in variable:
#     x[item].extend(y)
x = {}
for var in variable:
    directory = RepTemporaire + var + "/"
    y = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    x[var] = y




print("Resulta de X : ", x)



###

################################################################




