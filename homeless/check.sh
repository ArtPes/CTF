#!/bin/bash

HOST=192.168.1.113
UA=$1

die() {
    for pid in $(ps aux \
                 | grep -v grep \
                 | grep brute \
                 | awk '{ print $2 }'); do
        kill -9 $pid &>/dev/null
    done
}

RESP=$(curl -s -A "$UA" $HOST \
       | sed '32!d' \
       | sed -r -e 's/^[ \t]+//' -e 's/\t+.*$//')

if [ "$UA" != "$RESP" ]; then
    echo "[!] Found: \"$UA\" - $RESP"
    die
fi
