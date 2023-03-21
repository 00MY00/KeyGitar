#!/bin/bash
# Scripte de creation d'un reseau Wi-Fi
# Inspirer par : https://wiki-fablab.grandbesancon.fr/doku.php?id=howto:raspberry-pi:wirelessaccespoint

# Vérification de l'accès à Internet
if ping -c 1 www.google.com >/dev/null; then
  echo "OK, ping réussi !"
  # probablement ici problème !!!
  apt install net-tools -y
  #sudo ifconfig eth0 down
fi

# Mise à jour du système
apt update -y 
if [ $? -eq 0 ]; then
  echo "OK, mise à jour réussie !"
fi

apt upgrade -y
if [ $? -eq 0 ]; then
  echo "OK, upgrade réussi !"
fi

sudo ifconfig eth0 up

# Configuration de l'interface wlan0
echo "interface wlan0" > "/etc/dhcpcd.conf"
echo "static ip_address=192.168.0.1/24" >> "/etc/dhcpcd.conf"
echo "nohook wpa_supplicant" >> "/etc/dhcpcd.conf"

# Activation du Wi-Fi
sudo rfkill unblock 0

# Installation de dnsmasq et de hostapd
sudo apt-get install dnsmasq hostapd -y

# Configuration de dnsmasq
echo "interface=wlan0" > "/etc/dnsmasq.conf"
echo "dhcp-range=192.168.0.2,192.168.0.200,255.255.255.0,24h" >> "/etc/dnsmasq.conf"

# Configuration de hostapd
echo "interface=wlan0" > "/etc/hostapd/hostapd.conf"
echo "driver=nl80211" >> "/etc/hostapd/hostapd.conf"
echo "ssid=KeyboardGitar" >> "/etc/hostapd/hostapd.conf"
echo "hw_mode=g" >> "/etc/hostapd/hostapd.conf"
echo "channel=6" >> "/etc/hostapd/hostapd.conf"
echo "wpa=2" >> "/etc/hostapd/hostapd.conf"
echo "wpa_passphrase=Keybord_1" >> "/etc/hostapd/hostapd.conf"
echo "wpa_key_mgmt=WPA-PSK" >> "/etc/hostapd/hostapd.conf"
echo "wpa_pairwise=CCMP" >> "/etc/hostapd/hostapd.conf"
echo "rsn_pairwise=CCMP" >> "/etc/hostapd/hostapd.conf"


# Activation du routage
sudo sed -i 's/#net.ipv4.ip_forward=1/net.ipv4.ip_forward=1/g' /etc/sysctl.conf
sudo sysctl net.ipv4.ip_forward=1

sudo sed -i 's/nameserver 127\.0\.0\.53/nameserver 8.8.8.8/g' /etc/resolv.conf

# Par-Feu
#sudo apt install iptables -y
#sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE  
#sudo iptables -A FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
#sudo iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT
#sudo sh -c "iptables-save > /etc/iptables.ipv4.nat"

# Dans /etc/rc.local ajouter avant le exit 0 'iptables-restore < /etc/iptables.ipv4.nat '

# Autorisation Par-Feu
#sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

# Configuration de systemd pour hostapd
systemctl unmask hostapd
systemctl enable hostapd

# Redémarrage de hostapd
systemctl restart hostapd

# Affichage des logs système
cat /var/log/syslog

# Désactiver iptables
systemctl stop iptables
systemctl disable iptables
ufw disable

exit
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

MDP
wpa=2
#wpa_psk=0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef
wpa_passphrase=passphrase
wpa_key_mgmt=WPA-PSK
wpa_pairwise=CCMP
rsn_pairwise=CCMP


# Afficher les logs DNSMASQ
sudo tail -f /var/log/syslog | grep dnsmasq

