# Programa: convertir un número decimal (dos cifras) a binario de 8 bits
# Hecho por: Adrián García

numero = int(input("Ingrese un número decimal de dos cifras: "))

if numero >= 0 and numero <= 99:
    bits = ""
    n = numero

    for i in range(8):
        residuo = n % 2
        n = n // 2
        bits = str(residuo) + bits

    print("El número", numero, "en binario de 8 bits es:", bits)
else:
    print("Error: ingrese un número entre 0 y 99")
