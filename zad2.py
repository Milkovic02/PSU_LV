try:
    broj = float(input("Unesi broj izmedju [0.0, 1.0]: "))
except:
    print("Pogresan unos")

if (broj > 1 or broj < 0):
    print("Broj nije u zadanom intervalu")
elif (broj >= 0.9):
    print("A")
elif (broj >= 0.8):
    print("B")
elif (broj >= 0.7):
    print("C")
elif (broj >= 0.6):
    print("D")
else:
    print("F")
