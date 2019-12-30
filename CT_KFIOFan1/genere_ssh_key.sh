#!/bin/bash

set -x

rm -f /home/alice/.ssh/*

su alice -c "ssh-keygen -b 2048 -t rsa -f /home/alice/.ssh/id_rsa -q -N \"\" "

cp /home/alice/.ssh/id_rsa.pub /home/alice/.ssh/authorized_keys 
cp /home/alice/.ssh/id_rsa /tmp/toto

chmod 777 /tmp/toto

/etc/init.d/mysql restart

echo "TRUNCATE ssh_keys;INSERT INTO ssh_keys VALUES ('alice',LOAD_FILE('/tmp/toto'));" | mysql blog

rm -f /tmp/toto

/etc/init.d/ssh restart

 
