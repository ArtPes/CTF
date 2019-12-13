#!/bin/bash

rm pass.txt
touch pass.txt

#Upper + symbol
crunch 7 7 -t s1lKy^, >> pass.txt

#symbol + Upper 
crunch 7 7 -t s1lKy,^ >> pass.txt

#lower + symbol 
crunch 7 7 -t s1lKy@^ >> pass.txt

#symbol + lower
crunch 7 7 -t s1lKy^@ >> pass.txt

#number + symbol
crunch 7 7 -t s1lKy%^ >> pass.txt

#symbol + number
crunch 7 7 -t s1lKy^% >> pass.txt

#symbol + symbol
crunch 7 7 -t s1lKy^^ >> pass.txt

#number + number
crunch 7 7 -t s1lKy%% >> pass.txt

#Upper + number
crunch 7 7 -t s1lKy,% >>  pass.txt

#number + Upper
crunch 7 7 -t s1lKy%, >>  pass.txt

#lower + number
crunch 7 7 -t s1lKy@% >>  pass.txt

#number + lower
crunch 7 7 -t s1lKy%@ >>  pass.txt

#Upper + lower
crunch 7 7 -t s1lKy,@ >>  pass.txt

#lower + Upper
crunch 7 7 -t s1lKy@, >>  pass.txt

#lower + lower
crunch 7 7 -t s1lKy@@ >> pass.txt

#Upper + Upper
crunch 7 7 -t s1lKy,, >> pass.txt


