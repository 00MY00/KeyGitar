apt update -y && apt upgrade -y
python3 get-pip.py
python3 -m ensurepip --upgrade
apt install python3-pip -y
pip install keyboard
# Temporaire
pip install pygame --pre
############
# Retouche de fichier audio
pip install pydub
pip install ffmpeg --use-pep517
apt install ffmpeg -y
# Pour jouer son
pip install numpy
pip install simpleaudio
############

if [ $? -eq 0 ];
then
    echo -e "\033[32m[ OK ] Installation términée !\033[00m"
fi

echo -e "\033[35mpython3 PlaySond_PyDub.py \033[00m"

exit