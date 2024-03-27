dat = open("C:\\Users\\student\\Documents\\zad4\\song.txt", 'r')

rjecnik = {}

for line in dat:
    line = line.rsplit()
    for rijec in line:
        if rijec in rjecnik:
            rjecnik[rijec] += 1
        else:
            rjecnik[rijec] = 1

unikatne_rijeci = []

for rijec in rjecnik:
    if (rjecnik[rijec] == 1):
        unikatne_rijeci.append(rijec)

print(rjecnik)

print("Broj unikatnih rijeci: ", len(unikatne_rijeci))

print(unikatne_rijeci)
