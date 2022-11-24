import time

print("Hola");
name=str(input("Ingrese su nombre: "));
nac=int(input("Digite su año de nacimiento: "));
if (nac >= 2004):
    print("Lo sentimos mucho ",name," eres un menor de edad");
    time.sleep(3);
    print("");
    print("Hasta pronto!");
    time.sleep(5);
elif (nac < 2004):
    print("--------------------------");
    print("*** VENTAS DEL 2021 ***");
    print("--------------------------");
    sem_1 = float(input("Digite las ventas del primer semestre: "));
    sem_2 = float(input("Digite las ventas del segundo semestre: "));
    total = float(sem_1+ sem_2);
    if (sem_1 > sem_2):
        best = " 1ro. (Primer semestre)";
    elif (sem_2 > sem_1):
        best = " 2do. (Segundo semestre)";
    else:
        best = "Ambas ventas semetrales son iguales";

    if (total < 100000.00):
        medal = "Bronce";
        prize= "Un día libre";
    elif (total < 500000.00):
        medal = "Plata";
        prize = "Un día libre y un bono de Q250";
    elif (total < 1000000.00):
        medal = "Oro";
        prize = "Un día libre y un bono de Q500";
    else:
        medal = "Diamante";
        prize = "Dos días libres y un bono de Q1000";

    print("");
    print("---------------------------");
    print("=== RESUMEN DE REGISTRO ===");
    print("---------------------------");
    print("Vendedor: ",name);
    print("Ventas anuales: Q",total);
    print("Mejor semestre: ",best);
    print("Medalla acreditada: ",medal);
    print("Premio: ",prize);
    time.sleep(10);
    print("");
    print("Hasta pronto!");
    time.sleep(5);