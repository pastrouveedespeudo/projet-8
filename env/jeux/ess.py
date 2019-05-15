a = 'saliut, cest jb'

liste = [[],[]]
c=0
for i in a:
    if i == ',':
        c+=1
    else:
        liste[c].append(i)

liste = ["".join(i) for i in liste]
print(liste)
