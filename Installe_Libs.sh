apt update -y && apt upgrade -y
python get-pip.py
python -m ensurepip --upgrade
pip install keyboard
# Temporaire
pip install pygame --pre
pip install pydub
pip install ffmpeg --use-pep517

if [ $? -eq 0 ];
then
    echo -e "\033[32m[ OK ] Installation términée !\033[00m"
