

#gen pass rick and morty




a = "The Flesh Curtains"
dic = ["A","B","C","D","E","F","G","H","I","L","M","N","O","P","Q","R","S","T","U","V","Z","X","Y","W","K"]
digit = [1,2,3,4,5,6,7,8,9,0]
lista = []
f = open("pass_list.txt", "a")

for s in a.split(" "):
    for num in digit:
        for letter in dic:
           cmd = letter + str(num) + s + "\n"
           lista.append(cmd)
           f.write(cmd)
    
print lista


f.close()
