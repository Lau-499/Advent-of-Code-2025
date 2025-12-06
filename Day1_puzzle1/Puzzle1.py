f = open(r"Day1_puzzle1\rotations.txt")
# f.read() para leer todo y devolver una cadena
# f.readline() para leer una línea y devolver una cadena
# f.readlines() para leer todas las líneas y devolver una lista
# f.close() para cerrar el archivo

num = 50
cont = 0
print(num)
it = 0

for linea in f:
    linea = linea.strip()
    letra = linea[0]
    valor = int(linea[1:])
    if (letra == "L"):
        num -= valor
    elif (letra == "R"):
        num += valor
    else:
        print("No es una dirección válida")
    
    num = num%100
    
    it += 1

    print("Iteración ", it," : ", num)
    if (num == 0):
        cont += 1
        print("Contador: ", cont)
print("Contador final: ", cont)
print("Por lo tanto, la contraseña es ", cont, ", habiendo llegado al ", num, " en el vial", sep="")

f.close()





