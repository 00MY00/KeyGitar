#!/bin/bash
# Scripte de creation d'un reseau Wi-Fi
# Inspirer par : https://wiki-fablab.grandbesancon.fr/doku.php?id=howto:raspberry-pi:wirelessaccespoint

# Verification de l'accès internet
ping www.google.ch -c 1

if [ $? -eq 0 ];
then
    echo -e "OK ping réusit !"
    sudo ifconfig eth0 down
fi

apt update -y 

if [ $? -eq 0 ];
then
    echo -e "OK update réusit !"
fi

apt upgrade -y

if [ $? -eq 0 ];
then
    echo -e "OK upgrade réusit !"
fi

sudo ifconfig eth0 up



interface wlan0 > "/etc/dhcpcd.conf"
static ip_address=192.168.0.1/24 >> "/etc/dhcpcd.conf"
nohook wpa_supplicant >> "/etc/dhcpcd.conf"

sudo rfkill unblock 0


sudo apt-get install dnsmasq -y
sudo apt-get install hostapd -y
######################################
# changement dans le fichier de configuration "/etc/dnsmasq.conf" 
# On utilise l'interface wifi wlan0
interface=wlan0
#On définit une plage d'adresse ip ainsi que la durée du bail
dhcp-range=192.168.0.1,192.168.0.100,255.255.255.0,24h 


######################################
# Config de hostapd dans "/etc/hostapd/hostapd.conf"
# interface wlan du Wi-Fi
interface=wlan0

# nl80211 avec tous les drivers Linux mac80211 
driver=nl80211

# Nom du réseau Wi-Fi
ssid=KeyboardGitar

# mode Wi-Fi utilisé : a = IEEE 802.11a (5GHz) , b = IEEE 802.11b (2.4GHz), g = IEEE 802.11g) (2.4GHz)
hw_mode=g

# canal de fréquence Wi-Fi (1-14)
channel=6

#################################


# On indique à hostapd qu'il doit utiliser ce fichier de configuration en éditant le fichier /etc/default/hostapd afin qu'il contienne :
DAEMON_CONF="/etc/hostapd/hostapd.conf"

# On (re)démarre le serveur dhcp :

sudo systemctl restart dnsmasq
# On active le service hostapd :

sudo systemctl unmask hostapd
sudo systemctl enable hostapd
sudo systemctl start hostapd


# Afficher Logs
cat /var/log/syslog

###################################################################################################################

Non, vous n'êtes pas obligé d'utiliser une API pour contrôler une bande LED WiFi avec Python. Vous pouvez également utiliser des bibliothèques telles que "socket" pour communiquer directement avec le dispositif via un protocole de communication spécifique (comme UDP ou TCP).

Exemple de code pour contrôler une bande LED en utilisant un socket:

makefile
Copy code
import socket

IP_ADDRESS = "192.168.1.2"
PORT = 80

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP_ADDRESS, PORT))
client_socket.send(b"set_color 255 0 0")
client_socket.close()
Ce code suppose que votre bande LED est configurée pour accepter des connexions socket et que vous connaissez le protocole de communication utilisé. Assurez-vous de consulter la documentation du dispositif pour savoir comment il peut être contrôlé via un socket.


