apt update -y && apt upgrade -y
python3 get-pip.py
python3 -m ensurepip --upgrade
pip install keyboard
# Temporaire
pip install pygame --pre
pip install pydub
pip install ffmpeg --use-pep517
apt install ffmpeg -y
if [ $? -eq 0 ];
then
    echo -e "\033[32m[ OK ] Installation términée !\033[00m"
fi

echo "\033[35mpython3 PlaySond_PyDub.py"

exit