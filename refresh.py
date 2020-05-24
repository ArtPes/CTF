import subprocess


cmd = subprocess.check_output("ls", shell=True)

file = open("README_new.md","w")

file.write("![github-large](ctf.jpg)\n")
file.write("\n## Some CTFs\nList of VM:\n")

list = cmd.split("\n")

no_l = ["serial_nessus.txt","README.md","refresh.py","Corso_PT","CTF_Beg_2019.txt","CTF_Beginners_2019","ctf.jpg","Exercises","OSCP","HackTheBox",""," "]

n = 1

for i in list:
    if i in no_l:
        continue
    else:
        file.write("- [x] " + i + "  [--> Link](#)"+ "\n")
        n+=1

file.write("\nNumber of VMs rooted: "+str(n))
file.write("\nVMs of HackTheBox: HackTheBox")

file.close()
