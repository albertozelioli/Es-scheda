A = []
B = []
x = True
while x == True:
    print("Inserire la parola che si vuole aggiunge alla lista, altrimenti, se si vuole terminare l'elenco, scrivere STOP:")
    parola = input ()
    if parola == "STOP":
        break
    else:
        A.append(parola)
cont = len(A)
for y in range(cont):
    cont2 = len(A[y])
    B.append(cont2)
print("L'elenco del numero di lettere che compongono le parole inserite sono:", B)
