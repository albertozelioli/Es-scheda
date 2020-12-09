print("Inserire il nome, tutto minuscolo, della figura geometrica (quadrato, rettangolo, triangolo o cerchio) della quale si vuole calcolare l'area: ")
scelta = input()
if scelta == "quadrato":
    latoq = int(input("Inserire la misura del lato del quadrato: "))
    print("L'area del quadrato è: ", latoq*latoq)
elif scelta == "rettangolo":
    lato1r = int(input("Inserire la misura del lato corto del rettangolo: "))
    lato2r = int(input("Inserire la misura del lato lungo del rettangolo: "))
    print("L'area del rettangolo è: ", lato1r*lato2r)
elif scelta == "triangolo":
    base = int(input("Inserire la misura della base del triangolo: "))
    altezza = int(input("Inserire la misura dell'altezza del triangolo: "))
    print("L'area del triangolo è: ", base*altezza)
elif scelta == "cerchio":
    raggio = int(input("Inserire la misura del raggio del cerchio: "))
    print("L'area del cerchio è: ", raggio*raggio*3.14)
