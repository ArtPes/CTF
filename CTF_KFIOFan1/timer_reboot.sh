#!/bin/bash

decompte=`who | grep "alice" | awk '{print $4}' | cut -d":" -f2`

if [ -z "$decompte" ]
then
	echo "pas defini"
else
	decompte=$((`date +%M` - $decompte))
fi


if [ -z "$decompte" ]
then
	echo "pas defini"
elif [ $decompte -gt 10 ] || [ $decompte -lt 0 ]
then
	/sbin/init 6
fi

