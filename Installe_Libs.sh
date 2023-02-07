clear
echo -e "\033[33m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[00m"
apt update -yq > /dev/null 2>&1
if [ $? -eq 0 ];
then
    echo -e "   [ \033[32mOK\033[00m ] Update fait !"
else 
    echo -e "   [ \033[31mERREUR\033[00m ] Update !"
fi

apt upgrade -yq > /dev/null 2>&1
if [ $? -eq 0 ];
then
    echo -e "   [ \033[32mOK\033[00m ] Upgrade fait !"
else 
    echo -e "   [ \033[31mERREUR\033[00m ] Upgrade !"
fi

apt install python3-pip -yq > /dev/null 2>&1
if [ $? -eq 0 ];
then
    echo -e "   [ \033[32mOK\033[00m ] Installation de PIP !"
else 
    echo -e "   [ \033[31mERREUR\033[00m ] Installation de PIP !"
fi

python3 -m pip install --upgrade pip > /dev/null 2>&1
if [ $? -eq 0 ];
then
    echo -e "   [ \033[32mOK\033[00m ] Mise à jour de PIP !"
else 
    echo -e "   [ \033[31mERREUR\033[00m ] Mise à jour de PIP !"
fi

pip install keyboard --quiet
if [ $? -eq 0 ];
then
    echo -e "   [ \033[32mOK\033[00m ] Installation du Module keyboard !"
else 
    echo -e "   [ \033[31mERREUR\033[00m ] Installation du Module keyboard !"
fi

# Temporaire
# pip install pygame --pre
############
# Retouche de fichier audio
pip install pydub --quiet
if [ $? -eq 0 ];
then
    echo -e "   [ \033[32mOK\033[00m ] Installation du Module pydub !"
else 
    echo -e "   [ \033[31mERREUR\033[00m ] Installation du Module pydub !"
fi

pip install ffmpeg --use-pep517 --quiet
if [ $? -eq 0 ];
then
    echo -e "   [ \033[32mOK\033[00m ] Installation du Module ffmpeg !"
else 
    echo -e "   [ \033[31mERREUR\033[00m ] Installation du Module ffmpeg !"
fi

apt install ffmpeg -yq > /dev/null 2>&1
if [ $? -eq 0 ];
then
    echo -e "   [ \033[32mOK\033[00m ] Installation de ffmpeg !"
else 
    echo -e "   [ \033[31mERREUR\033[00m ] Installation de ffmpeg !"
fi

# Pour jouer son
pip install numpy --quiet
if [ $? -eq 0 ];
then
    echo -e "   [ \033[32mOK\033[00m ] Installation du Module numpy !"
else 
    echo -e "   [ \033[31mERREUR\033[00m ] Installation du Module numpy !"
fi

apt install libasound2-dev -yq > /dev/null 2>&1
if [ $? -eq 0 ];
then
    echo -e "   [ \033[32mOK\033[00m ] Installation de libasound2-dev !"
else 
    echo -e "   [ \033[31mERREUR\033[00m ] Installation de libasound2-dev !"
fi

pip install simpleaudio --quiet
if [ $? -eq 0 ];
then
    echo -e "   [ \033[32mOK\033[00m ] Installation du Module simpleaudio !"
    echo -e "\033[32m[ OK ] Installation términée !\033[00m"
else 
    echo -e "   [ \033[31mERREUR\033[00m ] Installation du Module simpleaudio !"
fi

############

echo -e "\033[33m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[00m"

echo -e "\033[35mpython3 PlaySond_PyDub.py \033[00m"

exit