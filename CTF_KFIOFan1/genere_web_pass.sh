#!/bin/bash

#set -x

ville_choisie=`shuf -n 1 ville.txt`

nom=$(echo $ville_choisie | awk -F" " '{print $1}')
coordo=$(echo $ville_choisie | awk -F" " '{print $2" "$3}')

/usr/bin/htpasswd -b /etc/apache2/list_pass Bob $nom

echo "<Location />\nAuthUserFile list_pass\nAuthType Basic\nAuthName \"$coordo\"\nRequire valid-user\n</Location>" > /etc/apache2/conf-secure/secure.conf

/etc/init.d/apache2 restart

 
