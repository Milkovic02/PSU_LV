dat = open("C:\\Users\\student\\Documents\\zad6\\SMSSpamCollection.txt", 'r')

brojac_ham = 0
brojac_spam = 0
suma_ham = 0
suma_spam = 0
brojac_usklicnik = 0

for line in dat:
    line = line.rsplit()
    if (line[0] == "ham"):
        brojac_ham += 1
        suma_ham += len(line)
    if (line[0] == "spam"):
        brojac_spam += 1
        suma_spam += len(line)
        if ("!" in line[-1]):
            brojac_usklicnik += 1
          
print("Prosjecan broj rijeci u ham porukama: ", suma_ham/brojac_ham)
print("Prosjecan broj rijeci u spam porukama: ", suma_spam/brojac_spam)
print("Broj poruka koje su spam i zavrsavaju s usklicnikom: ", brojac_usklicnik)

dat.close()
