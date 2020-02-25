#!/bin/bash

file=$1

echo "Rimozione di $file"

sed -i 's/ID: //g' $file
sed -i 's/Name: //g' $file
sed -i 's/Phone No: //g' $file
sed -i 's/Position: //g' $file
sed -i 's/Email: //g' $file
