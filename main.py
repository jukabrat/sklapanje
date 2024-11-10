import time
rec = input("Unesi recenicu: ")

lista = []
rezultat = []
alfabet = ["a","A","b","B","c","C","d","D","e","E","f","F","g","G","h","H","i","I","j","J","k","K","l","L","m","M","n","N","o","O","p","P","q","Q","r","R","s","S","t","T","u","U","v","V","w","W","x","X","y","Y","z","Z"]

for slovo in rec:
    lista.append(slovo)
    if slovo == ' ':
        rezultat.append(" ")
    else:
        rezultat.append("")


br = 0
for l in lista:
    ba = 0
    for a in alfabet:
        if l == ' ':
            break
        rezultat[br] = alfabet[ba]
        rez = ''.join(rezultat)
        print(rez)
        time.sleep(0.05)
        if l == a:
            break
        ba += 1
    br += 1

input("Enter")


